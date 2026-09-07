# Counterfactual Replay

Every counterfactual declares `counterfactual_id`, `source_trajectory_id`, `fork_point`, changed variables with before/after values, held-constant variables, seed policy, agent/world versions, and equivalence boundary. “Replay differently” is invalid. Undeclared material divergence is recorded as a confound and a severe boundary failure is `NOT_COMPARABLE`.

`SAME_SEED` repeats the recorded stream while stream structure remains comparable. `DERIVED_SEED` is deterministic from a versioned derivation and pinned inputs. `INDEPENDENT_SEED` is for robustness and cannot support exact seed equivalence. If RNG consumption differs, record stream ID and exact divergence cycle/event and stop claiming seed equivalence.

## Extension Points

Non-normative guidance for future work; this section changes no current contract.

### Replay comparators and seed derivations

Future comparison adapters can report additional confounds while preserving the declared fork point, held constants and before/after values. A changed RNG stream structure ends exact seed equivalence; independent seeds remain robustness evidence, not exact replay.

Version any derivation or equivalence-rule change and keep old counterfactuals bound to their original agent/world pins. Validate identical-input replay, an undeclared material divergence, and the exact cycle/event where RNG consumption diverges; retain NOT_COMPARABLE when the boundary fails.
