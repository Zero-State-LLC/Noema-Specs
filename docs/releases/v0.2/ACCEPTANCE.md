# v0.2 Frontier — Acceptance Criteria

A v0.2 implementation is accepted when **all** hold:

1. v0.1 C01–C26 remain green.
2. Situation Genome documents validate against `situation-genome/0.2`.
3. Deterministic mutation produces expected content digests for identical inputs.
4. Identical Frontier inputs produce **decision-equivalent** outputs ([FRONTIER-DIRECTOR.md](../../FRONTIER-DIRECTOR.md) equivalence boundary).
5. Anti-repetition rules are deterministic ([FRONTIER-CONTROLS.md](../../FRONTIER-CONTROLS.md)).
6. Unsafe or invalid candidates fail closed (reject, not silent repair).
7. Partial observability never leaks hidden world truth.
8. Noise is reproducible from declared seed stream + noise-model version.
9. Contradictory evidence remains representational; does not corrupt world truth.
10. Attention degradation is deterministic ([ATTENTION-PROJECTION.md](../../ATTENTION-PROJECTION.md)).
11. Frontier **cannot** directly mutate WorldState.
12. Selected situation enters world only via canonical event path (`SITUATION_INJECTED` + follow-ons).
13. Replay reproduces Frontier decision **and** resulting world effects under declared boundary.
14. Research-target metadata stays hidden from ordinary players/spectators.
15. Empty / no-safe-candidate plans are valid outcomes.
16. Missing evidence yields `NOT_COMPUTABLE`, not invented zero scores.

Normative suite: [CONFORMANCE.md](CONFORMANCE.md) · [`conformance/v0.2/`](../../../conformance/v0.2/).

## Extension Points

Non-normative future guidance; no current scope or acceptance claim changes.

### Frontier acceptance evidence

Extend acceptance receipts with pinned fixture inputs and the declared decision-equivalence boundary, retaining v0.1 regression evidence alongside Frontier checks. No-safe-candidate and NOT_COMPUTABLE outcomes are valid, not failures to be repaired into a selection.

Keep F01–F15 and catalog identities explicit; changed selection, mutation or noise semantics require revised versioned authority. Validate deterministic repeat decisions, resulting event-path effects and negative observability cases. A green specification suite does not by itself establish hosted deployment or authorize a world injection.
