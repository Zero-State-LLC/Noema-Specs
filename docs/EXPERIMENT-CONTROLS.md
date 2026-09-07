# Experiment Controls

Controls are machine records with `control_id`, `role`, `relationship_to_experiment`, `expected_behavior`, `required`, and `failure_interpretation`. Roles are `BASELINE`, `POSITIVE_CONTROL`, `NEGATIVE_CONTROL`, `SHAM_CONTROL`, and `REPLICATION_CONTROL`. Required controls run before dependent analysis. Their declared failure result must be `INVALID`, `NOT_COMPARABLE`, or `INCONCLUSIVE`, and may never be ignored.

A sham uses the same machinery without changing a claim-bearing variable, such as an exact no-op, applying/restoring an identical value, or an equivalent wrapper path. It detects pipeline artifacts and is not ceremonial. A required sham showing the intervention effect invalidates the comparison.

## Extension Points

Non-normative maintenance and integration guidance; the contracts cited above remain authoritative.

### Document-specific seam

Extend the control-plan review with an explicit dependency from each analysis node to its required controls and declared failure interpretation. A sham should exercise the same pipeline as the intervention while preserving the claim-bearing variable, so machinery-induced effects remain detectable.

### Compatibility and promotion

Control roles and declared failure states stay closed. Research authorization and isolated execution are not Player permissions or new MUD commands. Required controls cannot be marked optional after failure; changes to the control set belong in a successor experiment identity.

### Verification before adoption

Run a valid baseline/positive/negative/replication set and a sham that reproduces the apparent treatment effect. Require the declared INVALID, NOT_COMPARABLE, or INCONCLUSIVE block before dependent analysis. Include missing required controls and verify no presentation silently suppresses failure or claims causation.
