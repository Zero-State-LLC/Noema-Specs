# GC7 Crime Detection Evidence Algorithm — Design Note

**Status:** Design/research integration note. Inputs only. No contract, catalog, verb, or exposure change.

**Parents:** [STRATEGIC-CONFLICT.md](STRATEGIC-CONFLICT.md) · [GAME-COMPLETENESS-PLAN.md](GAME-COMPLETENESS-PLAN.md) (GC7) · [RFC-0002](../rfcs/RFC-0002-strategic-contestation-and-crime-events.md)

**Gap (SPEC-GAP-REGISTER-2026-08-25 B7b):** Published detection constants (`detection_base_millipoints`, `sensor_min_condition`) have no normative algorithm or runtime referent.

**Research inputs (2026-08-25 + prior):**
- First-hand / OCEAN observation preferred.
- Incomplete reputation information: missed observation, bad assessment, failed execution behave differently.
- Timely data > density for stabilization (from earlier hotspot models).
- Per-incident evidence, not aggregated.

**Proposed design framing (for future RFC):**
- Define a seeded, replayable evidence function for detection (false-positive / false-negative expectations stated).
- Use existing event provenance, condition, witnesses/sensors.
- Constants become inputs to the function, not magic.
- Output feeds `CRIME_DETECTED` (detection-only semantics per other seeds).
- No wall-clock randomness; deterministic from ledger + seeded RNG if needed for replay.

**Boundaries:** Pins the missing algorithm for producer. Research input only. Ties to NOTES-CRIME-DETECTION-EVIDENCE.md.

**Citations:** SPEC-GAP-REGISTER-2026-08-25.md (B7b), RESEARCH-ASSIMILATION-2026-08-25-CRIME.md, contest-config.v02.json, STRATEGIC-EVENT-COUPLING.md, RFC-0002, PR #305 + main continuation.

Smallest unit for the detection algorithm gap. Ready for RFC.