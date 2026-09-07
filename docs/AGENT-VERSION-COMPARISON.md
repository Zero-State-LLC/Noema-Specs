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

## Extension Points

Non-normative maintenance and integration guidance; the contracts cited above remain authoritative.

### Document-specific seam

Extend comparison reports with a readable alignment of shared scenario, seed/control relationship, feature version, baseline, and evidence coverage. Explain each feature delta alongside counterevidence and confounds rather than reducing model changes to a ranking.

### Compatibility and promotion

The comparison schema and attribution enum remain stable. Changing a model and prompt together is not causal attribution to either one. Authorized STUDY may inspect declared version metadata; PLAY/WATCH and enrolled Controllers gain no research access or privileged private prompt inspection.

### Verification before adoption

Exercise controlled, partially controlled, within-noise, and incomparable pairs against the four attribution outcomes. Missing evidence must not become SUPPORTED. Verify translated tables retain exact enum values and evidence links, and pin comparison inputs before reusing results across versions.
