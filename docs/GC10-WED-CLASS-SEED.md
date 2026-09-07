# GC10 WED Storm Classes and Irreversible Scars — Design Note

**Status:** Design/research integration note. Inputs only. No contract, catalog, verb, or exposure change.

**Parents:** [WORLD-EVENT-DIRECTOR.md](WORLD-EVENT-DIRECTOR.md) · [DEEP-TIME.md](DEEP-TIME.md) · [GAME-COMPLETENESS-PLAN.md](GAME-COMPLETENESS-PLAN.md) (GC10)

**Gaps (SPEC-GAP-REGISTER-2026-08-25 B10a/B10b):**
- Operator-triggered storm classes remain unpinned beyond bounded pressure families.
- Irreversible scar creation and recovery boundaries remain unpinned.

**Proposed framing (for future RFC):**
- Closed classes for WED pressure (preview, authorization, cooldown, rollback).
- Scar irreversibility with provenance, WATCH projection, and limited Player recovery paths.
- Ties to existing scheduled pressure and Deep Time.

**Boundaries:** Extends WED and Deep Time. No free-text spawn or history rewrite. Research input only.

**Citations:** SPEC-GAP-REGISTER-2026-08-25.md (B10a/B10b), WORLD-EVENT-DIRECTOR.md, DEEP-TIME.md, RFC-0014 + RFC-0027, PR #305 + main continuation.

Smallest units for GC10 gaps. Ready for RFC.

## Extension Points

Non-normative proposal-comparison seams for bounded pressures and scars.

- Extend the future-RFC packet with a per-candidate table of preview inputs, authorization, cooldown, provenance and the distinction between reversible operational recovery and an irreversible historical scar. Explicitly separate existing scheduled pressure from a proposed operator-triggered class.
- Preserve inputs-only status: no new class, scar creation rule, Player recovery entitlement or public exposure is authorized here. Free-text spawn and canonical history rewriting remain excluded; PLAY must not receive research class labels through translated planning copy.
- Compatibility/promotion: reconcile B10a/B10b with currently accepted WED/Deep Time authority before proposing change; historical “unpinned” status is not proof a gap remains. Any accepted expansion needs pinned schemas and replay/visibility fixtures rather than a design-note count.
- Verification proposal: require candidate cases for preview/activation agreement, denied authorizer, cooldown collision and attempted recovery that preserves scar provenance. Check WATCH receives only the approved public projection and replay retains the source events. Keep proposal acceptance, rejection and uncertainty readable in the ops/design table.
