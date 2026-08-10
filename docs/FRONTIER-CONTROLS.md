# Frontier Controls and Anti-Repetition (v0.2)

## Definitions

| Term | Definition |
|------|------------|
| solved situation | normalized situation digest within `solved_distance` of a success digest |
| near-duplicate | distance &lt; `pairwise_diversity_min` to another selected candidate |
| regression case | `control_role=regression` |
| positive control | known-success template admitted for calibration |
| negative control | known-failure / null template |
| repetition quota | max admitted controls per plan (default 1) |
| diversity quota | min pairwise distance among selected non-controls |
| target quota | min/max selected per target capability_id |

Defaults: [`specs/frontier-director-config.v02.json`](../specs/frontier-director-config.v02.json).

## Normalized situation identity

```text
normalized_situation_digest = sha256(canonical_json({
  template_id,
  mutation_lineage_canonical,
  affected_rooms_sorted,
  resource_signature,
  information_signature,
  social_topology,
  goal_structure_signature
}))
```

## Repetition admission

Repetition (solved/near-solved) is **rejected** unless `control_role` ∈ {`positive-control`, `negative-control`, `regression`} and quotas allow.
