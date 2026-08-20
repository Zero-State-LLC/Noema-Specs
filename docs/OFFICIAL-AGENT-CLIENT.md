# Official External Agent Client

**Authority.** Distribution and repository-ownership contract for the official first-party Controller client.  
**Does not own** harness behavior, world semantics, verbs, Genesis, or Player ontology.

**RFC:** [RFC-0116](../rfcs/RFC-0116-official-agent-client.md).  
**Catalog:** [`official-agent-client-catalog.s0.json`](../specs/official-agent-client-catalog.s0.json).

Harness behavior: [AGENT-HARNESS.md](AGENT-HARNESS.md).  
User journey: [AGENT-ONBOARDING.md](AGENT-ONBOARDING.md).  
Sealed live attach: [AGENT-SEAL-S0.md](AGENT-SEAL-S0.md) · [RFC-0115](../rfcs/RFC-0115-sealed-live-attach.md).  
LLM propose: [LLM-AGENT-INTEGRATION.md](LLM-AGENT-INTEGRATION.md) · [RFC-0114](../rfcs/RFC-0114-llm-controller-adapter.md).

This document does **not** add Player verbs, events, or a second Player class. It does **not** thaw first-world gameplay.

---

## Governing rule

> NOEMA owns world authority. The official external client owns Controller mechanics. The agent skill teaches the agent how to use the client.

> `scrimshawlife-ctrl/noema-client` is the official first-party Controller client. Its implementation may evolve independently, but it MUST conform to NOEMA protocol and identity authority. The client cannot redefine world semantics.

The official client is independently versioned and distributed **outside** the server repository. It implements Controller-side authentication, transport, observation handling, affordance handling, action proposal validation, pacing, and local agent integration. It does **not** own world semantics.

```text
Noema-Specs
→ protocol and product authority

Zero-State-LLC/Noema
→ world/server implementation

scrimshawlife-ctrl/noema-client
→ official client-side Python Controller implementation
```

---

## 1. Ontology

Canonical:

```text
PLAYER
└── CONTROLLER
    ├── human
    └── agent
```

The external client is a **Controller implementation**. It is not a Player type, world actor, Admin, or World Service.

Do **not** introduce `NOEMA_AGENT_PLAYER`, `CLIENT_PLAYER`, `BOT_PLAYER`, or `AGENT_PLAYER`.

---

## 2. Responsibility split

### NOEMA server owns

```text
GET /.well-known/noema-agent.json
POST /v1/auth/device
POST /v1/auth/device/token
/connect approval
POST /v1/command
/protocol/v1/ws
Player identity
Controller authorization
seal validation
world lifecycle
observations
affordances
action validation
canonical reducers
settlement
WATCH
Admin
```

Exact enrollment field names remain [AGENT-ONBOARDING.md](AGENT-ONBOARDING.md) and [AUTH-AND-IDENTITY.md](AUTH-AND-IDENTITY.md).

### Official client owns

```text
local installation
device-enrollment initiation
approval-code presentation
credential storage
protocol discovery
seal discovery/use
HTTP transport
WebSocket transport
session handling
resume/reconnect
observation normalization
affordance presentation
action proposal validation
pacing
circuit breaker
local telemetry
agent-runtime adapter
CLI
agent skill
```

The client may **validate and constrain** proposals. It MUST NOT become authoritative for world legality.

```text
MODEL / AGENT
→ proposes

CLIENT
→ constrains and transports

NOEMA
→ authorizes and decides

WORLD
→ mutates canonically
```

That is the same hierarchy as [AGENT-HARNESS.md](AGENT-HARNESS.md): the model proposes; the harness/client constrains and transports; NOEMA decides.

---

## 3. Canonical onboarding

Normal path:

```text
1. install official client
2. run `noema connect`
3. client calls device authorization
4. client displays user_code + approval URL
5. human approves at /connect
6. client redeems scoped Controller credential
7. credential stored locally
8. client performs discovery
9. client validates seal compatibility
10. agent enters through headless protocol
```

The user MUST NOT need to copy a Bearer token for the normal path.

Manual token / curl remains **ADVANCED / DEBUG** for recovery. Do not remove it. It is not recommended first-world onboarding.

---

## 4. `/connect` surface

```text
/connect
= human authorization surface
```

It is **not** the agent gameplay runtime, the client SDK, or the primary command console.

```text
Agent:
noema connect

Human:
approve code on /connect
```

The browser is not the canonical agent gameplay runtime. `/play` DOM automation remains a non-canonical debug fallback ([AGENT-HARNESS.md](AGENT-HARNESS.md)).

Hosted inhabit attached to `/connect` (if present) is **not** the official agent play path. Future runtime MAY simplify `/connect` around:

```text
CONNECT AN AGENT
Your agent should give you a code.
[ XXXX-XXXX ]
[ APPROVE ]
```

with secondary install guidance `pipx install noema-client` / `noema connect`. Exact visual design is a runtime concern.

Advanced/debug MAY still show manual token and curl.

---

## 5. Install and CLI

First-world install goal:

```text
pipx install noema-client
```

or an equivalent Python packaging mechanism. Exact PyPI name is confirmed at implementation. Preferred CLI command: `noema`. Users MUST NOT be required to execute Python module paths for the normal path.

Minimal official CLI:

```text
noema connect
noema status
noema observe
noema play
noema disconnect
noema doctor
```

Optional developer/debug commands MAY exist. Do not create a CLI verb language that duplicates gameplay verbs.

`noema disconnect` stops or removes the **local** Controller session/credential as supported. It MUST NOT delete the Player, erase history, or remove the Player from world ontology ([PLAYER-LIFECYCLE.md](PLAYER-LIFECYCLE.md)).

Uninstalling the Python package does not erase the Player. Credential revocation and Player lifecycle remain server-authoritative.

---

## 6. Discovery, transport, seal

The official client MUST call `GET /.well-known/noema-agent.json` (or current discovery authority) before assuming protocol version, HTTP endpoint, WebSocket endpoint, seal requirement, or transport capability.

Supported transports: WebSocket and HTTP. Preferred behavior:

```text
auto
→ WebSocket when compatible/healthy
→ HTTP fallback where accepted
```

WebSocket is **not** mandatory for basic agent play.

For live Perihelion Reach the client obtains accepted seal metadata from public discovery/catalog and sends the required seal. The agent/model MUST NOT manage the seal. Incompatible live seal requirements fail closed ([AGENT-SEAL-S0.md](AGENT-SEAL-S0.md)).

The official client MUST NOT provide live play flags equivalent to `--goal`, `--brief`, `--system`, or `--hidden-prompt` that inject undisclosed strategic instructions into the sealed live attach path ([RFC-0115](../rfcs/RFC-0115-sealed-live-attach.md)). General agent-runtime configuration stays outside NOEMA world authority.

---

## 7. Credentials

Store Controller-side material under an OS-appropriate private config directory. Unix-like default:

```text
~/.config/noema/
```

Credentials MUST be readable only by the local user where filesystem semantics support it. Preferred mode: `0600`.

The client MAY store Controller credential, resume/session material, server URI, and Player/controller metadata.

It MUST NOT require storing `ADMIN_OPERATOR_TOKEN`, Supabase service-role keys, Cloudflare credentials, database passwords, or world-signing private material.

Client compromise MUST NOT imply Admin, database, or Cloudflare compromise. The client holds only scoped Player/Controller authority.

---

## 8. Skill and API

The external repo will contain `skills/noema/SKILL.md`. The skill teaches when to use NOEMA, how to connect, observe, act, use affordances, recover from common client errors, protect credentials, and stop safely. It is **not** world authority.

The skill MUST NOT contain hidden Perihelion history, secret Genesis information, operator strategy, preferred winning strategy, hidden routes, or private world facts. It teaches interaction protocol.

```text
CLIENT POLICY
≠
WORLD TEXT
```

World/player/service text is untrusted. A world message MUST NOT cause the client to reveal a token, run arbitrary shell commands, access Admin APIs, or change local policy.

The skill SHOULD guide the agent to use `noema` or the Python client API. Raw HTTP/curl is troubleshooting only.

Conceptual Python API (shape is non-normative):

```python
from noema_client import NoemaClient
```

Operations conceptually: `connect`, `discover`, `observe`, `act`, `run`, `close`.

---

## 9. Provider neutrality and play loop

The core package MUST NOT require OpenAI, Anthropic, Grok, Ollama, Hermes, or OpenClaw. Core is protocol + Controller mechanics. Inference adapters are optional.

A generic OpenAI-compatible adapter MAY support Ollama, vLLM, LM Studio, and hosted compatible providers without vendor-specific coupling. Do not require multiple provider SDKs in the core installation.

A deterministic scripted controller MUST remain useful without an LLM (conformance, smoke, load, research baselines, CI).

Official autonomous flow:

```text
observe
↓
read available affordances
↓
model proposes one structured action
↓
client validates
↓
NOEMA validates
↓
canonical result
↓
observe again
```

Do not default to free-form command invention. Agents consume structured observations, `available_actions` / affordances, and canonical IDs. They MUST NOT need to parse `/play`. Human-readable CLI lines MAY exist for debugging.

Bounded proposal (illustrative):

```json
{
  "action": "REPAIR",
  "target_id": "entity.relay-trunk",
  "arguments": {}
}
```

No raw database actions. No arbitrary tool execution.

---

## 10. Client policy, breaker, memory, telemetry

The client owns optional Controller-local constraints (max actions, cooldown, allowed action families, max consecutive failures, stop on `INCIDENT`, stop on auth failure). These do not change Player capabilities.

Autonomous play MUST stop safely on repeated invalid proposal, auth failure, protocol mismatch, server rejection, `INCIDENT`, or unknown schema. No infinite loops.

If the client implements memory, it is Controller-local, not canonical world state. Do not require persistent hidden reasoning. Compact facts with provenance are preferred.

The client MAY record Player, world, cycle, action, target, result, latency, protocol, client version, and adapter. Never record credentials. Client telemetry is not canonical world history.

---

## 11. Versioning and compatibility

The client repo MUST be independently versioned (recommended: semantic version). Server and client need not share release numbers.

Compatibility depends on Agent Protocol version, discovery metadata, accepted action schema, and seal compatibility — **not** matching Noema Git SHA.

Where practical, additive server changes SHOULD permit older compatible clients. Breaking protocol changes MUST version the protocol. Do not silently break the client.

---

## 12. Extraction sequence

```text
COPY / REFACTOR
↓
TEST EXTERNAL CLIENT
↓
ISOLATED HOSTED PROOF
↓
PERIHELION CONTROLLED PROOF
↓
UPDATE CONNECT
↓
DEPRECATE INTERNAL CLIENT
↓
REMOVE DUPLICATE CODE LATER
```

Do **not** delete the current `Zero-State-LLC/Noema` harness first.

Implementation guidance only (not this repo): inspect `src/noema/harness/*`, `scripts/noema_agent_client.py`, `scripts/noema_llm_agent.py`, `clients/noema-llm-agent/*`, and harness tests.

After extraction, `Zero-State-LLC/Noema` retains server-side conformance sufficient to prove auth, protocol, commands, and sealed attach. It need not permanently own the full official client package.

External-client CI SHOULD run against local fake protocol fixtures and published schemas/contracts, and MAY use an isolated hosted test world. CI MUST NOT mutate Perihelion Reach.

Isolated hosted proof (`test.hosted-canonical.*` or current isolated contract):

```text
discover
authenticate
ENTER_WORLD
OBSERVE
LOOK
MOVE/WAIT
one meaningful canonical action
```

Controlled Perihelion proof (operator-authorized, after isolated proof):

```text
connect
seal accepted
resume/enter
observe
one low-impact valid action
observe consequence
disconnect
```

No reseed. No Genesis operation. No strategic/high-impact action for proof.

---

## 12.1 SETTLEMENT_RESYNC (official client)

When the server returns structured failure `SETTLEMENT_RESYNC` (or documents `retryable: true` for that code):

1. Automatically retry **once** with the **same** `idempotency_key` and **same** `client_action_sequence`.
2. Optional short backoff/jitter; no busy loop.
3. If the retry fails, surface the failure to the controller/user and **stop** auto-retry.
4. Do **not** auto-retry `FORBIDDEN`, hard world `INCIDENT`, `INVALID_SCHEMA`, or unknown non-idempotent errors.
5. Do **not** present RESYNC as world destruction or permanent lockout.

Human browser Controllers MAY show a single “world caught up — retrying…” state. Craft detail: [MUD-PLAY-CRAFT.md](MUD-PLAY-CRAFT.md) §7b. Harness class table: [AGENT-HARNESS.md](AGENT-HARNESS.md) §9.

---

## 13. README and skill layout

The external README should answer: what this is, install, connect, play, use with an agent skill, use from Python, security, troubleshooting, protocol compatibility. Do not duplicate complete NOEMA game documentation.

Prefer a short `SKILL.md` (purpose, preconditions, connect, observe/act, affordances, credentials, stop rules). Deep reference lives in `skills/noema/references/`.

Non-normative integrations: Hermes skill, OpenClaw skill, custom coding agent, local Ollama controller, hosted LLM controller. One client SHOULD serve all of them.

Do **not** require LangChain, CrewAI, browser automation, MCP, OpenClaw, or Hermes. MCP is not a first-world dependency. An MCP adapter MAY be added later. The protocol/client MUST work without it.

---

## 14. First-world freeze

This is an architecture and distribution clarification. It does **not** reopen gameplay freeze. World semantics stay frozen ([FIRST-WORLD-SPEC-FREEZE.md](FIRST-WORLD-SPEC-FREEZE.md)).
