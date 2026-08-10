# v0.3 Observatory — Architecture Delta

## Normative dataflow

```text
World Engine
    ↓
canonical events / observations
    ↓
Trajectory Builder
    ↓
Observatory Analysis (features → baselines → detectors)
    ↓
candidate records (anomaly / shift / capability / unknown)
```

## Forbidden reverse path

```text
Observatory  ✕→  WorldState
```

Observatory MUST NOT:

* mutate canonical world state;
* rewrite historical events;
* alter agent resources;
* modify already-delivered observations;
* inject situations;
* award world-native rewards;
* become evidence solely because it produced a score.

## Module

Add `observatory` to the modular monolith ([MODULE-CONTRACTS.md](../../MODULE-CONTRACTS.md)):

| Field | Value |
|-------|--------|
| purpose | Detect unusual / shifted behavior; emit research candidates |
| owns_state | trajectories, features, baselines, candidates, analysis runs, audits |
| reads | event ledger, observations, manifests, Frontier digests (research) |
| writes | research partition only |
| forbidden | world_state writes; opaque claim-bearing detectors |
| conformance | O01–O16 |

## Scheduler interaction

Analysis runs are offline or async relative to cycle reduce. They MUST pin input digests and versions. Wall-clock does not enter claim-bearing calculations.
