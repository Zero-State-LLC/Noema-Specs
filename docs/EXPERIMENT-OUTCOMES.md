# Experiment Outcomes

Dependent measures reuse Observatory features and metrics and pin `feature_id`, `metric_id`, `version`, `window`, `aggregation`, and `comparison_rule`; no execution may resolve “current” definitions. Outcome classes are `PERSISTED`, `DEGRADED`, `DISAPPEARED`, `CHANGED_FORM`, `NOT_COMPARABLE`, and `NOT_COMPUTABLE`. They describe observed behavior, not capability truth.

An effect is deterministic: `direction`, `magnitude`, `comparison_basis`, and `evidence_grade`, preferably fixed-point delta when justified. Deterministic single-run and replicated statistical evidence are distinct. Statistics record sample IDs, aggregation, estimator, interval/magnitude definition, and version. No threshold automatically validates capability.

## Extension Points

Non-normative guidance for future work; this section changes no current contract.

### Outcome measures and estimators

Additional outcomes can reuse pinned Observatory features, windows and comparison rules without promoting an observed outcome into capability truth. Missing data is not a zero effect, and deterministic single-run evidence is not replicated statistical evidence.

New estimators or claim-bearing comparison semantics need explicit versions; changes to the closed outcome classes require the owning contract change. Validate sample membership, aggregation and interval definitions against a reproducible fixture, including insufficient-data and non-comparable cases.
