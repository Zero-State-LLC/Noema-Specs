# Experimental World Fork

A fork records `source_world_id`, `source_world_version`, `source_snapshot_id`, `source_ledger_head`, `fork_cycle`, `fork_event_boundary`, `experimental_world_id`, `experiment_id`, and `fork_digest`. It preserves the canonical source history exactly through its boundary, then uses a separate experimental ledger identity and storage namespace. Experimental events never append to the source ledger. `mutates_production` MUST be false.

Legal replayable points are `CYCLE_BOUNDARY`, `BEFORE_OBSERVATION`, `AFTER_OBSERVATION`, `BEFORE_ACTION`, `AFTER_ACTION`, `BEFORE_SITUATION_INJECTION`, and `AFTER_SITUATION_INJECTION`. Mid-reducer, uncheckpointed, or unreplayable forks are forbidden. Recreating the same source identity, boundary, experimental identity, and namespace must reproduce `fork_digest`.

