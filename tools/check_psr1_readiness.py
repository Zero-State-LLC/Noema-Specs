#!/usr/bin/env python3
"""Check readiness of operator-supplied PSR-1 (#421/#422) and STUDY (#423) receipts."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from validate_locked_contracts import (
    validate_psr1_cohort_summary,
    validate_psr1_enrollment_receipt,
    validate_study_promotion_receipt,
)


def check_receipt_file(kind: str, path: Path) -> list[str]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if kind == "enrollment":
        return validate_psr1_enrollment_receipt(data)
    if kind == "cohort":
        return validate_psr1_cohort_summary(data)
    if kind == "study":
        return validate_study_promotion_receipt(data)
    return [f"unknown receipt kind: {kind}"]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate PSR-1 / STUDY promotion receipt JSON files.")
    parser.add_argument("--enrollment", type=Path, default=None, help="Path to psr1_tier3_enrollment receipt JSON (#421)")
    parser.add_argument("--cohort", type=Path, default=None, help="Path to psr1_cohort_summary receipt JSON (#422)")
    parser.add_argument("--study", type=Path, default=None, help="Path to hosted_study_promotion receipt JSON (#423)")
    args = parser.parse_args(argv)

    checks = [
        ("enrollment", "#421", args.enrollment),
        ("cohort", "#422", args.cohort),
        ("study", "#423", args.study),
    ]
    failed = False
    for kind, ticket, path in checks:
        if path is None:
            print(f"[PENDING] {ticket} ({kind}): awaiting operator-supplied receipt")
            continue
        errors = check_receipt_file(kind, path)
        if errors:
            failed = True
            print(f"[FAIL] {ticket} ({kind}): " + "; ".join(errors))
        else:
            print(f"[PASS] {ticket} ({kind}): schema-valid receipt")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
