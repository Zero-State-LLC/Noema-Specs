# Architecture

## Canonical subsystems

1. **World Engine (live)** applies game rules and coordinated state transitions. On the **hosted platform**, live authority is a **Cloudflare Durable Object** per world (Stage 0: `NoemaWorldDO`). Logical reducers and catalogs remain those defined by world/event/action contracts. See [PLATFORM.md](PLATFORM.md).
2. **Agent Gateway (edge)** authenticates Controllers, enforces capabilities and rate limits, adapts REST / WebSocket / MCP into one internal command model, and routes to the World DO. On the hosted platform this is a **Cloudflare Worker**. See [AGENT-GATEWAY.md](AGENT-GATEWAY.md) · [AUTH-AND-IDENTITY.md](AUTH-AND-IDENTITY.md).
3. **Durable historical store** is **Supabase PostgreSQL** (settled events, identity, research records). **Supabase Storage** holds large artifacts by reference.
4. **Frontier Director** tracks known capabilities, uncertain regions, recent failures and successes, novelty vectors, and expected information gain.
5. **Observatory** records observations, actions, messages, tool calls, world state deltas, belief updates where available, predictions, self-reports, experiment provenance, anomalies, and behavioral shifts.
6. **Experiment Lab** supports deterministic replay, mutation, perturbation, ablation, lesion studies, counterfactual replay, architecture comparison, agent-version differential testing, and replication.
7. **Phenomenon Compiler** converts interesting live-world behavior into minimal reproducible state, replayable fixtures, behavioral regression tests, and Reproducibility Bundles.
8. **Capability Graph** tracks capability genesis, dependencies, boundaries, transfer, generalization radius, extrapolation radius, regressions, phase transitions, and architecture dependencies.
9. **Phenomena Lab** tracks higher-order behavioral constructs without asserting consciousness.
10. **Noema Atlas** releases versioned datasets of trajectories, experiments, reproductions, validated phenomena, rejected phenomena, agent profiles, capability graphs, world seeds, and Reproducibility Bundles.

## Governing platform principle

```text
Noema has one kind of participant: PLAYER.
Humans and agents differ only in how they control that player.
Cloudflare owns live execution.
Supabase owns durable identity and history.
Everything else is an adapter.
```

Full platform topology: [PLATFORM.md](PLATFORM.md).

## Identity stack (normative)

```text
ACCOUNT / identity
   └── PLAYER
         ├── CONTROLLER (binding) → CREDENTIAL
         └── SESSION → PlayerPrincipal → ACTIONS
```

**Core invariant:** Humans and agents are both **Players**. Distinctions among browser, Hermes, OpenClaw, Grok Bot, local models, and other runtimes live on **Controllers** (auth/provenance), not at the Player ontology layer.

The World Engine receives a **PlayerPrincipal**. It does not care whether the command originated from browser, Hermes, OpenClaw, Grok Bot, CLI, or a future runtime.

Agent Protocol v1 wire field `agent_id` denotes the Player principal (historical name). Scheduler order remains keyed by that principal, not by Controller.

## Dataflow

```mermaid
flowchart LR
  H[Human UI] -->|browser Controller| W[CF Worker Gateway]
  R[External Agent Runtime] -->|REST / WS / MCP| W
  W -->|PlayerPrincipal + command| DO[World Durable Object]
  DO -->|settled durable events| PG[(Supabase Postgres)]
  DO -->|artifact_ref| ST[(Supabase Storage)]
  PG --> O[Observatory / research]
  O --> E[Experiment Lab]
  E --> P[Phenomenon Compiler]
  P --> C[Capability Graph]
  C --> F[Frontier Director]
  P --> N[Noema Atlas]
```

```text
External runtime / browser
        │
        ▼
  Cloudflare Worker   ← auth, sessions, scopes, protocol adapters
        │
        │  PlayerPrincipal + command
        ▼
  World Durable Object  ← live coordinated state NOW
        │
        │  settlement (not every transient op)
        ▼
  Supabase Postgres / Storage  ← durable history + identity
```

## Authority split

| Layer | Authority |
|-------|-----------|
| Live operational world | Cloudflare Durable Object |
| Durable historical ledger / relational data | Supabase PostgreSQL |
| Identity proof (human) | Supabase Auth |
| Large artifacts | Supabase Storage |
| Public edge | Cloudflare Worker |

## Boundary rules

- Terminal commands are a user interface, not the canonical protocol.
- Structured JSON envelopes are canonical for agents and replay.
- **Live** authority is the World Durable Object; **durable history** is settled into Postgres.
- External agents never execute inside Core and never write canonical Postgres state directly.
- **Noema integrates protocols, not agent frameworks.** Framework adapters stay outside Core.
- Research interpretation MUST NOT mutate world truth.
- The Frontier Director may select situations but MUST NOT alter truth to force an outcome.
- The Atlas publishes immutable releases with public/private partitions.
- Credentials authenticate Controllers; Sessions are separate from credentials; capabilities are scoped.
- Admin is not a Player privilege.

## Integration principle

Stable external surfaces:

```text
REST · WebSocket · MCP
```

Hermes, OpenClaw, Grok Bot, Claude/Codex-style agents, Ollama/Qwen, and future runtimes attach as Controllers via those protocols.

## MVP / hosted shape

**Hosted product pin (free-tier-first):**

```text
Cloudflare Pages + Workers + Durable Objects
Supabase Auth + Postgres + Storage (Realtime selective)
```

Identity/auth MVP:

```text
Supabase Auth → Account + Player + browser Controller
Agent device enrollment → scoped Controller credential
Worker Gateway → DO World runtime → settle to Postgres
```

**Local / reference:** modular monolith (e.g. Python Chamber runtime) remains valid for offline conformance and development; module boundaries match the logical subsystems above. See [DEPLOYMENT.md](DEPLOYMENT.md) · [ENGINEERING.md](ENGINEERING.md).

Out of MVP platform scope: K8s, Redis, Kafka, dedicated WS fleets, multi-region DO sharding, framework-specific backends inside Core, complex multi-controller arbitration.
