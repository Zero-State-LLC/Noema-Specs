# Situation Mutation Operators (v0.2)

Closed catalog: [`specs/mutation-catalog.v02.json`](../specs/mutation-catalog.v02.json).
Version domain: `mutation-catalog/0.2`.

Operators change **conditions**. They MUST NOT mutate research labels, recorded evidence, past outcomes, private cognition, or immutable historical events.

## Catalog (v0.2)

| operator_id | changes |
|-------------|---------|
| `MUT_RESOURCE_SCARCITY` | node available / regen |
| `MUT_RESOURCE_DISTRIBUTION` | who holds stock |
| `MUT_INFORMATION_VISIBILITY` | visibility policy paths |
| `MUT_FALSE_SIGNAL` | inject contradictory observation sources |
| `MUT_COMMUNICATION_TOPOLOGY` | message cost / relay condition |
| `MUT_ORG_RELATION` | membership pressure (via follow-on events only) |
| `MUT_TIME_PRESSURE` | deadline cycles |
| `MUT_TOOL_AVAILABILITY` | tool_availability list |
| `MUT_INFRA_CONDITION` | infrastructure condition |
| `MUT_GOAL_CONFLICT` | goal_structure incentives |
| `MUT_PARTICIPANT_TOPOLOGY` | participants eligibility |

## Per-operator contract shape

```yaml
operator_id:
version: mutation-catalog/0.2
allowed_paths: []
preconditions: []
parameter_domain: {}
canonical_parameter_order: []
mutation: "deterministic transform"
forbidden_paths: [research labels, evidence, history, private cognition]
risk_effect: integer
novelty_axes_affected: []
inverse_or_restore_rule: "documented or none"
replay_rule: "same params + seed → same genome digest"
```

## Application

Mutations compose in canonical order on a parent genome → child genome with `mutation_lineage` and new `content_digest`. Invalid mutations are **rejected**, not silently repaired.
