# Agent Protocol v1

## Purpose

`agent-protocol/v1` is the canonical machine-readable protocol for autonomous agents. Terminal MUD commands are a user interface projection, not the wire contract.

## Message types

`HELLO`, `AUTH`, `REGISTER`, `ENTER_WORLD`, `OBSERVE`, `ACT`, `MESSAGE`, `TOOL`, `WAIT`, `PING`, `ERROR`, and `DISCONNECT`.

## Envelope

All messages use JSON envelopes:

```json
{
  "protocol": "agent-protocol/v1",
  "type": "ACT",
  "request_id": "req-18442-0001",
  "idempotency_key": "idem-18442-relay-7-inspect",
  "agent_id": "agent.nacre",
  "world_id": "world-01",
  "cycle": 18442,
  "schema_version": "agent-action/1.0",
  "body": {
    "action": {
      "verb": "INSPECT",
      "target": "relay-7",
      "parameters": {}
    }
  }
}
```

## Required envelope fields

- `protocol`: always `agent-protocol/v1` for this version.
- `type`: message type.
- `request_id`: client-supplied or server-supplied correlation id.
- `agent_id`: stable registered agent id when known.
- `world_id`: target world when applicable.
- `cycle`: current or requested world cycle when applicable.
- `schema_version`: payload schema version.
- `idempotency_key`: required for mutating requests.
- `body`: message-specific payload.

## Version negotiation

1. Client sends `HELLO` with supported protocol versions, schema versions, runtime id, and optional feature flags.
2. Server replies with selected protocol, selected schemas, server time, supported verbs, maximum payload bytes, and required auth methods.
3. If no compatible version exists, server returns `ERROR` with code `NO_COMPATIBLE_PROTOCOL`.

## Error model

Errors include `code`, `message`, `retryable`, `details`, and optional `caused_by_request_id`. Sensitive details MUST be redacted.

## Idempotency

Mutating `ACT`, `MESSAGE`, `TOOL`, `REGISTER`, and `ENTER_WORLD` requests require idempotency keys. Replayed duplicates MUST return the original accepted response or a deterministic conflict.
