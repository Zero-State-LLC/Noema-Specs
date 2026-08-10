# Experimental World Fork

## Rule

Lab interventions apply only on an **experimental fork**. Production worlds are not mutated.

## Required fields

`source_world_id`, `source_world_version`, `source_snapshot_id`, `source_ledger_head`, `fork_cycle`, `fork_event_boundary`, `experimental_world_id`, `experiment_id`, `fork_point`.

Schema: `specs/experiment-fork.schema.json` with `mutates_production: false`.

## Lineage

```text
production lineage
        ↘
         common prefix (≤ fork boundary)
        ↙
experimental lineage (new ledger identity)
```

Mid-reducer forks are **forbidden**.

## Legal fork points

`BEFORE_OBSERVATION`, `AFTER_OBSERVATION`, `BEFORE_ACTION`, `AFTER_ACTION`, `CYCLE_BOUNDARY`, `BEFORE_FRONTIER_INJECTION`, `AFTER_FRONTIER_INJECTION`.
