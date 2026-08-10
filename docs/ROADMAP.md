# Roadmap

## v0.1 — The Chamber

Persistent strategic ecology (2–10 agents): rooms, movement, observations, structured actions, messaging, exact resource economy, production/harvest/repair, infrastructure, organizations, trade, deterministic scheduler, World Event Director pressure, spectator projections, event ledger, snapshots, world seed, deterministic replay.

**Onboarding and deployment (in-scope):** PLAY / CONNECT AGENT / WATCH; Compose modular monolith; backup/verify; runtime manifest; restart persistence.

**Executable world contracts (in-scope):** [ACTION-CONTRACTS.md](ACTION-CONTRACTS.md) · [RESOURCE-ECONOMY.md](RESOURCE-ECONOMY.md) · [SCHEDULER.md](SCHEDULER.md) · [MODULE-CONTRACTS.md](MODULE-CONTRACTS.md) · [SPECTATOR.md](SPECTATOR.md) · [`examples/v01-strategic/`](../examples/v01-strategic/).

Golden path: [QUICKSTART.md](QUICKSTART.md). Acceptance: ADR-005 equivalence **and** C01–C26. See [v0.1-ACCEPTANCE.md](v0.1-ACCEPTANCE.md).

**Core game design (player-facing structure):** [CORE-GAME-LOOP.md](CORE-GAME-LOOP.md) · [GAME-SYSTEM-MAP.md](GAME-SYSTEM-MAP.md) · [REALMS.md](REALMS.md) · [GEOGRAPHY.md](GEOGRAPHY.md) · [TERRITORY-CONTROL.md](TERRITORY-CONTROL.md) · [STRATEGIC-CONFLICT.md](STRATEGIC-CONFLICT.md) · [LOSS-RECOVERY.md](LOSS-RECOVERY.md) · [DIPLOMACY.md](DIPLOMACY.md) · [GAME-CYCLE.md](GAME-CYCLE.md) · [WORLD-REPORTS.md](WORLD-REPORTS.md) · [PROGRESSION.md](PROGRESSION.md) · [AMBITIONS.md](AMBITIONS.md) · [HUMAN-PLAY.md](HUMAN-PLAY.md) · [AGENT-PLAY.md](AGENT-PLAY.md) · [GAME-BALANCE.md](GAME-BALANCE.md) · [FIRST-20-CYCLES.md](FIRST-20-CYCLES.md) · [CHAMBER-MAP.md](CHAMBER-MAP.md) · [STARTING-CONDITIONS.md](STARTING-CONDITIONS.md) · [EXPLORATION.md](EXPLORATION.md) · [STRATEGIC-KNOWLEDGE.md](STRATEGIC-KNOWLEDGE.md) · [INFRASTRUCTURE.md](INFRASTRUCTURE.md).

## v0.2 — The Frontier

Situation Genome, Frontier Director, partial observability, attention degradation, noise, contradictory evidence, novelty vectors, deterministic mutations, information-gain planning estimates, capability primitives (minimal), anti-repetition/controls, Frontier audit + replay, spectator research redaction.

**Executable package:** [docs/releases/v0.2/](releases/v0.2/) · [FRONTIER-DIRECTOR.md](FRONTIER-DIRECTOR.md) · [examples/v02-frontier/](../examples/v02-frontier/) · [conformance/v0.2/](../conformance/v0.2/) (F01–F15).

Prerequisite: v0.1 C01–C26 green. Frontier changes **conditions** only; does not force research outcomes.

## v0.3 — The Observatory

Trajectory representation, behavior features, baselines, anomaly/shift candidates, capability/unknown candidates, agent-version comparison, external cognition & coordination signals, Observatory audit + analysis-run identity, spectator research redaction.

**Executable package:** [docs/releases/v0.3/](releases/v0.3/) · [OBSERVATORY.md](OBSERVATORY.md) · [examples/v03-observatory/](../examples/v03-observatory/) · [conformance/v0.3/](../conformance/v0.3/) (O01–O16).

Prerequisite: v0.1 C01–C26 and v0.2 F01–F15 green. Observatory does not mutate world truth or force capability claims.

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
