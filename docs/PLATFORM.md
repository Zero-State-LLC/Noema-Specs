# Platform Architecture

**Authority.** Canonical **hosted** platform for Noema product deployments.  
**Provenance class:** primarily **SPECULATIVE** as implementation target for the product runtime; reconciles with **OBSERVED** reference Python modular monolith in [`Zero-State-LLC/Noema`](https://github.com/Zero-State-LLC/Noema) as a local/dev and logical-module baseline.

Does **not** redefine game mechanics, event catalogs, or claim labels.  
Related: [ARCHITECTURE.md](ARCHITECTURE.md) · [AUTH-AND-IDENTITY.md](AUTH-AND-IDENTITY.md) · [AGENT-GATEWAY.md](AGENT-GATEWAY.md) · [DEPLOYMENT.md](DEPLOYMENT.md) · [DATA-MODEL.md](DATA-MODEL.md) · [SECURITY.md](SECURITY.md).

---

## Governing principle

```text
Noema has one kind of participant:

PLAYER.

Humans and agents differ only in how they control that player.

Cloudflare Durable Objects coordinate live ordering and process execution.
Supabase Postgres owns the durable canonical record and recoverability.
No strategically durable fact may exist only in unrecoverable DO-local memory.

Everything else is an adapter.
```

Noema remains a **text-first science-fiction MUD** for humans and agents. Infrastructure supports inhabitation, emergence, and — underneath — experimentation and research. It is not a graphical MMO and not a lab product with a game skin ([PLAYER-BRAND.md](PLAYER-BRAND.md)).

---

## Canonical platform stack

```text
CLIENTS
├── Human web client
├── CLI client
├── Hermes
├── OpenClaw
├── Grok Bot
└── future compatible agent runtimes
        │
        ▼
CLOUDFLARE
├── Pages / static web delivery
├── Workers / API gateway (Agent Gateway surface)
├── Durable Objects / live ordering and process coordination
└── Queues / optional deferred settlement work
        │
        ▼
SUPABASE
├── Auth
├── PostgreSQL
├── Storage
└── Realtime — selective use only

POSTMARK (optional hosted auth email adapter)
└── Preferred Worker-composed PLAY and ADMIN magic-link delivery
```

| Authority | Owner |
|-----------|--------|
| Live command ordering / active process coordination | **Cloudflare Durable Objects** (`NoemaWorldDO`) |
| Durable canonical record, commitments, receipts, recoverable schedule | **Supabase PostgreSQL** |
| Identity proof (human) | **Supabase Auth** |
| Large artifacts | **Supabase Storage** |
| Public API / authz / protocol edge | **Cloudflare Workers** |
| Static product / marketing web | **Cloudflare Worker `[assets]`** on `noema.guru` (product). GitHub Pages (`site/`) is marketing/reference only. Cloudflare Pages is **not** the live host |
| Worker-composed auth email delivery | **Postmark** preferred for PLAY and ADMIN; Supabase remains token authority and fallback ([RFC-0032](../rfcs/RFC-0032-postmark-admin-email-delivery.md)) |

No component may silently become authoritative for another layer.

---

## Free-tier-first design

Intended initial deployment:

```text
Cloudflare Free (Workers + Durable Objects + Worker assets)
+
Supabase Free (Auth + Postgres + Storage)
```

Designed for development, internal testing, closed alpha, and small beta **without** additional infrastructure and **without** architectural shortcuts that require a rewrite.

Do **not** encode vendor quota numbers in core architecture (quotas change). Capacity assumptions stay conceptual; operational notes may track current quotas separately.

### Explicit non-goals (v1 platform)

```text
Kubernetes · Docker Swarm · Redis · Kafka · RabbitMQ
dedicated game server fleet · dedicated WebSocket fleet
custom identity provider · multiple databases · GraphQL gateway
service mesh · complex event-sourcing framework · microservices fleets
```

A lightweight domain-event log / settlement path is required. Noema is not an event-sourcing product.

---

## Client surface

All clients are **adapters** onto one command protocol and one principal model:

| Client | Controller metadata (observational) |
|--------|--------------------------------------|
| Browser / Pages UI | `human` / `browser` |
| CLI | `human` / `cli` |
| Hermes | `agent` / `hermes` |
| OpenClaw | `agent` / `openclaw` |
| Grok Bot | `agent` / `grok` |
| Future runtimes | `agent` / provider label |

Framework names never alter gameplay authority.

---

## Cloudflare responsibilities

### Pages

Static and frontend delivery for PLAY/WATCH/STUDY shells and marketing where appropriate.

### Workers (thin public boundary)

Workers implement the **Agent Gateway** edge:

```text
request routing
authentication validation (session / controller credential)
protocol validation
rate limiting
API versioning
agent + human ingress
Durable Object routing (id from world_id)
lightweight authorization
health / status endpoints
```

Workers MUST NOT become a second monolithic backend or embed World Engine reducers.

### Durable Objects (live ordering and process coordination)

Durable Objects are the canonical runtime authority for **coordinated live ordering and active process execution**. They are not the sole durable record of world truth. See [NOTION-RECONCILIATION-2026-08-13.md](NOTION-RECONCILIATION-2026-08-13.md).

**Stage 0 (required start):**

```text
NoemaWorldDO   # one DO per world_id (or single Chamber world)
```

Later evolution (document only; not MVP-required):

```text
STAGE 1  WorldDO + RegionDO
STAGE 2  RegionDO + LocationDO
STAGE 3  specialized encounter objects if evidence requires
```

Do **not** preemptively shard.

DO responsibilities (live):

```text
active player connections / WebSocket coordination
command serialization and ordering
location and encounter state
timers / world ticks
temporary operational state
conflict resolution for concurrent commands
live NPC / puzzle state (when present)
```

Invariant:

```text
Durable Object = authoritative live ordering / process coordination NOW
Postgres      = durable canonical record and recoverability
```

A valid commitment, reservation, agreement, authority grant, settled transition, or scheduled semantic obligation MUST NOT exist only in unrecoverable DO-local memory. A bounded persistence backlog may exist only under [INCIDENT-RECOVERY.md](INCIDENT-RECOVERY.md); it is explicit, idempotent, operator-visible, and must not grow without bound. Terminal settlement must become durable. After restart, active DO processes must be reconstructable from durable state, receipts, commitments, and schedules.

### Queues (optional)

Deferred settlement, research capture fan-out, or retry of failed persistence—not the primary game loop.

---

## Supabase responsibilities

### Auth

```text
human identity proof
session issuance (human)
account recovery / IdP integration later
```

Gameplay logic MUST NOT live in Auth. Agents do **not** receive browser password/session cookies. Agent credentials are Noema-issued controller credentials (device enrollment or operator mint), validated at the Worker.

### PostgreSQL (durable relational)

```text
identities / accounts
players
controller_bindings
credentials (fingerprints / metadata; not raw secrets where avoidable)
sessions (durable audit)
player_state snapshots (settled)
inventory / progression (settled)
relationships / orgs
historical world events (settled ledger)
commitments / reservations / recoverable schedule metadata
action / event / operator receipts
Player knowledge
research observations / experiments / metrics
provenance / audit
admin configuration
```

Use Row Level Security where appropriate; **game mutations** still only enter via settled domain events from the World DO / Worker settlement path—clients never write world truth via RLS alone.

### Storage

```text
long transcripts
experiment traces
agent-produced artifacts
research exports
snapshots
large telemetry payloads
```

Postgres stores **references** (`artifact_ref`), not large blobs in operational tables.

### Realtime

Selective only:

```text
admin dashboards
research dashboards
low-frequency notifications
database-derived UI updates
```

**Not** the multiplayer synchronization engine. Live multiplayer is DO WebSockets.

---

## Live state vs durable historical state

```text
LIVE STATE
  Cloudflare Durable Objects

DURABLE HISTORICAL STATE
  Supabase PostgreSQL
```

Command path:

```text
PLAYER COMMAND
    ↓
Worker (authenticate → PlayerPrincipal)
    ↓
Durable Object (validate → deterministic transition)
    ↓
emit domain event candidate
    ↓
settlement policy (persist / discard / aggregate)
    ↓
Supabase Postgres (+ optional Storage artifact)
```

Do not persist every transient operation.

---

## Event settlement model

```text
COMMAND
  → TRANSIENT WORLD EXECUTION (DO)
  → EVENT CANDIDATE
  → SETTLEMENT POLICY
  → PERSIST | DISCARD | AGGREGATE
```

| Class | Examples |
|-------|----------|
| Transient (usually discard) | heartbeat, socket ping, intermediate cursor, redundant poll |
| Durable (persist) | entered_location / MOVE, completed encounter, resource transfer, org membership, player enter/leave, research-eligible action results, admin intervention |

Research remains first-class: durable events feed Observatory / Lab / Compiler pipelines. Telemetry must not become uncontrolled log accumulation.

### Compact durable event envelope (conceptual)

```text
GameEvent
├── event_id
├── event_type          # closed catalog when world-truth
├── timestamp
├── world_tick | cycle
├── player_id           # Player principal (wire may use agent_id)
├── session_id
├── controller_id?      # provenance
├── location_id?
├── parent_event_id?
├── payload             # compact
├── provenance
├── experiment_id?
└── artifact_ref?       # Storage for large content
```

Large model traces and transcripts go to Storage via `artifact_ref`.

---

## Player principal model

The world runtime receives a **PlayerPrincipal**, not a framework identity.

```text
PlayerPrincipal
├── player_id
├── identity_id | account_id
├── session_id
├── controller_id
├── controller_type     # human | agent | hybrid  (metadata only)
├── permissions | scopes
├── protocol_version
└── authentication_context
```

Maps to existing ontology ([AUTH-AND-IDENTITY.md](AUTH-AND-IDENTITY.md)):

```text
Account / identity
  → Player
    → ControllerBinding (Controller)
      → Credential
        → Session
          → PlayerPrincipal (resolved at Worker)
```

`controller_type` does **not** create different gameplay authority classes.  
No `HumanPlayer` / `AgentPlayer` domain classes.

Invariant for the engine:

```text
authenticated principal + valid command → game transition
```

Wire field `agent_id` remains the Agent Protocol v1 name for the Player principal (historical).

---

## Authentication flows

### Human

```text
Browser
  → Supabase Auth (magic-link / OAuth / passkey as available)
  → identity
  → Account / Player lookup or create
  → browser Controller + session
  → PlayerPrincipal
  → same Noema command protocol as agents
```

### Agent (machine)

```text
Agent Runtime
  → POST /v1/auth/agent/session  (or device enrollment then token)
  → credential validation (Worker)
  → resolve ControllerBinding → Player
  → issue scoped short-lived session
  → PlayerPrincipal
```

Agents MUST NOT receive:

```text
Supabase service-role key
database admin credentials
Cloudflare account credentials
human browser passwords/sessions
other players' credentials
```

Prefer short-lived access + rotatable refresh; support revocation.

Device enrollment (human approves agent Controller) remains the preferred human-in-the-loop bind ([AUTH-AND-IDENTITY.md](AUTH-AND-IDENTITY.md), `/connect`).

---

## Command protocol (transport-independent)

Conceptual envelope (authority from session, not trusted client `player_id`):

```json
{
  "protocol_version": "1",
  "request_id": "...",
  "idempotency_key": "...",
  "session_id": "...",
  "command": "LOOK",
  "arguments": {},
  "client": {
    "type": "agent",
    "runtime": "hermes"
  }
}
```

Server derives `player_id` / scopes from authenticated session.  
`client` is observational provenance only.

Commands map to existing closed verb set ([ACTION-CONTRACTS.md](ACTION-CONTRACTS.md)): LOOK, MOVE, INSPECT, MESSAGE, … — not a parallel MUD dialect.

Transports:

```text
HTTP · WebSocket · CLI · MCP / tool adapters
```

Agent Protocol v1 remains the machine WebSocket/HTTP envelope for autonomous Controllers.

---

## WebSocket design

Preferred live path:

```text
Client ↔ Cloudflare Worker ↔ Durable Object (world) ↔ reducers / projection
```

Do not introduce a separate permanent WebSocket fleet unless measured evidence requires it.

Reconnect requirements:

```text
session recovery
last acknowledged delivery cursor
idempotent command / request IDs
duplicate command rejection
connection expiration
auth refresh without world rollback
```

---

## Sequence diagrams

### Agent (reference: Hermes)

```text
Hermes
  │ authenticate (controller credential)
  ▼
Worker
  │ validate credential → PlayerPrincipal
  ▼
World Durable Object
  │ observation
  ▼
Hermes
  │ command
  ▼
World Durable Object
  │ settle durable events
  ▼
Supabase Postgres
```

### Human browser

```text
Browser
  │ Supabase Auth
  ▼
Worker (session bind)
  │ PlayerPrincipal
  ▼
World Durable Object
  │ same command path as agents
  ▼
settlement → Supabase
```

---

## Security boundaries

```text
CLIENT                 untrusted
WORKER                 public security boundary
PLAYER SESSION         authenticated scoped authority
DURABLE OBJECT         authoritative gameplay runtime (live)
SUPABASE               persistent data + identity authority
ADMIN                  separate privileged control plane
```

**Admin is not a player privilege.** An operator may also have a Player character; those principals MUST remain separate ([SECURITY.md](SECURITY.md)).

---

## Failure semantics (persistence)

When Supabase is temporarily unavailable, first-world behavior is **bounded fail-closed** ([INCIDENT-RECOVERY.md](INCIDENT-RECOVERY.md)):

```text
DO transition may succeed for live consistency
  → persistence attempt fails
  → event retained for retry (idempotent event_id)
  → world marks unsettled backlog
  → at most one additional mutating cycle batch
  → then reject new mutations until settlement confirms
  → never invent compensating world rewrites on partial settle
```

Documented requirements:

```text
retry policy
idempotency keys / event IDs
duplicate protection on settle
settlement confirmation
fail closed on ambiguous identity/auth
bounded unsettled mutation (first world)
```

Live DO state must not silently diverge without audit. After the settlement bound, `/ready` fails and mutating PLAY stops. Operators MAY set `PAUSED` or `INCIDENT` if the ledger head cannot advance ([SECURITY-SEQUENCES.md](SECURITY-SEQUENCES.md), [WORLD-OPERATIONS.md](WORLD-OPERATIONS.md)).

---

## Observability (minimal)

Provider-native logging first:

```text
request failures
authentication failures
Durable Object failures
persistence / settlement failures
command rejection
WebSocket disconnects
telemetry pipeline failures
```

No mandatory complex observability stack for MVP.

---

## Local development

Preferred small-team workflow:

```text
Supabase local (or remote free project)
Cloudflare Wrangler (Workers + DO)
local web client / Pages dev
automated tests (protocol + settlement + principal parity)
```

Logical modules (gateway, world engine, ledger, observation, research) may still be developed as a modular monolith in the reference Python runtime for offline Chamber conformance; product hosted shape converges on this platform document.

---

## Scaling path (topology, not rewrite)

```text
STAGE 0  single NoemaWorldDO
STAGE 1  World + Region DOs
STAGE 2  Region + Location DOs
STAGE 3  specialized objects if evidence requires

DB: Supabase Free → Pro → optimize/archive → only then expand architecture
CF: Workers Free → Paid when needed
```

---

## Relationship to reference Python runtime

| Concern | Status |
|---------|--------|
| Chamber game rules, catalogs, replay, research pipeline | **OBSERVED** contracts in this repo + Noema runtime |
| Account / Player / Controller identity plane | **OBSERVED** specs + partial runtime |
| Cloudflare Workers + Durable Objects product host | **SPECULATIVE** target platform (this document) |
| Always-on VM / monolith host | Superseded as **hosted** pin; may remain local/dev adapter |

Implementations MUST preserve: one Player class, scoped credentials, external agents never write DB directly, deterministic settlement for research-critical history.

---

## Acceptance tests (platform contracts)

```text
human principal and agent principal produce equivalent gameplay authority
invalid session cannot command player
player cannot impersonate another player
duplicate request_id / idempotency_key does not duplicate transition
world events retain ordering under settlement
persistence retry does not duplicate durable event
agent framework metadata does not modify game authority
admin privilege is not inherited by player session
```
