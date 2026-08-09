# v0.1 Minimum Seed World (Stub)

This directory should contain:

- `world-seed.json` — genesis state with ≥3 rooms, exits, one infrastructure entity, one resource node, and default budgets.
- `sample-trajectory.jsonl` — ordered World Events exercising LOOK, successful MOVE, MOVE_REJECTED, BUDGET_EXCEEDED, OBSERVATION_GENERATED, and at least one MESSAGE or ORG_CREATE.
- `equivalence-boundary.json` — the exact v0.1 boundary object from ADR-005 / docs/REPLAY.md.
- `expected-final-state-digest.txt` and observation digests for the focal agent.

Implementations MUST be able to load the seed, replay the trajectory, and match the digests under the boundary.

A concrete fixture will be added once the first World Engine prototype exists. Until then this directory documents the required shape.
