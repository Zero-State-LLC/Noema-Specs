# Noema Protocol 1.0

## Status and identifiers

This document defines protocol `noema.core` version `1.0.0`. Every wire document MUST carry these exact values in `protocol_id` and `protocol_version`. Protocol evolution follows semantic versioning. A receiver MUST reject an unsupported major version and MUST ignore only extension fields explicitly allowed by a negotiated schema.

The normative schemas are JSON Schema draft 2020-12 documents under `specs/`. RFC 2119 keywords are normative.

## Transport-neutral envelope

Commands, events, and replay requests are UTF-8 JSON objects. UUIDs MUST use canonical lowercase representation. Timestamps MUST be RFC 3339 UTC instants. Producers MUST NOT send members not defined by the applicable schema.

All messages contain `protocol_id`, `protocol_version`, `message_id`, `message_type`, `occurred_at`, `tenant_id`, `stream_id`, `correlation_id`, optional `causation_id`, and bounded scalar `metadata`.

`message_id` is the idempotency key. Consumers MUST durably deduplicate it within their advertised retention window.

## Commands

A command requests one state transition. `command.name` is a machine-readable dotted token matching `^[a-z][a-z0-9]*(?:\.[a-z][a-z0-9_]*)+$`. A command MUST state `target`, `expected_stream_version`, and an object `arguments`.

`expected_stream_version` provides optimistic concurrency: `0` requires a new stream, a positive integer requires that current stream version, and `null` explicitly disables the precondition. A handler emits zero or more events. Rejected commands MUST NOT advance the stream.

## Events

An event records an immutable fact. `event.name` follows the command-name grammar. `event_id` MUST equal envelope `message_id`. `stream_version` is positive and contiguous within a stream. `global_position` is positive and contiguous within an event store. `schema_version` identifies the event payload contract.

Stores MUST enforce uniqueness of `(tenant_id, stream_id, stream_version)`, `event_id`, and `global_position`. Events MUST NOT be updated in place. Corrections are new events.

## Replay

A replay request selects an inclusive global-position interval. Omitted `to_position` means the store's stable high-water mark captured when replay begins. Results MUST be ordered by ascending `global_position` and MUST contain no gaps inside the selected tenant range unless `allow_gaps` is true.

`batch_size` limits one response batch. `event_names` optionally filters events but does not renumber positions. A replay consumer MUST checkpoint the last fully applied `global_position`. Reapplying an event with the same `event_id` MUST be harmless.

Live handoff is race-free when the consumer records the replay high-water mark, consumes through it, then subscribes live starting at the next position.

## Determinism

Given the same ordered events and initial state, a conforming projector MUST produce the same state. Projectors MUST derive state from event fields and deterministic configuration, not wall-clock time, random values, or mutable external data. Side effects MUST be suppressed during replay or protected by event-id idempotency.

## Security and limits

Transports MUST authenticate principals and authorize tenant and stream access. Credentials and secrets MUST NOT appear in payloads or metadata. Implementations SHOULD bound document size, nesting, replay range, and batch size more tightly than schema maxima.
