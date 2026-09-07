# Experiment Controls

Controls are machine records with `control_id`, `role`, `relationship_to_experiment`, `expected_behavior`, `required`, and `failure_interpretation`. Roles are `BASELINE`, `POSITIVE_CONTROL`, `NEGATIVE_CONTROL`, `SHAM_CONTROL`, and `REPLICATION_CONTROL`. Required controls run before dependent analysis. Their declared failure result must be `INVALID`, `NOT_COMPARABLE`, or `INCONCLUSIVE`, and may never be ignored.

A sham uses the same machinery without changing a claim-bearing variable, such as an exact no-op, applying/restoring an identical value, or an equivalent wrapper path. It detects pipeline artifacts and is not ceremonial. A required sham showing the intervention effect invalidates the comparison.

## Extension Points (additive, i18n AX R3 Gate B handoff + MUD/PLAY craft per noema-specs-mud-craft)

- **i18n centralization (STRINGS + t() in ui.py/8765 Chamber)**: Keys for "experiment_controls", "control_id", "role_baseline", "role_positive_control", "role_negative_control", "role_sham_control", "role_replication_control", "sham_control", "failure_interpretation", "invalid", "inconclusive". Use t() for control tables, roles, sham descriptions in Chamber experiment surfaces.

- **R3 Chamber (RFC-0120 agent-only Player identity + human S0 withhold)**: Agent control records for experiments. Human S0 separate.

- **Gate B S0-S3 + version comparisons**: Role definitions, required before analysis, sham rules, failure results. Versioned controls.

- **AX (semantic/ARIA/keyboard/contrast/live regions per omh patterns + CDP)**: Tables for controls/roles with aria-labels, keyboard, live for failures.

- **Plugin atoms / graft / ops / maint-evolve (noema-specs-mud-craft)**: Atoms for control packs. Graft for role validation.

- **MUD native interaction / PLAY craft / LCA2 handoff (per noema-specs-mud-craft + MUD-PLAY-CRAFT)**: Native i18n for control roles/shams in MUD/PLAY experiments. Handoff to MUD-NATIVE-*, EXPERIMENT-DESIGN.md, PLAYER-*, AGENT-PLAY, LCA2.

- Cross-refs: EXPERIMENT-DESIGN.md, EXPERIENCE.md, MUD-PLAY-CRAFT.md, noema-specs-mud-craft, ui.py, elevation plan, graft, 8765, R3/Gate B, prior EPs, full list.
