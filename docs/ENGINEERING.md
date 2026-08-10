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

## Preferred stack for Zero State

Zero State implementations may prefer Next.js for operator/admin UI, TypeScript, Node.js, PostgreSQL or equivalent durable relational store, optional Redis, WebSocket for live text-world connection, REST or RPC for management APIs, structured JSON protocol for agent actions, filesystem or object storage for trajectory/replay bundles, and OpenTelemetry for traces/metrics. **None** of Redis, OTEL collector, Sentry, or model-provider keys are required for local Chamber boot.

## Interface contracts

- Agent runtime connects through [Agent Protocol v1](../protocols/agent-protocol-v1.md).
- World actions conform to [agent-action.schema.json](../specs/agent-action.schema.json) and [ACTION-CONTRACTS.md](ACTION-CONTRACTS.md).
- World events conform to [world-event.schema.json](../specs/world-event.schema.json) + closed catalog.
- Resources: [RESOURCE-ECONOMY.md](RESOURCE-ECONOMY.md).
- Scheduler: [SCHEDULER.md](SCHEDULER.md).
- Replay: [Replay Protocol v1](../protocols/replay-protocol-v1.md).

## Quality bar

Implementation repositories MUST declare compatible spec versions, preserve event provenance, validate schemas at trust boundaries, make nondeterminism explicit, and retain enough evidence to reproduce v0.1 acceptance sessions. Fable/runtime agents SHOULD implement transitions from ACTION-CONTRACTS without inventing costs or ordering.
