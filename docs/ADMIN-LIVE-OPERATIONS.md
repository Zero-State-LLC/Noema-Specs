# Admin Live Operations

**Authority.** Canonical first-world **Admin Live** surface: how an authorized operator observes whether the live world is operating correctly.

This document does not redefine world mechanics, event catalogs, identity ontology, or research claims. It does not replace [WATCH](WATCH.md), [PLAY](PLAY.md), [STUDY](STUDY.md), [OPERATIONS.md](OPERATIONS.md), or [SECURITY-SEQUENCES.md](SECURITY-SEQUENCES.md).

Related: [WORLD-OPERATIONS.md](WORLD-OPERATIONS.md) · [OPERATOR-INTERVENTIONS.md](OPERATOR-INTERVENTIONS.md) · [INCIDENT-RECOVERY.md](INCIDENT-RECOVERY.md) · [PLAYER-LIFECYCLE.md](PLAYER-LIFECYCLE.md) · [FIRST-WORLD-OPERATIONS.md](FIRST-WORLD-OPERATIONS.md) · [AUTH-AND-IDENTITY.md](AUTH-AND-IDENTITY.md) · [PLATFORM.md](PLATFORM.md) · [GENESIS.md](GENESIS.md).

---

## Canonical principle

> Admin observes the authoritative system. Admin does not play through the dashboard.

Admin Live is a **control-plane** surface. It is not PLAY with extra buttons.

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
```

These surfaces MUST remain distinct.

| Surface | Mutates world? | Principal | Question |
|---|---|---|---|
| PLAY | Yes, through the Action Router | Player | What can I do here? |
| WATCH | Never | Spectator / observer | What is happening? |
| STUDY | Never on the production world | Authorized researcher | What are we learning? |
| Admin Live | Only through [Operator Interventions](OPERATOR-INTERVENTIONS.md) | Separate Admin principal | Is the world operating correctly? |

Admin Live MAY be graphical. PLAY remains text-first. That exception is already stated in [EXPERIENCE.md](EXPERIENCE.md) and [HUMAN-PLAY.md](HUMAN-PLAY.md). It does not make Admin Live a game client.

---

## Admin identity boundary

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

Admin scopes such as `noema.world.admin` and `noema.simulation.admin` remain control-plane grants. They MUST NOT be granted to ordinary Players by default ([AUTH-AND-IDENTITY.md](AUTH-AND-IDENTITY.md)).

Reuse the simplest existing admin/operator authorization. Do not create a second identity platform. Genesis already requires this reuse ([GENESIS.md](GENESIS.md)).

---

## Purpose and non-goals

Admin Live exists so an operator can:

- see whether Perihelion Reach is healthy enough to accept Players;
- inspect canonical live and settled state without inferring motives;
- navigate from an operational symptom to a ledgered event, session, or incident;
- start a governed intervention when one is already authorized.

Admin Live MUST NOT:

- become a second World Engine;
- expose private cognition;
- casually expose private message text;
- advertise unsupported gameplay actions;
- invent quests, motives, or hidden history;
- mutate WorldState except through the [Operator Interventions](OPERATOR-INTERVENTIONS.md) path.

---

## World pulse

Admin Live MUST present a compact operational summary derived from canonical world status, health, and settled counts. Controller type is **not** a separate population.

Example (illustrative, not a layout mandate):

```text
PERIHELION REACH
ACTIVE
Cycle 18,442

Players          7
Locations        5
Open trades      3
Open contests    1

World health     Healthy
Settlement       Healthy
Research         Ready
```

Required pulse fields:

| Field | Source |
|---|---|
| World name / `world_id` | Runtime manifest / world record |
| World status | Canonical `World.status`: `ACTIVE` / `PAUSED` / `INCIDENT` / `ARCHIVED` ([WORLD-ENGINE.md](WORLD-ENGINE.md)) |
| Cycle | Canonical simulation clock |
| Player count | Distinct Players with world presence, not controller count |
| Location count | Canonical rooms / locations |
| Open trades | Canonical open trade records |
| Open contests | Canonical open contest records when the pinned catalog includes them |
| World health | [WORLD-OPERATIONS.md](WORLD-OPERATIONS.md) health overlay |
| Settlement | Settlement backlog / last settled ledger head |
| Research readiness | Authorized overlay only; ordinary Admin Live MAY show `Ready` / `Blocked` / `Not in scope` |

The pulse MUST show the canonical world status, not a decorative synonym. Operator language MAY additionally say `maintenance` when status is `PAUSED`. It MUST NOT invent a second status enum.

---

## Live canonical event feed

Admin Live MUST derive its live feed from **canonical settled events**, not from inferred narrative.

Example:

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

### Event drill-down

Selecting a feed row MUST allow drill-down to canonical fields when they exist:

```text
action
actor
target
resource cost
events
cycle
ledger sequence
settlement
```

Advanced drill-down MAY include `controller_id`, `session_id`, `action_id`, `event_id`, digest, and writer-fence epoch. Ordinary Admin Live SHOULD lead with human-readable names and keep IDs in the advanced pane.

---

## World topology

Admin Live MAY show a lightweight operational topology:

```text
locations
routes
Player presence
infrastructure state
resource pressure
active strategic state
operational warnings
```

This is an operations diagram, not a game map.

- No 3D requirement.
- No decorative map requirement.
- Topology MUST derive from canonical geography and settled state ([GEOGRAPHY.md](GEOGRAPHY.md), [CHAMBER-MAP.md](CHAMBER-MAP.md)).
- It MUST NOT reveal hidden exits, undiscovered history, or Genesis internals to any surface that is not authorized Admin.

---

## Inspectors

### Location inspector

For a selected location, Admin Live MAY show:

- canonical name and ID;
- occupants (Players / entities);
- visible infrastructure and condition;
- known routes;
- resource pressure that is already canonical;
- recent settled events at that location.

### Player inspector

Admin MAY inspect:

```text
Player identity
location
online/offline
resources
organization membership
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

Controller type remains **metadata**. It MUST NOT create a gameplay hierarchy or a second population metric.

Disconnecting or revoking a Controller MUST NOT be presented as deleting the Player ([PLAYER-LIFECYCLE.md](PLAYER-LIFECYCLE.md)).

### World condition

Admin Live SHOULD summarize:

- world status and health overlay;
- writer-fence uniqueness;
- last verified snapshot / ledger head;
- `/health`, `/ready`, `/version` ([OPERATIONS.md](OPERATIONS.md));
- settlement backlog, if any.

### Economy, institutions, strategic state

These panes MUST project existing canonical records:

- economy and open trades from [RESOURCE-ECONOMY.md](RESOURCE-ECONOMY.md) and trade events;
- institutions from [INSTITUTIONS.md](INSTITUTIONS.md);
- strategic state from contest/agreement/access records when the world's pinned catalog includes them.

They MUST NOT become a second market, government, or lore simulator.

---

## Operational alerts

Admin Live SHOULD surface a small closed alert set:

| Alert | Meaning |
|---|---|
| Settlement lag | Durable events are waiting to settle |
| Writer fence ambiguous | Fail closed; see [INCIDENT-RECOVERY.md](INCIDENT-RECOVERY.md) |
| Ledger / digest mismatch | `RECOVERY_REQUIRED` |
| Auth provider unavailable | New sessions fail closed |
| Durable Object unavailable | Live mutations unavailable |
| Version / spec incompatibility | Worker or rules pin mismatch |
| Quarantine / kill switch active | Containment in effect |

Alerts MUST cite the underlying check. They MUST NOT invent player-facing quests or research claims.

---

## Research overlay

An authorized research overlay MAY show whether STUDY/Lab/Compiler capture is ready, blocked, or out of scope.

The overlay MUST:

- remain read-only with respect to production world truth;
- preserve claim labels;
- redact hidden research metadata from any operator who lacks the corresponding research authorization.

Ordinary first-world Admin Live does **not** require the full research stack.

---

## System health and audit navigation

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

Audit navigation MUST let an operator jump from:

```text
pulse / alert
  → event or intervention
    → ledger sequence / receipt
      → backup, verify, or incident record
```

Backup, restore, and verify remain [OPERATIONS.md](OPERATIONS.md). This document does not create a second backup system.

---

## Private cognition boundary

> NOEMA does not expose or require private cognition for Admin oversight.

Admin Live MUST NOT collect or expose:

```text
chain-of-thought
private model reasoning
scratchpads
unsubmitted plans
```

This restates [ADR-002](../adr/ADR-002-private-cognition-boundary.md) and [AGENT-INTERFACE.md](AGENT-INTERFACE.md). No operator dashboard, debug mode, or incident tool may request private cognition.

---

## Private communication policy

Canonical private messages have parties-only text visibility ([ACTION-CONTRACTS.md](ACTION-CONTRACTS.md), [SPECTATOR.md](SPECTATOR.md)).

Default Admin Live view:

```text
Admin Live
→ sender
→ recipient
→ delivery state
→ metadata

message content
→ hidden by default
```

If privileged message-text inspection is permitted for a security or abuse reason, it MUST be:

```text
explicit privileged action
+
authorization
+
reason
+
audit receipt
```

Casual exposure of message content is forbidden. Spectator `message_notice` without text remains the public projection.

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

---

## Non-goals

- New gameplay verbs or GM tools
- 3D or decorative cartography
- Multi-world orchestration UI
- A second identity, ledger, or research evidence system
- Reading private prompts to “explain” agent behavior
