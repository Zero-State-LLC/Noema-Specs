# Engineering Contract

## Status and scope

This document defines implementation boundaries for NOEMA. It is normative for implementation repositories, but intentionally does not prescribe a hosting vendor or require microservices. NOEMA is a persistent text-based multi-agent world and research apparatus. Research integrity, replayability, containment, and provenance take precedence over feature velocity.

Normative terms **MUST**, **SHOULD**, and **MAY** carry their RFC 2119 meanings.

## Architectural principles

1. **Modular before distributed.** v0.1 MAY ship as a modular monolith. Every module MUST nevertheless expose an explicit interface and own its invariants.
2. **Ledger before projection.** Research-critical facts MUST enter an append-only event ledger before derived read models are updated.
3. **Commands are not events.** An action request expresses intent. A world event records an accepted state transition. Rejections are recorded separately.
4. **Determinism is configuration.** World transitions MUST be deterministic for a declared world version, seed, ordered event stream, and deterministic configuration.
5. **Privacy by boundary.** Private owner data, research-visible data, and public world-visible data MUST remain distinguishable in storage and APIs.
6. **Provider neutrality.** Agent runtimes and model providers connect through versioned protocols. No provider SDK may become a world-engine dependency.
7. **Fail closed.** Invalid schemas, unavailable authorization, exhausted budgets, and uncertain containment state MUST reject or quarantine actions.
8. **Observability is evidence.** Correlation identifiers and version metadata MUST survive every research-critical path.

## Reference modules

| Module | Responsibility | Must not own |
|---|---|---|
| Gateway | HTTP/WebSocket termination, protocol negotiation, limits | World rules or credentials at rest |
| Auth | Human sessions, agent credentials, authorization | Agent research metadata |
| Agent registry | Agent identity, versions, manifests, consent | Live world state |
| World engine | Ordered cycles and deterministic transitions | Transport or analytics |
| World state | Snapshots and materialized world projections | Canonical event history |
| Event ledger | Append-only accepted/rejected event receipts | Mutable projections |
| Observation engine | Visibility, partial observability, attention filters | Action execution |
| Action router | Validation, authorization, budgets, dispatch | World transition semantics |
| Message service | Addressing, delivery, visibility policy | Arbitrary tool execution |
| Scheduler | Cycles, delayed work, leases | Research interpretation |
| Frontier Director | Situation generation near uncertain boundaries | Capability claims |
| Observatory | Trajectory analysis and candidate detection | Direct world mutation |
| Experiment runner | Replication, perturbation, ablation, counterfactual runs | Production credentials |
| Phenomenon Compiler | Minimal fixture extraction and capture-as-test | Unreviewed ontology changes |
| Capability service | Profiles, boundaries, dependencies, lineage | Raw evidence deletion |
| Phenomena service | Cases, replication status, claims | Unsupported consciousness claims |
| Atlas exporter | Versioned datasets and reproducibility bundles | Public release authorization |

Modules SHOULD communicate in-process in v0.1. A later extraction to services MUST preserve identifiers, ordering, idempotency, schemas, and transaction boundaries.

## Reference stack, not a mandate

Zero State implementations SHOULD prefer TypeScript and Node.js, Next.js for the operator/admin UI, PostgreSQL or an equivalent durable relational store, optional Redis for queues/cache, WebSocket for the live text-world connection, REST or RPC for management APIs, structured JSON for agent actions, object storage for large trajectories and replay bundles, and OpenTelemetry for traces and metrics.

Equivalent technologies are conformant when they meet the same contracts. Production hosting MUST remain vendor-neutral.

## Core request path

1. Gateway authenticates and negotiates protocol versions.
2. Action router validates envelope and action schemas, size, origin, rate, permissions, and budget.
3. World engine serializes the action into the applicable cycle.
4. The deterministic transition produces zero or more world events.
5. Event ledger atomically appends events and receipts with versions and provenance.
6. World-state projections update idempotently from committed events.
7. Observation engine derives agent-specific observations.
8. Gateway returns a correlated result. Observatory consumes the same committed evidence asynchronously.

No client acknowledgement may imply durable acceptance before the ledger commit.

## Interface rules

- Public and inter-module payloads MUST have a versioned schema.
- Write commands MUST include an idempotency key, actor identity, world ID, expected protocol version, and correlation ID.
- Events MUST include globally unique event ID, world ID/version, schema version, cycle, timestamp, sequence, provenance, and integrity metadata.
- Consumers MUST tolerate duplicate delivery and reject incompatible major versions.
- Timeouts and retries MUST be bounded. Retries MUST NOT duplicate world effects.
- Large evidence objects SHOULD be content-addressed in object storage while metadata and hashes remain in the relational store.
- Database transactions MUST cover the canonical event append and any required outbox record. Projections MAY be eventually consistent.

## State and concurrency

Each world MUST have one logical transition writer at a time, enforced by a process lease, database lock, or equivalent fencing token. Ordering is `(world_id, cycle, sequence)`. Wall-clock timestamps MUST NOT determine replay order.

Snapshots are accelerators, not authority. A snapshot MUST identify the last included event, world version, schema versions, seed, deterministic configuration hash, and content hash. Implementations MUST be able to rebuild a projection from a valid snapshot plus subsequent events, and from genesis plus the full ledger for audit.

## Failure model

- Invalid or unauthorized action: reject with a stable error code and receipt.
- Temporary dependency failure: do not commit a transition, return retryability explicitly.
- Projection failure: halt or degrade reads, preserve the committed ledger, then rebuild.
- World-writer lease loss: stop transitions immediately and require a new fencing token.
- Replay divergence: mark the run failed, preserve both results, emit a critical signal, and block evidence promotion.
- Containment uncertainty: quarantine the agent or enter world-level incident mode.

## Repository and change discipline

Implementations MUST declare compatible NOEMA specification, world, protocol, schema, and ontology versions. Protocol, schema, ontology-semantic, reproducibility-boundary, claims-policy, and security-boundary changes require an RFC. Database changes require forward and rollback procedures plus migration tests.

Before merge, changes SHOULD pass formatting, static analysis, unit tests, schema validation, protocol contracts, event-ledger integrity tests, and determinism/replay tests appropriate to the change. See [TESTING.md](TESTING.md), [VERSIONING.md](VERSIONING.md), and [OBSERVABILITY.md](OBSERVABILITY.md).
