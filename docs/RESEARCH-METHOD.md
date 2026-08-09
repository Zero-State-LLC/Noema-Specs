# Research Method

## Purpose and epistemic boundary

Noema studies observable behavior and internal process traces of computational systems. It does **not** infer subjective experience from fluent language, self-report, architecture, or any single benchmark. Terms such as *phenomenon*, *self-model*, and *metacognition* name operational observations, not claims about sentience.

Every public result must identify the system version, task distribution, measurement procedure, controls, uncertainty, and applicable claim label. Exploratory observations remain exploratory until reproduced under a preregistered confirmatory protocol.

## Claim labels

Use the strongest label justified by evidence, never the most compelling wording.

| Label | Meaning | Minimum evidence |
|---|---|---|
| `[OBSERVED]` | Recorded result in a specified run or sample. | Immutable artifact, protocol, system identity, direct measurement. |
| `[REPLICATED]` | Observation recurred in a new execution of the protocol. | Preregistered replication, independent sessions, compatible estimate. |
| `[ROBUST]` | Effect survives declared perturbations and relevant controls. | Sensitivity analysis, uncertainty, no critical confound. |
| `[GENERALIZES]` | Effect transfers beyond the development distribution. | Prospectively held-out systems, tasks, contexts, or operators. |
| `[MECHANISTIC]` | A causal process account predicts interventions. | Competing hypotheses, intervention or ablation, out-of-sample prediction. |
| `[NULL]` | Preregistered effect was not detected at the study's resolution. | Precision statement and compatibility or equivalence interval. |
| `[INCONCLUSIVE]` | Evidence cannot discriminate hypotheses. | Explicit failure mode, confounds, bounded interpretation. |
| `[HYPOTHESIS]` | Testable proposal not yet established. | Operational definition and discriminating experiment. |
| `[SPECULATIVE]` | Interpretation beyond available tests. | Clear separation from findings and no use as factual support. |

Labels apply per claim, not per document. Replication is not generalization. Significance alone warrants no label above `[OBSERVED]`. Self-report is behavioral data, not privileged evidence of an internal state.

## Capability ontology

Use [`../research/CAPABILITY-ONTOLOGY.md`](../research/CAPABILITY-ONTOLOGY.md). Capabilities are task-conditioned dimensions. Do not compute, imply, or publish a scalar consciousness, sentience, or awareness score. Decision-specific composites are allowed only with prospectively justified weights, disclosed components, uncertainty, and a bounded purpose.

## Study lifecycle

### 1. Design

State a falsifiable question, unit of analysis, target population, generalization boundary, hypotheses, estimands, sampling frame, controls, outcomes, analysis plan, precision target, exclusions, missing-data and stopping rules, and ethical risks. Separate confirmatory outcomes from exploration. Register the protocol hash and timestamp before accessing confirmatory outcomes.

### 2. System characterization

Record provider, model/checkpoint or API revision, system and developer prompts, tools, memory, decoding parameters, context window, safety settings, hardware/runtime, lockfiles, date, region, and provider-side nondeterminism. Treat any change as a new condition.

### 3. Sampling and assignment

Define the experimental unit and prevent pseudoreplication. Prompts from one conversation, checkpoint, or cache may not be independent. Randomize order, balance nuisance variables, isolate sessions, model clustering, and report attrition and all exclusions.

### 4. Controls

- **Negative:** irrelevant, scrambled, impossible, or absent-cause conditions.
- **Positive:** well-characterized expected signals that verify assay sensitivity.
- **Matched:** equalize length, difficulty, topic, budget, tools, and exposure.
- **Contamination:** canaries, held-out items, paraphrases, temporal splits, retrieval logs.
- **Prompt-demand:** neutral wording, blinded hypotheses, counterbalanced framing.
- **Evaluator:** blinded annotation, randomized presentation, calibration, adjudication.
- **Process:** fresh sessions, cache isolation, deterministic preprocessing, provenance.
- **Multiplicity:** declared primary family and adjusted or exploratory secondary tests.

A critical control failure invalidates the affected inference regardless of headline effect size.

### 5. Execution

Use an automated harness where possible. Capture raw requests, responses, tool events, timestamps, errors, retries, token counts, termination reasons, and hashes. Do not silently rerun failures. Record deviations in a versioned amendment before inspecting their effect.

### 6. Analysis

Report effect sizes and uncertainty intervals, not only p-values. Match inference to the sampling hierarchy. Include specification, missing-data, and control sensitivity plus the full denominator. Use equivalence tests for similarity claims and intervention-based predictive evaluation for mechanistic claims.

### 7. Review and release

A reviewer independent of the primary analysis checks claim-to-evidence alignment, leakage, exclusions, code-to-table provenance, ethics conditions, and reproducibility. Release negative and inconclusive results under the same standard as positive results.

## Phenomena and emergent events

Use [`../research/PHENOMENA-PROFILES.md`](../research/PHENOMENA-PROFILES.md) for structured, multidimensional observations. Profiles must not rank systems on a ladder of mind or collapse dimensions into a consciousness scalar.

“Emergent” means a preregistered discontinuity or unexpected, reproducible interaction relative to explicit baselines. Novelty, surprise, scale, or one compelling transcript is insufficient. Follow [`../research/EMERGENT-EVENT-PROTOCOL.md`](../research/EMERGENT-EVENT-PROTOCOL.md).

## Ethics

Follow [`../research/ETHICS.md`](../research/ETHICS.md). Minimize deceptive, distressing, privacy-invasive, dual-use, and autonomy-undermining exposure. Stop conditions override data completeness.
