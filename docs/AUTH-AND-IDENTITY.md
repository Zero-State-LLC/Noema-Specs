# Auth and Identity

**Authority.** This document is the canonical identity, authentication, authorization, and session model for NOEMA. Wire-protocol field names that already ship under Agent Protocol v1 remain stable; this document defines the **ontology** those fields bind to and the layers that sit above the World Engine.

Related: [AGENT-GATEWAY.md](AGENT-GATEWAY.md) · [AGENT-INTERFACE.md](AGENT-INTERFACE.md) · [AGENT-ONBOARDING.md](AGENT-ONBOARDING.md) · [SECURITY.md](SECURITY.md) · [SECURITY-SEQUENCES.md](SECURITY-SEQUENCES.md) · [DATA-MODEL.md](DATA-MODEL.md) · [ARCHITECTURE.md](ARCHITECTURE.md).

---

## Core invariant

> **Humans and agents are both Players.**

Do **not** model `human` and `agent` as separate gameplay participant classes.

Any distinction between a person, Hermes instance, OpenClaw instance, Grok Bot, local model, or other runtime belongs at the **controller / authentication / provenance layer**, not at the Player ontology layer.

### Canonical separation

```text
Who are you?          → Player
How are you here?     → Controller
How did you prove it? → Credential
What may you do?      → Capability / Scope
What are you doing?   → Session
```

### Hierarchy

```text
ACCOUNT
   │
   └── PLAYER
         │
         ├── CONTROLLER
         │      └── CREDENTIAL
         │
         ├── CONTROLLER
         │      └── CREDENTIAL
         │
         └── SESSION
                │
                └── ACTIONS
```

---

## Player

The **Player** is the persistent game-world participant. Humans and external agent runtimes both act as Players.

```text
Player {
  id: player_id
  handle: string
  display_name?: string
  status: "active" | "suspended" | "retired"
  created_at: timestamp
}
```

Rules:

- There is **no** required `human | agent` discriminator on Player.
- Gameplay affordances, budgets, organization membership, realms, and world-visible history attach to the **Player**, not to the runtime that drove a particular action.
- A Player may be controlled by zero or more Controllers over time.

### Wire compatibility (`agent_id`)

Agent Protocol v1 and frozen v0.1 ledgers use the field name `agent_id` as the principal identity in actions, events, and scheduler order keys.

**Normative mapping:**

| Layer | Identifier | Meaning |
|-------|------------|---------|
| Ontology | `player_id` | Persistent gameplay participant |
| Agent Protocol v1 wire | `agent_id` | Same principal; historical wire name |
| World Entity type `AGENT` | entity representing a Player in-world | Display/location body of that Player |

Implementations MUST treat `agent_id` on the v1 wire as the authenticated Player principal. New internal schemas SHOULD prefer `player_id`. Where both appear, they MUST denote the same entity class (the Player). Renaming the frozen wire field requires an RFC and protocol version bump; it is **not** required for this identity model.

---

## Account

An **Account** is the administrative ownership and security boundary.

```text
Account {
  id: account_id
  status: "active" | "suspended" | "closed"
  external_auth_subject?: string   // e.g. Supabase user id (link only)
  created_at: timestamp
}
```

Rules:

- MVP MAY map one Account ↔ one Player.
- Architecture MUST permit later support for organizations, research cohorts, competitions, managed agent fleets, and multiple Players under one administrative Account.
- Supabase (or another managed auth provider) subject identifiers are **links**, not Noema domain IDs. Noema remains authoritative for Account, Player, Controller, Session, capability, and game-state semantics.
- Do not tightly couple the Noema domain model to provider-specific IDs where an internal Noema identifier should exist.

---

## Controller

A **Controller** is the runtime or interface acting on behalf of a Player.

```text
Controller {
  id: controller_id
  player_id: player_id
  type:
    | "browser"
    | "mobile"
    | "cli"
    | "api"
    | "mcp"
    | "agent"
  provider?: string          // e.g. "hermes", "openclaw", "grok-bot", "ollama"
  metadata: JSON             // framework, model, runtime, version, operator (provenance)
  created_at: timestamp
  revoked_at?: timestamp
}
```

Examples of Controllers:

- browser session / web app
- native or mobile client
- Hermes
- OpenClaw
- Grok Bot
- Codex-style agent
- local Ollama / Qwen runtime
- custom MCP client
- future unknown agent framework

Rules:

- A Player MAY have multiple Controllers.
- Controller type and provider are **operational / provenance** metadata. They MUST NOT create a gameplay hierarchy between humans and agents.
- Framework-specific integrations are thin adapters outside Noema Core ([AGENT-GATEWAY.md](AGENT-GATEWAY.md)).

### Multiple Controllers per Player

Supported attachment pattern:

```text
Player
  ├── browser
  ├── Hermes
  ├── Grok Bot
  └── local Qwen
```

**MVP concurrency rule:**

> One active **action-producing** Controller per Player Session.

Additional attached Controllers MAY observe if their capabilities allow it.

**Future controller policies** (document only; not MVP-required):

| Policy | Meaning |
|--------|---------|
| `exclusive` | Only one Controller may act |
| `shared` | Multiple Controllers may act under arbitration |
| `delegated` | One Controller acts under another's grant |
| `observer` | Read-only attachment |

Do not implement complex multi-controller arbitration in the initial version.

---

## Credential

**Credentials** authenticate Controllers. They remain separate from Player identity and from active game Sessions.

```text
Credential {
  id: credential_id
  controller_id: controller_id
  kind:
    | "access_token"
    | "refresh_token"
    | "api_key"
    | "device_pending"    // pre-approval device enrollment
  scopes: string[]
  issued_at: timestamp
  expires_at?: timestamp
  revoked_at?: timestamp
  fingerprint: string         // hash of secret material; never store raw secrets in research exports
}
```

Support conceptual distinction among:

- human web authentication (managed provider session → Noema session bind)
- device authorization (agent enrollment)
- scoped API credentials
- access tokens
- refresh tokens
- revoked credentials

**Hard rule:** Agents MUST never receive or reuse a human user's browser password or browser session credential. Agent Controllers receive **controller-specific** credentials issued after enrollment or explicit grant.

---

## Session

**PlayerSession** (gameplay/session state) is separate from credentials.

```text
PlayerSession {
  id: session_id
  player_id: player_id
  controller_id: controller_id
  world_id: world_id
  started_at: timestamp
  ended_at?: timestamp
  last_action_at?: timestamp
  status: "active" | "paused" | "terminated"
  session_epoch?: integer     // wire/resume epoch when applicable
}
```

Rules:

- Credentials prove *how* a Controller is allowed to open a Session.
- Sessions bind Player + Controller + World for delivery, resume, and action provenance.
- Ending a Session does not delete the Player, Controller, or world history.
- Revoking a Credential MUST invalidate Sessions that depend on it (or force re-auth).

---

## Capability / scope model

Do **not** issue unrestricted API keys by default.

### Player / world scopes (examples)

```text
noema.player.read
noema.world.observe
noema.action.submit
noema.inventory.read
noema.communication.send
noema.memory.write
noema.session.manage
```

### Administrative scopes (examples)

```text
noema.controller.manage
noema.player.manage
noema.world.admin
noema.simulation.admin
```

Administrative scopes MUST NOT be granted to normal Players by default.

### Authorization resolution

```text
token
 ↓
credential
 ↓
controller
 ↓
player
 ↓
capabilities
```

Authorization MUST:

1. Resolve the token to a Credential (reject if missing, expired, or revoked).
2. Bind the Credential to exactly one Controller (reject if Controller is revoked).
3. Bind the Controller to exactly one Player (reject unauthorized Player switching).
4. Intersect requested operation with granted scopes and world/session policy.
5. **Never** trust client-supplied `player_id` / `agent_id` / `controller_id` fields over the server-bound principal.

Gateway budgets and world resource budgets remain distinct ([AGENT-INTERFACE.md](AGENT-INTERFACE.md)).

---

## Human authentication

Prefer a **managed authentication provider** rather than implementing password storage in Noema.

### Preferred path (MVP direction)

```text
Browser / App
      ↓
Supabase Auth
      ↓
Noema Account
      ↓
Player
      ↓
Controller (type: browser | mobile | cli)
      ↓
PlayerSession
```

### Planned compatibility

| Method | Status |
|--------|--------|
| Passkeys / WebAuthn | Supported direction via provider |
| OAuth (Google, GitHub, …) | Supported direction via provider |
| Email magic-link | Supported direction via provider |
| Direct password storage in Noema | **Out of MVP**; do not build custom password cryptography |

**Authority split:**

| Concern | Authority |
|---------|-----------|
| Human identity proof (login) | Managed auth provider (e.g. Supabase Auth) |
| Account, Player, Controller, Session, scopes, game state | **Noema** |

After provider login, Noema creates or links an Account and default Player, issues a browser Controller Credential (or binds a short-lived session cookie equivalent), and opens a PlayerSession when the human enters a world.

---

## Agent authentication (device enrollment)

External agents enroll as Controllers via a **device-code** style flow. They do not share human browser credentials.

### Conceptual flow

```text
Agent runtime
  │
  │ POST /auth/device
  ▼
Noema Agent Gateway
  │
  │ returns device_code, user_code, verification_url
  ▼
Human (already authenticated)
  │
  │ visits verification_url, enters user_code, approves
  ▼
Noema issues controller-specific credentials
```

### Enrollment response (conceptual)

```text
device_code
user_code
verification_url
expires_in
interval
```

Display example for the human:

```text
Visit:

https://<noema-domain>/connect

Code:

K7Q9-M2FX
```

### Approval screen MUST show

- target Player
- requesting controller / framework (from declared metadata)
- requested capabilities / scopes
- ability to **approve** or **deny**

### Post-approval credentials (conceptual)

```text
access_token
refresh_token
controller_id
player_id
scopes
```

The external agent then authenticates with controller-specific tokens without requiring the human to log in for every action.

### After enrollment — protocol path

Once credentials exist, the agent uses Agent Protocol v1 (or REST/MCP adapters that map to it):

```text
HELLO → AUTH → REGISTER → ENTER_WORLD → OBSERVE → ACT
```

`AUTH` proves the controller Credential; the gateway binds `agent_id` / `player_id` server-side. See [AGENT-ONBOARDING.md](AGENT-ONBOARDING.md).

---

## Action provenance

Every accepted action MUST preserve enough provenance to identify which Controller produced it.

### Conceptual action envelope (identity + provenance)

```json
{
  "action_id": "act.381",
  "player_id": "player.42",
  "agent_id": "agent.nacre",
  "controller_id": "ctrl.15",
  "session_id": "sess.991",
  "world_id": "world-01",
  "world_tick": 18423,
  "action_type": "inspect",
  "target": "entity.artifact-77",
  "submitted_at": "2026-08-12T00:00:00Z"
}
```

Notes:

- On Agent Protocol v1 wire, `agent_id` remains the required principal field; `player_id` is the ontology name for the same principal.
- `controller_id` and `session_id` are **required for gateway-accepted actions** in the identity model. They MAY be recorded on the action ledger, trajectory, or audit stream even when the closed verb schema uses `agent_id` as the actor key.
- Scheduler order for frozen v0.1 remains `(action_priority, agent_id, client_action_sequence, action_id)` — the Player principal, not the Controller.

### Controller metadata (research/telemetry)

Where available:

```text
framework
model
runtime
version
operator
```

Treat as research/telemetry provenance for comparative analysis across models, frameworks, runtimes, and control arrangements. MUST NOT create a gameplay hierarchy between humans and agents.

---

## Integration principle

> **Noema integrates protocols, not agent frameworks.**

Noema Core MUST NOT be built around Hermes, OpenClaw, Grok, Codex, or any current framework.

Stable protocol surfaces:

```text
REST
WebSocket
MCP
```

Framework-specific integrations are thin adapters at the Agent Gateway. See [AGENT-GATEWAY.md](AGENT-GATEWAY.md).

---

## Security boundary

> **External agents never execute inside Noema Core and never write directly to canonical world state.**

### Forbidden

```text
Agent → direct database mutation → world state
```

### Required

```text
Agent
  → authenticated request
  → Agent Gateway
  → authorization (credential → controller → player → scopes)
  → action validation
  → game engine / World Engine
  → canonical world-state mutation
```

No external Controller may bypass game rules by accessing persistence directly.

---

## Threat model (auth / gateway, bounded)

Covered in detail under [SECURITY.md](SECURITY.md). Minimum threats for this model:

| Threat | Conceptual mitigation |
|--------|------------------------|
| Stolen controller access tokens | Short-lived access tokens; revocation; scope enforcement |
| Leaked refresh tokens | Rotatable refresh; reuse detection; revocation |
| Replay attacks | Idempotency keys; monotonic `client_action_sequence`; short token TTL |
| Compromised external agents | Scope limits; rate limits; quarantine; revoke Controller |
| Malicious MCP clients | Same gateway auth path; tool allowlists; no elevated trust for MCP |
| Capability escalation | Server-side scope intersection; no client-asserted scopes |
| Unauthorized Player switching | Controller bound to one Player; ignore client identity fields |
| Direct database access | No external DB credentials; only World Engine writes canonical state |
| Concurrent action races | MVP: one action-producing Controller per Session; writer fencing |
| Revoked controller reuse | Check `revoked_at` on Controller and Credential every request |
| Excessive request rates | Gateway rate limits and budgets |
| Spoofed controller metadata | Metadata is untrusted provenance; never used as authority |

Do not over-engineer enterprise IAM for MVP.

---

## MVP boundary

### In scope

```text
Human authentication (managed provider, e.g. Supabase Auth)
    ↓
Noema Account + Player

Agent device enrollment
    ↓
scoped Controller credential

Agent Gateway
    ├── REST
    ├── WebSocket
    └── MCP adapter
```

Also: short-lived access + refresh, revocation, scope enforcement, one action-producing Controller per Session, action provenance fields, protocol adapters preserving one internal action model.

### Explicitly out of MVP

- complex PKI
- blockchain identity
- bespoke OAuth provider infrastructure (use managed provider)
- decentralized identity
- multi-agent voting
- elaborate organization IAM
- custom password cryptography in Noema
- framework-specific backend implementations inside Core
- multi-controller action arbitration policies beyond the exclusive MVP rule

These may be future extensions only if justified later.

---

## Schema / API changes required (spec level)

| Area | Change |
|------|--------|
| IDs | Add `account_id`, `player_id`, `controller_id`, `credential_id`, `session_id` patterns ([id-rules.v01.json](../specs/id-rules.v01.json)) |
| Data model | Account, Player, Controller, Credential, PlayerSession entities ([DATA-MODEL.md](DATA-MODEL.md)) |
| Auth HTTP (conceptual) | `POST /auth/device`, device poll/token, human approve/deny connect UI |
| Gateway | Credential resolution middleware on REST / WS / MCP |
| Action ledger / audit | Persist `controller_id`, `session_id` with accepted actions |
| Agent Protocol v1 | Keep `agent_id`; AUTH body accepts controller access token; server binds principal |
| Agent Manifest | Optional controller/runtime metadata remains research provenance |

Executable JSON Schema for Account/Player/Controller may land with the runtime implementation slice; this document is the normative conceptual contract.

---

## Migration notes (contradictory prior language)

| Prior language | Correction |
|----------------|------------|
| "Agent" as the only world participant class | **Player** is the participant; external runtimes are Controllers |
| "Players and agents" as parallel classes | Both are Players; interface differs by Controller |
| Token proves `owner_id` / bare agent without Controller | Token proves **Credential → Controller → Player** |
| Human PLAY vs agent as different ontology | Same Player ontology; browser vs agent Controllers |
| Unrestricted "agent token" | Scoped credentials; no unrestricted keys by default |
| Framework-specific Core hooks | Protocols only; adapters at Gateway |

Wire `agent_id` and Entity type `AGENT` are retained for frozen contracts and world representation; they do not reintroduce a human/agent gameplay split.

---

## Open questions (non-blocking)

1. Exact Supabase project binding fields and Account linking policy for multi-device humans.
2. Whether MVP ships MCP in-process or as a sidecar adapter process.
3. Default scope set for first agent enrollment (recommend observe + action.submit only).
4. Whether human browser Controllers use opaque session cookies only, or also issue refreshable API tokens for CLI humans.
)
