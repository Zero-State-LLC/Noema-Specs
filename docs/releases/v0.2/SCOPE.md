# v0.2 Frontier — Scope

Product: NOEMA `0.2.0` (The Frontier).
Builds on: v0.1 Chamber (C01–C26). Canonical subsystem docs remain authoritative; this package defines the **delta**.

## Required scope

| Area | Canonical authority |
|------|---------------------|
| Situation Genome | [SITUATION-GENOME.md](../../SITUATION-GENOME.md), `situation-genome/0.2` |
| Frontier Director | [FRONTIER-DIRECTOR.md](../../FRONTIER-DIRECTOR.md), `frontier-director/0.2` |
| Novelty vector | [NOVELTY-VECTOR.md](../../NOVELTY-VECTOR.md), `novelty-axes/0.2` |
| Mutations | [SITUATION-MUTATION.md](../../SITUATION-MUTATION.md), `mutation-catalog/0.2` |
| Partial observability | [PARTIAL-OBSERVABILITY.md](../../PARTIAL-OBSERVABILITY.md) |
| Noise | [NOISE-MODEL.md](../../NOISE-MODEL.md), `noise-model/0.2` |
| Contradictory evidence | [CONTRADICTORY-EVIDENCE.md](../../CONTRADICTORY-EVIDENCE.md) |
| Attention degradation | [ATTENTION-PROJECTION.md](../../ATTENTION-PROJECTION.md) |
| Information-gain estimates | [INFORMATION-GAIN.md](../../INFORMATION-GAIN.md) |
| Controls / anti-repetition | [FRONTIER-CONTROLS.md](../../FRONTIER-CONTROLS.md) |
| Capability primitives (minimal) | [CAPABILITY-PRIMITIVES.md](../../CAPABILITY-PRIMITIVES.md) |
| Spectator Frontier overlays | [SPECTATOR.md](../../SPECTATOR.md) |
| Fixtures | [`examples/v02-frontier/`](../../../examples/v02-frontier/) |
| Conformance | [`conformance/v0.2/`](../../../conformance/v0.2/) |

## Product progression

```text
v0.1  interesting strategic behavior occurs naturally
  ↓
v0.2  NOEMA systematically selects/creates high-information situations
  ↓
v0.3  Observatory detects anomalies/candidates
```

## Hard product constraint

> The game remains a game. Research machinery changes world **conditions** but does not force research outcomes.

Frontier MUST present pressures as natural world events (shortage, rumor, infrastructure failure, conflicting reports, topology change). Player-facing UI MUST NOT use exam language (“Test: prove capability X”).

## Prerequisite

v0.1 C01–C26 remain green. Frontier enables only after modular-monolith Chamber is operational.
