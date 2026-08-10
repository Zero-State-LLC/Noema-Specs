# Experiment Lab

## Purpose

The Experiment Lab turns Observatory candidates into reproducible tests through deterministic replay, fork isolation, perturbation, ablation, lesion studies (when declared), counterfactual replay, version differentials, and replication.

## Pipeline

```text
Observatory candidate
        ↓
Experiment Design
        ↓
Experiment Plan
        ↓
Controlled World Fork / Replay
        ↓
Intervention
        ↓
Run
        ↓
Outcome Measurement
        ↓
Replication / Comparison
        ↓
Lab Result
        ↓
v0.5 Compiler candidate (if READY)
```

## Required experiment forms

- Replay from seed, world version, protocol versions, deterministic config, and event ledger.
- Situation Genome mutation (via Frontier contracts when applicable).
- Perturbation of information, timing, incentives, resources, tools, and topology.
- Ablation and lesion studies for tools, memory, context, modules, and delegation (lesions only when adapter-declared).
- Counterfactual replay with explicit changed variables.
- Replication across runs and agent versions.

## Isolation

Default: experimental fork only. Production world mutation is forbidden ([EXPERIMENT-FORK.md](EXPERIMENT-FORK.md)).

## Outputs

Experiment outcomes MUST include status, divergence notes, equivalence boundary, metrics, confounds, failed controls, null results, and links to source trajectories.

Failed experiments, failed controls, counterevidence, and non-results are first-class retained records.

## Executable package

- Release: [docs/releases/v0.4/](releases/v0.4/)
- Fixtures: [examples/v04-lab/](../examples/v04-lab/)
- Conformance: [conformance/v0.4/](../conformance/v0.4/) L01–L16

## Boundaries

| System | Role |
|--------|------|
| Observatory | discovers candidates |
| Lab | tests under intervention |
| Compiler (v0.5) | permanent fixtures — **not** Lab |
| World Engine | production truth — **not** mutated by Lab |

No experimental outcome becomes world-native reward or production state by default.  
No silent promotion of correlation to causation.  
No `PROVEN` status.
