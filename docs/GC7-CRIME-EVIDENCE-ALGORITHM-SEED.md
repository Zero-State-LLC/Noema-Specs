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

## Extension Points

Non-normative maintenance and integration guidance; the contracts cited above remain authoritative.

### Document-specific seam

Extend algorithm triage with a per-incident evidence trace that distinguishes missed observation, bad assessment, and failed execution. Identify how published detection constants would enter a versioned replayable function rather than assigning them an invented runtime meaning.

### Compatibility and promotion

This research seed does not implement a producer, activate constants, or settle guilt. Check current accepted detection contracts before opening any residual; closed work stays closed. No wall-clock randomness, private-cognition inference, automatic sanction, or new public exposure follows from an algorithm sketch.

### Verification before adoption

For any future proposal, require seeded repeatability, threshold-boundary cases, absent/invalid sensors, and false-positive/false-negative expectations. Separate CRIME_DETECTED production from consumption and projection. Tie each output to incident provenance and permission checks; mark missing evidence honestly rather than treating this planning note as observed detection.
