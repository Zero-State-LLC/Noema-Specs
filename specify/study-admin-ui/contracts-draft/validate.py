#!/usr/bin/env python3
"""Validate isolated draft record shapes; never authenticate or authorize."""
from __future__ import annotations

import argparse
from collections import Counter
from datetime import datetime
import json
from pathlib import Path
import re
import sys

from jsonschema import Draft202012Validator, FormatChecker
from referencing import Registry
from referencing.exceptions import NoSuchResource

ROOT = Path(__file__).resolve().parent
SCHEMA = "records.schema.json"
INDEX = "case-index.json"
EXAMPLES = "examples.json"


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("duplicate JSON key")
        result[key] = value
    return result


def load_packet_file(name):
    path = ROOT / name
    if path.is_symlink() or not path.is_file():
        raise ValueError("packet file missing or symlinked")
    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=unique_object)


def check_local_refs(value):
    if isinstance(value, dict):
        for key, child in value.items():
            if key in {"$ref", "$dynamicRef"} and (not isinstance(child, str) or not child.startswith("#/$defs/")):
                raise ValueError("non-local schema reference")
            check_local_refs(child)
    elif isinstance(value, list):
        for child in value:
            check_local_refs(child)


FORMATS = FormatChecker()


def refuse_external_resource(uri):
    raise NoSuchResource(ref=uri)


OFFLINE_REGISTRY = Registry(retrieve=refuse_external_resource)


@FORMATS.checks("noema-draft-utc-second")
def draft_utc_second(value):
    if not isinstance(value, str) or re.fullmatch(
        r"[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z", value
    ) is None:
        return False
    try:
        datetime.strptime(value, "%Y-%m-%dT%H:%M:%SZ")
    except ValueError:
        return False
    return True


def run():
    schema = load_packet_file(SCHEMA)
    index = load_packet_file(INDEX)
    examples_document = load_packet_file(EXAMPLES)
    check_local_refs(schema)
    Draft202012Validator.check_schema(schema)
    if set(index) != {"status", "schema_status", "cases"}:
        raise ValueError("unexpected case-index fields")
    if index["status"] != "isolated_draft_proposal" or index["schema_status"] != "not_accepted_not_registered":
        raise ValueError("wrong packet contract status")
    if set(examples_document) != {"status", "examples"} or examples_document["status"] != "synthetic_no_live_data":
        raise ValueError("wrong synthetic fixture status")
    cases = index["cases"]
    examples = examples_document["examples"]
    if not isinstance(cases, list) or not cases or not isinstance(examples, dict):
        raise ValueError("invalid case inventory")
    ids = [case.get("id") for case in cases]
    if any(not isinstance(item, str) or re.fullmatch(r"DS-[0-9]{3}", item) is None for item in ids):
        raise ValueError("invalid case identifier")
    if len(ids) != len(set(ids)) or set(ids) != set(examples):
        raise ValueError("duplicate, omitted or extra example")
    record_names = {entry["$ref"].removeprefix("#/$defs/") for entry in schema["oneOf"]}
    if {case.get("schema_def") for case in cases} != record_names:
        raise ValueError("record coverage mismatch")
    validators = {}
    for name in record_names:
        selected = {"$schema": schema["$schema"], "$defs": schema["$defs"], "$ref": "#/$defs/" + name}
        Draft202012Validator.check_schema(selected)
        validators[name] = Draft202012Validator(selected, format_checker=FORMATS, registry=OFFLINE_REGISTRY)
    results = []
    for case in cases:
        if set(case) != {"id", "schema_def", "expected_shape_valid", "purpose", "tier", "expected_failure"}:
            raise ValueError("unexpected case fields")
        if type(case["expected_shape_valid"]) is not bool or case["tier"] not in {"shape_conformance", "shape_limitation_control"}:
            raise ValueError("invalid case expectation tier")
        expected_failure = case["expected_failure"]
        if case["expected_shape_valid"]:
            if expected_failure is not None:
                raise ValueError("positive case carries a failure predicate")
        elif not isinstance(expected_failure, dict) or set(expected_failure) != {"keyword", "instance_path"}:
            raise ValueError("negative case lacks a precise failure predicate")
        errors = list(validators[case["schema_def"]].iter_errors(examples[case["id"]]))
        observed = not errors
        failure_matched = None if expected_failure is None else any(
            error.validator == expected_failure["keyword"]
            and list(error.absolute_path) == expected_failure["instance_path"] for error in errors
        )
        matched = observed == case["expected_shape_valid"] and failure_matched is not False
        results.append({"id": case["id"], "schema_def": case["schema_def"],
                        "tier": case["tier"], "expected_shape_valid": case["expected_shape_valid"],
                        "observed_shape_valid": observed, "matched": matched,
                        "expected_failure_matched": failure_matched,
                        "diagnostic_keywords": sorted({str(error.validator) for error in errors})})
    counts = Counter(row["matched"] for row in results)
    return {"scope": "isolated_draft_record_shape_conformance_only", "no_authz_or_security_claim": True,
            "schemas": len(validators), "cases": len(results), "matched": counts[True],
            "mismatched": counts[False], "expected_shape_valid": sum(row["expected_shape_valid"] for row in results),
            "expected_shape_invalid": sum(not row["expected_shape_valid"] for row in results),
            "limitation_controls": sum(row["tier"] == "shape_limitation_control" for row in results),
            "results": results}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true", help="emit sanitized shape-only result metadata")
    args = parser.parse_args()
    try:
        report = run()
    except Exception as error:
        # Never echo a JSON instance, credential-like value or arbitrary parser text.
        print(json.dumps({"scope": "isolated_draft_record_shape_conformance_only",
                          "no_authz_or_security_claim": True, "error_type": type(error).__name__}))
        return 2
    if args.json:
        print(json.dumps(report, indent=2))
    else:
        print(f"Draft shape-only checks: {report['matched']}/{report['cases']} expectations matched; "
              f"{report['schemas']} record shapes; {report['limitation_controls']} limitation controls. "
              "Not authentication, authorization, lifecycle or security qualification.")
    return 0 if not report["mismatched"] else 1


if __name__ == "__main__":
    sys.exit(main())
