# Spec Completion Contract Micro-Note (Migration/Version Behavior) — Design Note

**Status:** Micro-note per GAME-COMPLETENESS-PLAN section 11. Inputs only. No contract, catalog, verb, or exposure change.

**Element:** Migration/version behavior.

**Coverage notes:**
- Versioned via RFC process + seed lineage (RFC-0002 event catalog 0.2, prior RFCs).
- Migration via backward-compatible extensions, provenance in Deep Time, replayable events.
- GC-specific: WED class evolution, culture threshold inheritance, construction class additions via seeds.

**Boundaries:** Notes only. Cites GAME-COMPLETENESS-PLAN.md section 11 + prior + main.

Smallest unit for migration/version element.

## Extension Points

Non-normative future guidance; no new behavioral authority or reopening of accepted/deferred slices.

- **Document-specific seam:** Add evidence links for construction-class, WED-class, and culture-inheritance version transitions.
- **Invariants, compatibility, promotion, and verification:** This note does not authorize migrations or retroactive seed changes. New version behavior requires accepted contracts specifying old-reader behavior and lineage; verify old fixtures remain valid, unsupported versions fail closed, and historical replay retains original pins.
