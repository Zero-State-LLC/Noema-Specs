# Admin Live Operations

**Authority.** Canonical **Admin Live** operations surface: how an authorized Admin oversees a running world without becoming a special Player, bypassing world rules, leaking private information, or corrupting canonical history.

This document does not redefine world mechanics, event catalogs, identity ontology, Genesis, research claims, or security sequences. It does not replace [WATCH](WATCH.md), [PLAY](PLAY.md), [STUDY](STUDY.md), [OPERATOR-INTERVENTIONS.md](OPERATOR-INTERVENTIONS.md), [OPERATIONS.md](OPERATIONS.md), or [SECURITY-SEQUENCES.md](SECURITY-SEQUENCES.md).

This expansion closes **IMPLEMENTATION AMBIGUITY** and an **OPERATIONAL BLOCKER** under [FIRST-WORLD-SPEC-FREEZE.md](FIRST-WORLD-SPEC-FREEZE.md). It is not a new milestone, not v0.8, and not a release package.

Related: [WORLD-OPERATIONS.md](WORLD-OPERATIONS.md) · [OPERATOR-INTERVENTIONS.md](OPERATOR-INTERVENTIONS.md) · [INCIDENT-RECOVERY.md](INCIDENT-RECOVERY.md) · [PLAYER-LIFECYCLE.md](PLAYER-LIFECYCLE.md) · [OPERATOR-DIGESTS.md](OPERATOR-DIGESTS.md) · [FIRST-WORLD-OPERATIONS.md](FIRST-WORLD-OPERATIONS.md) · [AUTH-AND-IDENTITY.md](AUTH-AND-IDENTITY.md) · [PLATFORM.md](PLATFORM.md) · [GENESIS.md](GENESIS.md) · [SECURITY.md](SECURITY.md) · [MODULE-CONTRACTS.md](MODULE-CONTRACTS.md) · [ACTION-CONTRACTS.md](ACTION-CONTRACTS.md) · [EVENT-CATALOG.md](EVENT-CATALOG.md) · [EXPERIENCE.md](EXPERIENCE.md) · [PLAYER-BRAND.md](PLAYER-BRAND.md) · [VISUAL-DESIGN.md](VISUAL-DESIGN.md).

Admin Live shares brand tokens and type roles with PLAY. It MUST remain an operator register: schema names, telemetry, head/revision, and health overlays are correct here and forbidden as ordinary PLAY chrome.

---

## Canonical principle

> Admin observes the authoritative system. Admin does not play through the dashboard.

Admin Live is a **control-plane** surface. It is not PLAY with extra buttons, not a GM client, and not a second World Engine.

```text
PLAYER
├── human controller
└── agent controller

ADMIN
→ separate control-plane principal
```

An operator who wants to play MUST use a separate Player identity. Admin privilege MUST NOT be inherited by a Player session ([PLATFORM.md](PLATFORM.md), [SECURITY.md](SECURITY.md)).

Do **not** introduce:

```text
ADMIN_PLAYER
GM_PLAYER
SUPER_PLAYER
```

Admin is not automatically a Player. Do not model ADMIN as a world participant class.

Admin scopes such as `noema.world.admin` and `noema.simulation.admin` remain control-plane grants. They MUST NOT be granted to ordinary Players by default ([AUTH-AND-IDENTITY.md](AUTH-AND-IDENTITY.md)). Reuse the existing admin/operator authorization. Do not create a second identity platform. Genesis already requires this reuse ([GENESIS.md](GENESIS.md)).

---

## Distinct surfaces

```text
PLAY
→ What can I do?

WATCH
→ What is happening?

STUDY
→ What are we learning?

ADMIN LIVE
→ Is the world operating correctly?

OPERATOR DIGEST
→ What settled in this time window?
```

These surfaces MUST remain distinct. Admin Live is inspect-now. Operator Digests are time-window summaries that share source projections ([OPERATOR-DIGESTS.md](OPERATOR-DIGESTS.md)). CONNECT remains Controller onboarding, not a Player mode and not Admin Live ([EXPERIENCE.md](EXPERIENCE.md)).

| Surface | Mutates world? | Principal | Question |
|---|---|---|---|
| PLAY | Yes, through the Action Router | Player | What can I do here? |
| WATCH | Never | Spectator / observer | What is happening? |
| STUDY | Never on the production world | Authorized researcher | What are we learning? |
| Admin Live | Only through [Operator Interventions](OPERATOR-INTERVENTIONS.md) | Separate Admin principal | Is the world operating correctly? |

Admin Live MUST NOT be a public product door. WATCH parity does not include Admin Live. Ordinary PLAY, public WATCH, and CONNECT MUST NOT expose or advertise the Admin Live console ([EXPERIENCE.md](EXPERIENCE.md)).

---

## Admin Live capabilities

The Admin Live surface MUST support:

```text
OBSERVE
INSPECT
DIAGNOSE
OPERATE
AUDIT
```

| Capability | Meaning | Default |
|---|---|---|
| `OBSERVE` | Read derived operational projections of canonical status, pulse, events, and health | On |
| `INSPECT` | Drill into a Player, location, event, institution, or system object without becoming that object | On |
| `DIAGNOSE` | Correlate alerts, freshness, settlement, and failure guidance | On |
| `OPERATE` | Start a governed intervention already authorized by [OPERATOR-INTERVENTIONS.md](OPERATOR-INTERVENTIONS.md) | Off until explicit |
| `AUDIT` | Navigate to existing ledger, intervention, backup, and control-plane records | On, read-only |

Default Admin Live mode is **observational**: `OBSERVE`, `INSPECT`, `DIAGNOSE`, and read-only `AUDIT`. `OPERATE` is never the landing mode.

Keep PLAY, WATCH, STUDY, and administrative authority separated. Admin Live MUST NOT absorb Player verbs, spectator narrative, or research claim editing.

---

## Purpose and non-goals

Admin Live exists so an authorized operator can:

- understand whether the running world is healthy enough to accept Players;
- inspect Players, locations, and canonical events;
- diagnose system, settlement, and research health;
- start only explicit audited interventions through governed paths.

Admin Live MUST NOT:

- become a second World Engine or a second canonical world model;
- create a new Admin analytics datastore;
- expose private cognition;
- casually expose private message text;
- advertise unsupported gameplay actions;
- invent quests, motives, or hidden history;
- mutate WorldState except through the [Operator Interventions](OPERATOR-INTERVENTIONS.md) path;
- chat, trade, move, harvest, repair, or otherwise act as a Player via the control plane;
- change Genesis semantics or create new Player classes.

---

## Scope

Admin Live is an **information architecture contract**, not one screen. It MUST be able to project:

```text
world status
cycle
Players
locations
canonical events
infrastructure
resources
trade
institutions
contests / agreements (when the pinned catalog includes them)
system health
settlement health
research health
alerts
audit navigation
```

It MAY also project World Service status ([WORLD-SERVICES.md](WORLD-SERVICES.md)), Genesis status ([GENESIS.md](GENESIS.md)), and backup/evidence status ([OPERATIONS.md](OPERATIONS.md)). Those panes remain concise and MUST NOT dominate Live after activation.

This document does not mandate a visual layout. It mandates what an operator can answer, what must remain hidden, and which mutations are forbidden.

---

## Recommended information architecture

Recommended first-world navigation:

```text
Overview
Live
World
Players
Institutions
Economy
Research
Genesis
Backups
Evidence
System
Audit
```

This is a contract for findability. Implementations MAY collapse, rename for display, or nest panes if every capability remains reachable without inventing a second model.

| Pane | Answers | Must not become |
|---|---|---|
| Overview | Is the deployment operable? Status, health, alerts, last verify, last backup | A duplicate Live feed |
| Live | What is happening in the world **now**? Pulse, event feed, topology, open alerts | Config forms or Genesis controls |
| World | Condition, locations, infrastructure, routes | A Player map cheat sheet published to WATCH |
| Players | Who is in the world, where, session health | A human-vs-agent leaderboard |
| Institutions | Canonical institutions and World Services | Admin membership or stewardship |
| Economy | Open trades, resource pressure, reservations | A market that does not exist |
| Research | Ready / blocked / not in scope | World truth or claim editing |
| Genesis | Pre-activation controls; post-activation frozen provenance | A live reseed UI |
| Backups | Last backup, last verify, restore entry | A second backup system |
| Evidence | Receipt / export profile status | A research warehouse UI |
| System | `/health`, `/ready`, `/version`, writer fence, auth, DO | World condition copy |
| Audit | Intervention and control-plane records + ledger navigation | A second world ledger |

### Overview versus Live

Overview and Live MUST NOT be redundant.

```text
Overview
→ operator posture of the deployment

Live
→ operator-left-open pulse of the running world
```

Overview SHOULD emphasize status, health overlay, open alerts, last successful `noema verify`, last backup, and whether PLAY is currently acceptable. Live SHOULD emphasize cycle, Players, locations, canonical event feed, topology, and current operational warnings.

Live MUST remain a pulse the operator can leave open. It is not a settings form, Genesis wizard, or credential editor. Configuration, Genesis, backup restore, and identity operations belong on their own panes and MUST follow governed intervention rules when they mutate anything.

---

## World pulse

Admin Live MUST present a compact operational summary derived from canonical world status, health, and settled counts. Controller type is **not** a headline population split. Humans and agents are all Players.

Example (illustrative, not a layout mandate; Perihelion Reach names are non-normative):

```text
PERIHELION REACH
ACTIVE
Cycle 18,442

Players          7
Locations        5
Open trades      3
Open contests    1

World health     HEALTHY
Settlement       HEALTHY
Research         Ready
Freshness        live
```

Required pulse fields:

| Field | Source |
|---|---|
| World name / `world_id` | Runtime manifest / world record |
| World status | Canonical `World.status`: `ACTIVE` / `PAUSED` / `INCIDENT` / `ARCHIVED` ([WORLD-ENGINE.md](WORLD-ENGINE.md), [WORLD-OPERATIONS.md](WORLD-OPERATIONS.md)) |
| Cycle | Canonical simulation clock |
| Player count | Distinct Players with world presence, not controller count |
| Location count | Canonical rooms / locations |
| Open trades | Canonical open trade records |
| Open contests | Canonical open contest records when the pinned catalog includes them |
| World health | [WORLD-OPERATIONS.md](WORLD-OPERATIONS.md) health overlay |
| Settlement | Settlement backlog / last settled ledger head ([INCIDENT-RECOVERY.md](INCIDENT-RECOVERY.md)) |
| Research readiness | Authorized overlay only; ordinary Admin Live MAY show `Ready` / `Blocked` / `Not in scope` |
| Freshness | Operational freshness of this projection (`live` / `recent` / `stale` / `unavailable`) |

The pulse MUST show the canonical world status, not a decorative synonym. Operator language MAY additionally say `maintenance` when status is `PAUSED`. It MUST NOT invent a second status enum.

Controller metadata MAY appear as an optional advanced breakdown. It MUST NOT be the default population split and MUST NOT create a gameplay hierarchy.

---

## Controller metadata

Controller type, provider, protocol, and credential status are **operational / provenance metadata** ([AUTH-AND-IDENTITY.md](AUTH-AND-IDENTITY.md)).

Show them only when operationally useful, for example:

- diagnosing a stuck session;
- revoking a Controller;
- comparing provenance on an audited action;
- confirming one controlling PlayerSession per Player.

Do not expose controller metadata as game ontology. Do not label inhabitants “AI Agent” / “Human Player” as competing classes. Humans are not Players (RFC-0120). Admin is never a Player role.

---

## Canonical live event feed

Admin Live MUST derive its live feed from **canonical settled events**, not from inferred narrative. The feed is a projection of settled/canonical activity.

Example (illustrative):

```text
18:442 Nacre moved Grid Anchor → Coldline
18:442 Relay Trunk repaired 35 → 50
18:441 Vesper proposed trade
18:441 Archive Fragment inspected
```

Rules:

- Each row MUST cite a settled event (cycle, actor, verb/type, visible target or result).
- The feed MUST NOT infer motives, plans, or private reasoning.
- Unsettled live transitions MUST be marked unsettled and MUST NOT be presented as durable history.
- WATCH-style significance copy is optional and MUST remain grounded in the cited events ([WATCH.md](WATCH.md)).
- Event types, payloads, and reducer semantics remain [EVENT-CATALOG.md](EVENT-CATALOG.md). This feed does not add types.

The feed MUST be paginated or otherwise bounded. It is not an unbounded browser-side ledger dump.

---

## Progressive event inspection

Selecting a feed row MUST allow progressive drill-down:

```text
human-readable summary
  → canonical IDs
    → actor, target, cycle
      → costs, result
        → ledger sequence, settlement
```

Required drill-down fields when they exist:

```text
action / event type
actor
target
resource cost
result
cycle
ledger sequence
settlement
```

Advanced drill-down MAY include `controller_id`, `session_id`, `action_id`, `event_id`, digest, and writer-fence epoch. Ordinary Admin Live SHOULD lead with human-readable names and keep IDs in the advanced pane.

Do not fabricate missing fields. If a cost, target, or settlement field is absent from the canonical record, show it as unavailable rather than inventing a value.

---

## Operational topology

Admin Live MAY show a lightweight **operational topology**. This is an explicit Admin exception to text-first PLAY ([EXPERIENCE.md](EXPERIENCE.md), [HUMAN-PLAY.md](HUMAN-PLAY.md)). It does not weaken the PLAY presentation rule.

The topology is functional, not decorative:

```text
locations
routes
Player presence
infrastructure state
resource pressure
active strategic state
operational warnings
```

- No 3D requirement.
- No decorative cartography requirement.
- Topology MUST derive from canonical geography and settled state ([GEOGRAPHY.md](GEOGRAPHY.md), [CHAMBER-MAP.md](CHAMBER-MAP.md)).
- Tables, cards, charts, and topology MAY be used when they improve visibility, safety, or error prevention.

### Admin topology versus Player map

These are different projections.

| Projection | Audience | Content |
|---|---|---|
| Player map | Player | Known/visible geography only ([PLAY.md](PLAY.md), [PARTIAL-OBSERVABILITY.md](PARTIAL-OBSERVABILITY.md)) |
| WATCH map | Spectator | Public-derived geography ([SPECTATOR.md](SPECTATOR.md)) |
| Admin topology | Authorized Admin | Canonical operational graph, still subject to redaction classes |

Admin topology MUST distinguish visibility classes:

| Class | Meaning |
|---|---|
| Canonical | Authoritative world geography and settled occupancy |
| Public | Already projectable to PLAY/WATCH |
| Research-private | Research overlay; authorized research Admin only |
| Admin-private | Control-plane operational warnings, session health, fence/settlement markers |

Hidden exits, undiscovered history, and Genesis internals MUST NOT leak to any surface that is not authorized Admin. Even Admin Live SHOULD mark undiscovered-from-Players information as canonical-not-public rather than presenting it as a game map the operator is “playing.”

---

## Location inspector

For a selected location, Admin Live MAY show:

- canonical name and ID;
- occupants (Players / entities);
- visible infrastructure and condition;
- known routes;
- resource pressure that is already canonical;
- recent settled events at that location;
- open trades, contests, or World Service desks present there.

The inspector MUST NOT:

- teleport the Admin into the room as a Player;
- reveal private cognition of occupants;
- treat Admin inspection as presence, membership, or ownership.

---

## Player inspector

Default Player inspector:

```text
Player identity
location
online/offline
resources
organization / institution membership
recent canonical actions
session health
```

Advanced operational metadata MAY include:

```text
Player ID
Controller ID
controller type
credential status
session
client/protocol
last action sequence
```

Controller metadata remains metadata. It MUST NOT create a gameplay hierarchy or a second population metric.

Disconnecting or revoking a Controller MUST NOT be presented as deleting the Player ([PLAYER-LIFECYCLE.md](PLAYER-LIFECYCLE.md)).

Admin Live is **not omniscient surveillance by default**. Default Player inspection is operational: identity, location, resources, membership, recent canonical actions, and session health. It is not a live wiretap of private cognition, unsubmitted plans, or casual private-message text.

---

## Private cognition boundary

> NOEMA does not expose or require private cognition for Admin oversight.

Admin Live MUST NOT collect or expose:

```text
chain-of-thought
private model reasoning
hidden CoT
scratchpads
unsubmitted plans
private prompts
```

This restates [ADR-002](../adr/ADR-002-private-cognition-boundary.md) and [AGENT-INTERFACE.md](AGENT-INTERFACE.md). No operator dashboard, debug mode, incident tool, or “explain this agent” control may request private cognition.

Provenance MAY record controller/framework/model labels already declared as untrusted metadata. That is not private cognition.

---

## Private communication

Canonical private messages have parties-only text visibility ([ACTION-CONTRACTS.md](ACTION-CONTRACTS.md), [SPECTATOR.md](SPECTATOR.md)).

Default live view of MESSAGE activity:

```text
sent
sender
recipient
delivery state
```

Message **text** is hidden by default. Spectator `message_notice` without text remains the public projection.

If privileged message-text inspection is permitted for a security or abuse reason, it MUST be:

```text
explicit privileged action
+ authorization
+ reason
+ audit receipt
```

Casual exposure of message content is forbidden. Operator Digests follow the same default ([OPERATOR-DIGESTS.md](OPERATOR-DIGESTS.md)).

---

## World condition

Admin Live SHOULD summarize world condition as a **derived** overlay, not new world truth:

- world status and health overlay;
- infrastructure condition bands already canonical ([INFRASTRUCTURE.md](INFRASTRUCTURE.md));
- connectivity / isolation that is already implied by open routes;
- open contests or access restrictions when the pinned catalog includes them;
- writer-fence uniqueness;
- last verified snapshot / ledger head;
- settlement backlog, if any.

World condition MUST NOT invent a scalar “world score,” dramatic weather, or authored crisis copy. If evidence is insufficient, omit the claim or mark it unavailable.

---

## Resource pressure

Resource pressure MUST be a transparent aggregation of canonical stocks, node availability, reservations, and infrastructure modifiers ([RESOURCE-ECONOMY.md](RESOURCE-ECONOMY.md)).

Allowed:

```text
energy remaining at node X
storage used / capacity
open harvest reservations
relay condition
```

Forbidden:

- arbitrary pressure scores;
- opaque “instability” meters;
- rankings of Players by hidden efficiency.

Use integers, counts, condition bands, and cited events. Do not create a new resource.

---

## Institutions inspector

Institutions remain [INSTITUTIONS.md](INSTITUTIONS.md). World Services remain [WORLD-SERVICES.md](WORLD-SERVICES.md).

Admin MAY inspect:

- institution identity, status, succession, continuity;
- public practices and evidence refs;
- World Service status, allowed operations, failures, canonical actions emitted, request volume.

Inspecting an institution or World Service MUST NOT make Admin a member, custodian, or Player. Admin has no in-world stewardship by virtue of opening the inspector.

---

## Economy operational state

Economy panes MUST project existing canonical records: budgets, nodes, open trades, reservations, and transfers.

They MUST NOT add a market, order book, shop, or price index that does not already exist in world contracts. First-world freeze already defers a market order book ([FIRST-WORLD-SPEC-FREEZE.md](FIRST-WORLD-SPEC-FREEZE.md)).

---

## Strategic state

When the world’s pinned catalog includes v0.2 contestation ([STRATEGIC-CONFLICT.md](STRATEGIC-CONFLICT.md), [RFC-0002](../rfcs/RFC-0002-strategic-contestation-and-crime-events.md)):

Admin MAY inspect open contests, defenses, agreements, and access restrictions as canonical records.

Admin visibility is **not** Player visibility and **not** WATCH visibility. Players and spectators remain under partial observability and spectator redaction. Admin inspection of strategic state MUST still respect `SECRET` and research-private redaction classes below.

If the pinned catalog is v0.1 only, the strategic pane MUST say the catalog does not include those types rather than simulating them.

---

## Alerts

Alerts are for **operational attention**, not dramatic gameplay.

Routine gameplay is not an immediate alert. Summarize it in [Operator Digests](OPERATOR-DIGESTS.md). Immediate alerts stay reserved for operationally significant conditions.

### Severity

Use a small closed operator-attention vocabulary:

```text
INFO
ATTENTION
CRITICAL
```

This is not a PagerDuty-style incident-management product and does not replace `World.status` or the health overlay ([INCIDENT-RECOVERY.md](INCIDENT-RECOVERY.md) non-goals remain).

| Severity | Meaning |
|---|---|
| `INFO` | Notable operational fact; no action required |
| `ATTENTION` | Operator should inspect; PLAY may still continue |
| `CRITICAL` | Required property failed or authority is unsafe; follow incident recovery |

### World anomalies versus system alerts

Keep these distinct:

| Kind | Examples | Must not |
|---|---|---|
| World anomaly | Isolated location, failed infrastructure, open contest, resource node empty | Become a system `INCIDENT` by itself |
| System alert | Settlement lag, writer-fence ambiguous, ledger mismatch, auth unavailable, Durable Object unavailable, version pin mismatch, kill switch, backup failure | Be narrated as in-world drama |

Recommended closed system-alert set:

| Alert | Meaning |
|---|---|
| Settlement lag | Durable events are waiting to settle |
| Writer fence ambiguous | Fail closed; see [INCIDENT-RECOVERY.md](INCIDENT-RECOVERY.md) |
| Ledger / digest mismatch | `RECOVERY_REQUIRED` |
| Auth provider unavailable | New sessions fail closed |
| Durable Object unavailable | Live mutations unavailable |
| Version / spec incompatibility | Worker or rules pin mismatch |
| Quarantine / kill switch active | Containment in effect |
| World Service degraded / unavailable | Convenience adapter unhealthy; Action Router may still be fine |
| Backup / verify failed | Recovery path unhealthy |
| Research overlay blocked | STUDY/research pipeline unhealthy; PLAY MAY continue |

Alerts MUST cite the underlying check. They MUST NOT invent player-facing quests or research claims.

---

## Research overlay

An authorized research overlay MAY show whether STUDY / Lab / Compiler / LEARN capture is ready, blocked, or out of scope ([RESEARCH-WORKFLOW.md](RESEARCH-WORKFLOW.md), [STUDY.md](STUDY.md)).

The overlay MUST:

- remain read-only with respect to production world truth;
- preserve claim labels `OBSERVED` / `INFERRED` / `SPECULATIVE` / `NOT_COMPUTABLE`;
- redact hidden research metadata from any operator who lacks the corresponding research authorization.

Invariant:

```text
research overlay
≠
world truth
```

A failed Frontier, Observatory, Lab derivation, Compiler, or LEARN rebuild MUST NOT, by itself, stop gameplay ([INCIDENT-RECOVERY.md](INCIDENT-RECOVERY.md)). Ordinary first-world Admin Live does **not** require the full research stack.

---

## Observational default

Default Admin Live is observational.

World-changing controls, if present at all, MUST be:

- behind an explicit `OPERATE` workflow;
- disabled until the operator selects an already-authorized intervention class;
- absent from the Live pulse as one-click buttons.

There are no default Live controls of the form:

```text
GIVE ENERGY
SET LOCATION
TELEPORT
DELETE TRADE
EDIT MEMBERSHIP
REWRITE LEDGER
SPAWN CONTENT
```

Those raw edits are forbidden ([OPERATOR-INTERVENTIONS.md](OPERATOR-INTERVENTIONS.md)).

---

## Intervention boundary

Any Admin operation that changes world truth MUST follow the existing governed path. Admin Live MUST NOT mutate WorldState, Durable Object fields, or Postgres ledger rows directly.

```text
AdminPrincipal
  → authorized operation
  → validation
  → consequence preview
  → confirmation
  → Action Router / declared recovery path
  → canonical result
  → audit receipt
```

Authority: [OPERATOR-INTERVENTIONS.md](OPERATOR-INTERVENTIONS.md), [MODULE-CONTRACTS.md](MODULE-CONTRACTS.md), [ACTION-CONTRACTS.md](ACTION-CONTRACTS.md) operator path.

Closed intervention classes remain:

```text
CONTROL_PLANE
WORLD_OPERATION
EXTERNAL_INPUT
RECOVERY
```

Read-only inspection is not a world-changing operation and does not use this path.

### Action Router

World-changing Admin operations that affect canonical world truth MUST enter through the Action Router or a declared external-input / recovery path. Operator surfaces MUST NOT bypass `action_router` ([MODULE-CONTRACTS.md](MODULE-CONTRACTS.md)).

Control-plane session/credential operations are **not** world actions. They use identity-plane stores and [SECURITY-SEQUENCES.md](SECURITY-SEQUENCES.md). They MUST NOT be submitted as Player LOOK / MOVE / MESSAGE / TRADE actions.

### Intervention semantics

A conforming operator intervention is:

```text
authenticated
authorized
versioned
validated
canonical
ledgered
auditable
```

High-impact operations MUST show a **consequence preview** before confirmation. Preview is derived from existing contracts (status change, session termination, PLAY rejection, restore identity). It MUST NOT invent unstated world mutations.

Destructive or high-impact operations require **deliberate confirmation**. No one-click destructive mutation. Restore is never a one-click Live action ([INCIDENT-RECOVERY.md](INCIDENT-RECOVERY.md)).

Privileged world-changing interventions and privileged private-message inspection MUST record a concise operator reason. Ordinary read-only inspection does not.

---

## Audit

Admin Live MUST use the **existing** event ledger, intervention receipts, and control-plane audit records. It MUST NOT create a second world ledger.

```text
pulse / alert
  → event or intervention
    → ledger sequence / receipt
      → backup, verify, or incident record
```

### Operational audit versus world history

| Kind | What it is | Authority |
|---|---|---|
| World history | Canonical settled events | Event ledger ([EVENT-CATALOG.md](EVENT-CATALOG.md)) |
| Operational audit | Control-plane actions, session ops, verify/backup, intervention receipts | [SECURITY-SEQUENCES.md](SECURITY-SEQUENCES.md), [OPERATIONS.md](OPERATIONS.md), [OPERATOR-INTERVENTIONS.md](OPERATOR-INTERVENTIONS.md) |

Do not inject operator reason text into world history unless a canonical event already requires an operator note. Do not treat Admin navigation logs as WorldEvents.

Deep Time evidence and archaeology remain [HISTORICAL-EVIDENCE.md](HISTORICAL-EVIDENCE.md) / [DEEP-TIME.md](DEEP-TIME.md). Admin Live MAY navigate to those records; it MUST NOT become a hidden-ledger leak into PLAY or WATCH.

---

## Graphics exception

PLAY remains text-first. Authorized ADMIN surfaces MAY use tables, cards, charts, and topology when they improve visibility, safety, or error prevention ([EXPERIENCE.md](EXPERIENCE.md)).

That exception does not weaken text-first PLAY and does not make Admin Live a graphical MMO client.

Charts are allowed only for operational questions, for example:

- settlement lag over recent cycles;
- Player session counts;
- infrastructure condition distribution;
- open-trade counts.

Charts MUST NOT become player-facing victory scores, consciousness scores, or research-claim dashboards. No scalar consciousness or intelligence score.

---

## Data freshness

Every Live projection SHOULD state operational freshness:

| Freshness | Meaning |
|---|---|
| `live` | Current cycle / current settled head within the refresh bound |
| `recent` | Settled, but older than the current cycle or last refresh |
| `stale` | Behind a known settlement/outage marker |
| `unavailable` | Source cannot be read; show guidance, not invented state |

This is an Admin Live freshness label. It is not the observation `quality_class` / `stale` vocabulary in [PARTIAL-OBSERVABILITY.md](PARTIAL-OBSERVABILITY.md), though implementations MAY map between them in advanced detail.

Unsettled live transitions MUST remain marked unsettled.

---

## Performance

Bounded polling is sufficient. Admin Live MUST NOT require WebSockets. Hosted Realtime MAY be used selectively for dashboards ([PLATFORM.md](PLATFORM.md)); it is not the multiplayer sync engine and is not required for a conforming Admin Live.

Admin Live MUST NOT degrade PLAY:

- no unbounded history scans on each refresh;
- no research-graph rebuild as a Live poll side effect;
- no extra mutating cycle work to “keep the dashboard interesting”;
- Operator Digest generation remains downstream and MUST NOT advance cycles ([OPERATOR-DIGESTS.md](OPERATOR-DIGESTS.md)).

Pagination / bounded history is required for event feeds, Player lists, audit lists, and digest history. Do not keep unlimited generated reports in the browser.

---

## Redaction classes

Admin Live projections MUST classify fields with this closed control-plane redaction vocabulary:

```text
WORLD_PUBLIC
WORLD_PRIVATE
PLAYER_PRIVATE
RESEARCH_PRIVATE
ADMIN_PRIVATE
SECRET
```

| Class | Meaning | Default Live |
|---|---|---|
| `WORLD_PUBLIC` | Already projectable to PLAY/WATCH | Visible |
| `WORLD_PRIVATE` | Canonical world state not in the public projection | Visible to authorized Admin; never copy to WATCH |
| `PLAYER_PRIVATE` | Parties-only or self-only Player data (message text, private inspect) | Hidden by default |
| `RESEARCH_PRIVATE` | Research overlay, candidates, detector metadata | Hidden unless research-authorized |
| `ADMIN_PRIVATE` | Control-plane operational detail (fence epoch, session health, intervention reasons) | Admin only |
| `SECRET` | Passwords, keys, tokens, service-role, Cloudflare secrets, signing material | **Never** to the browser |

These classes are an Admin Live projection contract. They do not replace observation visibility classes (`visible` / `hidden` / `partial` / …) or invent protocol fields. They MUST map onto existing consent, spectator, and security rules.

`SECRET` MUST NEVER be sent to the browser, including Admin Live. Logging and error messages remain [OBSERVABILITY.md](OBSERVABILITY.md) / [ENVIRONMENT.md](ENVIRONMENT.md).

---

## Secret handling

Admin Live MAY show secret **configuration status** only:

```text
configured
missing
invalid
```

Never display:

```text
passwords
API keys
tokens
service-role keys
Cloudflare secrets
signing material
database credentials
provider keys
```

Fingerprints or last-four metadata already permitted by [AUTH-AND-IDENTITY.md](AUTH-AND-IDENTITY.md) MAY appear in advanced audit. Raw secret material MUST NOT.

Backup bundles follow [OPERATIONS.md](OPERATIONS.md): non-secret configuration digest only.

---

## WATCH parity and Player privacy

Do not expose Admin Live publicly.

| Surface | Sees Admin Live? |
|---|---|
| Public WATCH | No |
| Ordinary PLAY | No |
| CONNECT | No |
| Authorized Admin | Yes, allowlisted |
| STUDY | Research overlay only when authorized; not the Admin Live console |

Player privacy: Admin is not omniscient surveillance by default. Default views stay on canonical public-or-operational fields. Privileged expansion of `PLAYER_PRIVATE` requires authorization, reason, and audit as specified above.

---

## Admin MUST NOT play

Admin MUST NOT chat, trade, move, harvest, repair, inspect-as-Player, or otherwise act through the control plane as if Admin were a Player.

Credential and session operations are control-plane, not world actions:

```text
revoke credential
terminate session
disable controller
suspend account
quarantine
```

These follow [PLAYER-LIFECYCLE.md](PLAYER-LIFECYCLE.md) and [SECURITY-SEQUENCES.md](SECURITY-SEQUENCES.md).

Session termination is **not**:

- canonical world relocation;
- Player deletion;
- `AGENT_LEFT_WORLD` from transport close;
- ledger truncation.

The Player remains at last canonical location. Committed history remains.

---

## Genesis status

Genesis remains admin-only and one-time ([GENESIS.md](GENESIS.md)).

Before activation, Admin Live / Genesis pane MAY show preview, profile, story seeds, world seed, and Cycle 0 digest to authorized operators.

After activation:

- Genesis configuration is frozen;
- Genesis MUST NOT dominate Live;
- PLAY and WATCH still MUST NOT expose profile, story seeds, or world seed;
- Live MAY show a concise “Genesis frozen / activated” marker and link to provenance.

This document does not change Genesis semantics, profiles, or story seeds. Perihelion Reach identity remains [FIRST-WORLD-OPERATIONS.md](FIRST-WORLD-OPERATIONS.md).

---

## Backup and evidence status

Backup, restore, and verify remain [OPERATIONS.md](OPERATIONS.md). Evidence receipts remain [SECURITY.md](SECURITY.md) / [REPRODUCIBILITY.md](REPRODUCIBILITY.md).

Admin Live SHOULD show concise status only:

```text
last backup time / result
last noema verify result
last evidence-export receipt status (authorized)
```

It MUST NOT create a second backup system, snapshot format, or evidence warehouse. Restore remains the explicit sequenced intervention, never a one-click Live control.

---

## Failure states

When a required source is unhealthy, Admin Live MUST show an operator-actionable failure state rather than a blank or invented world.

Reuse the [INCIDENT-RECOVERY.md](INCIDENT-RECOVERY.md) failure matrix. Minimum Live guidance:

| Condition | Operator guidance |
|---|---|
| Durable Object unavailable | Live mutations blocked; inspect last settled head; do not invent a fallback world |
| Settlement `DEGRADED` | Inside one-batch bound; watch catch-up; do not rewrite history |
| Settlement `BLOCKING` | Fail closed; `PAUSED` or `INCIDENT`; restore/reconcile |
| Ledger mismatch | `RECOVERY_REQUIRED`; restore / reconcile; never pick the prettier digest |
| Auth provider unavailable | New Admin/Player login fail closed; no auth bypass |
| Research overlay blocked | Repair research pipeline; do not pause PLAY |
| Secret missing/invalid | Show status only; restore secrets out of band |

---

## System health versus world condition

Keep these distinct:

```text
System health
→ process, ready, pins, writer fence, ledger integrity,
  snapshot integrity, settlement confirmation, auth reachability

World condition
→ derived canonical infrastructure, routes, resources,
  institutions, contests, occupancy
```

A healthy world can have damaged relays. A healthy relay network can sit behind a failed writer fence. Do not collapse these into one score.

System health is the combination of:

```text
process /health
readiness /ready
version / spec pins
writer fence
ledger integrity
snapshot integrity
settlement confirmation
auth provider reachability
```

---

## Accessibility and viewport

Admin Live SHOULD be keyboard-operable, with visible focus, semantic headings/tables, strong contrast, readable text, and non-color-only status. Reduced motion SHOULD be respected.

Viewport expectation:

| Viewport | Expectation |
|---|---|
| Desktop | Primary operational console |
| Tablet | Operational: pulse, alerts, event feed, inspectors |
| Mobile | Limited: status, alerts, and critical guidance; not a full topology/operate workstation |

Complex graphical presentation is not a requirement. PLAY accessibility rules remain on the PLAY surface ([HUMAN-PLAY.md](HUMAN-PLAY.md)).

---

## No second model

Admin Live MUST NOT:

- create a second canonical world model;
- cache a private “true map” that diverges from WorldState;
- introduce a new Admin analytics datastore as authority;
- store generated dashboard prose as canonical history.

All Live panes are **projections** of existing canonical state, ledgers, identity records, operations receipts, and authorized research overlays. Rebuildable projections are allowed. A new source of world truth is not.

---

## Non-normative Perihelion Reach examples

Names such as Perihelion Reach, Nacre, Vesper, Grid Anchor, Coldline, and Relay Trunk in this document are **illustrative**. They MUST NOT be hard-coded as world semantics.

The production pin remains [FIRST-WORLD-OPERATIONS.md](FIRST-WORLD-OPERATIONS.md). Aster Reach fixtures remain non-authoritative examples.

---

## Bounded checklist

Keep these checks small. They are the SPEC-CHECKLIST surface for this document:

1. Admin is a separate control-plane principal; no `ADMIN_PLAYER` / `GM_PLAYER` / `SUPER_PLAYER`.
2. Default Live is observational (`OBSERVE` / `INSPECT` / `DIAGNOSE`); `OPERATE` is explicit.
3. Pulse shows canonical status, cycle, Player count (not controller count), and health.
4. Event feed cites settled events and does not infer motives.
5. Event drill-down reaches actor, target, cycle, costs, result, ledger, and settlement when those fields exist.
6. Topology is an Admin graphics exception and is not the Player/WATCH map.
7. Private cognition is absent; MESSAGE text is hidden by default.
8. World-changing controls go through Action Router / declared recovery; no direct WorldState edits.
9. `SECRET` never reaches the browser; secrets show configured/missing/invalid only.
10. Admin Live is not a public WATCH/PLAY door.
11. Session termination does not relocate or delete the Player.
12. System health and world condition remain distinct.
13. No new schema, milestone, or v0.8 package is required to implement this surface.

---

## Acceptance

A conforming Admin Live implementation proves:

1. An operator can answer “is the world operating correctly?” without entering PLAY as a super-player.
2. The pulse shows canonical status, cycle, Player count (not controller count), and health.
3. The event feed cites settled events and does not infer motives.
4. Drill-down reaches action, actor, target, cost, events, sequence, and settlement when those fields exist.
5. Player inspection can show identity, location, status, resources, membership, recent actions, and session health.
6. Private cognition is absent.
7. Message text is hidden by default; any reveal is privileged, reasoned, and audited.
8. World-changing controls, if present, follow [OPERATOR-INTERVENTIONS.md](OPERATOR-INTERVENTIONS.md).
9. Overview and Live are not the same page with different titles.
10. Redaction classes are enforced; `SECRET` is never in the browser payload.
11. Admin cannot MOVE / MESSAGE / TRADE via the dashboard.
12. Genesis does not dominate Live after activation.
13. Polling is bounded; PLAY is not degraded by the console.

---

## Unresolved spec gaps

These remain unspecified here on purpose. They are not silent defaults:

- Exact poll interval numbers and chart widget sets (runtime choice, bounded).
- Multi-operator concurrent `OPERATE` arbitration beyond existing writer-fence / intervention receipts.
- A machine-readable Admin Live schema (not required; add only if a runtime cannot implement this document without ambiguity).
- Privileged message-text policy beyond the explicit + reason + audit gate (legal/abuse policy is deployment-specific).
- Email or other digest delivery UI (owned by [OPERATOR-DIGESTS.md](OPERATOR-DIGESTS.md)).

If a runtime would need to invent a lifecycle, identity class, world mutation, or public exposure rule, that is a **SPEC DEFECT**. Do not invent it in the dashboard.

---

## Non-goals

- Runtime UI implementation in this repository
- New gameplay verbs or GM tools
- New Player classes
- Genesis semantic change
- 3D or decorative cartography
- Multi-world orchestration UI
- A second identity, ledger, backup, or research evidence system
- A new Admin analytics database
- A new milestone / v0.8 / release package
- Reading private prompts to “explain” agent behavior
- PagerDuty-style severity matrices
- WebSocket requirement for Admin Live
