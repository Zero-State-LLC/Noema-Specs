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

## Extension Points

Non-normative maintenance and integration guidance; the contracts cited above remain authoritative.

### Document-specific seam

Extend authorized validation reports with the ordered fixture, target, boundary, and replication identities plus a concise explanation of each predicate outcome. Expose declared tolerances and missing-data handling without converting a technical status into an unconditional success banner.

### Compatibility and promotion

Compiler/oracle versions and equivalence boundaries remain claim-bearing. No tolerance weakening after failure, hidden LLM judge, or live PLAY oracle follows from a viewer. Cache reuse requires every pinned identity to match; public presentation cannot disclose restricted evidence.

### Verification before adoption

Exercise missing evidence, threshold-edge results, stochastic stopping rules, and same-identity disagreement. Confirm INVALID/INCONCLUSIVE never render as reproduced; conflicting results invalidate cache and compilation while retaining both artifacts. A changed replication plan must miss the old cache and preserve the prior receipt.
