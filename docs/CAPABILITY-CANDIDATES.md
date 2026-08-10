# Capability Candidates (v0.3)

Hypothesis generated from evidence patterns. **Not** Capability Graph. **Not** proof.

Schema: [`specs/capability-candidate.schema.json`](../specs/capability-candidate.schema.json).

## Fields

```text
candidate_capability_id
capability_primitive_id?          # if matched known primitive
novel_unknown_marker?              # UNKNOWN_CAPABILITY_<id>
supporting_anomaly_refs[]
behavior_shift_refs[]
trajectory_refs[]
observed_conditions
counterexamples[]
confounds[]
generalization_unknowns[]
replication_required: true
status
claim_label                         # typically SPECULATIVE or INFERRED
```

## Classes

* `KNOWN_PRIMITIVE_CANDIDATE` — maps to CAPABILITY-PRIMITIVES id  
* `UNKNOWN_CAPABILITY_<id>` — must not force ontology mapping  

Status remains unvalidated until later Lab evidence. Observatory does not emit world-truth capability labels.
