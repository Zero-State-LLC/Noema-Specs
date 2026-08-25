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
    "docs/LCA-GATE-A-PROMOTION-2026-08-25.md",
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
    # Both Specs commits are load-bearing and were previously unvalidated: the
    # baseline this package is written against, and the commit the live build
    # implements. They answer different questions and must not silently merge.
    for key in ("production_specs_baseline", "production_implements_specs"):
        value = parsed.get("evidence_commits", {}).get(key)
        if not isinstance(value, str) or not re.fullmatch(r"[0-9a-f]{7,40}", value):
            fail(f"{key} must be a Git commit")
    if parsed.get("evidence_commits", {}).get("production_specs_baseline") != "492ccc9":
        fail("production Specs baseline must pin canonical main 492ccc9 used for Gate A promotion")
    if parsed.get("capabilities", {}).get("integrated_small_civilization_run", {}).get("state") != "BLOCKED":
        fail("Gate C run must remain BLOCKED until Gate B passes")
    if parsed.get("active_campaign", {}).get("state") != "ACTIVE_INTEGRATION":
        fail("Living Civilization Alpha campaign must remain ACTIVE_INTEGRATION")
    implemented = parsed.get("runtimes", {}).get("advanced_worker_runtime", {}).get("implemented_systems")
    if not isinstance(implemented, list) or len(implemented) < 10:
        fail("advanced Worker implementation inventory is incomplete")
    for marker in (
        "schema_version: noema-current-state/1.0",
        "advanced_worker_runtime:",
        f"evidence_commit: {evidence_commit}",
        "production_implements_specs:",
        "production_specs_baseline: 492ccc9",
        "world: world.perihelion-reach-3",
        "required_endpoints: [/ready, /version]",
        "Noema PR #551",
        "Noema PR #552",
        "Noema PR #587",
        "current_milestone: LCA-2",
        "Gate A is complete",
        "remaining_lca2_prerequisites:",
        "integrated_small_civilization_run:",
        "state: ACTIVE_INTEGRATION",
        "Gate C remains unproven",
        "01ebc196-b762-4689-a166-272e26bd73ad",
        "hosted_live.worker_version_id matches live",
        "Noema PR #570",
        "61234cc",
        "canonical operator device enrollment",
    ):
        if marker not in state:
            fail(f"current state missing marker: {marker}")
    if "0bddbeb" in state:
        fail("production Specs baseline 0bddbeb is stale after canonical main 492ccc9")
    if "2bb3a8b4" in state:
        fail("current state must not claim stale Worker 2bb3a8b4")
    if "66f2417d" in state:
        fail("advanced Worker pin 66f2417d is stale after Noema #570")
    if "in-flight Noema #561" in state:
        fail("Noema #561 is merged; do not call it in-flight")
    if "noema-client #24 remains open" in state:
        fail("noema-client #24 is landed; do not call it open")

    used = set(re.findall(r"\b[A-Z][A-Z_]+\b", state)) & STATUSES
    missing = STATUSES - used
    if missing:
        fail(f"status vocabulary not exercised: {sorted(missing)}")

    campaign = (ROOT / "docs/LIVING-CIVILIZATION-ALPHA.md").read_text(encoding="utf-8")
    for marker in (
        "not a greenfield feature campaign",
        "Gate A is complete",
        "LCA-1",
        "LCA-5",
        "IMPLEMENTED_RUNTIME",
        "canonical operator enrollment",
        "Gate C remains unproven",
    ):
        if marker not in campaign:
            fail(f"campaign missing marker: {marker}")

    acceptance = (ROOT / "docs/LIVING-ALPHA-ACCEPTANCE.md").read_text(encoding="utf-8")
    for marker in (
        "Gate A is complete",
        "LCA-GATE-A-PROMOTION-2026-08-25.md",
        "lca2-gate-b-three-external-agent-population",
        "Gate C remains unproven",
        "compatibility-at-scale claim",
        "canonical operator device enrollment",
    ):
        if marker not in acceptance:
            fail(f"acceptance missing marker: {marker}")

    if "Gate A is not complete" in state or "Gate A is not complete" in campaign or "Gate A is not complete" in acceptance:
        fail("Gate A promotion is accepted; stale non-complete guidance remains")
    if "Gate A is complete" not in state or "Gate A is complete" not in campaign or "Gate A is complete" not in acceptance:
        fail("Gate A promotion must agree across machine state and campaign authorities")
    if "in-flight Noema #561" in campaign or "in-flight Noema #561" in acceptance:
        fail("Noema #561 is merged; do not call it in-flight")
    if "noema-client #24 remains open" in campaign or "noema-client #24 remains open" in acceptance:
        fail("noema-client #24 is landed; do not call it open")

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
