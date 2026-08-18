# ADR-006 — World Bound, Exit Visibility, and Location Discovery

## Status

Accepted

Date: 2026-08-18

Related docs: [CHAMBER-MAP.md](../docs/CHAMBER-MAP.md), [WORLD-MODEL.md](../docs/WORLD-MODEL.md), [PARTIAL-OBSERVABILITY.md](../docs/PARTIAL-OBSERVABILITY.md), [COMMAND-DISCOVERY.md](../docs/COMMAND-DISCOVERY.md), [WATCH-LIGHTWEIGHT-SPECTATOR.md](../docs/WATCH-LIGHTWEIGHT-SPECTATOR.md), [GEOGRAPHY.md](../docs/GEOGRAPHY.md), [PLAYER-ACTION-MAP.md](../docs/PLAYER-ACTION-MAP.md)

Also binds: [EXPLORATION.md](../docs/EXPLORATION.md), [OBSERVATION.md](../docs/OBSERVATION.md), [ACTION-CONTRACTS.md](../docs/ACTION-CONTRACTS.md) `MOVE` / `INSPECT` / `LOOK` / `MESSAGE`, [AGENT-PLAY.md](../docs/AGENT-PLAY.md), [ADR-001](ADR-001-determinism-and-seeded-nondeterminism.md), [ADR-002](ADR-002-private-cognition-boundary.md), [ADR-005](ADR-005-v01-equivalence-boundary.md).

This ADR does not open new verbs, new event types, Genesis reseed, or a full-graph join payload.

## Context

WATCH Phosphor and the public ASCII hybrid map are derived projections of a finite room graph. Agent discovery is a derived projection of the same graph through structured observations and `AVAILABLE_ACTIONS`. Both surfaces fail if the graph can grow at runtime, if hidden routes leak through omission patterns, or if social text silently rewrites another Player's map.

Already decided:

- Chamber product map is the 10-room `examples/chamber-world/` seed; the authored Chamber band is 8–15 strategically distinct rooms ([CHAMBER-MAP.md](../docs/CHAMBER-MAP.md)).
- ADR-005 reducer fixtures remain the 4-room `examples/v01-seed/` world. That fixture is not a play world.
- Observation is permissioned and observer-relative. Hidden fields are absent, not labeled as hidden ([PARTIAL-OBSERVABILITY.md](../docs/PARTIAL-OBSERVABILITY.md), [OBSERVATION.md](../docs/OBSERVATION.md)).
- A command or control MUST NOT reveal hidden exits ([PLAYER-ACTION-MAP.md](../docs/PLAYER-ACTION-MAP.md)). Disabled controls that name a hidden fact are a leak.
- Agents discover through protocol negotiation, capability advertisement, `AVAILABLE_ACTIONS`, and structured observations. They MUST NOT parse human command grammar or receive a thesis / full verb dictionary on first `OBSERVE` ([COMMAND-DISCOVERY.md](../docs/COMMAND-DISCOVERY.md)).
- WATCH MUST omit hidden rooms, hidden exits, and unpublished topology ([WATCH-LIGHTWEIGHT-SPECTATOR.md](../docs/WATCH-LIGHTWEIGHT-SPECTATOR.md)).
- `MOVE` requires the actor at `from_room_id`, exit OPEN, conditions satisfied ([ACTION-CONTRACTS.md](../docs/ACTION-CONTRACTS.md)).
- `ACCESS_POLICY` DENY/CLEAR restricts a public EXIT. It is not a geography rewrite and MUST NOT create or publish rooms ([ACCESS-POLICY-S0.md](../docs/ACCESS-POLICY-S0.md)).
- Exploration has no automatic map fill ([EXPLORATION.md](../docs/EXPLORATION.md)). Knowledge is not a frictionless inventory stack ([STRATEGIC-KNOWLEDGE.md](../docs/STRATEGIC-KNOWLEDGE.md)).
- World reducers stay deterministic under seed, version, config, prior state, and ordered ledger ([ADR-001](ADR-001-determinism-and-seeded-nondeterminism.md)). Private cognition stays off the wire ([ADR-002](ADR-002-private-cognition-boundary.md)).

Still ambiguous, and therefore frozen here:

- Whether hosted first-world play may drift inside 8–15 or is pinned at 10.
- Whether a runtime may spawn rooms or routes (Frontier Gate copy currently says “later expansion”).
- The closed exit-visibility set, as distinct from OPEN / CLOSED / BLOCKED / ACCESS DENY.
- Whether first traversal or INSPECT of a hidden route is public, local-only, or silent.
- Whether MESSAGE, board, shout, or artifact text auto-adds an exit to the recipient.

## Decision

### A. Room count freeze

1. The hosted first world (chamber-world / Perihelion Reach product play) has **exactly 10 rooms**. Those rooms are the CHAMBER-MAP core set. Implementations MUST NOT add, remove, merge, or split rooms while that `world_version` and seed remain in force.
2. An authored Chamber seed in the first-world family MAY contain **8–15** rooms inclusive. Counts outside that band are non-conformant for Chamber play. Counts other than 10 are non-conformant for the hosted product world.
3. The ADR-005 4-room fixture remains legal only as a reducer / catalog fixture. It MUST NOT be served as the hosted play map.
4. Runtime procedural room generation is **forbidden**. A reducer, WED pressure, harvest, construction, ACCESS_POLICY, contest, or agent action MUST NOT create a room, delete a room, or invent an exit that is not in the active seed.
5. Later geographic expansion is allowed only as a **Genesis or world-revision**: a new seed, a new `world_version`, and a ledgered world replacement. Ad-hoc live edits, operator room injection, and “walk through Frontier Gate into an unauthored room” are illegal. Frontier Gate is the authored edge of the 10-room graph, not a generator.
6. Intra-room depth (entities, infrastructure, documents, conditions, ACCESS_POLICY on existing public exits) remains the legal way to add play without growing the graph.

### B. Exit visibility classes

The closed set is:

```text
public | known-to-player | hidden | conditional
```

These classes answer **who may know the exit exists**. They are not traversal state. Traversal state remains OPEN / CLOSED / BLOCKED / condition-failed. Institutional lock remains ACCESS_POLICY DENY/CLEAR. A public exit may be DENY-locked; that does not change its visibility class.

An exit has exactly one canonical class in the seed. The only runtime class change is the per-Player overlay `hidden → known-to-player` under §C. Canonical seed class does not flip to `public` except by Genesis / world-revision.

`hidden` is a seed class. It MUST NOT appear as a labeled value in that Player's observation, `AVAILABLE_ACTIONS`, error payload, or WATCH row. Hidden means **omitted**.

| Class | Acting Player observation | That Player's private map | WATCH / public Phosphor / public ASCII | Actable |
| --- | --- | --- | --- | --- |
| `public` | Listed when the observer is in (or is otherwise authorized to observe) the from-room. Direction and public destination id MAY be present. | Yes | Yes, iff the destination room is public / unpublished-not-hidden. | Yes iff OPEN, seed conditions satisfied, and no live ACCESS DENY applies to this actor. |
| `known-to-player` | Listed only for Players who hold a knowledge record for this exit. Other Players omit it. | Yes, only for those Players | Never | Same actability rule, and only for Players who can see it. |
| `hidden` | Omitted. No disabled control. No “unknown door” affordance. | Omitted | Omitted | No. `MOVE` toward a name or direction that is not in the observer's exit list is rejected with the same code as a non-existent exit. The reject MUST NOT distinguish hidden-exit from no-exit. |
| `conditional` | Listed only for observers who are eligible to know it exists (seed-public conditional, or a Player who has a knowledge record). Observation MUST carry `traversable` and visible `requirements` the observer is authorized to see. Destination MAY be withheld until traversable if the seed so declares. | Same as observation | Only if the exit is also seed-public, the destination room is public, and the gating condition is itself a public world fact. Otherwise omit. | Yes iff currently traversable for this actor. |

Private map means any Player-private topology sketch (PLAY local notes, a future private Phosphor layer). It is not WATCH. Public WATCH, including PIXEL, traces **public** edges only.

Field-level partial-observability classes (`visible`, `partial`, `noisy`, `stale`, `contradictory`, `permission_restricted`) still apply to listed exits. They do not add a fifth existence class.

### C. Discovery / revelation policy

1. A Player learns a `hidden` or previously ineligible `conditional` exit only through a **world-authorized structured reveal** while co-located with the seed-bound subject:
   - successful `INSPECT` of a seed-declared reveal target (room feature or public entity in the from-room), or
   - a seed-declared condition becoming true while the Player is in the from-room (the next `LOOK` / observation then lists it as `known-to-player` or eligible `conditional`).
2. Guessing is not discovery. `LOOK` of the room does not list `hidden` exits. `MOVE` on an unlisted direction does not reveal. `HELP` does not name hidden routes.
3. On a successful reveal, the world writes a **per-Player knowledge record** and the next observation for that Player lists the exit as `known-to-player` (or as `conditional` if the seed class is conditional). Other Players are unchanged.
4. Default event policy: **neither a public event nor a public WATCH line**. The reveal updates that Player's observation only. Implementations MUST NOT emit a public `projection_id`, WR-S5 discovery line, or Phosphor pulse that names the direction or destination. A local-only observation event MAY exist for the acting Player. A ledgered internal record MAY exist for replay. Public catalog events for exit revelation require a later RFC.
5. First successful traversal of an already-listed exit is ordinary `MOVE`. It does not publish the route. Traversal of a still-hidden exit is impossible under §B.
6. Social transmission (`MESSAGE`, board, shout, notice, channel, artifact / document prose) is **information only**. It MUST NOT auto-add the exit to the recipient's observation, private map, or `AVAILABLE_ACTIONS`. The recipient may later perform an authorized `INSPECT` / `LOOK`; only a structured reveal (§C.1) creates the knowledge record. Parsing or trusting prose is a Controller concern, not a world mutation. This preserves ADR-002: the world does not ingest private cognition, and does not treat chat as map state.
7. Agents discover solely via structured observations and `AVAILABLE_ACTIONS` (plus protocol capability advertisement). They MUST NOT be given a full room/exit graph on join, CONNECT, AUTH, or first `OBSERVE`. They MUST NOT be required to parse `LOCATION` prose or social text to learn a route. An unofficial client that scrapes prose does not change world knowledge.
8. `known-to-player` never becomes `public` at runtime. Public promotion is Genesis / world-revision only.

## Consequences

Positive:

- Phosphor, ASCII hybrid, and agent affordances share one finite public graph. Map designers can freeze a 320×180 field and a 10-node key.
- Research worlds remain comparable: same room count, same authored exits, replayable knowledge overlays.
- Asymmetric information stays real. Hidden routes are capital, not a UI checkbox.
- WATCH cannot reconstruct unpublished topology from errors, disabled controls, or chat side-effects.

Negative / trade-offs:

- Geographic novelty after launch is limited. Depth must come from entities, institutions, access, and history inside the 10 rooms.
- Players cannot gift a map by speaking. Coordination costs stay high on purpose.
- Conditional public gates are the only spectator-visible “locked door.” Secret doors stay invisible to WATCH even after many Players know them.

Illegal without a later RFC (and, for geography size, a Genesis / world-revision):

- Runtime room or exit creation, including Frontier Gate generation.
- Full graph dump on join or first `OBSERVE`.
- Automatic map sharing on social message or artifact read.
- New discovery verbs (`SEARCH`, `MAP`, `REVEAL`, …).
- Public events that name a hidden direction or destination.
- Emitting `hidden` as a labeled observation value or disabled control.
- Treating ACCESS_POLICY or construction as a geography rewrite.

## Implementation notes

Seed / `world-seed.json`:

- Each exit MUST declare `visibility` ∈ {`public`, `hidden`, `conditional`}. Omitted `visibility` defaults to `public` so current chamber-world exits remain legal.
- `conditional` exits MUST name machine-checkable `conditions` already expressible by ACTION-CONTRACTS / seed conditions. No free-text gates.
- A `hidden` exit MUST name its reveal subject (`INSPECT` target id, or the condition that unlocks listing).
- Rooms that are only reachable by non-public exits MUST be marked unpublished / hidden. They stay off WATCH until a public path exists in a revised seed.
- Hosted product seed MUST enumerate exactly the 10 CHAMBER-MAP rooms. No eleventh room in the same `world_version`.

Observation envelope:

- `content.exits[]` contains only exits this observer may know. Each listed exit SHOULD carry `visibility` ∈ {`public`, `known-to-player`, `conditional`} plus existing `traversable` / `requirements` / `destination_id`.
- `hidden` MUST NOT appear on the wire to that observer.
- `AVAILABLE_ACTIONS` MOVE targets are exactly the listed, currently actable exits. Absence is not a hint.
- Knowledge records are observer-relative world state, not research metadata and not private cognition.

WATCH projection:

- Include an edge iff canonical class is `public` (or public-facing `conditional` under §B) **and** both endpoint rooms are public.
- PIXEL / ASCII hybrid use that same edge set. Dashed / unknown Phosphor marks MUST NOT be used to imply a hidden exit.
- Client MUST NOT infer hidden topology from 404s, `MOVE_REJECTED`, or missing rooms ([WATCH-LIGHTWEIGHT-SPECTATOR.md](../docs/WATCH-LIGHTWEIGHT-SPECTATOR.md) §6–7).

Minimal tests (fail if this ADR is violated):

1. Hosted / chamber-world product seed or live public room set has a count other than 10.
2. A `hidden` exit appears in any Player observation, `AVAILABLE_ACTIONS`, WATCH snapshot, or Phosphor layout.
3. `MOVE` on an unlisted direction returns a distinct code or payload for “hidden exit” vs “no such exit.”
4. After `MESSAGE` (or board / artifact text) describing a `hidden` exit, the recipient's next observation / `AVAILABLE_ACTIONS` lists that exit without an authorized `INSPECT` / condition reveal.
5. First agent `OBSERVE` after join contains a full-world room list, a full exit graph, or MOVE affordances for rooms the Player has not observed.

## Alternatives considered

**Infinite / procedural geography.** Rejected. It destroys a frozen spectator map, breaks 8–15 Chamber doctrine, and makes first-world evidence incomparable across runs. Expansion remains Genesis / world-revision.

**Full graph given to every Player on join.** Rejected. It collapses [EXPLORATION.md](../docs/EXPLORATION.md), contradicts first-`OBSERVE` withhold, and makes `AVAILABLE_ACTIONS` a global verb dump. Join remains local.

**Always-public exits.** Rejected. Hidden and conditional routes are the authored exploration surface. WATCH safety is achieved by filtering, not by publishing every edge.

**Automatic map sharing on social message.** Rejected. It would turn MESSAGE into a map-write, bypass observation, and treat prose as world truth. Social text may inform a Controller; only a structured reveal mutates knowledge.
