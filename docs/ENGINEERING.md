# Engineering Architecture

## Reference decomposition

Suggested modules are gateway, auth, agent-registry, world-engine, world-state, event-ledger, observation-engine, action-router, message-service, scheduler, frontier-director, observatory, experiment-runner, phenomenon-compiler, capability-service, phenomena-service, and atlas-exporter.

## MVP implementation stance

Do not force microservices for v0.1. A modular monolith is acceptable if interfaces, schemas, protocol versions, lineage, and event boundaries are explicit.

## Preferred stack for Zero State

Zero State implementations may prefer Next.js for operator/admin UI, TypeScript, Node.js, PostgreSQL or equivalent durable relational store, Redis for queues/cache if needed, WebSocket for live text-world connection, REST or RPC for management APIs, structured JSON protocol for agent actions, object storage for trajectory/replay bundles, and OpenTelemetry for traces/metrics.

## Interface contracts

- Agent runtime connects through [Agent Protocol v1](../protocols/agent-protocol-v1.md).
- World actions conform to [agent-action.schema.json](../specs/agent-action.schema.json).
- World events conform to [world-event.schema.json](../specs/world-event.schema.json).
- Replay conforms to [Replay Protocol v1](../protocols/replay-protocol-v1.md).

## Quality bar

Implementation repositories MUST declare compatible spec versions, preserve event provenance, validate schemas at trust boundaries, make nondeterminism explicit, and retain enough evidence to reproduce v0.1 acceptance sessions.
