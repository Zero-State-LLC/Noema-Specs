#!/usr/bin/env python3
"""Validate LCA-2 Gate B requirement and changed-output traceability coverage."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TRACE = ROOT / "docs/LCA2-GATE-B-TRACEABILITY.md"
RUNBOOK = ROOT / "docs/LCA2-GATE-B-PREPARATION.md"
ACCEPTANCE = ROOT / "docs/LIVING-ALPHA-ACCEPTANCE.md"
ROADMAP = ROOT / "docs/ROADMAP.md"
STATE = ROOT / "specs/current-state.v1.yaml"

IDS = [
    "CHK-SPECS", "CHK-DOC", "CHK-PY", "CHK-WORKER", "CHK-HTTP", "CHK-WS", "CHK-ISO", "CHK-SHELL", "CHK-TRACE",
    *(f"E-{i:02d}" for i in range(1, 10)),
    *(f"R-{i:02d}" for i in range(1, 17)),
    *(f"P-{i:02d}" for i in range(1, 7)),
    *(f"A-{i:02d}" for i in range(1, 10)),
    *(f"V-{i:02d}" for i in range(1, 5)),
    *(f"S-{i:02d}" for i in range(1, 8)),
    *(f"C-{i:02d}" for i in range(1, 8)),
]


def main() -> None:
    for path in (TRACE, RUNBOOK, ACCEPTANCE, ROADMAP, STATE):
        if not path.exists():
            raise SystemExit(f"FAIL: missing required file: {path}")

    text = TRACE.read_text()
    missing = [identifier for identifier in IDS if f"`{identifier}`" not in text]
    if missing:
        raise SystemExit(f"FAIL: missing traceability rows: {', '.join(missing)}")

    runbook_text = RUNBOOK.read_text()
    acceptance_text = ACCEPTANCE.read_text()
    roadmap_text = ROADMAP.read_text()
    state_text = STATE.read_text()
    if "LCA2-GATE-B-TRACEABILITY.md" not in runbook_text:
        raise SystemExit("FAIL: traceability matrix is not linked from the Gate B runbook")
    if "LCA2-GATE-B-PREPARATION.md" not in acceptance_text or "LCA2-GATE-B-PREPARATION.md" not in roadmap_text:
        raise SystemExit("FAIL: preparation packet links are missing")
    if "  external_agent_population_gate_b:\n    state: BLOCKED\n" not in state_text:
        raise SystemExit("FAIL: external_agent_population_gate_b is not BLOCKED")
    if "  integrated_small_civilization_run:\n    state: BLOCKED" not in state_text:
        raise SystemExit("FAIL: Gate C integration state is not BLOCKED")
    if "REPRESENTATIVE VALIDATION COMPLETE" not in text:
        raise SystemExit("FAIL: matrix must identify representative, not complete external, validation")
    if "No production enrollment, deployment, or world mutation was performed" not in text:
        raise SystemExit("FAIL: matrix is missing the no-production-mutation boundary")
    if "Bearer eyJ" in text or "BEGIN PRIVATE KEY" in text:
        raise SystemExit("FAIL: traceability matrix contains credential-like material")

    print(f"OK: {len(IDS)} Gate B requirement/output rows mapped to checks and observed results")
    print("OK: preparation/runbook links resolve and Gate B plus Gate C remain BLOCKED")
    print("OK: representative-validation and credential-safety boundaries preserved")


if __name__ == "__main__":
    main()
