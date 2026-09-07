# GC8 Lot Grade Residuals — Design Note

**Status:** Design/research integration note. Inputs only. No contract, catalog, verb, or exposure change.

**Parents:** [ECONOMIC-SPECIALIZATION.md](ECONOMIC-SPECIALIZATION.md) · [GAME-COMPLETENESS-PLAN.md](GAME-COMPLETENESS-PLAN.md) (GC8) · accepted GC8 slice RFCs

**Gap (SPEC-GAP-REGISTER-2026-08-25 B8a):** Exact bounded lot-grade residuals remain after implemented quality/provenance slices.

**Proposed framing (for future RFC):**
- Lot-grade attributes (quality, provenance, condition effects) use closed, versioned tables.
- Bounded magnitudes only; no unbounded scaling.
- Visibility and transfer rules tie to existing TRADE/INSPECT surfaces.
- Provenance from Deep Time and construction/repair events.

**Boundaries:** Extends existing GC8 slices. No new verbs or unbounded mechanics. Research input only.

**Citations:** SPEC-GAP-REGISTER-2026-08-25.md (B8a), ECONOMIC-SPECIALIZATION.md, GC8-FIRST-SLICE.md and follow-ons, PR #305 + main continuation.

Smallest unit for GC8 lot-grade gap. Ready for RFC.

## Extension Points

Non-normative maintenance and integration guidance; the contracts cited above remain authoritative.

### Document-specific seam

Extend residual review by mapping a proposed lot attribute to its current quality/provenance contract, transfer behavior, and observable effect on an existing TRADE or INSPECT. Demonstrate a missing bounded case before proposing a new table entry.

### Compatibility and promotion

Accepted GC8 slices remain authoritative; this seed does not activate formal markets, v0.6B, new resources, or unbounded quality scaling. A historical construction/repair reference is not automatically lot provenance. New attributes or transfer semantics need an RFC and explicit compatibility review.

### Verification before adoption

Compare graded and ungraded legacy lots, transfer under the current pin, and unauthorized inspection. Test bounds and provenance preservation without inventing default grades for missing data. Reconcile the dated gap against accepted follow-ons; attach fixtures only for a genuine residual and never claim runtime completion from this seed.
