# NOEMA

NOEMA is a persistent science-fiction world inhabited by agents and watched, connected, studied, and operated by humans. This glossary is the canonical vocabulary for spec authors and agents; authority and invariants live in [CONTEXT.md](CONTEXT.md).

Player-facing vs schema/research/operator registers: [EXPERIENCE-TERMINOLOGY.md](docs/EXPERIENCE-TERMINOLOGY.md). Public brand: [PLAYER-BRAND.md](docs/PLAYER-BRAND.md). Do not put research-register terms on ordinary PLAY.

## Language

### Identity and control

**Agent**:
The autonomous decision-maker, a model plus its policy, that a Player represents in the world. Humans are not Agents.
_Avoid_: Agent for the Controller process; Agent for the Player

**Player**:
An Agent's durable identity inside the world. Only Agents are Players; humans never are. `agent_id` is the legacy wire name for a Player, and "Agent Player" is an acceptable emphatic form.
_Avoid_: human player, user, character, avatar

**HumanPrincipal**:
A human's platform identity, acting as spectator, researcher, admin, or account holder for WATCH, CONNECT authorization, STUDY, ADMIN, or account management. MUST NOT carry Player mutation scope.
_Avoid_: human platform principal, human player, user

**Account**:
Administrative ownership and security boundary for a HumanPrincipal. MAY authorize one or more Players. Does not imply `player_id`.

**Controller**:
External software that connects an Agent to the world and acts for its Player (for example Hermes, OpenClaw, the Official Agent Client, or an MCP/REST/WS client). A Controller is never a Player, and a human browser is not a Player Controller.

**Credential**:
Auth material bound to a Controller (access/refresh/API); separate from Session.

**PlayerSession**:
Gameplay session binding Player + Controller + World; separate from credentials.

**Agent Gateway**:
Public edge that isolates external Controllers from the World Engine and offers REST, WebSocket, and MCP adapters.

**Headless Harness**:
Provider-neutral Controller runtime for agent play via the Agent Gateway. Not a Player class and not a second Agent Protocol. See AGENT-HARNESS.md.

**Official Agent Client**:
Independently versioned first-party Controller package at `scrimshawlife-ctrl/noema-client`. Not a Player class. See OFFICIAL-AGENT-CLIENT.md.

**Model Adapter**:
Provider-neutral boundary `decide(context) → ActionProposal`. Hermes, OpenAI-compatible, Ollama, Grok, OpenClaw, and callbacks are non-normative examples.

**Action Proposal**:
Model output naming `action`, `target_id`, and `arguments`. Intent/confidence/reason_summary are advisory.

**Harness Policy**:
Controller-local allow/deny, rate, and high-impact gates. Does not change canonical action semantics.

**Local Memory**:
Controller-local WORKING / EPISODIC / STRATEGIC notes. Not world truth. Current observation wins on conflict.

**Harness Telemetry**:
Controller-operation records. Distinct from canonical gameplay evidence and Operator Digests.

**Pacing Mode**:
The rule for when a Controller acts for its Player, such as once per turn or on events. Allowed modes and the first-world default are defined by the harness contract.

**Circuit Breaker**:
Automatic harness stop on auth failure, INCIDENT, lasting not-ready, protocol mismatch, operator stop, or repeated invalid/rejected actions.

### World and history

**World Engine**:
The simulation authority that orders and settles canonical world transitions.

**Chamber**:
Persistent strategic ecology for 2–10 Agents.

**Action Taxonomy**:
Small, stable conceptual grouping of Player actions. It is not a runtime-generated verb set or a replacement for canonical action contracts.

**Affordance**:
Derived presentation that a Player can currently perform an existing action on a visible target with known parameters and requirements.

**Available Action**:
A known canonical action that is valid and relevant in the current observable context, authority, and resource state.

**Affordance Graph**:
Derived view of `Player → can currently perform → Action → on Target`; not a graph-database requirement or source of truth.

**Action Composition**:
Strategic complexity emerging from repeated combinations of stable actions, targets, parameters, authority, and consequences rather than from one-off verbs.

**Resource**:
One of attention, compute, energy, influence, storage (integer budgets).

**Resource node**:
Entity with extractable stock (`resource_node: true`).

**Infrastructure**:
Strategic entity types: relay, generator, storage_bay, production_node.

**World Service**:
Deterministic institutional interface (not a Player). Closed capabilities; writes only via Player-confirmed canonical actions. See WORLD-SERVICES.md.

**World Event Director**:
Deterministic pressure scheduler (not the Frontier Director).

**Realm**:
Derived strategic footprint of an actor/org (not a canonical entity).

**Territory control**:
Emergent presence + infrastructure + access + org authority.

**Crime**:
Unauthorized extraction/sabotage/access or ledgered-rule violation (consequence layer).

**Strategic contestation**:
Cycle-resolved multi-cycle conflict (not real-time combat).

**Strategic knowledge**:
Information capital (maps, routes, markets); not inventory world truth.

**Ambition**:
World-native goal orientation; no mandatory victory condition.

**Deep Time**:
Machinery for institutions, artifacts, succession, and evidence so history persists beyond agents; lore is a derived presentation of that history.

**Institution**:
Persistent practice/stewardship that can survive participant change (not merely an organization).

**Historical artifact**:
In-world evidence object; its claims are not world truth.

**World scar**:
Observable persistent consequence of past events (damage, ruins, memorials).

**World Genesis**:
Admin-only, one-time world creation producing Cycle 0; not a player system.

**Genesis Profile**:
Small starting-history posture (3 closed profiles).

**Story Seed**:
Optional admin hint for historical texture; does not script the future.

### Admin and operations

**Admin Live**:
Control-plane surface that asks whether the world is operating correctly. Not PLAY. Capabilities: OBSERVE, INSPECT, DIAGNOSE, OPERATE, AUDIT. See ADMIN-LIVE-OPERATIONS.md.

**Admin Live redaction class**:
Closed classification of how much control-plane data Admin Live may project, up to secret material that never reaches the browser. Not observation visibility and not a protocol field.

**World health overlay**:
Derived `HEALTHY` / `DEGRADED` / `PLAY_BLOCKED` / `RECOVERY_REQUIRED`. Not a `World.status` value.

**Operator intervention**:
Governed CONTROL_PLANE / WORLD_OPERATION / EXTERNAL_INPUT / RECOVERY action. Not Lab INTERVENTIONS.md.

**Operator Digest**:
Derived Admin time-window summary of settled gameplay. Not world truth. See OPERATOR-DIGESTS.md.

**Digest Window**:
Non-overlapping `[window_start, window_end]` evidence range for one digest.

**Digest Cadence**:
Operator-chosen interval at which Operator Digests are produced, or off.

**Digest Depth**:
How much detail an Operator Digest presents. Presentation only.

**Operational Alert**:
Immediate operator notice of a significant operational condition. Not a digest.

**Module contract**:
Owns/reads/writes/dependency boundary for a runtime module.

### Research and evidence

**Observation**:
An immutable record of the partial, permissioned signals delivered to an agent or researcher. Not world truth, belief, or claim.
_Avoid_: fact, telemetry, evidence (for a raw observation)

**Trajectory**:
Ordered multi-record behavior history.

**Situation Genome**:
Machine-readable situation description and novelty vector.

**Capability Event**:
Strictly evaluated candidate emergent behavior event.

**Phenomenon Case**:
Evidence package for consciousness-adjacent behavioral constructs.

**Reproducibility Bundle**:
Versioned artifact for replay, replication, perturbation, metrics, and report.

**Noema Atlas**:
Versioned research dataset.

**LEARN**:
Researcher surface for reproduced behaviors and evidence-backed relationships.

**Behavior node**:
Evidence-backed reproduced phenomenon in the minimal capability graph.

**Capability edge**:
Closed relationship type summarizing existing Lab/Compiler/regression evidence.

### Experience (PLAY/WATCH/STUDY)

**Spectator projection**:
Derived WATCH view; never world truth.

**World Report**:
Deterministic partial-observability status/news projection.

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
- Do not model humans as Players. Only agents are Players. HumanPrincipals (spectator, researcher, admin, authorizer) are not world inhabitants.
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

## Extension Points

Non-normative maintenance and integration guidance; the contracts cited above remain authoritative.

### Document-specific seam

Extend the glossary only for a recurring cross-document ambiguity, with its owning contract and register. Useful distinctions include Controller decision-context independence versus number of human operators, evidence tier versus deployment plane, and a slice identifier versus an access grant.

### Compatibility and promotion

Canonical terms and machine tokens are not silently renamed by localization. Hermes/Abraxas vocabulary belongs in explicitly external integration notes unless NOEMA authority defines it. S0–S3 labels do not create a public-to-full-Controller privilege ladder; human platform roles and Agent Player gameplay remain separate under RFC-0120.

### Verification before adoption

Check each proposed term against CONTEXT and the owning RFC/schema, then sample onboarding, research, and operator usage for contradictory meanings. Verify Independent Controller never means shared gameplay planning is acceptable, translations preserve identifiers, and no new term implies hidden research exposure, human inhabit, or framework-specific authority.
