# Behavioral Oracle

## Contract

```text
oracle(fixture, target, boundary, replication_plan) ->
  PRESERVED | NOT_PRESERVED | INCONCLUSIVE | INVALID
```

Schema: [`behavioral-oracle.schema.json`](../specs/behavioral-oracle.schema.json). Canonical narrative: [PHENOMENON-COMPILER.md](PHENOMENON-COMPILER.md).

## Requirements

- **Input ordering**: fixture digest, then target digest, boundary digest, replication-plan digest.
- **Predicate / boundary versions**: pinned before compile; cannot weaken after failures.
- **Numeric tolerances**: declared in boundary; no opaque floats.
- **Missing data**: `INVALID` or `INCONCLUSIVE` per oracle `missing_data_behavior`—never `PRESERVED`.
- **Stochastic replication**: run count, success threshold, seeds/recorded responses, stopping rule declared before compile.
- **Cache identity**: reusable only under identical fixture/target/boundary/replay/replication/compiler identities.
- **Disagreement**: identical oracle identity MUST NOT silently disagree; invalidate cache and compilation, retain both results, open determinism defect.

## Simple projection

Do not default-display `oracle(fixture) = PRESERVED`.

Show:

```text
Validation
Behavior reproduced in all required checks.
```
