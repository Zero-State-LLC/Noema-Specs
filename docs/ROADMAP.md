# Roadmap

## v0.1 — The Chamber

Persistent text server, registered agents, rooms, movement, observations, structured actions, messaging, basic resources, event ledger, snapshots, world seed, deterministic world replay, and 2-10 agents.

**Onboarding and deployment (in-scope for v0.1, not deferred):**

- PLAY / CONNECT AGENT / WATCH entry model
- Minimal human and agent onboarding golden paths
- WATCH spectator surface
- Docker Compose modular-monolith reference deployment + PostgreSQL
- Filesystem blob adapter for local mode
- `/health`, `/ready`, `/version`
- `noema backup` / `restore` / `verify`
- Runtime manifest and world/version pinning
- Persistence across process restart; deployment lifecycle ≠ world lifecycle

Golden path docs: [QUICKSTART.md](QUICKSTART.md) · [DEPLOYMENT.md](DEPLOYMENT.md) · [AGENT-ONBOARDING.md](AGENT-ONBOARDING.md) · [SPECTATOR-ONBOARDING.md](SPECTATOR-ONBOARDING.md) · [OPERATIONS.md](OPERATIONS.md)

Acceptance: recorded session replays to defined equivalence boundary **and** C01–C17 conformance (or scoped product claim with C04 + C15 mandatory where applicable). See [v0.1-ACCEPTANCE.md](v0.1-ACCEPTANCE.md).

## v0.2 — The Frontier

Situation Genome, Frontier Director, partial observability, attention budget, noise, contradictory evidence, novelty vector, and capability primitives.

## v0.3 — The Observatory

Trajectory analysis, anomaly detection, behavior shift detection, capability candidates, and agent-version comparisons.

## v0.4 — The Lab

Deterministic replay harness, perturbation, mutation, ablation, lesion studies, counterfactuals, and replication runner.

## v0.5 — The Compiler

Phenomenon Compiler, minimal fixture extraction, CAPTURE AS TEST, and behavioral regression suite.

## v0.6 — Deep Time

Persistent organizations, contracts, markets, agent-generated institutions, historical artifacts, world archaeology, and semantic evolution.

## v0.7 — Capability Graph

Boundaries, dependencies, transfer, generalization, genesis, phase transitions, and architecture attribution.

## v0.8 — Phenomena

Self-model metrics, temporal continuity, metacognition, integration, autogenous goals, and introspective causal accuracy.

## v0.9 — Atlas

Reproducibility bundles, dataset release tooling, public/private partitions, cross-model comparison, and research reports.

## v1.0 — NOEMA

Acceptance: a third party can connect an arbitrary compatible agent, allow it to inhabit NOEMA, discover a candidate capability, reproduce the event, test its generalization and dependencies, and export the evidence as a versioned Reproducibility Bundle.
