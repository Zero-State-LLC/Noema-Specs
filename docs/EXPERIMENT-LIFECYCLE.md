# Experiment Lifecycle

## Execution states

```text
DRAFT → VALIDATED → READY → RUNNING → COMPLETE
```

Exits: `INVALID`, `ABORTED`, `PARTIAL`, `NOT_COMPUTABLE`, `QUARANTINED`.

## Interpretation states (post-analysis)

```text
SUPPORTED | PARTIALLY_SUPPORTED | NOT_SUPPORTED | INCONCLUSIVE
```

**Forbidden:** `PROVEN`.

## Transitions

Every transition records: previous state, new state, reason code, actor, evidence refs, cycle, digest ([LAB-AUDIT.md](LAB-AUDIT.md)).

Execution status and interpretation are separate from research claim labels (`OBSERVED` / `INFERRED` / `SPECULATIVE` / `NOT_COMPUTABLE`).
