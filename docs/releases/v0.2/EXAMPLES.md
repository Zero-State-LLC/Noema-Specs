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

## Extension Points

Non-normative future guidance; this section grants no new behavioral authority and does not reopen accepted or deferred slices.

- **Seam:** Additional Frontier walkthrough annotations can connect the existing genome, request, candidate, plan, observations, and replay digests.
- **Unchanged invariants:** Keep agents unscripted and preserve the validity of the legacy situation-genome/1.0 sample. Fixtures are not live-world canon.
- **Compatibility, promotion, and verification:** New scenario packages should pin their schemas and replay inputs rather than replacing historical examples. Validate positives and genome negatives and compare repeat-run digests before presenting a package as conformant.
