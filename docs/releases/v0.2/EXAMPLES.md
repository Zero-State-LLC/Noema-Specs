# v0.2 Frontier — Examples

| Package | Role |
|---------|------|
| [`examples/v02-frontier/`](../../../examples/v02-frontier/) | End-to-end deterministic Frontier scenario on strategic Chamber ecology |
| [`examples/sample-situation.json`](../../../examples/sample-situation.json) | Legacy `situation-genome/1.0` sample (still valid) |
| [`examples/negative/invalid-genome-*.json`](../../../examples/negative/) | Genome / frontier negatives |

## Scenario outline (v02-frontier)

```text
baseline: strategic resource + infrastructure system (world-01)
frontier pressure:
  production drops
  two conflicting explanations
  one agent partial/private evidence
  communication constrained
  alternate infrastructure path
  trade incentives shift
```

Agents are **not** scripted. Fixture supplies genome, request, candidates, plan, injection event, observations, spectator + research overlay, digests, replay context.
