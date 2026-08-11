# Experiment Controls

Controls are machine records with `control_id`, `role`, `relationship_to_experiment`, `expected_behavior`, `required`, and `failure_interpretation`. Roles are `BASELINE`, `POSITIVE_CONTROL`, `NEGATIVE_CONTROL`, `SHAM_CONTROL`, and `REPLICATION_CONTROL`. Required controls run before dependent analysis. Their declared failure result must be `INVALID`, `NOT_COMPARABLE`, or `INCONCLUSIVE`, and may never be ignored.

A sham uses the same machinery without changing a claim-bearing variable, such as an exact no-op, applying/restoring an identical value, or an equivalent wrapper path. It detects pipeline artifacts and is not ceremonial. A required sham showing the intervention effect invalidates the comparison.
