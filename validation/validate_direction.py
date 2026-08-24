#!/usr/bin/env python3
from __future__ import annotations

import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = [
    "docs/LIVING-CIVILIZATION-ALPHA.md",
    "docs/CIVILIZATION-CAPABILITY-MATRIX.md",
    "docs/LIVING-ALPHA-ACCEPTANCE.md",
    "docs/EXECUTION-SEQUENCE-90-DAY.md",
    "docs/DIRECTION-AUTHORITY.md",
    "specs/current-state.v1.yaml",
]
STATUSES = {
    "LIVE_HOSTED",
    "IMPLEMENTED_RUNTIME",
    "IMPLEMENTED_OFFLINE",
    "SPEC_COMPLETE",
    "ACTIVE_INTEGRATION",
    "NEXT",
    "BLOCKED",
    "DEFERRED",
    "SPECULATIVE",
    "RETIRED",
}
FORBIDDEN_LIVE_GUIDANCE = [
    "Humans and agents are both Players",
    "humans and agents are both Players",
    "humans and agents both Players",
    "both are Players",
    "human browser → human Controller → Player",
    "human-controlled Player",
    "Human Player lifecycle",
    "PLAY is the only primary action",
    "human/agent Player parity remain frozen",
]

ONTOLOGY_AUTHORITY_FILES = [
    "docs/TERMINOLOGY.md",
    "docs/AGENT-INTERFACE.md",
    "docs/ARCHITECTURE.md",
    "docs/ADMIN-LIVE-OPERATIONS.md",
    "docs/AUTH-AND-IDENTITY.md",
    "docs/DATA-MODEL.md",
    "docs/PLATFORM.md",
    "docs/ROADMAP.md",
    "SPEC-CHECKLIST.md",
]


def fail(message: str) -> None:
    raise SystemExit(f"FAIL: {message}")


def main() -> None:
    for rel in REQUIRED:
        if not (ROOT / rel).is_file():
            fail(f"missing direction artifact: {rel}")

    state_path = ROOT / "specs/current-state.v1.yaml"
    state = state_path.read_text(encoding="utf-8")
    parsed = yaml.safe_load(state)
    if not isinstance(parsed, dict):
        fail("current state must parse as a mapping")
    if parsed.get("schema_version") != "noema-current-state/1.0":
        fail("unexpected current-state schema version")
    if parsed.get("evidence_commits", {}).get("advanced_worker_runtime") != "63869fb":
        fail("advanced Worker evidence commit is not pinned")
    implemented = parsed.get("runtimes", {}).get("advanced_worker_runtime", {}).get("implemented_systems")
    if not isinstance(implemented, list) or len(implemented) < 10:
        fail("advanced Worker implementation inventory is incomplete")
    for marker in (
        "schema_version: noema-current-state/1.0",
        "advanced_worker_runtime:",
        "evidence_commit: 63869fb",
        "integrated_small_civilization_run:",
        "state: ACTIVE_INTEGRATION",
    ):
        if marker not in state:
            fail(f"current state missing marker: {marker}")

    used = set(re.findall(r"\b[A-Z][A-Z_]+\b", state)) & STATUSES
    missing = STATUSES - used
    if missing:
        fail(f"status vocabulary not exercised: {sorted(missing)}")

    campaign = (ROOT / "docs/LIVING-CIVILIZATION-ALPHA.md").read_text(encoding="utf-8")
    for marker in ("not a greenfield feature campaign", "LCA-1", "LCA-5", "IMPLEMENTED_RUNTIME"):
        if marker not in campaign:
            fail(f"campaign missing marker: {marker}")

    corpus = "\n".join((ROOT / rel).read_text(encoding="utf-8") for rel in ONTOLOGY_AUTHORITY_FILES)
    for stale in FORBIDDEN_LIVE_GUIDANCE:
        if stale in corpus:
            fail(f"stale live guidance remains: {stale}")

    for rel in REQUIRED[:-1]:
        text = (ROOT / rel).read_text(encoding="utf-8")
        if "current-state.v1.yaml" not in text and rel != "docs/LIVING-ALPHA-ACCEPTANCE.md":
            fail(f"direction artifact lacks current-state link: {rel}")

    print("OK: direction package is complete, implementation-aware, and status-disciplined")


if __name__ == "__main__":
    main()
