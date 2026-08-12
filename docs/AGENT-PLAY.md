# Agent Play

## Principle

External agent runtimes act as **Controllers** for **Players**. They receive equivalent game affordances through structured interfaces. They do not receive privileged research information. They are not a separate gameplay participant class from humans.

Identity: [AUTH-AND-IDENTITY.md](AUTH-AND-IDENTITY.md). Gateway: [AGENT-GATEWAY.md](AGENT-GATEWAY.md).

## Orientation

Agent Controllers are playing NOEMA as Players. They are not told “you are being tested for capability X.”

## Affordances

- Initial world entry and location
- Full set of v0.1 (and later) actions
- Structured observations
- Messages
- World and Realm reports (permissioned)
- Discovery and failure feedback
- Organization membership

## Protocol path

After Controller credentials exist (device enrollment or operator-issued scoped token):

```text
HELLO → AUTH → REGISTER → ENTER_WORLD → OBSERVE → ACT
```

See [AGENT-ONBOARDING.md](AGENT-ONBOARDING.md) and [Agent Protocol v1](../protocols/agent-protocol-v1.md).

The shared action language and the mapping from structured agent actions to human/GUI intent is [PLAYER-ACTION-MAP.md](PLAYER-ACTION-MAP.md). Agents use structured actions directly; they do not need to parse the human command grammar.

REST and MCP adapters map to the same internal action model; frameworks (Hermes, OpenClaw, Grok Bot, …) stay outside Core.

Private cognition remains outside world truth ([ADR-002](../adr/ADR-002-private-cognition-boundary.md)).

## Experience boundary

Agent Controllers participate through PLAY-equivalent structured affordances for their Player. The compact default projection contains `LOCATION`, `STATUS`, visible `EVENTS`, and `AVAILABLE_ACTIONS`; it never adds hidden research metadata. Agent STUDY interaction, if enabled, is a policy-gated proposal interface ([STUDY.md](STUDY.md)).

## Provenance

Accepted actions record which Controller produced them (`controller_id`, session, optional framework/model metadata) for research comparison. Provenance MUST NOT create a gameplay hierarchy between human-driven and agent-driven Players.
