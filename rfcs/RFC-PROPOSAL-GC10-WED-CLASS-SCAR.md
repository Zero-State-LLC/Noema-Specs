# RFC-PROPOSAL: GC10 WED Storm Classes and Irreversible Scars (B10a/B10b)

**Status:** Minimal draft proposal, **scar half corrected 2026-08-31**. Derived from design note. Inputs only until accepted.

**Correction.** This note was drafted against `B10b` while that row said scar creation and recovery boundaries "remain unpinned". The row was stale and is corrected at source; [RFC-0051](RFC-0051-irreversible-scar.md) (GC10-S2, **Accepted**) already pins most of the scar bullet below:

| Proposed here | RFC-0051 |
|---|---|
| scar irreversibility | "a scar is **not** repairable" |
| provenance | public `DISMANTLE` → `ENTITY_DESTROY`, then a `scar=true` `RUIN` labelled `scarred-{class}` |
| WATCH projection | "PLAY MAY say `A scar remains.` **WATCH silent**" — the projection decision is made, not open |
| recovery paths | "pressure does not scar"; scheduled pressure stays recoverable; the class slot is freed for rebuild |

RFC-0051 is not in this note's citations. Re-proposing those four would duplicate an Accepted RFC.

**What survives on the scar side:** scar provenance from causes other than public `DISMANTLE`, which RFC-0051 does not reach.

**The storm-class half stands unchanged.** `B10a` was audited and is accurate: [RFC-0027](RFC-0027-additional-world-pressure.md) pins three bounded pressure classes and explicitly **rejects** broader engines rather than pinning them, so closed operator-triggered classes with preview, authorization, receipts, cooldown and rollback remain genuinely unpinned and are the useful part of this proposal.

**Parent gaps:** SPEC-GAP-REGISTER-2026-08-25 B10a/B10b (OPEN_SPEC in GC10).

**Source design note:** [GC10-WED-CLASS-SEED.md](../docs/GC10-WED-CLASS-SEED.md)

**Proposed change (bounded):**
- Closed classes for operator-triggered WED pressure (preview, authorization, receipts, cooldown, rollback). **This is the live half.**
- ~~Scar irreversibility with provenance, WATCH projection, and limited Player recovery paths.~~ Pinned by RFC-0051; see the correction above. Only scar provenance from causes other than public `DISMANTLE` remains.
- Ties to existing scheduled/authorized pressure and Deep Time.

**Scope boundaries (per seed + doctrine):**
- One narrow RFC for closed classes and scar boundaries.
- Extends WED and Deep Time. No free-text spawn or history rewrite.
- Research input only.

**Citations:**
- SPEC-GAP-REGISTER-2026-08-25.md (B10a/B10b)
- GC10-WED-CLASS-SEED.md
- WORLD-EVENT-DIRECTOR.md, DEEP-TIME.md, RFC-0014 + RFC-0027, [RFC-0051](RFC-0051-irreversible-scar.md) (added 2026-08-31; closes the scar bullet)
- GAME-COMPLETENESS-PLAN.md (GC10)
- PR #305 + main 2026-08 continuation

**Readiness:** Smallest viable units from the seed for WED classes and scars. Ready for review as narrow RFC.

**Next smallest if accepted:** Implement in WED parameters and Deep Time scar mechanics.
