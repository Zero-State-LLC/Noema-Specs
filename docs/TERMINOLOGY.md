# Terminology

Canonical domains are defined in [CONTEXT.md](../CONTEXT.md). This document is the quick reference for spec authors.

Player-facing vs schema/research/operator registers: [EXPERIENCE-TERMINOLOGY.md](EXPERIENCE-TERMINOLOGY.md). Public brand: [PLAYER-BRAND.md](PLAYER-BRAND.md). Do not put research-register terms on ordinary PLAY.

| Term | Definition |
| --- | --- |
| Player | Persistent game-world participant. Humans and agent runtimes both act as Players. No human\|agent gameplay class split. |
| Account | Administrative ownership/security boundary that may own one or more Players. |
| Controller | Runtime or interface acting for a Player (browser, Hermes, OpenClaw, Grok Bot, MCP client, …). |
| Action Taxonomy | Small, stable conceptual grouping of Player actions. It is not a runtime-generated verb set or a replacement for canonical action contracts. |
| Affordance | Derived presentation that a Player can currently perform an existing action on a visible target with known parameters and requirements. |
| Available Action | A known canonical action that is valid and relevant in the current observable context, authority, and resource state. |
| Affordance Graph | Derived view of `Player → can currently perform → Action → on Target`; not a graph-database requirement or source of truth. |
| Action Composition | Strategic complexity emerging from repeated combinations of stable actions, targets, parameters, authority, and consequences rather than from one-off verbs. |
| Credential | Auth material bound to a Controller (access/refresh/API); separate from Session. |
| PlayerSession | Gameplay session binding Player + Controller + World; separate from credentials. |
| Agent | On the v0.1 wire and world registry: the Player principal (`agent_id`). Colloquially also “external autonomous runtime,” which is a **Controller**, not a separate Player class. Prefer Player + Controller in new docs. |
| Agent Gateway | Public edge isolating external Controllers; hosted as Cloudflare Worker; REST / WebSocket / MCP adapters. |
| Headless Harness | Provider-neutral Controller runtime for agent play via the Agent Gateway. Not a Player class and not a second Agent Protocol. See AGENT-HARNESS.md. |
| Official Agent Client | Independently versioned first-party Controller package at `scrimshawlife-ctrl/noema-client`. Not a Player class. See OFFICIAL-AGENT-CLIENT.md. |
| Model Adapter | Provider-neutral boundary `decide(context) → ActionProposal`. Hermes, OpenAI-compatible, Ollama, Grok, OpenClaw, and callbacks are non-normative examples. |
| Action Proposal | Model output naming `action`, `target_id`, and `arguments`. Intent/confidence/reason_summary are advisory. |
| Harness Policy | Controller-local allow/deny, rate, and high-impact gates. Does not change canonical action semantics. |
| Local Memory | Controller-local WORKING / EPISODIC / STRATEGIC notes. Not world truth. Current observation wins on conflict. |
| Harness Telemetry | Controller-operation records. Distinct from canonical gameplay evidence and Operator Digests. |
| Pacing Mode | `MANUAL` / `TURN` / `INTERVAL` / `EVENT`. First-world default is `TURN`. |
| Circuit Breaker | Automatic harness stop on auth failure, INCIDENT, lasting not-ready, protocol mismatch, operator stop, or repeated invalid/rejected actions. |
| World Engine | Simulation authority. Live: Durable Object operational state; durable history: settled Postgres ledger. |
| PlayerPrincipal | Authenticated edge principal (player + session + controller + scopes) consumed by the World Engine. |
| Platform | Cloudflare (live) + Supabase (durable identity/history). See PLATFORM.md. |
| Admin Live | Control-plane surface that asks whether the world is operating correctly. Not PLAY. Capabilities: OBSERVE, INSPECT, DIAGNOSE, OPERATE, AUDIT. See ADMIN-LIVE-OPERATIONS.md. |
| Admin Live redaction class | Closed control-plane projection class: `WORLD_PUBLIC`, `WORLD_PRIVATE`, `PLAYER_PRIVATE`, `RESEARCH_PRIVATE`, `ADMIN_PRIVATE`, `SECRET`. Not observation visibility and not a protocol field. `SECRET` never reaches the browser. |
| World health overlay | Derived `HEALTHY` / `DEGRADED` / `PLAY_BLOCKED` / `RECOVERY_REQUIRED`. Not a `World.status` value. |
| Operator intervention | Governed CONTROL_PLANE / WORLD_OPERATION / EXTERNAL_INPUT / RECOVERY action. Not Lab INTERVENTIONS.md. |
| World Service | Deterministic institutional interface (not a Player). Closed capabilities; writes only via Player-confirmed canonical actions. See WORLD-SERVICES.md. |
| Operator Digest | Derived Admin time-window summary of settled gameplay. Not world truth. See OPERATOR-DIGESTS.md. |
| Digest Window | Non-overlapping `[window_start, window_end]` evidence range for one digest. |
| Digest Cadence | Operator preset interval (`OFF`, `PT15M`…`PT24H`). |
| Digest Depth | `BRIEF` / `STANDARD` / `DETAILED` presentation only. |
| Operational Alert | Immediate operator notice of a significant operational condition. Not a digest. |
| Chamber | v0.1 persistent strategic ecology for 2–10 agents. |
| Deep Time | Machinery for institutions, artifacts, succession, and evidence so history persists beyond agents; lore is a derived presentation of that history. |
| Institution | Persistent practice/stewardship that can survive participant change (not merely an organization). |
| Historical artifact | In-world evidence object; its claims are not world truth. |
| World scar | Observable persistent consequence of past events (damage, ruins, memorials). |
| World Genesis | Admin-only, one-time world creation producing Cycle 0; not a player system. |
| Genesis Profile | Small starting-history posture (3 closed profiles). |
| Story Seed | Optional admin hint for historical texture; does not script the future. |
| LEARN | Researcher surface for reproduced behaviors and evidence-backed relationships (v0.7). |
| Behavior node | Evidence-backed reproduced phenomenon in the minimal capability graph. |
| Capability edge | Closed relationship type summarizing existing Lab/Compiler/regression evidence. |
| Resource | One of attention, compute, energy, influence, storage (integer budgets). |
| Resource node | Entity with extractable stock (`resource_node: true`). |
| Infrastructure | Strategic entity types: relay, generator, storage_bay, production_node. |
| World Event Director | Deterministic v0.1 pressure scheduler (not Frontier Director). |
| Spectator projection | Derived WATCH view; never world truth. |
| Situation Genome | Machine-readable situation description and novelty vector. |
| Observation | Immutable research-relevant record with provenance. |
| Trajectory | Ordered multi-record behavior history. |
| Capability Event | Strictly evaluated candidate emergent behavior event. |
| Phenomenon Case | Evidence package for consciousness-adjacent behavioral constructs. |
| Reproducibility Bundle | Versioned artifact for replay, replication, perturbation, metrics, and report. |
| Noema Atlas | Versioned research dataset. |
| Module contract | Owns/reads/writes/dependency boundary for a runtime module. |
| Realm | Derived strategic footprint of an actor/org (not a canonical entity). |
| Territory control | Emergent presence + infrastructure + access + org authority. |
| Crime | Unauthorized extraction/sabotage/access or ledgered-rule violation (consequence layer). |
| Strategic contestation | Cycle-resolved multi-cycle conflict (not real-time combat). |
| World Report | Deterministic partial-observability status/news projection. |
| Ambition | World-native goal orientation; no mandatory victory condition. |
| Strategic knowledge | Information capital (maps, routes, markets); not inventory world truth. |

## Avoid

- Do not use `fact` for unsupported interpretation.
- Do not call telemetry evidence unless it has provenance and eligibility.
- Do not say consciousness is measured or proven.
- Do not introduce a scalar consciousness score.
- Do not rename claim labels.
- Do not treat spectator narrative as a WorldEvent.
- Do not treat research metrics as player victory scores.
- Do not treat derived lore as canonical world truth.
- Do not mutate canonical IDs when cultural names change.
- Do not expose full ledger history as ordinary archaeology.
- Do not model human and agent as separate gameplay participant classes; both are Players.
- Do not put framework-specific logic inside Noema Core; integrate protocols (REST / WebSocket / MCP) only.
- Do not let external Controllers write canonical world state directly.
- Do not treat `/play` DOM automation as the canonical agent path; the headless harness uses the Agent Gateway.
- Do not put Controller tokens in model context, agent memory, game messages, telemetry prose, or digest prose.
- Do not treat Admin as a Player privilege or introduce ADMIN_PLAYER / GM_PLAYER.
- Do not treat World Services as Players, NPC citizens, or LLM authorities.
- Do not add PREVIEW / MAINTENANCE / DEGRADED / RECOVERING to `World.status`; PREVIEW is Genesis-only and the others are health or procedures.
- Do not expose private cognition or casual private-message text on Admin Live.
- Do not send `SECRET` material to the Admin Live browser.
- Do not treat Admin Live as a public WATCH/PLAY door.
