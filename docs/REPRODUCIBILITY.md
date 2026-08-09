# Reproducibility

## Bundle layout

```text
phenomena/NP-000381/
  manifest.json
  world-config.json
  world-seed.txt
  protocol-versions.json
  agent-manifest.json
  agent-state.snapshot
  original-trajectory.jsonl
  minimal-world-state.json
  situation.json
  observations.jsonl
  actions.jsonl
  outcomes.json
  replications.jsonl
  perturbations.jsonl
  ablations.jsonl
  counterfactuals.jsonl
  metrics.json
  report.md
```

## Boundary types

- Deterministic world replay: world state transitions reproduce under seed, version, deterministic config, initial state, and ordered ledger.
- Deterministic protocol replay: protocol envelopes, validation outcomes, and event ordering reproduce.
- Stochastic agent replay: external nondeterministic model APIs may vary and MUST be labeled as such.
- Behavioral equivalence replay: outcome is considered equivalent when predefined state, observation, metric, or behavior predicates match.

## Equivalence criteria

Every bundle MUST declare exact byte-for-byte fields, tolerated nondeterministic fields, semantic equivalence predicates, divergence reporting, and stop conditions.
