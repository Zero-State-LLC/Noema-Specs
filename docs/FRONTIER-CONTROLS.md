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


## Extension Points

Non-normative guidance for future maintenance; this section changes no current behavior or promotion status.

- Additional calibration examples can exercise the existing positive-control, negative-control, and regression admission paths without expanding the closed control-role vocabulary or allowing solved situations through ordinary candidate selection.

- Changes to normalized situation identity, distance rules, or quotas belong in the versioned Frontier configuration and governing contracts. Retain old digest inputs and selection results so replay of an existing plan does not silently use new normalization.

- Validate boundary pairs at solved_distance and pairwise_diversity_min, quota exhaustion, target quota interaction, and reordered affected-room input. Record both rejected repetitions and admitted controls with the configuration and normalized digest that explain the decision.
