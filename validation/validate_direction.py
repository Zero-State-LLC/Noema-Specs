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
    evidence_commit = parsed.get("evidence_commits", {}).get("advanced_worker_runtime")
    if not isinstance(evidence_commit, str) or not re.fullmatch(r"[0-9a-f]{7,40}", evidence_commit):
        fail("advanced Worker evidence commit must be a Git commit")
    runtime_commit = parsed.get("runtimes", {}).get("advanced_worker_runtime", {}).get("evidence_commit")
    if runtime_commit != evidence_commit:
        fail("advanced Worker evidence commits disagree")
    implemented = parsed.get("runtimes", {}).get("advanced_worker_runtime", {}).get("implemented_systems")
    if not isinstance(implemented, list) or len(implemented) < 10:
        fail("advanced Worker implementation inventory is incomplete")
    for marker in (
        "schema_version: noema-current-state/1.0",
        "advanced_worker_runtime:",
        f"evidence_commit: {evidence_commit}",
        "world: world.perihelion-reach-3",
        "required_endpoints: [/ready, /version]",
        "Noema PR #551",
        "Noema PR #552",
        "current_milestone: LCA-1",
        "Gate A is not complete",
        "remaining_lca2_prerequisites:",
        "integrated_small_civilization_run:",
        "state: ACTIVE_INTEGRATION",
        "Gate C remains unproven",
        "d9aab067-e3ca-447c-bb8b-fccc59729bbf",
    ):
        if marker not in state:
            fail(f"current state missing marker: {marker}")

    used = set(re.findall(r"\b[A-Z][A-Z_]+\b", state)) & STATUSES
    missing = STATUSES - used
    if missing:
        fail(f"status vocabulary not exercised: {sorted(missing)}")

    campaign = (ROOT / "docs/LIVING-CIVILIZATION-ALPHA.md").read_text(encoding="utf-8")
    for marker in (
        "not a greenfield feature campaign",
        "LCA-1",
        "LCA-5",
        "IMPLEMENTED_RUNTIME",
        "Gate A is not complete",
        "remaining LCA-2 prerequisites",
        "Gate C remains unproven",
    ):
        if marker not in campaign:
            fail(f"campaign missing marker: {marker}")

    acceptance = (ROOT / "docs/LIVING-ALPHA-ACCEPTANCE.md").read_text(encoding="utf-8")
    for marker in (
        "Gate A is not complete",
        "lca2-gate-b-three-external-agent-population",
        "Gate C remains unproven",
        "compatibility-at-scale claim",
        "remaining LCA-2 prerequisites",
    ):
        if marker not in acceptance:
            fail(f"acceptance missing marker: {marker}")

    if "Gate A is complete" in campaign or "Gate A is complete" in acceptance:
        fail("Gate A must not be promoted without remaining LCA-2 prerequisite evidence")

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
