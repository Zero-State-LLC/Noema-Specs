# Spec Completion Contract Micro-Note (State/Lifecycle/Transitions) — Design Note

**Status:** Micro-note per GAME-COMPLETENESS-PLAN section 11. Inputs only. No contract, catalog, verb, or exposure change.

**Element:** Exact state + lifecycle + exact transitions + deterministic ordering.

**GC1:** Mastery levels/states from MASTERY-SPECIALIZATION + seeds (recognition states, focus, decay).
**GC2:** Construction entity states (owned, unclaimed, in-progress) from CONSTRUCTION + B2 seeds.
**GC3:** Relationship edge states (trust, betrayal, restitution) from SOCIAL-MEMORY.
**GC4-10:** Office states, message delivery states, discovery states, contest stages, specialization states, culture states, WED pressure states (via seeds + authorities).

**Boundaries:** Notes only. Ties to existing GC authorities. Cites GAME-COMPLETENESS-PLAN.md section 11 + matrix A-J + prior seeds/PR #305 + main.

Smallest unit for state/lifecycle element.


## Extension Points

Non-normative guidance for future maintenance; this section changes no current behavior or promotion status.

- Lifecycle inventory rows can identify a concrete state domain, initial state, transition trigger, ordering phase, and terminal/reversible states. Distinguish canonical construction/office state from derived relationship or culture projections instead of treating every descriptive label as a stored enum.

- Preserve the owning mastery, construction, social-memory, and higher-GC version pins. This note adds no lifecycle state or reducer; proposed changes to state semantics or deterministic order require accepted contract review and an explicit historical replay/migration boundary.

- Validate each added row against a permitted transition and a forbidden one, plus simultaneous triggers where ordering matters. Cite before/after state and event fixtures, including in-progress construction recovery and expired grants/messages where relevant, rather than asserting all GC lifecycles complete from seed coverage.
