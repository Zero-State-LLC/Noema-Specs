# Next

The current hand-off: latest review verdict and the next work order. Whoever finishes a slice or a review overwrites this file. Read it at the start of a session.

## Latest slice (2026-11-11): reconcile landed evidence and unchanged gates

- **Per-GC fixture inventory:** [#394](https://github.com/Zero-State-LLC/Noema-Specs/pull/394) is merged at `b572ea9f087f1498b4e19e99955fa1b918fac77f`. [SPEC-COMPLETION-FIXTURES-INVENTORY.md](../SPEC-COMPLETION-FIXTURES-INVENTORY.md) records 83 `examples/gc*` packs and 458 fixtures; every GC1–GC10 has executed positive and negative fixtures. Issue #388 is closed. The checklist's fixture row was already checked by that landing; this slice corrects only its stale explanatory sentence. This is Specs fixture/validator evidence, not runtime, hosted or gate acceptance.
- **WATCH D3 per-visit note:** [#393](https://github.com/Zero-State-LLC/Noema-Specs/pull/393) is merged at `69353da2079adece6cae5dbc7f1d800fc7d07c7b`, not waiting for review. Its adopted scope is unchanged.
- **PSR-2 summary:** [the campaign exit](../POPULATION-AND-STUDY-READINESS.md#exit-criteria) now repeats the existing [scenario Exit](../PSR-2-STUDY-READINESS-SCENARIO.md#exit): only after the complete evidence pack and Danny human-yes may `hosted_study_pipeline` move BLOCKED → NEXT. `surfaces.study_hosted` stays BLOCKED pending its separate hosting RFC. No gate has been promoted or hosting authorized.

**Review state:** this documentation reconciliation still requires its own review and CI before landing. No checkbox, RFC status, machine-state, schema, fixture, validator or runtime change is included.

## Next work order

1. **#364 stays open.** The RFC-0128 Review and verification checkboxes remain unchecked. An accountable reviewer must compare the RFC against PLAYER-TEMPO.md and FIRST-WORLD-OPERATIONS.md and record the actual decision before either task changes. MUD R4 retains its separate runtime matrix and follow-ups; do not promote it from fixture inventory completion.
2. **Slice-level fixture gaps** (recorded in the inventory, not filled): `gc2-thaw-play`, `gc7-thaw-play`, `gc3-decay-rehab` and `gc8-lot-quality` have no negative fixture of their own. Adding one needs the owning slice's authority, not this inventory or docs cleanup.
3. **PSR-1 / #383:** two outside-operator enrollment receipts remain a human operational prerequisite. The existing device-code plus Admin-session route is already selected; do not invent another auth path or publish user codes/credentials.
4. **PSR-2 / #362:** PSR-1 completion and a named, consenting research-and-ethics steward precede any separately authorized natural-play window. No hosting, enrollment, recruitment, production action, issue closure or bypass follows from this documentation slice.
