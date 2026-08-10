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
