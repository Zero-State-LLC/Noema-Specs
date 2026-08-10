# v0.3 Observatory — Data Model Delta

Research-layer entities (not world truth):

| Entity | Schema / catalog |
|--------|------------------|
| Trajectory (0.3) | `trajectory/0.3` |
| BehaviorFeatureVector | behavior-feature-catalog.v03 |
| Baseline | baseline.schema.json |
| AnomalyCandidate | anomaly-candidate.schema.json |
| BehaviorShiftCandidate | behavior-shift-candidate.schema.json |
| CapabilityCandidate | capability-candidate.schema.json |
| UnknownBehaviorCandidate | unknown-candidate.schema.json |
| AgentVersionComparison | agent-version-comparison.schema.json |
| ObservatoryAnalysisRun | observatory-analysis-run.schema.json |
| ObservatoryAuditRecord | observatory-audit-record.schema.json |
| ContextProfile | context-normalization |
| CoordinationSignal | coordination-signals |
| ExternalCognitionSignal | external-cognition |

IDs: `traj.*`, `baseline.*`, `anom.*`, `shift.*`, `capcand.*`, `unkbehav.*`, `unkcap.*`, `avcmp.*`, `oarun.*`.
