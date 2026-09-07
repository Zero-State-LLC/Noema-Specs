# GC4 Broader Conflict-of-Interest and Extra Office Profiles — Design Note

**Status:** Design/research integration note. Inputs only. No contract, catalog, verb, or exposure change.

**Parents:** [INSTITUTIONAL-AUTHORITY.md](INSTITUTIONAL-AUTHORITY.md) · [GAME-COMPLETENESS-PLAN.md](GAME-COMPLETENESS-PLAN.md) (GC4) · GC4-FIRST-SLICE.md + follow-on slices

**Gap (SPEC-GAP-REGISTER-2026-08-25 B4):** Broader conflict-of-interest and extra office profiles remain edge cases.

**Proposed framing (for future RFC):**
- Conflict-of-interest rules as versioned office constraints (e.g., cannot hold overlapping roles with financial overlap).
- Extra office profiles (advisor, specialist) as bounded extensions of core founder/officer/member/advisor.
- Ties to GC4 emergency scopes and succession.
- Enforcement via ROLE_VACATED or review triggers.

**Boundaries:** Extends existing GC4 authority. No superuser or implicit privileges. Research input only.

**Citations:** SPEC-GAP-REGISTER-2026-08-25.md (B4), INSTITUTIONAL-AUTHORITY.md, GC4-S* slices, PR #305 + main continuation.

Smallest unit for GC4 COI gap. Ready for RFC.

## Extension Points

Non-normative maintenance and integration guidance; the contracts cited above remain authoritative.

### Document-specific seam

Extend residual triage with a concrete conflicting office assignment or financial overlap that existing bounded grants cannot express. Record the affected authority profile, expected refusal, and the accepted rule that is insufficient before proposing a new constraint.

### Compatibility and promotion

This seed is not executable. In particular, the proposed ROLE_VACATED wording above grants no event authority; closed catalogs and existing succession events win. Extra profile names never imply capabilities, and no automatic vacancy, superuser, or institutional privilege is created by this EP.

### Verification before adoption

Compare overlap and non-overlap cases, vacant and occupied seats, and inherited versus newly assigned authority. First check the accepted GC4 slices for an existing solution. Promote only a demonstrated residual through the RFC/schema/fixture process; absent that, retain design-input status and no runtime enforcement claim.
