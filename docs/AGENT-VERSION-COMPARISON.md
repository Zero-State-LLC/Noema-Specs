# Agent-Version Comparison (v0.3)

Schema: [`specs/agent-version-comparison.schema.json`](../specs/agent-version-comparison.schema.json).

## Comparable pairs

same agent / new model · same model / new prompt · same model / new memory · different architecture · different model family

## Required dimensions

```text
agent_version_a, agent_version_b
shared world/scenario
seed/control relationship
feature_version, baseline_id
differences (feature deltas)
confounds
evidence_coverage
```

## Attribution outcomes

| Outcome | Meaning |
|---------|---------|
| `SUPPORTED` | controlled comparison supports difference claim |
| `PARTIALLY_SUPPORTED` | partial controls |
| `NOT_DISTINGUISHABLE` | difference within noise/threshold |
| `NOT_COMPUTABLE` | missing evidence or incomparable context |

Do not claim causation from uncontrolled multi-variable changes.
