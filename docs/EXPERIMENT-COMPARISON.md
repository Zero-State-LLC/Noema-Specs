# Experiment Comparison

Every comparison records run A/B, comparison variable, held constants, pinned feature/metric versions, equivalence boundary, confounds, comparison rule, and effect result. It never uses a current baseline or mutable metric. Missing measure is `NOT_COMPUTABLE`; failed material boundary/severe confound is `NOT_COMPARABLE`; only then may the pinned predicate/fixed-point comparison classify an effect. Interpretation and claim labels cannot override the comparison.

## Extension Points (additive, i18n AX R3 Gate B handoff + MUD/PLAY craft per noema-specs-mud-craft)

- **i18n centralization (STRINGS + t() in ui.py/8765 Chamber)**: Keys for "experiment_comparison", "comparison_variable", "held_constants", "pinned_feature_metric_versions", "equivalence_boundary", "comparison_rule", "effect_result". Use t() for comparison tables, rules, effects in Chamber experiment/s tudy surfaces.

- **R3 Chamber (RFC-0120 agent-only Player identity + human S0 withhold)**: Agent comparison records for experiments. Human S0 separate.

- **Gate B S0-S3 + version comparisons**: NOT_COMPUTABLE/NOT_COMPARABLE rules, pinned versions, no override by labels. Versioned comparisons.

- **AX (semantic/ARIA/keyboard/contrast/live regions per omh patterns + CDP)**: Tables for comparisons with aria-labels, keyboard, live for results.

- **Plugin atoms / graft / ops / maint-evolve (noema-specs-mud-craft)**: Atoms for comparison packs. Graft for rule validation.

- **MUD native interaction / PLAY craft / LCA2 handoff (per noema-specs-mud-craft + MUD-PLAY-CRAFT)**: Native i18n for comparison effects in MUD/PLAY. Handoff to MUD-NATIVE-*, EXPERIMENT-DESIGN.md, PLAYER-*, AGENT-PLAY, LCA2.

- Cross-refs: EXPERIMENT-DESIGN.md, EXPERIENCE.md, MUD-PLAY-CRAFT.md, noema-specs-mud-craft, ui.py, elevation plan, graft, 8765, R3/Gate B, prior EPs, full list.
