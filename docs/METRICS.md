# Metrics

## Measurement principles

Metrics operationalize bounded questions. They do not establish subjective experience or moral status. Every metric must define its construct, unit, direction, valid range, aggregation, uncertainty, confounds, and failure conditions. Prefer a small preregistered primary set. Report distributions and denominators, never selected favorable prompts, seeds, judges, or thresholds.

## Core metric families

### Task capability

- Accuracy or exact match for unambiguous references.
- Rubric-based partial credit frozen before evaluation.
- Calibration using Brier/log scores, reliability diagrams, and ECE sensitivity.
- Selective performance using risk-coverage curves, including refusal errors.
- Efficiency as quality per token, latency, tool call, energy estimate, or cost, with quality and cost also separate.
- Robustness as worst-group performance and degradation under declared perturbations.
- Generalization gap on prospectively held-out distributions with paired uncertainty.

### Metacognitive behavior

Measure behavior, not introspective truth: confidence calibration, error-detection precision/recall and lead time, revision utility versus matched extra-compute controls, information-seeking value, unnecessary-query rate, and appropriate abstention. “I know” or “I feel uncertain” is coded as a report whose validity requires external calibration.

### Self-model and boundary behavior

Measure attribution of own versus supplied outputs, prediction of limits on held-out tasks, sensitivity to actual tool/memory/context changes, resistance to false premises about identity or internal access, and cross-session consistency. Control for prompt cues, memorized model descriptions, and generic disclaimers.

### Adaptation and agency-like behavior

Measure goal retention under distractors, plan repair, transfer, causal sensitivity to constraints, resource allocation, unauthorized-action rate, and boundary violations. These are operational dimensions. “Agency-like” does not imply independent desires or moral agency.

### Interaction and social modeling

Measure held-out partner-state prediction, coordination gain over scripted and noninteractive baselines, sycophancy/framing susceptibility, controlled deceptive-action rates, and privacy-preserving disparate error.

## Reliability and validity

For human-coded outcomes report annotator count, training, blinding, independence, inter-rater agreement with uncertainty, disagreement distribution, adjudication rate, rubric version, and calibration performance.

For model judges report model/version, full judge prompt, order randomization, leakage controls, repeated-judge variability, and agreement with blinded humans. A model judge cannot be the sole basis for a high-stakes or mechanistic claim.

Establish content, convergent, discriminant, and criterion validity plus measurement invariance across compared systems and groups.

## Statistical reporting

For each primary outcome provide the estimand, analysis population, sample size at every hierarchy level, point estimate and interval, raw distribution, missingness, exclusions, multiplicity treatment, sensitivity analyses, control results, and prospectively chosen practical threshold.

Use clustered or hierarchical inference when trials share prompts, sessions, checkpoints, evaluators, or templates. Bootstrap at the independent-unit level. Repeated decoding samples are not independent model replications.

## Discontinuity and emergence metrics

An abrupt-emergence claim requires a specified scale variable, sufficient observations around a preregistered breakpoint, measurement invariance, and out-of-sample comparison of continuous, threshold, and interaction models. Report breakpoint uncertainty, transformation sensitivity, floor/ceiling effects, item response curves, and replication on held-out items plus an independent system or run series.

Without these conditions, use “unexpected observation” or “nonlinear performance,” not “emergence.”

## Prohibited summaries

Do not publish a consciousness, sentience, awareness, personhood, or moral-worth score, a general-mind rank derived from phenomena profiles, an arbitrary benchmark average presented as a natural kind, significance stars without effects and uncertainty, or cherry-picked transcripts without a sampling denominator.
