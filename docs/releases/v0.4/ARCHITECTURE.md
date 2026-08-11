# v0.4 Lab: Architecture Delta

```text
Observatory candidate (research) → immutable experiment design → validated plan DAG
  → isolated experimental world fork/replay → explicit intervention → ordered runs
  → pinned feature/metric measurement → controls + replication → Lab result
  → READY-only evidence handoff to v0.5 Compiler
```

The production World Engine is outside the mutating side of this flow. The fork has a separate ledger, storage namespace, tools/network containment, and research partition. Execution, interpretation, and claim label remain separate. Scheduler order is explicit in the plan graph and concurrency cannot change claim-bearing order.
