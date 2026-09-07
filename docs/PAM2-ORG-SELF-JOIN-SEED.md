# PAM2 Organization Self-Join — Design Note

**Status:** Design/research integration note. Inputs only. No contract, catalog, verb, or exposure change.

**Gap (SPEC-GAP-REGISTER-2026-08-25 PAM2):** Organization self-join remains unpinned.

**Proposed framing (for future RFC if needed):** Narrow membership RFC with authority, visibility, and failure semantics. Only if onboarding requires it. No unconditional self-membership.

**Boundaries:** Out of core GC scope. Research input only. Deferred unless onboarding evidence demands it.

**Citations:** SPEC-GAP-REGISTER-2026-08-25.md (PAM2), PLAYER-ACTION-MAP.md, organization authority docs, PR #305 + main continuation.

PAM2 residual deferred. No new design needed for GC1-10.

## Extension Points

Non-normative future guidance; no new behavioral authority or reopening of accepted/deferred slices.

- **Document-specific seam:** Collect onboarding evidence demonstrating whether lack of self-join actually blocks an authorized membership path.
- **Invariants, compatibility, promotion, and verification:** PAM2 remains deferred, outside core GC scope, with no unconditional self-membership. Only that evidence can motivate a separate RFC pinning authority, visibility, and failures; verify unknown/private org handling and unauthorized joins before any promotion.
