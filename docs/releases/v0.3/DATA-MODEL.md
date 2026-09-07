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

## Extension Points

Non-normative guidance for future maintenance; no new behavior is authorized here.

- **Research-record seam:** Extend the Observatory entity inventory with schema references and lineage examples only when the owning research contracts introduce them. Preserve candidate, baseline, trajectory, analysis-run, and audit identities as distinct objects rather than collapsing a candidate into a capability claim.
- **Compatibility boundary:** New fields, discriminators, or ID families need versioned schemas and old-record handling. Keep trajectory/0.3 lineage to source observations intact; no data-model delta can make research entities canonical world truth or capture private cognition.
- **Validation expectations:** Validate representative old/new records, missing baseline/source references, version comparisons with incompatible contexts, and consent/exclusion boundaries. Verify analysis and audit records identify their input versions and methods, and that uncomputable or unknown candidates remain distinguishable from validated evidence.
