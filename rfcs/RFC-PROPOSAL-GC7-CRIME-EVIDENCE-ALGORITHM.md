# RFC-PROPOSAL: GC7 Crime Detection Evidence Algorithm (B7b)

**Status:** Minimal draft proposal. Derived from design note. Inputs only until accepted.

**Parent gap:** SPEC-GAP-REGISTER-2026-08-25 B7b (OPEN_SPEC in GC7 crime).

**Source design note:** [GC7-CRIME-EVIDENCE-ALGORITHM-SEED.md](../docs/GC7-CRIME-EVIDENCE-ALGORITHM-SEED.md)

**Proposed change (bounded):**
- Define a seeded, replayable evidence function for `CRIME_DETECTED` (with stated false-positive / false-negative expectations).
- Use existing event provenance, condition values, witnesses/sensors as inputs.
- Published constants (`detection_base_millipoints`, `sensor_min_condition`) become explicit inputs to the function (no longer magic).
- Output is strictly detection (feeds `CRIME_DETECTED` with detection-only semantics).
- Deterministic from ledger + seeded replayable RNG if needed; no wall-clock randomness.

**Scope boundaries (per seed + doctrine):**
- Pins the missing normative algorithm for the producer side.
- One narrow RFC for the function definition and expectations.
- Research input only. Ties to NOTES-CRIME-DETECTION-EVIDENCE.md and other B7 seeds.
- No new events; keeps detection semantics clean.

**Citations:**
- SPEC-GAP-REGISTER-2026-08-25.md (B7b)
- GC7-CRIME-EVIDENCE-ALGORITHM-SEED.md
- RESEARCH-ASSIMILATION-2026-08-25-CRIME.md
- contest-config.v02.json, STRATEGIC-EVENT-COUPLING.md, RFC-0002
- PR #305 + main 2026-08 continuation (design notes pass)

**Readiness:** Smallest viable unit from the seed for the detection algorithm gap. Ready for review/acceptance as narrow RFC.

**Next smallest if accepted:** Implement the evidence function (deterministic, replayable).
