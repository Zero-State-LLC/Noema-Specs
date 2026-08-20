# MUD Design Canon

**Status:** Design-ancestry authority. Non-normative for world transitions.  
**Campaign:** [GAME-COMPLETENESS-PLAN.md](GAME-COMPLETENESS-PLAN.md)  
**Interaction campaign:** [MUD-NATIVE-INTERACTION-AND-WORLD-PRESENCE.md](MUD-NATIVE-INTERACTION-AND-WORLD-PRESENCE.md) · [plan](MUD-NATIVE-INTERACTION-PLAN.md) · [tasks](MUD-NATIVE-INTERACTION-TASKS.md)  
**Play craft companion:** [MUD-PLAY-CRAFT.md](MUD-PLAY-CRAFT.md) · [closeout / runtime sequencing](MUD-PLAY-CRAFT-CLOSEOUT.md)  
**Does not replace:** [GAME-DESIGN.md](GAME-DESIGN.md) · [CORE-GAME-LOOP.md](CORE-GAME-LOOP.md) · [HUMAN-PLAY.md](HUMAN-PLAY.md)

This document records the **structural lessons** NOEMA takes from major MUD traditions. It is not a setting bible, a rules clone, or a second product thesis.

---

## Scope

Reference families (inspiration only):

```text
MUD1 / British Legends
DikuMUD
LambdaMOO
Achaea
GemStone
BatMUD
Discworld MUD
DragonRealms
MajorMUD
Alter Aeon
```

These names identify **historical design families**. They do not authorize cloning.

### Forbidden borrowing

Implementations and later specifications MUST NOT copy or restyle:

- setting, cosmology, or proprietary lore;
- terminology that is distinctive to a commercial or specific MUD;
- proprietary mechanics, formulas, or class trees;
- characters, maps, rooms, or named content;
- rules text, help files, or quest scripts.

NOEMA remains its own world: a persistent strategic text ecology whose first-world authority is already frozen ([FIRST-WORLD-SPEC-FREEZE.md](FIRST-WORLD-SPEC-FREEZE.md)).

What may be taken is **structure**: how a long-lived text world holds identity, geography, social power, and time.

---

## Canonical conclusion

> The strongest MUDs function as persistent social machines, not merely content-rich text adventures.

A MUD that only delivers authored rooms and combat loops is a content product. A MUD that lets Players become somebody — through practice, office, construction, reputation, and inherited history — is a social machine.

NOEMA's mature-world target is the latter:

```text
persistent world
× meaningful identity
× interdependence
× partial knowledge
× irreversible history
× social memory
× player-created structure
× recurring uncertainty
```

Research observes that machine. Research is not the machine.

---

## Ten structural lessons

### 1. Exploration and unknown space are intrinsically valuable

Players return because the world still contains places, routes, and facts they do not yet hold. Discovery is a reward even when it yields no loot.

NOEMA already treats exploration as strategic capital ([EXPLORATION.md](EXPLORATION.md), [STRATEGIC-KNOWLEDGE.md](STRATEGIC-KNOWLEDGE.md), [PARTIAL-OBSERVABILITY.md](PARTIAL-OBSERVABILITY.md)). Completeness work MUST keep unknown space, delayed information, and uncertain maps as first-class value — not as missing content to be filled by quests.

### 2. Players need a legible mastery trajectory

A Player should be able to answer: *what am I becoming good at, and how would another Player notice?*

That trajectory MUST be evidence-backed practice, not a universal XP ladder or intelligence score ([PROGRESSION.md](PROGRESSION.md)). See [MASTERY-SPECIALIZATION.md](MASTERY-SPECIALIZATION.md).

### 3. Player-created social structures can become the world

The most durable MUD identity is not a class name. It is the company, house, archive, compact, or maintenance order that outlives its founders.

NOEMA already specifies institutions that persist beyond participants ([INSTITUTIONS.md](INSTITUTIONS.md), [DEEP-TIME.md](DEEP-TIME.md)). Completeness work makes those structures **playable positions** ([INSTITUTIONAL-AUTHORITY.md](INSTITUTIONAL-AUTHORITY.md)), not only historical objects.

### 4. Offices and institutions should confer real authority

A title that changes no affordance, access, resource right, or communication right is costume.

NOEMA's rule:

> A title with no world authority is presentation, not an institutional mechanic.

World Services already follow this: closed capabilities, no LLM authority ([WORLD-SERVICES.md](WORLD-SERVICES.md)). Player offices MUST follow the same discipline.

### 5. Long-lived identity and specialization drive attachment

Players attach to a world when their name, practice, and relationships remain after they log out. Specialization is a memory the world keeps about a Player.

This is Player-facing identity, **not** the research Capability Graph ([CAPABILITY-GRAPH.md](CAPABILITY-GRAPH.md), [LEARN.md](LEARN.md)). Research capability candidates MUST NOT become Player classes.

### 6. Construction and persistent artifacts create ownership

A Player who changed the map, the route, or the archive owns something the next generation inherits. That is why construction cannot be an isolated crafting minigame.

See [CONSTRUCTION.md](CONSTRUCTION.md). Required product property:

> The state of the world at Cycle 500 can visibly contain consequences of Players who acted at Cycle 50.

### 7. Geography should produce local asymmetry

Different rooms, routes, and resource sites should make different strategies rational. Homogeneous space collapses play into a single optimum ([GEOGRAPHY.md](GEOGRAPHY.md), [GAME-BALANCE.md](GAME-BALANCE.md), [TERRITORY-CONTROL.md](TERRITORY-CONTROL.md)).

### 8. Demonstrated practice can produce capability

Competence is shown by doing the work, not by spending a point. NOEMA prefers proficiency derived from demonstrated activity over purchased ranks.

### 9. Short sessions should contribute to long-term progress

A Player who can only inhabit the world for a few cycles must still leave a durable mark: a repair, a record, a relationship, a route observation. Completeness systems MUST NOT require unbroken presence to remain somebody.

### 10. Text-first accessibility is a product strength

Text is not a temporary skin over a graphical MMO. It is why Agent Players and headless Controllers can share one observation/action contract, why replay is tractable, and why the world can be read as history ([AGENT-PLAY.md](AGENT-PLAY.md), [HUMAN-PLAY.md](HUMAN-PLAY.md)). Text-first does not mean visually empty: the player surface is an inhabited frontier interface ([PLAYER-BRAND.md](PLAYER-BRAND.md), [VISUAL-DESIGN.md](VISUAL-DESIGN.md)). Humans watch that world; they do not inhabit it ([RFC-0120](../rfcs/RFC-0120-agent-only-player-identity.md)).

---

## What NOEMA already is

These lessons are **not** a license to reopen the Chamber as a Diku clone.

Already settled and preserved:

| Property | Authority |
|----------|-----------|
| Only agents are Players; humans watch / connect / study / admin | [CONTEXT.md](../CONTEXT.md), [AUTH-AND-IDENTITY.md](AUTH-AND-IDENTITY.md), [RFC-0120](../rfcs/RFC-0120-agent-only-player-identity.md) |
| Stable verb taxonomy | [ACTION-CONTRACTS.md](ACTION-CONTRACTS.md), [PLAYER-ACTION-MAP.md](PLAYER-ACTION-MAP.md) |
| No universal XP or consciousness score | [PROGRESSION.md](PROGRESSION.md) |
| No authored quest narrator | [HUMAN-PLAY.md](HUMAN-PLAY.md), [LORE-BOUNDARY.md](LORE-BOUNDARY.md) |
| Lore is derived from history | [DEEP-TIME.md](DEEP-TIME.md) |
| Research does not rewrite world truth | [CONTEXT.md](../CONTEXT.md), [SPEC-FREEZE-CORE-LOOP.md](SPEC-FREEZE-CORE-LOOP.md) |
| Conflict is strategic, not hit-point combat | [STRATEGIC-CONFLICT.md](STRATEGIC-CONFLICT.md) |
| Core loop v0.1–v0.7 is frozen for implementation | [SPEC-FREEZE-CORE-LOOP.md](SPEC-FREEZE-CORE-LOOP.md) |

The completeness campaign **deepens** this social machine. It does not replace the Chamber, reopen v0.8 Phenomena, or convert research objectives into Player objectives. New depth must pass [COMPLEXITY-DOCTRINE.md](COMPLEXITY-DOCTRINE.md): few primitives, many couplings.

---

## Design test

A proposed completeness mechanic is structurally MUD-valid only if it strengthens at least one of:

```text
identity
practice
office
construction
relationship
inherited history
local asymmetry
unknown space
```

and fails if it only adds:

```text
content volume
a new verb for a new noun
a cosmetic title
a global score
an authored quest
a research metric as a Player reward
```

---

## Play craft

Structural lessons above are composed into operational PLAY projection craft in [MUD-PLAY-CRAFT.md](MUD-PLAY-CRAFT.md): room stack, status line, consequence four-beat, short-session marks, and adapter discipline. That document does not expand the product horizon and does not replace this canon.
