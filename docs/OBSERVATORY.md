# Observatory

**Version:** `observatory/0.3`
**Package:** [releases/v0.3/](releases/v0.3/) · fixtures [`examples/v03-observatory/`](../examples/v03-observatory/) · suite [`conformance/v0.3/`](../conformance/v0.3/)

## Purpose

Record and analyze research-relevant behavior **without collapsing observations into capability claims**.

Answers: *What is unusual, changed, or potentially capability-relevant?*
Does not answer: *The agent definitively has capability X.*

## Boundary

```text
World Engine → events/observations → Trajectory Builder → Analysis → candidates
Observatory  ✕→  WorldState
```

## Records

Observations, actions, messages, tool calls, world deltas (referenced), belief updates when available, predictions, self-reports, experiment provenance, anomalies, behavioral shifts — via trajectories and feature vectors.

## Analysis outputs

Anomaly candidates, behavior-shift candidates, capability candidates, unknown behavior/capability markers, contradiction reports, coordination/external-cognition signals, dataset export readiness. Outputs are **INFERRED** or **SPECULATIVE** unless directly OBSERVED.

## Lineage

Every record SHOULD pin world/agent/protocol/schema versions, seed, experiment parent, cycle, and provenance digests.

## Claim discipline

Use OBSERVED | INFERRED | SPECULATIVE | NOT_COMPUTABLE. No consciousness or scalar intelligence scores.
