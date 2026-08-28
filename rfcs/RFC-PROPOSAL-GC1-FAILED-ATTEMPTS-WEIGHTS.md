# RFC-PROPOSAL: GC1 Failed-but-Legal Practice Attempt Weights (B1a)

**Status:** Minimal draft proposal. Derived from design note. Inputs only until accepted.

**Parent gap:** SPEC-GAP-REGISTER-2026-08-25 B1a (OPEN_SPEC in GC1 mastery).

**Source design note:** [GC1-FAILED-ATTEMPTS-SEED.md](../docs/GC1-FAILED-ATTEMPTS-SEED.md)

**Proposed change (bounded):**
- Legal but failed practice attempts contribute to proficiency evidence at a lower, versioned weight than successful ones.
- Weighting is track-specific (per MASTERY-SPECIALIZATION), evidence-based only.
- No new verbs, events, mechanical benefits, XP, or levels. No impact on frozen v0.1–v0.7.
- Versioned via existing GC1 parameter surfaces; fails closed if evidence insufficient.

**Scope boundaries (per seed + doctrine):**
- Extends MASTERY-SPECIALIZATION.md and GC1-S9–S11 only.
- Does not create new Player-facing rewards for failure.
- Research/game membrane preserved; no runtime invention.

**Citations:**
- SPEC-GAP-REGISTER-2026-08-25.md (B1a)
- GC1-FAILED-ATTEMPTS-SEED.md
- MASTERY-SPECIALIZATION.md, GC1-FIRST-SLICE.md + S9–S11 slices
- GAME-COMPLETENESS-PLAN.md (GC1 continuation)
- PR #305 + main 2026-08 continuation (design notes pass)

**Readiness:** Smallest viable unit from the seed. Ready for review/acceptance as narrow RFC if Gate C evidence supports. No broader rebalance.

**Next smallest if accepted:** Implement in MASTERY-SPECIALIZATION parameters only.
