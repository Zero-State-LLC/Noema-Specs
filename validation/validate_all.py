#!/usr/bin/env python3
"""NOEMA-Specs merge-gate validator."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def fail(msg: str) -> None:
    print(f"FAIL: {msg}")
    sys.exit(1)

def ok(msg: str) -> None:
    print(f"OK: {msg}")

def check_required_structure() -> None:
    required = [
        "README.md", "CONTEXT.md", "AGENTS.md", "CONTRIBUTING.md",
        "SECURITY.md", "CHANGELOG.md", ".env.example", "SPEC-CHECKLIST.md",
        "docs/VISION.md", "docs/ARCHITECTURE.md", "docs/WORLD-ENGINE.md",
        "docs/OBSERVATION.md", "docs/AGENT-INTERFACE.md", "docs/REPLAY.md",
        "docs/EVENT-CATALOG.md", "docs/ENVIRONMENT.md", "docs/ROADMAP.md",
        "protocols/agent-protocol-v1.md", "protocols/event-ledger-v1.md",
        "protocols/mud-command-v1.md", "protocols/replay-protocol-v1.md",
        "specs/agent-manifest.schema.json", "specs/observation.schema.json",
        "specs/world-event.schema.json", "specs/phenomenon-case.schema.json",
        "research/phenomena-ontology.md", "research/claims-policy.md",
        "rfcs/README.md", "rfcs/RFC-0000-template.md",
        "adr/README.md",
    ]
    missing = [p for p in required if not (ROOT / p).exists()]
    if missing:
        fail(f"Missing required paths: {missing}")
    ok("Required structure present")

def check_json_files() -> None:
    schemas = list((ROOT / "specs").glob("*.json")) if (ROOT / "specs").exists() else []
    examples = []
    if (ROOT / "examples").exists():
        examples = list((ROOT / "examples").rglob("*.json")) + list((ROOT / "examples").rglob("*.jsonl"))
    for path in schemas + examples:
        try:
            text = path.read_text(encoding="utf-8")
            if path.suffix == ".jsonl":
                for i, line in enumerate(text.splitlines(), 1):
                    if line.strip():
                        json.loads(line)
            else:
                json.loads(text)
        except Exception as e:
            fail(f"JSON parse error in {path.relative_to(ROOT)}: {e}")
    ok(f"Parsed {len(schemas)} schemas and {len(examples)} example JSON/JSONL files")

def check_markdown_links() -> None:
    link_re = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
    broken = []
    for md in ROOT.rglob("*.md"):
        if ".git" in md.parts:
            continue
        text = md.read_text(encoding="utf-8")
        for _, target in link_re.findall(text):
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            clean = target.split("#")[0]
            if not clean:
                continue
            resolved = (md.parent / clean).resolve()
            try:
                resolved.relative_to(ROOT)
            except ValueError:
                continue
            if not resolved.exists():
                broken.append(f"{md.relative_to(ROOT)} -> {target}")
    if broken:
        fail("Broken relative links:\n  " + "\n  ".join(broken[:20]))
    ok("Internal Markdown links resolve")

def check_claim_labels() -> None:
    path = ROOT / "research" / "phenomena-ontology.md"
    if not path.exists():
        fail("Missing phenomena-ontology.md")
    text = path.read_text(encoding="utf-8")
    if "do not create a scalar consciousness score" not in text.lower() and "Do not create a scalar consciousness score" not in text:
        fail("Phenomena ontology missing explicit ban on scalar consciousness score")
    ok("Claim-label and consciousness policy scan clean")

def main() -> None:
    print("NOEMA-Specs validation")
    check_required_structure()
    check_json_files()
    check_markdown_links()
    check_claim_labels()
    print("\nPASS")

if __name__ == "__main__":
    main()
