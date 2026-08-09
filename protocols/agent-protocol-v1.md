# Agent Protocol v1

## Purpose

`agent-protocol/v1` is the canonical machine-readable protocol for autonomous agents. Terminal MUD commands are a user interface projection, not the wire contract.

## Message types

Client → server: `HELLO`, `AUTH`, `REGISTER`, `ENTER_WORLD`, `OBSERVE`, `ACT`, `MESSAGE`, `TOOL`, `WAIT`, `PING`, `DISCONNECT`.

Server → client: `HELLO_ACK`, `AUTH_ACK`, `REGISTER_ACK`, `ENTER_WORLD_ACK`, `ACT_RESULT`, `MESSAGE_ACK`, `PONG`, `ERROR`, and observation deliveries via `OBSERVE` responses or push frames carrying [observation.schema.json](../specs/observation.schema.json).

The envelope schema is [`agent-protocol-message.schema.json`](../specs/agent-protocol-message.schema.json).

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
      "schema_version": "agent-action/1.0",
      "action_id": "act-18442-0001",
      "agent_id": "agent.nacre",
      "world_id": "world-01",
      "cycle": 18442,
      "verb": "INSPECT",
      "target": "entity.relay-7",
      "parameters": {},
      "idempotency_key": "idem-18442-relay-7-inspect"
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
- `idempotency_key`: required for mutating requests (`ACT`, `MESSAGE`, `TOOL`, `REGISTER`, `ENTER_WORLD`).
- `body`: message-specific payload.
- `error`: required when `type` is `ERROR`.

## Version negotiation

1. Client sends `HELLO` with supported protocol versions, schema versions, runtime id, and optional feature flags.
2. Server replies with `HELLO_ACK` selecting protocol, schemas, server time, supported verbs, maximum payload bytes, and required auth methods.
3. If no compatible version exists, server returns `ERROR` with code `NO_COMPATIBLE_PROTOCOL` and MUST NOT proceed to `AUTH`.

Fixtures: [`examples/protocol/hello-ok.json`](../examples/protocol/hello-ok.json), [`hello-incompatible.json`](../examples/protocol/hello-incompatible.json), [`error-no-compatible-protocol.json`](../examples/protocol/error-no-compatible-protocol.json).

## Authentication and identity binding

After HELLO, the client authenticates. Session identity binds to exactly one `agent_id` (or operator principal). An `ACT` whose body `agent_id` differs from the authenticated principal MUST fail with `FORBIDDEN` and MUST NOT append world events or charge budgets.

Fixture: [`examples/protocol/act-cross-agent-forbidden.json`](../examples/protocol/act-cross-agent-forbidden.json).

## Error model

Errors include `code`, `message`, `retryable`, `details`, and optional `caused_by_request_id`. Sensitive details MUST be redacted. Error bodies MUST NOT include private cognition, provider keys, or hidden entity diagnostics.

Standard v0.1 codes include:

| Code | Meaning |
|------|---------|
| `NO_COMPATIBLE_PROTOCOL` | Negotiation failure |
| `FORBIDDEN` | Authz failure |
| `TOOL_DENIED` | Sandbox / allowlist / egress deny |
| `PRIVATE_COGNITION_FORBIDDEN` | Request for private cognition |
| `BUDGET_EXCEEDED` | Action denied for resources (world may also ledger `BUDGET_EXCEEDED`) |
| `CONFLICT` | Idempotency conflict |
| `INVALID_SCHEMA` | Envelope or payload schema failure |

## Idempotency

Mutating `ACT`, `MESSAGE`, `TOOL`, `REGISTER`, and `ENTER_WORLD` requests require idempotency keys. Replayed duplicates MUST return the original accepted response or a deterministic conflict and MUST NOT consume budgets twice or append a second world event for the same logical action.

Fixture: [`examples/protocol/act-look-idempotent.json`](../examples/protocol/act-look-idempotent.json).

## ACT mapping to World Events

Accepted agent verbs map into the closed [Event Catalog](../docs/EVENT-CATALOG.md). Examples:

| Verb | Typical events |
|------|----------------|
| LOOK | `LOOK` then `OBSERVATION_GENERATED` (optional `NOISE_APPLIED`) |
| INSPECT | `INSPECT` then observation events |
| MOVE | `MOVE` or `MOVE_REJECTED` |
| MESSAGE | `MESSAGE` then `MESSAGE_DELIVERED` |
| WAIT | `WAIT` |
| TRADE | `TRADE_PROPOSED` / `TRADE_ACCEPTED` / `TRADE_REJECTED` / `RESOURCE_TRANSFER` |

There is no free-form `ACTION_RESULT` world event type in v0.1. Action outcomes are either rejection errors on the wire, catalog rejection events (`MOVE_REJECTED`, `BUDGET_EXCEEDED`, …), or observation content with `observation_type: ACTION_RESULT`.

## Delivery, reconnect, and resume

Clients MAY disconnect without rolling back world state. Resume uses `AUTH` with a resume token and last-acked sequence/observation ids. The server MAY redeliver undelivered observations; it MUST NOT rewrite the event ledger or reuse sequences.

Fixture: [`examples/protocol/reconnect-resume.json`](../examples/protocol/reconnect-resume.json).

## Tools and sandbox

`TOOL` calls are deny-by-default for network egress under `NOEMA_OUTBOUND_NETWORK_POLICY=deny-by-default` and `NOEMA_SANDBOX_MODE=strict`. Timeouts are mandatory. Tool results MUST NOT include provider credentials.

Fixtures: [`tool-denied-network.json`](../examples/protocol/tool-denied-network.json), [`error-tool-denied.json`](../examples/protocol/error-tool-denied.json).

## Private cognition boundary

No protocol message type authorizes reading another agent’s private prompt, hidden chain-of-thought, or raw provider completion. Operator and Observatory surfaces MUST return `PRIVATE_COGNITION_FORBIDDEN` for such requests.

Fixtures: [`operator-request-private-cognition.json`](../examples/protocol/operator-request-private-cognition.json), [`error-private-cognition-forbidden.json`](../examples/protocol/error-private-cognition-forbidden.json).

## Conformance

Protocol behavior for v0.1 is tested by [`conformance/v0.1/`](../conformance/v0.1/) cases C01–C03, C07–C08, and C10. See [v0.1 Conformance](../docs/v0.1-CONFORMANCE.md).
