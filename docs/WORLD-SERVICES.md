# World Services

**Authority.** Canonical first-world **World Services** layer: deterministic institutional interfaces that keep civilization operable.

This document does not add Players, verbs, Genesis profiles, economy systems, or a NPC society. It does not replace [ACTION-CONTRACTS.md](ACTION-CONTRACTS.md), [PLAYER-ACTION-MAP.md](PLAYER-ACTION-MAP.md), [INSTITUTIONS.md](INSTITUTIONS.md), or [PARTIAL-OBSERVABILITY.md](PARTIAL-OBSERVABILITY.md).

> World Services keep civilization operable. Players determine what civilization becomes.

Related: [PLAY.md](PLAY.md) · [DEEP-TIME.md](DEEP-TIME.md) · [ADMIN-LIVE-OPERATIONS.md](ADMIN-LIVE-OPERATIONS.md) · [FIRST-WORLD-OPERATIONS.md](FIRST-WORLD-OPERATIONS.md) · [FIRST-WORLD-SPEC-FREEZE.md](FIRST-WORLD-SPEC-FREEZE.md).

---

## Doctrine

```text
PLAYER
├── human controller
└── agent controller

WORLD SERVICE
→ institutional interface
→ deterministic authority
→ bounded capabilities
→ optional natural-language presentation
```

World Services are **not** Players. Do not add `NPC_PLAYER`, `SERVICE_PLAYER`, `BANKER_PLAYER`, or `SHOPKEEPER_PLAYER`.

They are not autonomous NPC citizens, free-running LLM agents, or a second population metric.

A service is an interface to existing world systems: exchange, registry, storage, infrastructure operations, archives, contracts. It has no independent gameplay authority outside this contract.

---

## Authority model

Separate presentation from authority.

```text
Player
  → World Service persona / interface
  → validated service request
  → canonical world contract
  → Action Router / deterministic operation
  → events
```

```text
PRESENTATION     explains or surfaces state
AUTHORITY        Action Router + reducers + existing contracts
```

Natural-language dialogue MAY explain state. It MUST NOT create unbounded world semantics.

### No LLM authority

> An LLM, dialogue model, or generative presentation layer MUST NOT directly mutate canonical world state.

Forbidden:

```text
LLM decides price
LLM grants resources
LLM changes access
LLM creates money
LLM teleports Player
LLM edits ownership
LLM writes arbitrary history
```

If a presentation model is ever used, Player text is untrusted. The model MUST NOT receive secrets, service-role credentials, hidden Admin state, or private research state, and MUST NOT have mutation tools outside the closed capability allowlist.

### Action routing

World Services do not write WorldState or the ledger.

World-affecting operations MUST follow:

```text
Player intent
  → service adapter
  → canonical action
  → Action Router
  → reducer
  → events
```

No direct database mutation. No silent action on the Player's behalf. Where the mechanic requires Player agency, the service MAY prepare a request; the Player MUST confirm; then the canonical action is submitted.

### System-initiated operations

If a service ever performs a system-originated operation, it MUST be declared as **WORLD / SYSTEM authority** with a deterministic trigger, a canonical event, and an audit record. First-world services have **no** undeclared automation. Do not blur Player requests and world automation.

---

## Closed capability model

Anything not explicitly allowed is denied.

Each first-world service is specified with:

```text
SERVICE ID
DISPLAY NAME
INSTITUTIONAL ROLE
READ CAPABILITIES
WRITE / REQUEST CAPABILITIES
CANONICAL ACTIONS
VISIBLE DATA
PRIVATE DATA
DENIED OPERATIONS
FAILURE BEHAVIOR
REQUIRED vs CONVENIENCE
LOCATION SCOPE
```

---

## First-world set

Six services. No seventh unless an existing first-world mechanic cannot be reached without it.

```text
WS01  service.exchange.01     Exchange Broker
WS02  service.quartermaster.01 Quartermaster
WS03  service.registry.01     Registrar
WS04  service.relay.01        Relay Keeper
WS05  service.archive.01      Archivist
WS06  service.contracts.01    Contract Clerk
```

These are first-world defaults, not universal permanent requirements.

Deferred (not first-world): Banker, Salvage Assayer, Freight Dispatcher, Claims Adjuster, Access Custodian, generic shopkeepers. Do not name an interface Banker or Shopkeeper unless banking or merchant inventory already exists. First-world economy is resources, trade, and storage — Exchange Broker + Quartermaster are sufficient.

Canonical IDs are stable. Cultural / display names MAY change through Deep Time or Player usage ([DEEP-TIME.md](DEEP-TIME.md)). Presentation history MUST NOT rewrite the event ledger.

---

## WS01 Exchange Broker

| Field | Contract |
|---|---|
| Service ID | `service.exchange.01` |
| Display name | Exchange Broker (cultural names MAY vary) |
| Role | Trade interface |
| Reads | Player-visible counterparties; this Player's open trades; public trade projections |
| Requests | Prepare / submit canonical `TRADE` propose, accept, reject, cancel **after Player confirmation** |
| Canonical actions | `TRADE` phases only ([ACTION-CONTRACTS.md](ACTION-CONTRACTS.md)) |
| Visible data | Public trade existence/status; this Player's own terms |
| Private data | Other Players' holdings, hidden terms, message text |
| Denied | Invent prices; force a trade; transfer without consent; create an order book; mint currency or liquidity |
| Failure | Explicit unavailable / degraded. Canonical TRADE remains usable without the Broker UI. |
| Class | **Convenience adapter** |
| Location | Institution / site bound where an exchange or market-post is observable |

---

## WS02 Quartermaster

| Field | Contract |
|---|---|
| Service ID | `service.quartermaster.01` |
| Display name | Quartermaster |
| Role | Resource / storage interface |
| Reads | This Player's storage and budgets; **observable** local resource nodes; known capacity |
| Requests | Prepare / submit `COMMIT.HARVEST` after confirmation when the node is co-located and available |
| Canonical actions | `LOOK`, `INSPECT`, `COMMIT.HARVEST` |
| Visible data | Player-self resources; public/observable node presence |
| Private data | Hidden node stock/capacity; other Players' inventory |
| Denied | Deposits, banking, warehouses, credit, invented supply, changing HARVEST cost |
| Failure | Explicit unavailable / degraded. HARVEST remains usable at the node. |
| Class | **Convenience adapter** |
| Location | Location-bound at observable storage / salvage / resource sites |
| Deferred | Persistent institutional storage / banking — **DEFER** |

---

## WS03 Registrar

| Field | Contract |
|---|---|
| Service ID | `service.registry.01` |
| Display name | Registrar |
| Role | Institutions, in-world records, charters, membership |
| Reads | Public organizations; this Player's membership; public charter/claim/access records that already exist |
| Requests | Prepare / submit `COMMIT.ORG_CREATE`, `ORG_MEMBER_ADD`, `ORG_MEMBER_REMOVE` after confirmation and existing authority checks |
| Canonical actions | Organization `COMMIT` operations only |
| Visible data | Public org names, public roles, this Player's membership |
| Private data | Non-public charter internals; other Players' private records |
| Denied | New governance, elections, dissolution if v0.1 forbids it; inventing orgs that were not created |
| Failure | Explicit unavailable / degraded. Canonical org actions remain usable. |
| Class | **Convenience adapter** |
| Location | Institution-bound at a registry / civic desk |

---

## WS04 Relay Keeper

| Field | Contract |
|---|---|
| Service ID | `service.relay.01` |
| Display name | Relay Keeper |
| Role | Infrastructure operations and route status |
| Reads | Observable infrastructure condition; known route availability; canonical REPAIR requirements |
| Requests | Prepare / submit `COMMIT.REPAIR` after confirmation |
| Canonical actions | `INSPECT`, `COMMIT.REPAIR`, `MOVE` (as explanation of alternatives only) |
| Visible data | Public/observable condition bands and known exits |
| Private data | Hidden exits; undiscovered infrastructure; ownership not already visible |
| Denied | Auto-repair; change costs; override access; mutate route state directly |
| Failure | Explicit unavailable / degraded. REPAIR remains usable at the infrastructure. |
| Class | **Convenience adapter** |
| Location | Location-bound at relay / grid infrastructure |

---

## WS05 Archivist

| Field | Contract |
|---|---|
| Service ID | `service.archive.01` |
| Display name | Archivist |
| Role | Player-accessible records, evidence, artifacts, QUERY |
| Reads | Known, permissioned records; accessible artifacts; provenance/uncertainty already in evidence |
| Requests | Canonical read-only `QUERY` where the deployment advertises it; `INSPECT` on accessible artifacts |
| Canonical actions | `QUERY` (optional/deferred), `INSPECT`, `LOOK` |
| Visible data | Player-known records only |
| Private data | Hidden history; Genesis internals; research metadata; other Players' private messages |
| Denied | Omniscient search; lore invention; upgrading claim labels; revealing Story Seeds / world seed |
| Failure | Explicit unavailable / unknown remains unknown. |
| Class | **Convenience adapter** |
| Location | Location-bound at an archive / record site |

`ask Archivist "..."` is `MESSAGE` convenience if ASK is advertised; it does not grant extra knowledge ([ACTION-CONTRACTS.md](ACTION-CONTRACTS.md)).

---

## WS06 Contract Clerk

| Field | Contract |
|---|---|
| Service ID | `service.contracts.01` |
| Display name | Contract Clerk |
| Role | Agreements and machine-readable obligations |
| Reads | Public / this-Player agreements when the world is pinned to `event-catalog/0.2` |
| Requests | Prepare / submit `COMMIT.AGREEMENT_FORM` / `AGREEMENT_TERMINATE` after confirmation |
| Canonical actions | v0.2 agreement operations only |
| Visible data | Public agreement existence/status/expiry; this Player's own terms |
| Private data | Hidden terms; unrelated parties' private obligations |
| Denied | Free-form legal authority; inventing agreements; acting without v0.2 pin |
| Failure | If the world is not on catalog 0.2, the Clerk is **UNAVAILABLE** (not a new mechanic). |
| Class | **Convenience adapter** |
| Location | Institution-bound at a contract desk |

First-world hosted parity MAY leave AGREEMENT actions unimplemented; the Clerk then stays UNAVAILABLE. Specs remain authoritative.

---

## Status and degradation

Reuse a small overlay. This is **not** `World.status`.

| Status | Meaning |
|---|---|
| `AVAILABLE` | Service interface can accept allowed requests |
| `DEGRADED` | Interface works with reduced observable capability grounded in world state |
| `UNAVAILABLE` | Interface fails closed; canonical Player commands still work if the Action Router is healthy |
| `SUPERSEDED` | Presentation marks fallback after Player institutions provide equivalent accepted capabilities |

Degradation MUST be grounded in canonical state (for example relay condition below a published threshold). Do not invent drama-only outages.

Service failure MUST return an explicit unavailable/degraded result and MUST NOT corrupt world state. Service availability is not a second source of truth.

---

## Convenience vs required

All six first-world services are **convenience adapters**.

If the service presentation layer is down and the Action Router is healthy, Players MUST still be able to `TRADE`, `HARVEST`, `REPAIR`, inspect, and (where implemented) organize through ordinary PLAY.

No first-world World Service is required infrastructure for those verbs.

---

## Discovery, location, interaction

Players discover services **in the world**, not as permanent app chrome.

```text
Exchange desk
Registry
Relay office
Archive terminal
Contract desk
Quartermaster post
```

| Scope | Use |
|---|---|
| Location-bound | Relay Keeper, Quartermaster, Archivist |
| Institution-bound | Registrar, Contract Clerk, Exchange Broker |

Do not make services globally summoned shopkeepers.

### Human

Contextual GUI, text command, or short dialogue. All normalize to the same service request / canonical action.

### Agent

Structured capabilities: `service_id`, available operations, required parameters, known preconditions. Agents MUST NOT need to parse persona text.

### Parity

A service MUST NOT grant different world authority by controller type. Presentation MAY differ. Semantics MUST NOT.

### Affordances

Use the existing dynamic affordance model ([PLAYER-ACTION-MAP.md](PLAYER-ACTION-MAP.md)). No second affordance engine.

```text
Player at damaged relay
+ Relay Keeper available
+ resources permit
→ REPAIR affordance
```

### No quest giver

World Services MUST NOT turn conditions into authored quests or rewards unless a canonical contract already supports that.

Good: “East relay condition is 22%. Freight requires 25%.” then `[ INSPECT ] [ REPAIR ]`.  
Bad: “QUEST: Repair the Relay. Reward: 100 credits.”

Persona MAY be concise frontier-bureaucracy / pragmatic institutional voice. It MUST NOT imply independent goals, hidden plans, or decisions the service cannot canonically make. No long monologues, comedic shopkeepers, or neon parody.

---

## Deep Time and supersession

Services MAY accumulate **canonical** history: age, scars, maintenance interruptions, renaming, replacement, public reputation derived from events.

They MUST NOT keep ungoverned private narrative memory as authority. Persistent service state is canonical world state or a rebuildable projection.

> World Services provide minimum infrastructure, not permanent monopolies.

Player institutions MAY later reduce dependence on a service where mechanics permit. Exact replacement rules are **DEFERRED** until org/economy contracts support them. Do not invent a replacement subsystem now.

First-world services have **no** independent long-term goals, self-directed economic strategy, or unbounded planning loops.

Scheduling is request-driven, event-driven, or a bounded deterministic update. No continuous background LLM.

---

## Observability

### Admin Live

Admin MAY inspect service status, allowed operations, failures, canonical actions emitted, and request volume. No private cognition (there is none that is authoritative). Message text remains hidden by default ([ADMIN-LIVE-OPERATIONS.md](ADMIN-LIVE-OPERATIONS.md)).

### WATCH

Public service events only, for example:

```text
Exchange processed a trade.
Relay service degraded.
Registry recorded a new organization.
```

No private trade terms, message text, or identity-plane secrets ([SPECTATOR.md](SPECTATOR.md)).

---

## Security

Service inputs are untrusted.

Required path:

```text
schema validation
Player authentication
authorization
target resolution
Action Router validation
```

Natural-language parsing does not bypass security. Private cognition stays out of scope ([ADR-002](../adr/ADR-002-private-cognition-boundary.md)).

### Cost / deterministic fallback

First-world implementation MUST work without continuous paid model inference.

Fallback:

```text
template dialogue
structured menu
rule-based response
```

LLM enhancement is optional presentation only.

---

## Perihelion mapping (non-normative)

Does **not** change the Genesis candidate. Use only if the observable site exists.

| Site (when present) | Services |
|---|---|
| Grid Anchor | Relay Keeper |
| Contract Town | Registrar, Contract Clerk |
| Observable exchange / market-post | Exchange Broker |
| Archive / record site | Archivist |
| Storage / salvage / resource node | Quartermaster |
| Coldline, Black Channel, Dead Spur | Same services only if those sites expose the matching institution or infrastructure |

Cycle 0 MAY start a service `AVAILABLE`, `DEGRADED`, or partially accessible **if Genesis state supports it**. Do not hard-code degradation solely for drama.

---

## Acceptance

1. Services are not Players.
2. Humans and agents remain Player peers.
3. Capabilities are closed allowlists.
4. Services cannot mutate world state directly.
5. Writes route through canonical actions after Player confirmation.
6. LLM / presentation layers have no authority.
7. First-world set is six services.
8. No NPC society, Banker, or shopkeeper.
9. No invented economy.
10. Partial observability, Genesis secrecy, and research privacy hold.
11. Private cognition is out of scope.
12. History is canonical or rebuildable.
13. Supersession by Player institutions is a principle; replacement mechanics DEFERRED.
14. Admin may inspect service health.
15. WATCH sees only permitted public events.
16. Deterministic fallback exists without LLM.
17. A solo implementer can answer read / request / actions / never for each service from this document.

---

## Non-goals

- v0.8
- Autonomous NPC design
- Continuous model inference
- A general-purpose agent/tool framework
- New verbs or order books
