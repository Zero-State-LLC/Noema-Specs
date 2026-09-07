# v0.4 Lab: Architecture Delta

```text
Observatory candidate (research) → simple TEST intent → deterministic intent compiler
  → immutable experiment design → validated plan DAG
  → isolated experimental world fork/replay → explicit intervention → ordered runs
  → pinned feature/metric measurement → controls + replication → Lab result
  → deterministic simple result projection → READY-only evidence handoff to v0.5 Compiler
```

The production World Engine is outside the mutating side of this flow. The fork has a separate ledger, storage namespace, tools/network containment, and research partition. Execution, interpretation, and claim label remain separate. Scheduler order is explicit in the plan graph and concurrency cannot change claim-bearing order.

The simple request and advanced view are distinct projections of the same `experiment_id`, source intent, result, and audit lineage. `CAPTURE AS TEST` is available only when the retained Lab result reports `compiler_readiness: READY`.

## Extension Points

Non-normative guidance for future maintenance; no new behavior is authorized here.

- **Pipeline seam:** Extend adapter and scheduling examples at the intent-compiler, isolated-fork, measurement, and result-projection boundaries. Preserve one experiment_id and source lineage across simple and advanced views rather than branching into separate execution paths.
- **Compatibility boundary:** New intervention adapters or plan-DAG semantics need versioned Lab contracts and compatibility cases. They cannot mutate production World Engine state, relax fork containment, or bypass READY-only handoff to the Compiler.
- **Validation expectations:** Compare claim-bearing order under serial and concurrent execution, prove separate ledger/storage namespaces, test unsupported adapters and containment failure, and verify a non-READY result exposes no capture handoff. Measurement and interpretation should retain their separate labels and pinned identities.
