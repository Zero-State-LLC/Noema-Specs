# Experimental World Fork

A fork records `source_world_id`, `source_world_version`, `source_snapshot_id`, `source_ledger_head`, `fork_cycle`, `fork_event_boundary`, `experimental_world_id`, `experiment_id`, and `fork_digest`. It preserves the canonical source history exactly through its boundary, then uses a separate experimental ledger identity and storage namespace. Experimental events never append to the source ledger. `mutates_production` MUST be false.

Legal replayable points are `CYCLE_BOUNDARY`, `BEFORE_OBSERVATION`, `AFTER_OBSERVATION`, `BEFORE_ACTION`, `AFTER_ACTION`, `BEFORE_SITUATION_INJECTION`, and `AFTER_SITUATION_INJECTION`. Mid-reducer, uncheckpointed, or unreplayable forks are forbidden. Recreating the same source identity, boundary, experimental identity, and namespace must reproduce `fork_digest`.

## Extension Points (additive, i18n AX R3 Gate B handoff + MUD/PLAY craft per noema-specs-mud-craft)

- **i18n centralization (STRINGS + t() in ui.py/8765 Chamber)**: Keys for "experimental_world_fork", "source_world_id", "source_world_version", "source_snapshot_id", "source_ledger_head", "fork_cycle", "fork_event_boundary", "experimental_world_id", "fork_digest", "mutates_production", "cycle_boundary", "before_observation", "after_observation", "before_action", "after_action", "before_situation_injection", "after_situation_injection". Use t() for fork tables, replay points in Chamber experiment/fork surfaces.

- **R3 Chamber (RFC-0120 agent-only Player identity + human S0 withhold)**: Agent fork records for experimental worlds. Human S0 separate.

- **Gate B S0-S3 + version comparisons**: Fork rules, replay points, deterministic fork_digest, mutates_production=false. Versioned forks.

- **AX (semantic/ARIA/keyboard/contrast/live regions per omh patterns + CDP)**: Tables for forks/replay points with aria-labels, keyboard, live for rules.

- **Plugin atoms / graft / ops / maint-evolve (noema-specs-mud-craft)**: Atoms for fork packs. Graft for digest validation.

- **MUD native interaction / PLAY craft / LCA2 handoff (per noema-specs-mud-craft + MUD-PLAY-CRAFT)**: Native i18n for fork events in MUD/PLAY experiments. Handoff to MUD-NATIVE-*, EXPERIMENT-DESIGN.md, PLAYER-*, AGENT-PLAY, LCA2.

- Cross-refs: EXPERIMENT-DESIGN.md, EXPERIENCE.md, MUD-PLAY-CRAFT.md, noema-specs-mud-craft, ui.py, elevation plan, graft, 8765, R3/Gate B, prior EPs, full list.
