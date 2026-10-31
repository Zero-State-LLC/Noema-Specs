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
    "docs/LCA-GATE-E-PROMOTION-2026-09-20.md",
    "docs/LCA-GATE-F-PROMOTION-2026-09-21.md",
    "docs/EXECUTION-SEQUENCE-90-DAY.md",
    "docs/DIRECTION-AUTHORITY.md",
    "docs/POPULATION-AND-STUDY-READINESS.md",
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
    "GLOSSARY.md",
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


def check_campaign_invariant(campaign: dict) -> None:
    """An active Campaign must still have something to prove; any other state lists nothing (#361)."""
    name = campaign.get("id") or "<unnamed campaign>"
    unproven = campaign.get("unproven_gates") or []
    if campaign.get("state") == "ACTIVE_INTEGRATION":
        if not unproven:
            fail(f"campaign {name} is ACTIVE_INTEGRATION but lists no unproven_gates")
        if "COMPLETE" in str(campaign.get("active_gate") or ""):
            fail(f"campaign {name} is ACTIVE_INTEGRATION but its active_gate is already COMPLETE")
    elif unproven:
        fail(f"campaign {name} is {campaign.get('state')} but still lists unproven_gates")


GATE_ID = re.compile(r"\bPSR-\d+\b")
UNLOCKED_MARKERS = ("TO LOCK", "TO NAME")


def check_gate_contracts(campaign: dict, root: Path, campaign_doc: str) -> None:
    """Every unproven Gate has a linked scenario contract; an unblocked active Gate has no unlocked values (#379)."""
    contracts = campaign.get("gate_contracts") or {}
    for gate in campaign.get("unproven_gates") or []:
        match = GATE_ID.search(str(gate))
        if not match:
            continue
        gate_id = match.group(0)
        rel = contracts.get(gate_id)
        if not rel or not (root / rel).is_file():
            fail(f"Gate {gate_id} has no scenario contract in active_campaign.gate_contracts")
        if Path(rel).name not in campaign_doc:
            fail(f"Gate {gate_id} scenario contract {rel} is not linked from the campaign document")
    active_gate = str(campaign.get("active_gate") or "")
    match = GATE_ID.search(active_gate)
    if match and "BLOCKED" not in active_gate:
        text = (root / contracts[match.group(0)]).read_text(encoding="utf-8")
        for marker in UNLOCKED_MARKERS:
            if marker in text:
                fail(f"active Gate {match.group(0)} is no longer BLOCKED but its contract still says {marker}")


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
    gate_e = parsed.get("capabilities", {}).get("endurance_gate_e", {})
    if gate_e.get("state") != "LIVE_HOSTED":
        fail("Gate E endurance must be LIVE_HOSTED after promotion")
    if "Gate E is complete" not in str(gate_e.get("claim") or ""):
        fail("Gate E claim must record completion")
    gate_f = parsed.get("capabilities", {}).get("successor_decision_gate_f", {})
    if gate_f.get("state") != "LIVE_HOSTED":
        fail("Gate F successor decision must be LIVE_HOSTED after promotion")
    if "Gate F is complete" not in str(gate_f.get("claim") or ""):
        fail("Gate F claim must record completion")
    if parsed.get("surfaces", {}).get("study_hosted") != "BLOCKED":
        fail("hosted STUDY must remain BLOCKED after Gate F promotion")
    if parsed.get("capabilities", {}).get("hosted_study_pipeline", {}).get("state") != "BLOCKED":
        fail("hosted_study_pipeline must remain BLOCKED after Gate F promotion")
    gate_b = parsed.get("capabilities", {}).get("external_agent_population_gate_b", {})
    if gate_b.get("state") != "LIVE_HOSTED":
        fail("Gate B external population must be LIVE_HOSTED after promotion")
    if "Gate B is complete" not in str(gate_b.get("claim") or ""):
        fail("Gate B claim must record completion")
    active_campaign = parsed.get("active_campaign", {})
    check_campaign_invariant(active_campaign)
    check_gate_contracts(
        active_campaign,
        ROOT,
        (ROOT / "docs/POPULATION-AND-STUDY-READINESS.md").read_text(encoding="utf-8"),
    )
    if active_campaign.get("id") != "population-and-study-readiness":
        fail("active campaign must be population-and-study-readiness after the #361 direction packet")
    if active_campaign.get("supersedes") != "living-civilization-alpha":
        fail("active campaign must record that it supersedes living-civilization-alpha")
    prior = {c.get("id"): c for c in parsed.get("completed_campaigns") or []}.get("living-civilization-alpha")
    if not prior or len(prior.get("completed_gates") or []) != 6:
        fail("living-civilization-alpha must be recorded in completed_campaigns with Gates A-F")
    psr1_contract = (ROOT / str(active_campaign.get("gate_contracts", {}).get("PSR-1", ""))).read_text(encoding="utf-8")
    if "TO LOCK" in psr1_contract:
        fail("PSR-1 criteria are locked (#381); its scenario contract must not contain TO LOCK")
    if "prerequisites open" not in str(active_campaign.get("active_gate") or ""):
        fail("PSR-1 active_gate must name its open prerequisites until they close (#381)")
    if parsed.get("capabilities", {}).get("spark_orin_nvidia_stack", {}).get("state") != "SPECULATIVE":
        fail("spec 014 Spark/Orin stack must be SPECULATIVE (no implementation authority)")
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
        "current_milestone: PSR-1",
        "Gate A is complete",
        "Gate B is complete",
        "Gate C is complete",
        "Gate D is complete",
        "Gate E is complete",
        "remaining_lca2_prerequisites:",
        "integrated_small_civilization_run:",
        "watch_legibility_gate_d:",
        "endurance_gate_e:",
        "successor_decision_gate_f:",
        "state: ACTIVE_INTEGRATION",
        "Gate F is complete",
        "Noema PR #570",
        "61234cc",
        "canonical operator device enrollment",
        "LCA-GATE-B-PROMOTION-2026-09-08.md",
        "LCA-GATE-C-PROMOTION-2026-09-08.md",
        "LCA-GATE-D-PROMOTION-2026-09-09.md",
        "LCA-GATE-E-PROMOTION-2026-09-20.md",
        "LCA-GATE-F-PROMOTION-2026-09-21.md",
        "acceptance_authority_digest:",
        "lca3-gate-c-existing-system-civilization",
        "lca4-gate-d-watch-legibility",
        "lca5-gate-e-endurance",
        "lca6-gate-f-successor-decision",
        "path8_recover_json:",
        "592c06a4-fa8c-40f6-bec7-21cbc45689f9",
        "e5603e4b-7565-4e4a-a8d1-85360558a8ef",
        "1e52e827-695c-4386-9795-d42b175ec166",
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
        "Gate E is complete",
        "LCA-1",
        "LCA-5",
        "IMPLEMENTED_RUNTIME",
        "canonical operator enrollment",
        "Gate F is complete",
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
        "LCA-GATE-E-PROMOTION-2026-09-20.md",
        "LCA-GATE-F-PROMOTION-2026-09-21.md",
        "lca2-gate-b-three-external-agent-population",
        "lca3-gate-c-existing-system-civilization",
        "lca4-gate-d-watch-legibility",
        "lca5-gate-e-endurance",
        "lca6-gate-f-successor-decision",
        "Gate D is complete",
        "Gate E is complete",
        "Gate F is complete",
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
    if "Gate E is complete" not in state or "Gate E is complete" not in campaign or "Gate E is complete" not in acceptance:
        fail("Gate E promotion must agree across machine state and campaign authorities")
    if "Gate E remains unproven" in state or "Gate E remains unproven" in campaign or "Gate E remains unproven" in acceptance:
        fail("Gate E promotion is accepted; stale unproven guidance remains")
    if "Gate E is not complete" in state or "Gate E is not complete" in campaign or "Gate E is not complete" in acceptance:
        fail("Gate E promotion is accepted; stale non-complete guidance remains")
    if "Gate F is complete" not in state or "Gate F is complete" not in campaign or "Gate F is complete" not in acceptance:
        fail("Gate F promotion must agree across machine state and campaign authorities")
    if "Gate F remains unproven" in state or "Gate F remains unproven" in campaign or "Gate F remains unproven" in acceptance:
        fail("Gate F promotion is accepted; stale unproven guidance remains")
    if "Gate F is not complete" in state or "Gate F is not complete" in campaign or "Gate F is not complete" in acceptance:
        fail("Gate F promotion is accepted; stale non-complete guidance remains")
    # Living Alpha closed at LCA-5 without an LCA-6; the next Campaign uses its own milestone ids.
    if prior.get("final_milestone") != "LCA-5":
        fail("living-civilization-alpha must close at LCA-5 (no LCA-6)")
    if str(active_campaign.get("current_milestone", "")).startswith("LCA-"):
        fail("the next campaign must not extend Living Alpha milestone numbering (no LCA-6)")
    if "compatibility-at-scale" not in str(active_campaign.get("active_gate") or "").lower():
        fail("first active gate must be compatibility-at-scale (#363) per the #361 direction packet")
    roadmap = (ROOT / "docs/ROADMAP.md").read_text(encoding="utf-8")
    if "POPULATION-AND-STUDY-READINESS.md" not in roadmap:
        fail("ROADMAP current direction must point at the next campaign")
    if "no further Living Alpha gate" in str(active_campaign):
        fail("active campaign must not carry the superseded 'no further Living Alpha gate' guidance")
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
