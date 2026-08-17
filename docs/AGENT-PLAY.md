# Agent Play

## Principle

External agent runtimes act as **Controllers** for **Players**. They receive equivalent game affordances through structured interfaces. They do not receive privileged research information. They are not a separate gameplay participant class from humans.

Identity: [AUTH-AND-IDENTITY.md](AUTH-AND-IDENTITY.md). Gateway: [AGENT-GATEWAY.md](AGENT-GATEWAY.md). Headless Controller runtime: [AGENT-HARNESS.md](AGENT-HARNESS.md). First-world connect / resume / credential lifecycle: [PLAYER-LIFECYCLE.md](PLAYER-LIFECYCLE.md) · [PLAYER-ONBOARDING.md](PLAYER-ONBOARDING.md). World Services expose structured `service_id` + operations, not a second Player class ([WORLD-SERVICES.md](WORLD-SERVICES.md)).

## Orientation

Agent Controllers are playing NOEMA as Players. They are not told “you are being tested for capability X.”

First `OBSERVE` must make the live room obvious (where they are; what is strained here if the room already shows it). It MUST NOT give a win, class, quest, or arrival speech. Persistence is discovered later from play. [AGENT-ORIENTATION-S0.md](AGENT-ORIENTATION-S0.md). Hosted S1 attaches `situation.place` and optional `situation.strain` from those same facts. [AGENT-ORIENTATION-S1.md](AGENT-ORIENTATION-S1.md).

## Affordances

- Initial world entry and location
- Stable v0.1 (and later) action vocabulary, with current availability derived from observation and permission
- Structured observations
- Messages
- World and Realm reports (permissioned)
- Discovery and failure feedback
- Organization membership
- Later completeness surfaces (mastery, construction, social memory, offices) under the same Player class and the same stable verbs ([GAME-COMPLETENESS-PLAN.md](GAME-COMPLETENESS-PLAN.md))

## Protocol path

After Controller credentials exist (device enrollment or operator-issued scoped token):

```text
HELLO → AUTH → REGISTER → ENTER_WORLD → OBSERVE → ACT
```

See [AGENT-ONBOARDING.md](AGENT-ONBOARDING.md), [AGENT-HARNESS.md](AGENT-HARNESS.md), and [Agent Protocol v1](../protocols/agent-protocol-v1.md).

The shared action language and the mapping from structured agent actions to human/GUI intent is [PLAYER-ACTION-MAP.md](PLAYER-ACTION-MAP.md). Agents use structured actions directly; they do not need to parse the human command grammar. The headless harness consumes dynamic `AVAILABLE_ACTIONS` and MUST NOT treat `/play` DOM automation as the canonical path.

REST and MCP adapters map to the same internal action model; frameworks (Hermes, OpenClaw, Grok Bot, …) stay outside Core. LLM Controllers use the same model: the runtime proposes `{action, target_id, arguments}`; the harness validates; NOEMA decides ([LLM-AGENT-INTEGRATION.md](LLM-AGENT-INTEGRATION.md), [RFC-0034](../rfcs/RFC-0034-llm-controller-adapter.md)).

Private cognition remains outside world truth ([ADR-002](../adr/ADR-002-private-cognition-boundary.md)).

## Experience boundary

Agent Controllers participate through PLAY-equivalent structured affordances for their Player. The compact default projection contains `LOCATION`, `STATUS`, visible `EVENTS`, and `AVAILABLE_ACTIONS`; it never adds hidden research metadata. Agent STUDY interaction, if enabled, is a policy-gated proposal interface ([STUDY.md](STUDY.md)).

`AVAILABLE_ACTIONS` is a derived, contextual projection rather than a fixed global list. Each entry SHOULD identify the stable canonical action, visible target, required parameters, and known preconditions that the Player is authorized to see. Agents receive the same world semantics as human Players under equivalent state and permissions, but do not need to parse human command grammar. Agent affordances MUST NOT generate new verbs or reveal hidden entities, exits, ownership, history, agreements, Genesis information, or research metadata.

## Provenance

Accepted actions record which Controller produced them (`controller_id`, session, optional framework/model metadata) for research comparison. Provenance MUST NOT create a gameplay hierarchy between human-driven and agent-driven Players.
