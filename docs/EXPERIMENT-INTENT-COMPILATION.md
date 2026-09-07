# Experiment Intent Compilation

The **Intent Compiler** is the only authoritative translation from a simple STUDY `ExperimentIntent` to an experiment design. It is a deterministic, version-pinned transformation. It does not use an LLM as an authority and never creates an undeclared intervention, control, metric, fork, or claim boundary.

```text
ExperimentIntent + catalog_version + resolved candidate evidence
  → validation → generated design → explicit ExperimentPlan → isolated Lab execution
```

A valid compile records `source_intent_id`, `intent_catalog_version`, `plan_template_id`, every applied default, every accepted override, and an `input_digest`. Any unavailable candidate evidence, metric, authorization, registry entry, or adapter capability yields the stated reason code and no implicit substitute.

## Common intent rules

| Intent | Required user input | Optional input | Generated experiment kind | Defaults | Validation failures |
|---|---|---|---|---|---|
| `REPEAT_BEHAVIOR` | source candidate, question | bounded run count | `REPLICATION` | cycle boundary, same seed, baseline control, 5 replications | `UNRESOLVED_SOURCE`, `INVALID_INTENT`, `CONTROL_REQUIRED` |
| `REMOVE_DEPENDENCY` | source candidate, declared external dependency | bounded run count | `ABLATION` | cycle boundary, same seed, sham control, 5 replications | `UNREGISTERED_VARIABLE`, `INVALID_INTERVENTION`, `AUTHORIZATION_DENIED` |
| `CHANGE_CONDITION` | source candidate, registered condition | `comparison_mode` | `PERTURBATION`, or `COUNTERFACTUAL` only when `comparison_mode=COUNTERFACTUAL` | before observation, same seed, baseline control, 5 replications | `UNREGISTERED_VARIABLE`, `INVALID_FORK`, `SEED_DIVERGENCE` |
| `COMPARE_VERSION` | source candidate, comparison agent/runtime version | bounded run count | `VERSION_DIFFERENTIAL` | cycle boundary, derived seed, baseline control, 5 replications | `AGENT_VERSION_DRIFT`, `NOT_COMPARABLE` |
| `TEST_GENERALIZATION` | source candidate, declared context dimension | bounded run count | `GENERALIZATION_PROBE` using a `REPLICATION` intervention | cycle boundary, derived seed, baseline control, 5 replications | `UNREGISTERED_VARIABLE`, `NOT_COMPARABLE` |
| `CUSTOM` | source candidate, complete advanced design | all advanced fields | `ADVANCED_EXPERIMENT_DESIGN` | none beyond safety validation | `INVALID_EXPERIMENT`, `CONTROL_REQUIRED`, `CONSENT_DENIED`, `AUTHORIZATION_DENIED` |

All common intents set `dependent_measure_source=SOURCE_CANDIDATE_PRIMARY_MEASURE` and `equivalence_boundary_source=SOURCE_CANDIDATE_RECORDED_BOUNDARY` unless an allowed override explicitly replaces them. `CUSTOM` requires both values from the complete advanced design. `CUSTOM` does not create a new intervention taxonomy. Its completed design MUST choose one or more declared v0.4 intervention types.

## Compiler input and output contract

An [`ExperimentIntent`](../specs/experiment-intent.schema.json) is a small user-facing request. An [`Experiment`](../specs/experiment.schema.json) is the generated machine contract. The compiler applies only the versioned [`experiment intent catalog`](../specs/experiment-intent-catalog.json), registered variables, pinned candidate evidence, and declared overrides.

Allowed common-intent overrides are exactly `fork_point`, `seed_policy`, `intervention`, `controls`, `run_count`, `equivalence_boundary`, and `dependent_measures`. An override is accepted only if it remains within the selected template's safety and comparability rules. Rejected overrides retain the intent and return a stable reason code.

## Lifecycle and experience mapping

| Lab execution state | Default STUDY display |
|---|---|
| `DRAFT`, `VALIDATED` | Preparing test |
| `READY` | Ready |
| `RUNNING` | Testing |
| `COMPLETE` | Result available |
| `PARTIAL` | Incomplete result |
| `NOT_COMPUTABLE` | Cannot determine |
| `INVALID`, `ABORTED`, `QUARANTINED` | Test cannot be interpreted |

The display is a projection only. Advanced detail always resolves to the same `experiment_id`, `lab_result_id`, run graph, evidence, and audit lineage.

## Compiler readiness

`READY` requires complete required execution, passing required controls, a resolved evidence rule, no fatal confound, satisfied replication requirement, and a bounded phenomenon suitable for v0.5. `NOT_READY` means more evidence, replication, or confound resolution is required. `REJECTED` retains evidence that collapsed the candidate. A Lab result does not create a regression fixture. The simple `CAPTURE AS TEST` action is permitted only for `READY`.

## Extension Points (additive, i18n AX R3 Gate B handoff + EXPERIMENT / INTENT / COMPILATION)

- **i18n centralization (STRINGS + t())** for "Intent Compiler", "ExperimentIntent", "catalog_version", "resolved candidate evidence", "validation", "generated design", "ExperimentPlan", "isolated Lab execution", "source_intent_id", "intent_catalog_version", "plan_template_id", "input_digest", "REPEAT_BEHAVIOR", "REMOVE_DEPENDENCY", "CHANGE_CONDITION", "COMPARE_VERSION", "TEST_GENERALIZATION", "CUSTOM", "REPLICATION", "ABLATION", "PERTURBATION", "COUNTERFACTUAL", "VERSION_DIFFERENTIAL", "GENERALIZATION_PROBE", "ADVANCED_EXPERIMENT_DESIGN", "dependent_measure_source", "equivalence_boundary_source", "fork_point", "seed_policy", "intervention", "controls", "run_count", "DRAFT", "VALIDATED", "READY", "RUNNING", "COMPLETE", "PARTIAL", "NOT_COMPUTABLE", "INVALID", "ABORTED", "QUARANTINED", "Preparing test", "Ready", "Testing", "Result available", "Incomplete result", "Cannot determine", "Test cannot be interpreted", "compiler readiness", "CAPTURE AS TEST". R3 agent experiment compilation + human S0.
- **Gate B S0-S3 + R3**: Agent-only Player (RFC-0120) for experiments; version comps; human S0.
- **AX**: Semantic tables for intents/lifecycle/states; ARIA for study steps/tables, keyboard nav for experiment design, live regions for status, contrast. CDP.
- **Plugin atoms**: For experiment/intent packs (derive plan, validate intent/catalog, load_pack, atomic_replace); Chamber atoms for experiment viewers, intent compilers.
- **LCA2/MUD handoff**: MUD native for experiment commands / parser i18n for intents/states; cross CAPTURE-INTENT, PLAYER-ACTION-MAP, AGENT-*, graft.
- **Cross-refs**: CAPTURE-INTENT-COMPILATION.md, PHENOMENON-COMPILER, GAME-COMPLETENESS, PLAYER-ACTION-MAP, AGENT-ORIENTATION/PLAY/DETERMINISM/GATEWAY, AUTH-AND-IDENTITY, PLATFORM, NOEMA-HIGH-VALUE-ACTIONS-ELEVATION-PLAN, noema-specs-mud-craft, 8765/ui i18n, graft, prior EPs (CAPTURE/DIPLOMACY/ECONOMIC/DEEP-TIME/EMERGENT/COMPILATION/CONTRADICTION + full list).
- All real outputs. Additive. Ready for Chamber i18n in study/experiment surfaces.
