# Experiment Identity

Experiment identity is immutable and content-addressed. `input_digest` is SHA-256 of canonical JSON of the claim-bearing identity payload, excluding digest fields. It includes `experiment_id`, `experiment_version`, `experiment_design_version`, `source_intent_id`, source candidate/trajectory IDs, world ID/version/rules/catalog versions, agent ID/version, fork point, intervention/control-set digests, feature/metric versions, seed policy, equivalence boundary, consent basis, research-policy version, and authorization. The run boundary also pins source snapshot and ledger head.

Changing any claim-bearing input, variable definition, intervention semantic, comparison or analysis rule creates a new experiment identity. A correction appends a successor linked by `supersedes_experiment_id`; it never rewrites prior identity. Run IDs are deterministic derivatives of experiment identity, plan-node ID, replicate ordinal, and seed identity.

## Extension Points (additive, i18n AX R3 Gate B handoff + MUD/PLAY craft per noema-specs-mud-craft)

- **i18n centralization (STRINGS + t() in ui.py/8765 Chamber)**: Keys for "experiment_identity", "input_digest", "sha_256", "experiment_version", "supersedes_experiment_id", "run_id", "deterministic_derivative". Use t() for identity tables, digests, run IDs in Chamber experiment surfaces.

- **R3 Chamber (RFC-0120 agent-only Player identity + human S0 withhold)**: Agent immutable experiment identities. Human S0 separate.

- **Gate B S0-S3 + version comparisons**: Content-addressed, input_digest SHA-256, supersedes, deterministic run IDs. Versioned identities.

- **AX (semantic/ARIA/keyboard/contrast/live regions per omh patterns + CDP)**: Tables for identities/digests with aria-labels, keyboard, live for rules.

- **Plugin atoms / graft / ops / maint-evolve (noema-specs-mud-craft)**: Atoms for identity packs. Graft for digest validation.

- **MUD native interaction / PLAY craft / LCA2 handoff (per noema-specs-mud-craft + MUD-PLAY-CRAFT)**: Native i18n for experiment identities in MUD/PLAY. Handoff to MUD-NATIVE-*, EXPERIMENT-DESIGN.md, PLAYER-*, AGENT-PLAY, LCA2.

- Cross-refs: EXPERIMENT-DESIGN.md, EXPERIENCE.md, MUD-PLAY-CRAFT.md, noema-specs-mud-craft, ui.py, elevation plan, graft, 8765, R3/Gate B, prior EPs, full list.
