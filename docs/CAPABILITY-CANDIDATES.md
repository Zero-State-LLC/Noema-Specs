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

## Extension Points

Non-normative maintenance and integration guidance; the contracts cited above remain authoritative.

### Document-specific seam

Extend candidate review with linked anomaly/trajectory evidence, counterexamples, confounds, and explicit generalization unknowns. Keep unmatched behavior under its UNKNOWN_CAPABILITY marker rather than forcing it into the primitive ontology.

### Compatibility and promotion

Candidates are hypotheses, not Capability Graph proof or world-truth labels. Required replication and later Lab evidence remain the promotion path. Neither Controller enrollment nor an ALLOW_ONLY movement policy authorizes research access; no candidate discovery reward or candidate field is added to PLAY/WATCH.

### Verification before adoption

Validate known and unknown candidate cases against the schema and retain claim_label and replication_required through export. Test unsupported mapping, missing evidence and counterevidence. Verify a candidate cannot become a validated capability merely by changing UI status, and redacted views cannot recover private trajectory content.
