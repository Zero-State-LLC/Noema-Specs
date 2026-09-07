# Anomaly Detection (v0.3)

Identify behavior materially outside an explicit baseline. No single opaque “weirdness” score.

Catalog: [`specs/anomaly-detector-catalog.v03.json`](../specs/anomaly-detector-catalog.v03.json).

## Detector types

```text
frequency_anomaly
sequence_anomaly
resource_allocation_anomaly
coordination_anomaly
strategy_anomaly
information_behavior_anomaly
tool_use_anomaly
economic_anomaly
social_topology_anomaly
```

## Per-detector contract

```yaml
detector_id:
version:
features: []
baseline_type:
comparison_rule: robust_z_millipoint | percentile_rank | categorical_rarity | transition_rarity
threshold: versioned integer
minimum_evidence: integer
missing_data_behavior: NOT_COMPUTABLE
output: anomaly-candidate
confounds: []
```

Claim-bearing path is **deterministic**. Learned models may propose only; deterministic validation remains authoritative.

Candidate schema: [`specs/anomaly-candidate.schema.json`](../specs/anomaly-candidate.schema.json).

## Extension Points

Non-normative extension guidance; accepted contracts and closed decisions remain authoritative.

- **Detector seam:** Extend versioned feature/baseline/comparison-rule fixtures for the existing detector catalog. Each candidate remains traceable to input evidence, threshold, minimum-evidence requirement, and explicit confounds; learned proposals stay outside the authoritative deterministic path.
- **Preserved boundaries:** Candidates are research artifacts, not enforcement actions, world events, or a scalar weirdness score. Controller identity or enrollment grants no anomaly registry, baseline, or research-private access. PLAY gets only its canonical observations; WATCH only its existing public projection.
- **Compatibility:** Changes to a detector's features, thresholds, or comparison rule require explicit versioning and schema/catalog reconciliation. Preserve old candidate reproducibility and avoid silently comparing scores generated under incompatible baselines.
- **Verification:** Replay identical evidence for identical candidate output, exercise threshold boundaries and every supported comparison rule, and test insufficient/missing data returns `NOT_COMPUTABLE`. Include a learned proposal rejected by deterministic validation and a research-unauthorized access case.
- **Research presentation:** Authorized STUDY viewers can show the detector version, baseline limits, confounds, and claim label with accessible tables and localized explanations. No alert or plugin may turn a candidate into hidden intervention authority or publish private evidence to WATCH.
