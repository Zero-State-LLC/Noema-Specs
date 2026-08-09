# Event Ledger v1

## Purpose

`event-ledger/v1` defines append-only research-critical event recording for world replay, audit, tamper evidence, and Atlas export.

## Event record

World events conform to [world-event.schema.json](../specs/world-event.schema.json). The closed 24-type v0.1 `event_type` and payload catalog is defined by [Event Catalog](../docs/EVENT-CATALOG.md) and its machine-readable [event-types.json](../specs/event-types.json). Every event includes event id, type, world id, cycle, occurred timestamp, actor when applicable, sequence number, payload, provenance, and optional digest links.

## Append rules

- Events are immutable after append.
- Corrections append new events that supersede, invalidate, or annotate prior events.
- Sequence numbers are contiguous per world ledger.
- Idempotency keys prevent duplicate mutating actions.
- Ledger digests SHOULD chain previous event digest, event payload digest, and schema version.

## Tamper evidence

Implementations SHOULD sign event receipts where feasible. A receipt includes event id, sequence, world id, cycle, digest, previous digest, schema version, and signer id.

## Research use

Telemetry is not automatically evidence. Events become evidence only when provenance, consent, schema validation, and research eligibility rules are satisfied.
