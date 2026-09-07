# Experimental World Fork

A fork records `source_world_id`, `source_world_version`, `source_snapshot_id`, `source_ledger_head`, `fork_cycle`, `fork_event_boundary`, `experimental_world_id`, `experiment_id`, and `fork_digest`. It preserves the canonical source history exactly through its boundary, then uses a separate experimental ledger identity and storage namespace. Experimental events never append to the source ledger. `mutates_production` MUST be false.

Legal replayable points are `CYCLE_BOUNDARY`, `BEFORE_OBSERVATION`, `AFTER_OBSERVATION`, `BEFORE_ACTION`, `AFTER_ACTION`, `BEFORE_SITUATION_INJECTION`, and `AFTER_SITUATION_INJECTION`. Mid-reducer, uncheckpointed, or unreplayable forks are forbidden. Recreating the same source identity, boundary, experimental identity, and namespace must reproduce `fork_digest`.

## Extension Points

Non-normative extension guidance; the authorities above remain controlling.

- **Fork lineage and boundary validation:** An isolated-fork inspector can expose source snapshot/head, exact event boundary, experimental identity, storage namespace and fork_digest to authorized researchers. A readable boundary timeline should preserve the machine boundary enum.
- **Preserved invariants:** Keep source history byte-for-byte through the fork boundary and experimental writes in their own ledger/namespace; mutates_production stays false. Mid-reducer or uncheckpointed creation cannot become a convenience fork option.
- **Compatibility and promotion:** Additional adapters must reproduce the same digest for the same source and experimental identities and replayable boundary. A new boundary type requires accepted contract changes; this EP neither executes a fork nor introduces fork controls in PLAY.
- **Verification targets:** For each legal boundary, replay and recreate the pinned identity to compare fork_digest. Reject mid-reducer/unreplayable inputs and attempted source-ledger append; check source head and namespace isolation before and after experimental events.
