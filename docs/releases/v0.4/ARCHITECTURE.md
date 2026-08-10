# v0.4 Lab — Architecture Delta

## Normative dataflow

```text
Observatory candidate
        ↓
Experiment Design / Plan
        ↓
Controlled World Fork
        ↓
Intervention + Controls
        ↓
Experiment Runs
        ↓
Outcome Measurement (Observatory features/metrics)
        ↓
Replication / Comparison
        ↓
Lab Result
        ↓
v0.5 Compiler candidate (if READY)
```

## Forbidden reverse path

```text
Lab  ✕→  production WorldState
Lab  ✕→  source world ledger append
```

Default mode: **experimental fork only**.

## Module

Add `lab` to the modular monolith:

| Field | Value |
|-------|--------|
| purpose | Controlled experimental tests of research candidates |
| owns_state | experiments, plans, forks, runs, lab results, lab audits |
| reads | Observatory candidates, trajectories, snapshots, manifests |
| writes | research / lab partition and experimental world ledgers only |
| forbidden | production world mutation; silent causal claims; PROVEN status |
| conformance | L01–L16 |

## Relation to World Engine

Forks create a new `experimental_world_id` with shared history prefix. Interventions apply only on the fork ledger.
