# Data Model

Storage-neutral canonical entities for NOEMA. v0.1 Chamber entities below are **implementation-ready**. Later research entities remain listed but are not all required for Chamber play.

Machine-readable ID rules: [`specs/id-rules.v01.json`](../specs/id-rules.v01.json).

Identity and auth ontology (Account, Player, Controller / ControllerBinding, Credential, PlayerSession, PlayerPrincipal): [AUTH-AND-IDENTITY.md](AUTH-AND-IDENTITY.md). Platform: [PLATFORM.md](PLATFORM.md). Gateway: [AGENT-GATEWAY.md](AGENT-GATEWAY.md).

**Authority note:** Live coordinated world state is operationally owned by the World Durable Object; Postgres holds durable settled history, identity, and research records. See settlement model in PLATFORM.md.

## Canonical entity inventory

**Identity plane (auth/gateway; MVP-required for multi-controller and human login):** Account (identity), Player, Controller / ControllerBinding, Credential, PlayerSession.

**v0.1 world plane required:** Agent (wire/world principal; maps to Player), AgentVersion, World, WorldVersion, Room, Exit, Entity (incl. infrastructure & resource nodes), Organization, OrganizationMembership, ResourceAccount, Action, WorldEvent, Observation, Message, Snapshot, Trajectory, RuntimeManifest, AgentManifest.

> **Identity invariant.** Humans and agents are both **Players**. Do not introduce a `human | agent` gameplay class split. Controllers carry runtime/interface provenance. Wire field `agent_id` is the historical name for the Player principal under Agent Protocol v1.

> **v0.4 Lab delta.** Experiment designs, forks, interventions, plans, runs, results, and audits are immutable research-side records. They link to, but never rewrite, canonical world history. See [releases/v0.4/DATA-MODEL.md](releases/v0.4/DATA-MODEL.md).
**Later / research:** Institution, Artifact (beyond DOCUMENT entities), ToolCall, BeliefUpdate, Prediction, SelfReport, SituationGenome (optional inject), Experiment, Replication, Perturbation, Ablation, Counterfactual, Capability\*, Phenomenon\*, ReproducibilityBundle, DatasetRelease.

## ID and lineage rules

Machine-readable ID rules in [`specs/id-rules.v01.json`](../specs/id-rules.v01.json) are the authority for typed ID patterns. Schema-bound documents MUST use the field-specific typed pattern, such as `agent_id`, `room_id`, `event_id`, or `snapshot_id`, instead of a generic identifier pattern when the semantic type is known. Legacy `world-[0-9]+` world IDs remain valid only where the ID rules explicitly allow them.

### ID properties

IDs MUST be:

* stable;
* globally unambiguous within the NOEMA domain;
* never reused for another entity;
* deterministic in fixtures (`prefix.stable-slug`);
* opaque in production when deterministic generation would leak protected information (UUIDv4 with prefix allowed).

### Patterns (v0.1)

| ID | Pattern | Example |
|----|---------|---------|
| `world_id` | `^world\.[A-Za-z0-9_-]+$` or legacy `^world-[0-9]+$` | `world-01` |
| `world_version` | `^world/v[0-9]+$` or integer string | `world/v1` |
| `account_id` | `^acct\.[A-Za-z0-9_.-]+$` | `acct.operator-1` |
| `player_id` | `^player\.[A-Za-z0-9_.-]+$` | `player.nacre` |
| `controller_id` | `^ctrl\.[A-Za-z0-9_.-]+$` | `ctrl.hermes-1` |
| `credential_id` | `^cred\.[A-Za-z0-9_.-]+$` | `cred.access-1` |
| `session_id` | `^sess\.[A-Za-z0-9_.-]+$` | `sess.world-01.nacre.1` |
| `agent_id` | `^agent\.[A-Za-z0-9_.-]+$` | `agent.nacre` |
| `agent_version_id` | `^agentver\.[A-Za-z0-9_.-]+$` | `agentver.nacre.1` |
| `room_id` | `^room\.[A-Za-z0-9_.-]+$` | `room.relay-quarter` |
| `exit_id` | `^exit\.[A-Za-z0-9_.-]+$` | `exit.rq-east` |
| `entity_id` | `^entity\.[A-Za-z0-9_.-]+$` | `entity.relay-7` |
| `organization_id` | `^org\.[A-Za-z0-9_.-]+$` | `org.relay-repair` |
| `membership_id` | `^membership\.[A-Za-z0-9_.-]+$` | `membership.org.relay-repair.agent.nacre` |
| `action_id` | `^act\.[A-Za-z0-9_.-]+$` | `act.18442.0001` |
| `event_id` | `^evt\.[A-Za-z0-9_.-]+$` | `evt.v01.013` |
| `observation_id` | `^obs\.[A-Za-z0-9_.-]+$` | `obs.v01.001` |
| `message_id` | `^msg\.[A-Za-z0-9_.-]+$` | `msg.v01.001` |
| `snapshot_id` | `^snap\.[A-Za-z0-9_.-]+$` | `snap.genesis` |
| `trajectory_id` | `^traj\.[A-Za-z0-9_.-]+$` | `traj.v01.strategic` |
| `trade_id` | `^trade\.[A-Za-z0-9_.-]+$` | `trade.v01.001` |
| `transfer_id` | `^xfer\.[A-Za-z0-9_.-]+$` | `xfer.v01.001` |

Legacy fixture IDs that already use these forms remain valid. New IDs SHOULD follow the table.

## Canonical serialization, numeric values, timestamps, and bytes

Replay-critical JSON artifacts use `noema-cjson-jcs-digest/v1`, defined in [Replay](REPLAY.md). State, seed, snapshot, action, event, observation, trajectory, and reproducibility artifacts that contribute to replay identity MUST be valid I-JSON and MUST be canonicalized with RFC 8785 JCS before JSON digests are computed.

Replay-critical quantities are JSON integers in a declared fixed-point scale. The scale is declared by the resource type, currency, world version, or deterministic configuration field and MUST NOT be inferred from a decimal literal. Resource balances, budgets, stock, capacity, costs, reservations, cycle counters, sequence counters, and revision counters are replay-critical. Non-replay-critical research metadata such as confidence values MAY use JSON numbers only when they remain valid I-JSON and do not affect world truth or replay equivalence.

Timestamps are RFC3339 UTC strings with trailing `Z`. They record provenance or declared external inputs. They MUST NOT be used as hidden reducer inputs. Binary payload digests are over raw bytes, not over incidental text encodings, unless the text encoding is itself the declared artifact.

### Causal lineage fields

| Field | Required when |
|-------|----------------|
| `parent_event_id` | event is a direct follow-on (e.g. OBSERVATION_GENERATED ← LOOK) — SHOULD |
| `caused_by_action_id` | event produced by agent ACT — MUST when known |
| `actor_agent_id` / `actor_id` / `player_id` | Player-originated events — MUST (`agent_id` wire alias) |
| `controller_id` | gateway-accepted actions — MUST when identity plane is enabled |
| `session_id` | gateway-accepted actions — SHOULD; MUST when resume-bound |
| `world_id` | all world-scoped records — MUST |
| `world_version` | snapshots, runtime manifest, seeds — MUST |
| `cycle` | all world events — MUST |
| `sequence` | all world events — MUST |
| `protocol_version` | protocol messages — MUST |
| `schema_version` | all schema-bound documents — MUST |

---

## Entity contracts (identity plane)

### Account

| Aspect | Spec |
|--------|------|
| ID | `account_id` |
| immutable | `account_id`, `created_at` |
| mutable | `status`, linked external auth subjects |
| required | `account_id`, `status` |
| ownership | administrative security boundary |
| visibility | private (operator / account holder) |
| lifecycle | active → suspended → closed; never hard-delete IDs |
| relationships | Player\* (MVP may be 1:1; architecture allows many) |
| create | after managed human auth (e.g. Supabase) or operator provision |
| notes | Provider subject IDs are links only; Noema owns Account semantics |

### Player

| Aspect | Spec |
|--------|------|
| ID | `player_id` |
| immutable | `player_id`, `created_at` |
| mutable | `handle`, `display_name`, `status` |
| required | `player_id`, `handle`, `status` |
| ownership | Account |
| visibility | public: handle/display_name; private: account linkage |
| lifecycle | active → suspended → retired; never hard-delete |
| relationships | Controller\*, PlayerSession\*, world Agent principal mapping |
| uniqueness | `player_id` global; handle unique within deployment policy |
| create | with Account (human) or enrollment grant (agent Controller on existing Player) |
| discriminator | **none** for human vs agent — both are Players |
| replay | principal in events (via `agent_id` wire alias where applicable) |

### Controller

| Aspect | Spec |
|--------|------|
| ID | `controller_id` |
| immutable | `controller_id`, `player_id`, `created_at` |
| mutable | `metadata`, `revoked_at` |
| required | `controller_id`, `player_id`, `type`, `created_at` |
| type | `browser` \| `mobile` \| `cli` \| `api` \| `mcp` \| `agent` |
| ownership | Player |
| visibility | private; metadata may appear in research provenance |
| lifecycle | active until `revoked_at` set |
| relationships | Credential\*, PlayerSession\* |
| create | human login bind, or agent device enrollment approval |
| notes | framework/model fields are provenance only |

### Credential

| Aspect | Spec |
|--------|------|
| ID | `credential_id` |
| immutable | `credential_id`, `controller_id`, `issued_at`, `kind` |
| mutable | `revoked_at`, rotation successor |
| required | `credential_id`, `controller_id`, `kind`, `scopes`, `fingerprint` |
| ownership | Controller |
| visibility | secret material never stored in exports; fingerprint only |
| lifecycle | issued → active → expired/revoked |
| create | enrollment approval, token refresh, operator issue |
| hard rule | agent Controllers MUST NOT receive human browser passwords/sessions |

### PlayerSession

| Aspect | Spec |
|--------|------|
| ID | `session_id` |
| immutable | `session_id`, `player_id`, `controller_id`, `world_id`, `started_at` |
| mutable | `status`, `ended_at`, `last_action_at` |
| required | ids above, `status` |
| ownership | Player + Controller |
| lifecycle | active → paused → terminated |
| MVP rule | one **action-producing** Controller per active Session |
| distinct from | Credential (auth material) and connection transport id |

## Entity contracts (v0.1 world plane)

For each: ID format, immutable/mutable fields, required/optional, ownership, visibility, lifecycle, relationships, uniqueness, lineage, create/mutate rules, tombstone, serialization, replay/spectator relevance.

### Agent

The **Agent** registry record is the world/wire principal for a Player under frozen v0.1 contracts. Ontologically it **is** the Player in the game world; the field name `agent_id` is retained for protocol and ledger compatibility.

| Aspect | Spec |
|--------|------|
| ID | `agent_id` (maps to Player principal; see AUTH-AND-IDENTITY) |
| immutable | `agent_id`, `owner_id` / account linkage, `created_at` |
| mutable | `display_name`, `status`, `active_agent_version_id` |
| required | `agent_id`, `display_name`, `owner_id`, `status` |
| ownership | Account / administrative owner (`owner_id`); gameplay participant is the Player |
| visibility | public: display_name; private: owner / account linkage |
| lifecycle | REGISTERED → ACTIVE_IN_WORLD → INACTIVE; never hard-delete |
| relationships | AgentVersion\*, ResourceAccount, memberships, Controller\* (via Player) |
| uniqueness | `agent_id` global |
| create | AUTH + REGISTER (after Controller Credential validated) |
| mutate | owner/operator; not other Players |
| tombstone | status ARCHIVED; retain history |
| serialization | agent-manifest + registry record |
| replay | identity in events |
| spectator | display_name only unless Agent POV |
| note | Not a separate class from human Players; humans also play as this principal via browser Controllers |

### AgentVersion

| Aspect | Spec |
|--------|------|
| ID | `agent_version_id` |
| immutable | all declaration fields after create |
| required | `agent_version_id`, `agent_id`, `manifest_id` or embedded manifest digest |
| create | REGISTER / re-REGISTER version bump |
| replay | pin in trajectory |

### World / WorldVersion

| Aspect | Spec |
|--------|------|
| ID | `world_id` / `world_version` |
| immutable | `world_id`, seed digest at genesis |
| mutable | `cycle`, `status`, live indexes |
| required | id, version, seed, catalog_version, state_revision, canonicalization_version, hash_algorithm, budget_defaults |
| lifecycle | ACTIVE / PAUSED / INCIDENT / ARCHIVED |
| uniqueness | (`world_id`,`world_version`) lineage |
| tombstone | ARCHIVED; no ID reuse |
| serialization | world-seed, world-state, runtime-manifest |

### Room

| Aspect | Spec |
|--------|------|
| ID | `room_id` |
| immutable | `room_id`, `created_cycle` |
| mutable | description, entity occupancy indexes |
| required | `room_id`, `name`, `description` |
| visibility | public unless tagged restricted |
| relationships | Exit\*, Entity\* |
| tombstone | soft destroy rare; prefer ENTITY_DESTROY on contents |

### Exit

| Aspect | Spec |
|--------|------|
| ID | `exit_id` |
| required | `from_room_id`, `to_room_id`, `direction` |
| mutable | `state` OPEN/CLOSED/BLOCKED/HIDDEN/DESTROYED, conditions |
| uniqueness | exit_id; recommend unique (from, direction) |

### Entity

| Aspect | Spec |
|--------|------|
| ID | `entity_id` |
| types | AGENT, OBJECT, ARTIFACT, INFRASTRUCTURE, ORGANIZATION, CURRENCY, DOCUMENT |
| required | `entity_id`, `entity_type`, `location` |
| mutable | `properties`, `state`, `inventory`, `owner_id`, `controller_id` |
| infrastructure state | `condition` 0–100, `capacity`, `infra_type` ∈ relay\|generator\|storage_bay\|production_node |
| resource node | `properties.resource_node=true`, `state.available`, `state.capacity` |
| tombstone | `ENTITY_DESTROY` → destroyed_cycle; no hard delete |
| replay | full |
| spectator | label + type; state per SPECTATOR.md |

### Organization / OrganizationMembership

| Aspect | Spec |
|--------|------|
| ID | `org_id` / `membership_id` |
| required org | name, status, members[] |
| roles | founder, officer, member, advisor |
| mutable | members, status |
| visibility | name public; charter public by default; private membership **not** supported in v0.1 (all members world-visible) |
| create | ORG_CREATE |
| mutate | ORG_MEMBER_ADD/REMOVE |
| tombstone | status DISSOLVED retains history |

### ResourceAccount

| Aspect | Spec |
|--------|------|
| ID | implicit (`agent_id` + resource name) or `acct.{agent}.{resource}` |
| resources | attention, compute, energy, influence, storage |
| mutable | balance, reserved |
| constraints | ≥ 0; see RESOURCE-ECONOMY.md |
| replay | mandatory |

### Action

| Aspect | Spec |
|--------|------|
| ID | `action_id` |
| required | agent_id (Player principal), world_id, cycle, verb, parameters, idempotency_key |
| gateway provenance | controller_id, session_id, submitted_at (identity plane) |
| immutable | after accept |
| schema | agent-action.schema.json (wire); provenance envelope in AUTH-AND-IDENTITY / AGENT-GATEWAY |
| engine care | Player + requested action — not the framework that generated the request |

### WorldEvent

| Aspect | Spec |
|--------|------|
| ID | `event_id` |
| required | envelope fields + digest chain + catalog-specific payload binding |
| immutable | append-only |
| catalog | closed 24 types for `event-catalog/0.1`, 31 types for `event-catalog/0.2` |
| schema | generic envelope `world-event.schema.json` plus composed admission schema `event-catalog-0.1.schema.json` or `event-catalog-0.2.schema.json` |

### Observation

| Aspect | Spec |
|--------|------|
| ID | `observation_id` |
| immutable | after generate |
| visibility | permissioned |
| schema | observation.schema.json |

### Message

| Aspect | Spec |
|--------|------|
| ID | `message_id` |
| states | QUEUED → DELIVERED |
| visibility | parties only for text |
| events | MESSAGE, MESSAGE_DELIVERED |

### Snapshot / Trajectory / RuntimeManifest

| Entity | Spec |
|--------|------|
| Snapshot | snapshot_id, world_state digest, cycle, sequence, world_version, catalog_version, state_revision, canonicalization_version, hash_algorithm, lineage |
| Trajectory | ordered events + observations + versions |
| RuntimeManifest | runtime-manifest.schema.json |

## Append-only preference

Research-critical and **settled** world events use append-only ledgers. Corrections are new events. Transient DO operations (heartbeats, redundant polls) are not required to become durable events.

## Conceptual durable tables (platform)

Minimum relational surface (names indicative; implement in Supabase):

```text
identities / accounts
players
controller_bindings
credentials          # fingerprints / metadata; not raw secrets when avoidable
sessions
worlds
locations / rooms
player_state         # settled snapshots as needed
inventory
events               # settled durable GameEvents / WorldEvents
experiments
observations
metrics
artifacts            # Storage refs
```

Authoritative vs derived: live DO state is operational; Postgres events/snapshots are durable truth for replay/research after settlement.

## Append-only preference (continued)

## Public/private separation

Agent private metadata, research metadata, and public world-visible metadata remain separate. Dataset releases MUST preserve this partition.
