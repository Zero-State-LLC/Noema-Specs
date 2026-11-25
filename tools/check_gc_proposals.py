#!/usr/bin/env python3
"""Validate specs/gc-rfc-proposals.v1.json against rfcs/RFC-PROPOSAL-GC*.md and seed docs."""

from __future__ import annotations

import json
import sys
from pathlib import Path

VALID_STATUSES = {"draft", "accepted", "deferred", "superseded"}


def main() -> int:
    root = Path(__file__).resolve().parent.parent
    reg_path = root / "specs" / "gc-rfc-proposals.v1.json"
    if not reg_path.is_file():
        print("ERROR: specs/gc-rfc-proposals.v1.json missing", file=sys.stderr)
        return 1

    data = json.loads(reg_path.read_text(encoding="utf-8"))
    errors: list[str] = []

    adr = root / str(data.get("ratification_adr", ""))
    if not adr.is_file():
        errors.append(f"ratification_adr missing: {data.get('ratification_adr')}")

    proposals = data.get("proposals")
    if not isinstance(proposals, list) or not proposals:
        errors.append("proposals must be a non-empty list")
        proposals = []

    registered_paths: set[str] = set()
    for entry in proposals:
        pid = entry.get("id", "<missing>")
        rel_path = str(entry.get("path", ""))
        seed_doc = str(entry.get("seed_doc", ""))
        status = entry.get("status")
        if status not in VALID_STATUSES:
            errors.append(f"{pid}: invalid status {status!r}")
        if not (root / rel_path).is_file():
            errors.append(f"{pid}: missing RFC file {rel_path}")
        if not (root / seed_doc).is_file():
            errors.append(f"{pid}: missing seed_doc {seed_doc}")
        registered_paths.add(rel_path)

    disk_paths = {
        str(p.relative_to(root))
        for p in sorted((root / "rfcs").glob("RFC-PROPOSAL-*.md"))
    }
    unregistered = sorted(disk_paths - registered_paths)
    for rel in unregistered:
        errors.append(f"unregistered GC proposal on disk: {rel}")

    if errors:
        for err in errors:
            print(f"ERROR: {err}", file=sys.stderr)
        return 1

    print(json.dumps({"ok": True, "registered_proposals": len(proposals)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
