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
- **i18n (STRINGS + t() in ui.py / 8765)**: Centralize detector types (frequency_anomaly, sequence_anomaly, resource_allocation_anomaly, coordination_anomaly, strategy_anomaly, information_behavior_anomaly, tool_use_anomaly, economic_anomaly, social_topology_anomaly), thresholds, confounds, claim labels (OBSERVED/INFERRED/SPECULATIVE/NOT_COMPUTABLE), "Interesting work", "Evidence", "Observed trails", "Test results", "Captured work", "Learned behaviors", "Rebuild LEARN", "plain language", "Notice recent activity", "STUDY path", steps (01 notice etc.), "Open STUDY", "not connected", study metrics kickers, "Notice is an offline read...", JS labels (refreshing, live, unavailable, authorized view, operator token required) in /study /watch /play surfaces. Ties to prior i18n sweeps.
- **R3 Chamber**: Full anomaly detection, candidate listing, and evidence in agent-only controller mode (full access, sims, policy enforcement); human NON-CANONICAL limited public WATCH projections (no private anomalies), permissioned STUDY for evidence/traces, PLAY isolated with observable effects only. Per RFC-0120 agent-only identity.
- **Gate B (S0-S3 controller policies)**: S0 public anomaly overviews in WATCH; S1-S2 for basic detections; S3 full controller access to anomaly registry, baselines, confounds, and enforcement actions. Human S0 only. Version comparisons (anomaly catalog v0.3 vs prior). Controller enrollment impacts (agent vs human for anomaly authority).
- **AX (semantic/ARIA/keyboard/live/contrast)**: Semantic lists/cards for detectors (role="list" or "region"), ARIA labels for types/thresholds, live regions for new detections/alerts, keyboard navigation for filters/steps, high-contrast via theme vars, reduced motion. CDP/browser_exec verification on /study.
- **noema skill / plugin atoms**: Modular atoms for anomaly detector registry/viewer, candidate list, alert notifier for hermes-desktop-plugins + gateway /study integration + Chamber LEARN/matrix/contest/ecology. Ties to BEHAVIOR-FEATURES, CONTEST-RESOLUTION, CIVILIZATION-CAPABILITY-MATRIX.
- **LCA2 / MUD handoff / cross-refs**: To GAME-COMPLETENESS-PLAN (GC anomaly coverage), BEHAVIOR-FEATURES, STRATEGIC-CONFLICT (crime/exposure), DATA-MODEL (evidence), R3 evidence bundle, MUD craft for anomaly mechanics, Observatory/Phenomenon Compiler, ACCESS-POLICY, WORLD-REPORTS. Full R3 Chamber fixtures for Gate B.
- **Elevation (UX/DX/AX)**: UX discoverable anomaly evidence in Chamber; DX modular catalog + clean i18n + graft + atoms; AX semantic/ARIA + CDP. Additive, backward-compatible. Per AGENTS.md.

(Expanded per "merge and continue" + prior slices to 83+ EPs.)
