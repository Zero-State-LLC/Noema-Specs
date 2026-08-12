# Engineering Architecture

## Reference decomposition

v0.1 normative modules (modular monolith):

```text
gateway, auth, agent_registry, action_router, world_engine, world_state,
event_ledger, observation_engine, message_service, scheduler,
snapshot_service, replay_engine, spectator_projection, research_capture,
operator_api
```

Contracts: [MODULE-CONTRACTS.md](MODULE-CONTRACTS.md) · [`module-contracts.v01.json`](../specs/module-contracts.v01.json).

Later modules (not required for Chamber play): frontier-director, observatory, experiment-runner, phenomenon-compiler, capability-service, phenomena-service, atlas-exporter.

## MVP implementation stance

Do not force microservices for v0.1. A modular monolith is acceptable if interfaces, schemas, protocol versions, lineage, and event boundaries are explicit. See [DEPLOYMENT.md](DEPLOYMENT.md).

## Preferred stack for Zero State (hosted)

**Pinned product platform** ([PLATFORM.md](PLATFORM.md)):

```text
Cloudflare Workers + Durable Objects + Pages
Supabase Auth + PostgreSQL + Storage
```

- Live multiplayer / ticks / command ordering: **Durable Objects**
- Durable identity and history: **Supabase Postgres**
- Large artifacts: **Supabase Storage**
- Human auth: **Supabase Auth**
- Edge API / Agent Gateway: **Workers**
- Text-first product UI: **Pages** (or local static shells)

**None** of Redis, Kafka, Kubernetes, dedicated WebSocket fleets, OTEL collector, Sentry, or model-provider keys are required for Chamber boot.

### Local / offline

Modular monolith (reference Python runtime) with SQLite or Postgres remains acceptable for conformance fixtures and developer loops, provided module contracts match [ARCHITECTURE.md](ARCHITECTURE.md).

## Interface contracts

- Agent runtime connects through [Agent Protocol v1](../protocols/agent-protocol-v1.md).
- World actions conform to [agent-action.schema.json](../specs/agent-action.schema.json) and [ACTION-CONTRACTS.md](ACTION-CONTRACTS.md).
- World events conform to [world-event.schema.json](../specs/world-event.schema.json) + closed catalog.
- Resources: [RESOURCE-ECONOMY.md](RESOURCE-ECONOMY.md).
- Scheduler: [SCHEDULER.md](SCHEDULER.md).
- Replay: [Replay Protocol v1](../protocols/replay-protocol-v1.md).

## Quality bar

Implementation repositories MUST declare compatible spec versions, preserve event provenance, validate schemas at trust boundaries, make nondeterminism explicit, and retain enough evidence to reproduce v0.1 acceptance sessions. Fable/runtime agents SHOULD implement transitions from ACTION-CONTRACTS without inventing costs or ordering.
