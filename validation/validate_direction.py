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
    "docs/LCA-GATE-B-PROMOTION-2026-09-08.md",
    "docs/LCA-GATE-C-PROMOTION-2026-09-08.md",
    "docs/LCA-GATE-D-PROMOTION-2026-09-09.md",
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
    gate_c = parsed.get("capabilities", {}).get("integrated_small_civilization_run", {})
    if gate_c.get("state") != "LIVE_HOSTED":
        fail("Gate C run must be LIVE_HOSTED after promotion")
    if "Gate C is complete" not in str(gate_c.get("claim") or ""):
        fail("Gate C claim must record completion")
    gate_d = parsed.get("capabilities", {}).get("watch_legibility_gate_d", {})
    if gate_d.get("state") != "LIVE_HOSTED":
        fail("Gate D WATCH legibility must be LIVE_HOSTED after promotion")
    if "Gate D is complete" not in str(gate_d.get("claim") or ""):
        fail("Gate D claim must record completion")
    if parsed.get("surfaces", {}).get("study_hosted") != "BLOCKED":
        fail("hosted STUDY must remain BLOCKED after Gate D promotion")
    if parsed.get("capabilities", {}).get("hosted_study_pipeline", {}).get("state") != "BLOCKED":
        fail("hosted_study_pipeline must remain BLOCKED after Gate D promotion")
    gate_b = parsed.get("capabilities", {}).get("external_agent_population_gate_b", {})
    if gate_b.get("state") != "LIVE_HOSTED":
        fail("Gate B external population must be LIVE_HOSTED after promotion")
    if "Gate B is complete" not in str(gate_b.get("claim") or ""):
        fail("Gate B claim must record completion")
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
        "current_milestone: LCA-4",
        "Gate A is complete",
        "Gate B is complete",
        "Gate C is complete",
        "Gate D is complete",
        "remaining_lca2_prerequisites:",
        "integrated_small_civilization_run:",
        "watch_legibility_gate_d:",
        "state: ACTIVE_INTEGRATION",
        "Gate E remains unproven",
        "Noema PR #570",
        "61234cc",
        "canonical operator device enrollment",
        "LCA-GATE-B-PROMOTION-2026-09-08.md",
        "LCA-GATE-C-PROMOTION-2026-09-08.md",
        "LCA-GATE-D-PROMOTION-2026-09-09.md",
        "acceptance_authority_digest:",
        "lca3-gate-c-existing-system-civilization",
        "lca4-gate-d-watch-legibility",
        "path8_recover_json:",
        "592c06a4-fa8c-40f6-bec7-21cbc45689f9",
    ):
        if marker not in state:
            fail(f"current state missing marker: {marker}")
    # The live Worker id is a deployment fact, not a constant. Pinning a literal
    # id here previously froze a stale value into the validator: correcting the
    # file to the real live Worker would have failed validation. Check the shape
    # and the internal agreement instead, and let validate_freshness compare the
    # recorded pin against GET /version.
    live_ids = {
        parsed.get("evidence_commits", {}).get("live_worker_version_id"),
        parsed.get("runtimes", {}).get("production_alpha", {}).get("live_worker_version_id"),
    }
    if len(live_ids) != 1:
        fail("live Worker id disagrees between evidence_commits and runtimes.production_alpha")
    live_id = live_ids.pop()
    if not isinstance(live_id, str) or not re.fullmatch(r"[0-9a-f]{8}(-[0-9a-f]{4}){3}-[0-9a-f]{12}", live_id):
        fail("live Worker id must be a Worker version UUID")
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
        "Gate B is complete",
        "Gate C is complete",
        "Gate D is complete",
        "LCA-1",
        "LCA-5",
        "IMPLEMENTED_RUNTIME",
        "canonical operator enrollment",
        "Gate E remains unproven",
    ):
        if marker not in campaign:
            fail(f"campaign missing marker: {marker}")

    acceptance = (ROOT / "docs/LIVING-ALPHA-ACCEPTANCE.md").read_text(encoding="utf-8")
    for marker in (
        "Gate A is complete",
        "Gate B is complete",
        "Gate C is complete",
        "LCA-GATE-A-PROMOTION-2026-08-25.md",
        "LCA-GATE-B-PROMOTION-2026-09-08.md",
        "LCA-GATE-C-PROMOTION-2026-09-08.md",
        "LCA-GATE-D-PROMOTION-2026-09-09.md",
        "lca2-gate-b-three-external-agent-population",
        "lca3-gate-c-existing-system-civilization",
        "lca4-gate-d-watch-legibility",
        "Gate D is complete",
        "Gate E remains unproven",
        "compatibility-at-scale claim",
        "canonical operator device enrollment",
    ):
        if marker not in acceptance:
            fail(f"acceptance missing marker: {marker}")

    if "Gate A is not complete" in state or "Gate A is not complete" in campaign or "Gate A is not complete" in acceptance:
        fail("Gate A promotion is accepted; stale non-complete guidance remains")
    if "Gate A is complete" not in state or "Gate A is complete" not in campaign or "Gate A is complete" not in acceptance:
        fail("Gate A promotion must agree across machine state and campaign authorities")
    if "Gate B is complete" not in state or "Gate B is complete" not in campaign or "Gate B is complete" not in acceptance:
        fail("Gate B promotion must agree across machine state and campaign authorities")
    if "Gate B is not complete" in state or "Gate B is not complete" in campaign or "Gate B is not complete" in acceptance:
        fail("Gate B promotion is accepted; stale non-complete guidance remains")
    if "Gate C is complete" not in state or "Gate C is complete" not in campaign or "Gate C is complete" not in acceptance:
        fail("Gate C promotion must agree across machine state and campaign authorities")
    if "Gate C is not complete" in state or "Gate C is not complete" in campaign or "Gate C is not complete" in acceptance:
        fail("Gate C promotion is accepted; stale non-complete guidance remains")
    if "Gate D is complete" not in state or "Gate D is complete" not in campaign or "Gate D is complete" not in acceptance:
        fail("Gate D promotion must agree across machine state and campaign authorities")
    if "Gate D remains unproven" in state or "Gate D remains unproven" in campaign or "Gate D remains unproven" in acceptance:
        fail("Gate D promotion is accepted; stale unproven guidance remains")
    if "Gate D is not complete" in state or "Gate D is not complete" in campaign or "Gate D is not complete" in acceptance:
        fail("Gate D promotion is accepted; stale non-complete guidance remains")
    if parsed.get("active_campaign", {}).get("current_milestone") != "LCA-4":
        fail("campaign current_milestone must remain LCA-4 after Gate D promotion (endurance is still Gate E)")
    if parsed.get("active_campaign", {}).get("next_milestone") != "LCA-5":
        fail("campaign next_milestone must remain LCA-5 after Gate D promotion")
    active_gate = str(parsed.get("active_campaign", {}).get("active_gate") or "")
    if "Gate E" not in active_gate:
        fail("campaign active_gate must be Gate E endurance after Gate D promotion")
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
