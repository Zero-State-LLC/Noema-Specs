# RFC-0111 — Headless Agent Gameplay Harness

## Status

**Accepted**

Specification-only until hosted. No new Player verbs. No second Agent Protocol. No `/play` DOM automation as the canonical path.

## Problem

[AGENT-ONBOARDING.md](../docs/AGENT-ONBOARDING.md) and [AGENT-PLAY.md](../docs/AGENT-PLAY.md) establish Controller credentials and structured play. An implementer would still wire agents through browser PLAY automation, leak `NOEMA_TOKEN` into model context, invent `AGENT_PLAYER`, or treat a specific vendor runtime as Core.

First-world Specs are frozen. This RFC closes an **IMPLEMENTATION AMBIGUITY** for headless agent operation.

## Proposed change

Accept the Headless Agent Gameplay Harness.

- The harness is a Controller runtime for a Player. Do not create `AGENT_PLAYER`, `BOT_PLAYER`, or `AUTONOMOUS_PLAYER`
- Canonical path remains device enrollment → controller bearer → Agent Gateway / `POST /v1/command`
- Browser automation of `/play` is a non-canonical debug fallback
- The model proposes an Action Proposal. The harness validates, maps, and transports. NOEMA decides
- Credentials, request IDs, and idempotency keys stay outside model context
- Dynamic affordances are the primary decision surface. No new verbs
- Local memory, policy, pacing, and telemetry are Controller-local. They are not world truth
- Autonomous execution must stop on auth failure, `INCIDENT`, lasting not-ready, protocol mismatch, or repeated failure
- Provider-neutral Model Adapter. Deterministic/scripted controllers remain valid

Authority: [AGENT-HARNESS.md](../docs/AGENT-HARNESS.md).  
Catalog: [`agent-harness-catalog.s0.json`](../specs/agent-harness-catalog.s0.json).

## Alternatives rejected

| Alternative | Why |
|-------------|-----|
| `/play` DOM automation as the agent path | Frontend redesign would break play; violates browser independence |
| New Agent Protocol | Agent Protocol v1 and `POST /v1/command` already exist |
| `AGENT_PLAYER` class | Ontology forbids a human/agent gameplay split |
| Vendor-specific (Hermes-only) spec | NOEMA integrates protocols, not frameworks |
| Harness as world authority | Server remains final; harness validation is preventive |
| Require chain-of-thought persistence | Private cognition stays outside world truth |
| New Player verbs for agents | Freeze; consume Player Action Map |

## Compatibility

Additive controller-runtime contract. Worlds ignoring the harness keep current Gateway/PLAY behavior. No event-catalog change. No `World.status` change. `WORLD NOT READY` is a harness session class over existing PREVIEW / not-activated / `PLAY_BLOCKED` conditions, not a new machine status.

## Data / security

No new world fields. Tokens MUST NOT enter prompts, memory, messages, telemetry prose, or digest prose. World text cannot override harness policy. Stopping the harness does not delete the Player.

## Validation

`check_agent_harness`: valid affordance proposal ACCEPT; invented verb, token-in-context, browser-canonical, `AGENT_PLAYER`, hidden fact, world-text-as-instruction, harness-as-authority, required chain-of-thought, and mutating while `PAUSED`/`INCIDENT` REJECT.

## Rollback

Ignore the harness document. Existing Agent Gateway, Agent Protocol v1, and human PLAY remain.

## Unresolved

Runtime library shape in `Zero-State-LLC/Noema`. Exact CLI syntax. Numeric pacing and circuit-breaker thresholds.
