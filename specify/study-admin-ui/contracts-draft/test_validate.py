"""Opt-in tests of the draft checker's CLI; no product/authentication tests."""
from __future__ import annotations

import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

PACKET = Path(__file__).resolve().parent
FILES = ("records.schema.json", "case-index.json", "examples.json", "validate.py")


class DraftCheckerCliTests(unittest.TestCase):
    def setUp(self):
        workspace = os.environ.get("TMPDIR")
        if not workspace or not Path(workspace).is_dir():
            raise RuntimeError("TMPDIR must name an existing owned workspace")
        self.storage = tempfile.TemporaryDirectory(prefix="noema-draft-check-", dir=workspace)
        self.addCleanup(self.storage.cleanup)
        self.packet = Path(self.storage.name)
        for name in FILES:
            shutil.copyfile(PACKET / name, self.packet / name)

    def read_json(self, name):
        return json.loads((self.packet / name).read_text(encoding="utf-8"))

    def write_json(self, name, value):
        (self.packet / name).write_text(json.dumps(value), encoding="utf-8")

    def invoke(self):
        environment = {key: os.environ[key] for key in ("PATH", "HOME", "TMPDIR") if key in os.environ}
        environment["PYTHONDONTWRITEBYTECODE"] = "1"
        result = subprocess.run(
            [sys.executable, "-I", str(self.packet / "validate.py"), "--json"],
            env=environment, capture_output=True, text=True, timeout=30,
        )
        self.assertEqual(result.stderr, "")
        return result.returncode, json.loads(result.stdout)

    def test_complete_packet_matches_its_indexed_shape_expectations(self):
        code, result = self.invoke()
        self.assertEqual(code, 0)
        self.assertEqual(result["scope"], "isolated_draft_record_shape_conformance_only")
        self.assertTrue(result["no_authz_or_security_claim"])
        self.assertEqual(result["cases"], 56)
        self.assertEqual(result["matched"], 56)
        self.assertEqual(result["schemas"], 9)
        self.assertEqual(result["limitation_controls"], 2)
        self.assertNotIn("examples", result)
        self.assertTrue(all(row["matched"] for row in result["results"]))

    def test_missing_example_is_an_inventory_failure_not_a_partial_pass(self):
        examples = self.read_json("examples.json")
        examples["examples"].pop("DS-001")
        self.write_json("examples.json", examples)
        code, result = self.invoke()
        self.assertEqual((code, result["error_type"]), (2, "ValueError"))
        self.assertNotIn("results", result)

    def test_duplicate_json_key_is_refused_without_echoing_record_values(self):
        path = self.packet / "examples.json"
        path.write_text('{"status":"synthetic_no_live_data","examples":{},"examples":{}}', encoding="utf-8")
        code, result = self.invoke()
        self.assertEqual((code, result["error_type"]), (2, "ValueError"))
        self.assertEqual(set(result), {"scope", "no_authz_or_security_claim", "error_type"})

    def test_nonlocal_static_and_dynamic_refs_are_filtered_before_resolution(self):
        original = self.read_json("records.schema.json")
        for keyword in ("$ref", "$dynamicRef"):
            with self.subTest(keyword=keyword):
                schema = json.loads(json.dumps(original))
                schema["$defs"]["Grant"][keyword] = "urn:noema:draft:unavailable-fixture"
                self.write_json("records.schema.json", schema)
                code, result = self.invoke()
                self.assertEqual((code, result["error_type"]), (2, "ValueError"))
                self.assertNotIn("unavailable-fixture", json.dumps(result))

    def test_wrong_negative_failure_predicate_cannot_hide_behind_any_error(self):
        index = self.read_json("case-index.json")
        case = next(row for row in index["cases"] if row["id"] == "DS-019")
        case["expected_failure"]["instance_path"] = ["different-field"]
        self.write_json("case-index.json", index)
        code, result = self.invoke()
        self.assertEqual(code, 1)
        failed = [row for row in result["results"] if not row["matched"]]
        self.assertEqual([row["id"] for row in failed], ["DS-019"])
        self.assertFalse(failed[0]["observed_shape_valid"])
        self.assertFalse(failed[0]["expected_failure_matched"])

    def test_calendar_assertion_detects_a_disabled_format_checker(self):
        path = self.packet / "validate.py"
        source = path.read_text(encoding="utf-8")
        self.assertEqual(source.count("format_checker=FORMATS"), 1)
        path.write_text(source.replace("format_checker=FORMATS", "format_checker=None"), encoding="utf-8")
        code, result = self.invoke()
        self.assertEqual(code, 1)
        self.assertEqual([row["id"] for row in result["results"] if not row["matched"]], ["DS-034"])

    def test_capability_assertions_detect_a_widened_schema(self):
        schema = self.read_json("records.schema.json")
        schema["$defs"]["ReadOnlyCapability"] = {"type": "array", "items": {"type": "string"}}
        self.write_json("records.schema.json", schema)
        code, result = self.invoke()
        self.assertEqual(code, 1)
        self.assertEqual([row["id"] for row in result["results"] if not row["matched"]], ["DS-019", "DS-020"])

    def test_symlinked_packet_input_is_refused(self):
        source = self.packet / "examples.json"
        saved = self.packet / "examples.saved"
        source.rename(saved)
        try:
            source.symlink_to(saved.name)
        except (OSError, NotImplementedError) as error:
            self.skipTest(f"platform cannot create test-owned symlink: {type(error).__name__}")
        code, result = self.invoke()
        self.assertEqual((code, result["error_type"]), (2, "ValueError"))


if __name__ == "__main__":
    unittest.main()
