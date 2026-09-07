# GC1 S9–S11 Slices Closeout (Post 2026-08-27 Research)

**Status:** Design notes complete for listed remaining GC1 items.  
**Authorizing:** [MASTERY-SPECIALIZATION.md](MASTERY-SPECIALIZATION.md) (research assimilation 2026-08-27) · [GAME-COMPLETENESS-PLAN.md](GAME-COMPLETENESS-PLAN.md) · [POST-RESEARCH-ASSIMILATION-NEXT-10-STEPS-PLAN.md](POST-RESEARCH-ASSIMILATION-NEXT-10-STEPS-PLAN.md) · [MASTERY-SPECIALIZATION-RESEARCH-SEED.md](MASTERY-SPECIALIZATION-RESEARCH-SEED.md)

## Slices Delivered
- **GC1-S9 Multi-Focus**: Bounded active set (cap 1–3), maintenance credit on active, research-informed trajectory/skill-graph management. Builds directly on S7.
- **GC1-S10 Decay-Window Credit**: Extra idle tolerance only for active focus tracks. Builds on S3 + S7/S9. Research signals for autonomous focus selection to protect high-evidence tracks.
- **GC1-S11 Further Parameters**: Richer options on BUILD/TRADE/INSPECT for focused MAINTAINED specialists. Extends S8 pattern.

All:
- Same verbs only.
- No new events, no discounts, no class trees.
- Incorporate SkillMaster/autonomous mastery signals (trajectory review, compositional graphs, multi-track management) from 2026-08-27 assimilation.
- Cite doctrine, prior slices (S3, S7, S8), and research artifacts.

## Updates Made
- MASTERY-SPECIALIZATION.md: S9–S11 closed sections added; "Still open (later)" cleared for these items; research section refreshed.
- SPEC-CHECKLIST.md: Entries for S9–S11.
- GAME-COMPLETENESS-PLAN.md: New slices referenced under research seeds 2026-08-27.

## Remaining (explicitly left open for future RFC)
- Event types (if recognition ever becomes ledgered / canonical).
- Full RFC body, fixtures, conformance, and runtime implementation for S9–S11.

## Verification Notes
- All new docs follow established slice pattern (doctrine table, contract table, lines, runtime rule, citations).
- No mutation of shipped S0–S8, frozen v0.1–v0.7, or event catalog.
- Research integration is design-note only.

**Phase complete for these GC1 remaining items.** Ready for operator review → RFC drafting (smallest slices first) → re-derive.

See also: GC1-S9/10/11 docs, updated MASTERY-SPECIALIZATION.md, the 2026-08-27 research assimilation and handoff.

## Extension Points

Non-normative follow-on traceability guidance; the historical phase completion is design-note completion only.

- **Seam:** extend the delivered-slice list with a review ledger that separately records S9 active-set limits and replacement rules, S10 credit amount and timing, and S11 the exact additional BUILD/TRADE/INSPECT parameter shapes. Link each unresolved choice to its proposal and fixtures instead of treating the shared research provenance as a completed contract.
- **Retained invariants:** preserve shipped S0–S8 semantics and the historical closeout body. Same verbs, no class trees, no discounts, no new events, and no automatic recognition remain the boundary; research trajectories are not Player proficiency awards or public telemetry.
- **Compatibility/promotion:** an accepted successor RFC is needed before any S9–S11 mechanical or discovery change. Track dependency order explicitly and use [DIRECTION-AUTHORITY.md](DIRECTION-AUTHORITY.md) plus [current-state.v1.yaml](../specs/current-state.v1.yaml) for promotion claims; this closeout does not supply runtime or hosted evidence.
- **Proposed checks:** resolve all three slice references, compare each proposed parameter against S8 access rules, test cap/replacement and decay boundary fixtures under the selected contract, and confirm legacy requests remain valid. A review packet should fail if it presents an illustrative magnitude as pinned, silently changes S3 rehabilitation, or equates “closed” design notes with shipped behavior.
