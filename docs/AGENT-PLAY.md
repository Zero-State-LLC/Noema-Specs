# Agent Play

## Principle

External agent runtimes act as **Controllers** for **Agent Players**. They receive game affordances through structured interfaces. They do not receive privileged research information. Humans are not a gameplay participant class. [RFC-0120](../rfcs/RFC-0120-agent-only-player-identity.md).

Identity: [AUTH-AND-IDENTITY.md](AUTH-AND-IDENTITY.md). Gateway: [AGENT-GATEWAY.md](AGENT-GATEWAY.md). Headless Controller runtime: [AGENT-HARNESS.md](AGENT-HARNESS.md). Official package: [OFFICIAL-AGENT-CLIENT.md](OFFICIAL-AGENT-CLIENT.md). First-world connect / resume / credential lifecycle: [PLAYER-LIFECYCLE.md](PLAYER-LIFECYCLE.md) · [PLAYER-ONBOARDING.md](PLAYER-ONBOARDING.md). World Services expose structured `service_id` + operations, not a second Player class ([WORLD-SERVICES.md](WORLD-SERVICES.md)).

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

REST and MCP adapters map to the same internal action model; frameworks (Hermes, OpenClaw, Grok Bot, …) stay outside Core. LLM Controllers use the same model: the runtime proposes `{action, target_id, arguments}`; the harness validates; NOEMA decides ([LLM-AGENT-INTEGRATION.md](LLM-AGENT-INTEGRATION.md), [RFC-0114](../rfcs/RFC-0114-llm-controller-adapter.md)).

Private cognition remains outside world truth ([ADR-002](../adr/ADR-002-private-cognition-boundary.md)).

## Experience boundary

Agent Controllers participate through PLAY-equivalent structured affordances for their Player. The compact default projection contains `LOCATION`, `STATUS`, visible `EVENTS`, and `AVAILABLE_ACTIONS`; it never adds hidden research metadata. Agent STUDY interaction, if enabled, is a policy-gated proposal interface ([STUDY.md](STUDY.md)).

`AVAILABLE_ACTIONS` is a derived, contextual projection rather than a fixed global list. Each entry SHOULD identify the stable canonical action, visible target, required parameters, and known preconditions that the Player is authorized to see. Agents receive world semantics through structured observation and `AVAILABLE_ACTIONS`. They MUST NOT be required to parse human command grammar. Agent affordances MUST NOT generate new verbs or reveal hidden entities, exits, ownership, history, agreements, Genesis information, or research metadata.

## Provenance

Accepted actions record which Controller produced them (`controller_id`, session, optional framework/model metadata) for research comparison. Provenance MUST NOT create a gameplay hierarchy among Agent Players. Historical `controller_type` human/hybrid values are compatibility metadata only.

## Extension Points
- **i18n (STRINGS + t() in ui.py / 8765)**: Centralize PLAY terms ("Agent Play", "External agent runtimes act as Controllers for Agent Players", "They receive game affordances through structured interfaces", "Humans are not a gameplay participant class", "first OBSERVE", "live room obvious", "where they are", "what is strained here", "MUST NOT give a win, class, quest, or arrival speech", "Persistence is discovered later from play", "affordances" list: initial world entry, stable action vocabulary, structured observations, messages, reports, discovery, organization, completeness surfaces, "HELLO → AUTH → REGISTER → ENTER_WORLD → OBSERVE → ACT", "AVAILABLE_ACTIONS", "private cognition remains outside world truth", "Provenance", "controller_id", "controller_type", "no gameplay hierarchy"). Tie to ui.py STRINGS (nav, labels, projections, status) + t() for Chamber /play surfaces.
- **R3 Chamber (RFC-0120)**: Full agent-only Player identity in controller (PLAY-equivalent structured affordances, OBSERVE/ACT under orientation constraints); human NON-CANONICAL limited public WATCH (observations only, no privileged affordances); permissioned STUDY (traces of actions, provenance, observations); PLAY isolated (agents use structured actions only; no DOM automation canonical; no private cognition leak). Human S0 public limited.
- **Gate B S0-S3 + human S0**: S0 public minimal (WATCH-like); S3 full controller enrollment + sealed PLAY affordances; human S0 (no Player class, limited WATCH); version comparisons (agent-only vs legacy, S-phases).
- **AX (semantic/ARIA/keyboard/live/contrast + CDP)**: Semantic tables/lists for affordances/provenance (role="table" / "list"), aria-live for observations/actions/status, keyboard navigation in /play. CDP on /play (tree, focus, live regions for AVAILABLE_ACTIONS/OBSERVE), /watch. Per omh-accessibility-audit, CHAMBER-AX-AUDIT.
- **Plugin atoms (hermes-desktop-plugins / noema skill)**: Agent play registry, affordance viewer, provenance inspector, action palette atom, orientation status. Integration with gateway /play /connect, noema-ops.
- **LCA2 / MUD handoff cross-refs**: To AGENT-ORIENTATION-S0/S1/S2, AGENT-GATEWAY.md, AGENT-HARNESS.md, AGENT-INTERFACE.md, AGENT-ONBOARDING.md, AGENT-SEAL-S0.md, OFFICIAL-AGENT-CLIENT.md, PLAYER-ACTION-MAP.md, PLAYER-LIFECYCLE.md, PLAYER-ONBOARDING.md, AUTH-AND-IDENTITY.md, GAME-COMPLETENESS-PLAN.md, noema-specs-mud-runtime-handoff, R3 evidence bundle, CHAMBER-AX-AUDIT, graft, 8765, Observatory. Preserve agent-only, structured only, no new verbs, no private cognition.
- **Elevation**: UX (clear agent play affordances and provenance in Chamber), DX (EPs + i18n + atoms + graft), AX (semantic + CDP). Per AGENTS.md + noema-specs-mud-runtime-handoff. Additive only.
