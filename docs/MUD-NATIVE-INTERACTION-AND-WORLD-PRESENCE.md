# MUD-Native Interaction and World Presence

**Status:** Specification campaign — additive PLAY-depth work.  
**Method:** Spec-Driven Development: constitution/context → specify → plan → tasks → implementation.  
**Package:** [spec](MUD-NATIVE-INTERACTION-AND-WORLD-PRESENCE.md) · [plan](MUD-NATIVE-INTERACTION-PLAN.md) · [tasks](MUD-NATIVE-INTERACTION-TASKS.md)  
**Depends on:** [CONTEXT.md](../CONTEXT.md) · [MUD-DESIGN-CANON](MUD-DESIGN-CANON.md) · [COMMAND-DISCOVERY](COMMAND-DISCOVERY.md) · [PLAYER-ACTION-MAP](PLAYER-ACTION-MAP.md) · [ACTION-CONTRACTS](ACTION-CONTRACTS.md) · [HUMAN-PLAY](HUMAN-PLAY.md) · [DEEP-TIME](DEEP-TIME.md) · [WATCH](WATCH.md).  
**Does not reopen:** Genesis, frozen verbs, settlement semantics, v0.8, crypto.

## Problem

NOEMA already has a persistent, deterministic world and a rich canonical action model. The remaining product risk is interaction drift: the world can be more expressive than the interface used to inhabit it.

A Player should experience:

```text
place → perception → intention → action → consequence → memory
```

not:

```text
runtime surface → command catalog → protocol-shaped response → telemetry
```

This campaign makes NOEMA feel natively like a persistent MUD without weakening replay, action authority, or the shared Player model.

## Governing constraints

1. World truth is authoritative. Presentation never invents entities, exits, affordances, causes, memories, or history.
2. Canonical actions stay canonical. No second action taxonomy and no reopening frozen verbs.
3. Agents do not parse human MUD text. Structured Controllers use protocol capabilities, structured observations, and canonical actions.
4. Humans and agents remain Players. Controller type is metadata.
5. Replay remains deterministic. Human normalization resolves to an explicit canonical action before mutation.
6. No LLM authority for parsing, noun resolution, aliases, help, room grammar, or presentation.
7. Research remains instrumentation; PLAY does not expose research labels/scores as game objectives.
8. Deep Time is derived from world history; traces require provenance.
9. Progressive disclosure beats interface density.
10. Text remains primary.

### Frozen surfaces not reopened

- Genesis seed or first-world topology
- v0.1–v0.7 core-loop semantics
- canonical action costs or settlement semantics unless separately approved
- agent protocol action meaning
- research claim labels
- v0.8 Phenomena
- crypto, wallets, x402, external settlement

## Feature A — Deterministic forgiving human command resolver

Human input adapter only:

```text
raw human input
→ tokenize
→ normalize
→ alias expansion
→ verb resolution
→ local noun resolution
→ preposition/argument resolution
→ canonical action candidate
→ validate against local affordances + canonical action contract
→ submit canonical action
```

Required equivalence examples:

```text
e / east / go east / walk east / move east
→ MOVE(direction=east)

look crane / look at crane / inspect crane / inspect the crane
→ INSPECT(entity_id=<resolved local entity>)

tell rhea hello / message rhea hello / say to rhea hello
→ canonical MESSAGE when resolution is unambiguous
```

Rules:
- command keywords case-insensitive;
- safe article normalization (`the`, `a`, `an`);
- direction abbreviations only for supported directions;
- exact local labels before prefix matches;
- resolve only currently observable/nameable entities;
- never leak hidden IDs through fuzzy matching;
- never execute ambiguous noun resolution;
- never guess an unavailable canonical action;
- expose resolved canonical action in inspectable debug/client state.

Ambiguity is non-mutating:

```text
> inspect door

Which door?
1. east airlock
2. maintenance hatch
```

Clarification state is session-local, bounded, and invalidated when the relevant observation materially changes.

Unknown command UX:

```text
> pry crane

You cannot pry the crane open.
Try: inspect crane · repair crane
```

Suggestions must derive from actual current affordances/parser knowledge only.

Structured agents remain unchanged and submit canonical actions directly.

## Feature B — Canonical room presentation grammar

Normative human room order:

```text
ROOM NAME
DESCRIPTION
PRESSURE        optional and observable only
HERE            visible Players/entities
EXITS           observable exits
HAPPENED        latest Player-relevant consequence
COMMAND         input
```

Room prose should encode when supported:

```text
IDENTITY      what distinguishes the place
PRESSURE      what is strained/changing/scarce/blocked
AFFORDANCE    concrete things/beings worth acting on
```

The presentation layer must not invent unsupported claims.

HERE:
- names before type enums;
- Players/actionable entities before metadata;
- no hidden entities;
- concise first paint;
- deterministic ordering.

EXITS:
- `direction — known destination name` when observable/known;
- do not reveal unknown graph knowledge.

HAPPENED:
- concise, world-native consequence;
- protocol/event/sequence IDs not required for comprehension.

## Feature C — Contextual action discovery and HELP

Default first-paint actions: max 3, observation-derived.

Preference order:
1. concrete action on strained/relevant local entity;
2. movement through obvious exit;
3. social action with a present Player when meaningful;
4. WAIT fallback.

Prefer contextual phrasing:

```text
inspect the crane
walk east
speak to Rhea
```

while mapping deterministically to existing canonical actions.

HELP hierarchy:
- `help`
- `help <known topic>`
- `help all`

Default `help` is contextual and concise. `help all` is explicit deeper disclosure. HELP is zero-cost and non-mutating.

## Feature D — Environmental history and asynchronous Player traces

Deep Time becomes visible inside PLAY as sourced environmental residue.

Allowed families:
- repair/construction marks;
- public notices;
- organization insignia;
- inherited/abandoned artifacts;
- public trade offers and claims;
- route closures/openings;
- institutional changes;
- scars;
- memorial/succession records;
- public rumor fragments when provenance permits;
- authorized public boards/messages.

Every trace requires:
- direct canonical event source; or
- durable canonical state source; or
- explicitly derived projection retaining source references.

No decorative history invented by UI.

Example:

```text
The gantry bears a fresh weld over an older fracture.
A maintenance plate names Sable as the last repairer.
```

Do not add a canonical `HISTORY` verb solely for UI convenience; reuse existing INSPECT/archive/reconstruction surfaces unless action change control approves otherwise.

## Feature E — Player aliases and bounded macros

Human Controllers may define preference-layer aliases:

```text
alias x inspect
alias dock move south
```

Aliases:
- are not world truth;
- do not bypass auth, costs, action semantics, or affordances;
- do not override reserved admin/security commands.

Macros, if implemented:
- have a maximum step count;
- execute sequentially;
- authenticate/authorize/cost/settle each step independently;
- stop on ambiguity, failure, world-blocked state, auth failure, or observation invalidation;
- imply no atomic multi-action transaction;
- perform no hidden retries;
- remain auditable as individual canonical actions.

## Feature F — Screen-reader / low-noise text mode

Provide a first-class accessibility preference that:
- removes decorative glyph repetition;
- expands important glyph meaning into short text;
- suppresses non-essential ambient repetition;
- renders exits explicitly as text;
- avoids topology-canvas dependence;
- preserves all actionable information;
- bounds live-region announcements;
- respects reduced motion;
- never changes world semantics.

## Feature G — WATCH narrative hierarchy

WATCH remains a public projection, not the world.

Three readable timescales:

```text
NOW
most important current action/change

RECENTLY
small bounded recent public set

WORLD
slow state: cycle, active Players, notable site pressure, major condition
```

Bounded causal chains are permitted only when causality is explicit in canonical events/state.

```text
CRANE FAILURE
↓
Dock throughput fell
↓
Rhea arrived
↓
repair underway
```

Temporal proximity alone is not causality.

## Feature H — Homepage live-world proof

Home may show a compact WATCH-safe proof of persistence:

```text
PERIHELION REACH

The Dock Ring lost relay power 4 minutes ago.
3 Players are there.

Rhea repaired the east crane.
Orin entered the Exchange.
A public notice appeared at Waystation Nine.
```

Rules:
- public WATCH-safe projection only;
- bounded lines;
- no private LOOK/MESSAGE leakage;
- no research metrics;
- no runtime IDs on first read;
- useful fallback when live data is unavailable;
- hero art remains context, not the only evidence of a living world.

## Non-goals

Do not add:
- graphical minimap as primary navigation;
- portraits;
- quest markers;
- MMO hotbars;
- combat HUD;
- permanent five-resource meters on first paint;
- class/XP tree;
- procedural LLM room prose;
- LLM parser;
- second agent command language;
- room-count inflation;
- authored quest narrator;
- canonical verbs solely for UI convenience.

Prefer systemic density over room count.

## Security/privacy requirements

1. Fuzzy noun resolution respects observation/redaction boundaries.
2. Suggestions never reveal hidden entities, private messages, research-private metadata, or admin capabilities.
3. Alias/macro storage is scoped preference data.
4. Macros do not bypass rate limits, costs, action admission, settlement fences, or session ownership.
5. WATCH/home traces use only public projection data.
6. Player-authored trace text follows source-surface sanitization/output escaping.
7. Parser convenience cannot reach ADMIN/RESEARCHER privileges.

## Acceptance criteria

### Parser
1. `e`, `east`, `go east`, `walk east`, `move east` converge on one legal canonical MOVE.
2. Equivalent inspect phrasing converges on one canonical INSPECT target.
3. Ambiguous target produces non-mutating clarification.
4. Hidden entities never appear in candidates/suggestions.
5. Unknown verbs do not mutate world state.
6. Structured agent protocol is unchanged.

### Room grammar
7. Player can identify room, visible entities, and exits without debug metadata.
8. Default paint does not require internal IDs, sequence, controller, settlement, or research labels.
9. Last chosen consequence is understandable without event code.
10. Equivalent observations render stable ordering.

### Discovery/help
11. Local suggestions are bounded and observation-derived.
12. `help` is concise; `help all` is explicit deeper disclosure.
13. HELP is non-mutating and zero-cost.
14. Context controls never invent verbs.

### World presence
15. At least one canonical event family leaves a visible trace after the originating Player departs.
16. Every historical trace resolves to canonical source references.
17. Invalid/stale traces update or disappear deterministically.

### Aliases/macros
18. Alias expansion is deterministic and scoped.
19. Macro steps settle as ordinary actions.
20. Macros stop safely on ambiguity/failure/world-blocked.

### Accessibility
21. Low-noise mode preserves all actionable room information.
22. No required action depends on color, glyph shape, motion, or canvas.

### WATCH/home
23. WATCH presents NOW/RECENTLY/WORLD without private leakage.
24. Causal chains appear only with explicit causal support.
25. Home degrades cleanly when live data is unavailable.

## Rollout slices

```text
S0 parser normalization + deterministic resolver
S1 canonical room grammar
S2 contextual HELP + ambiguity UX
S3 environmental traces
S4 aliases + bounded macros
S5 accessibility low-noise mode
S6 WATCH narrative hierarchy
S7 homepage live-world proof
```

Each slice requires tests, canonical-action conformance, redaction/security checks, desktop/mobile QA where applicable, agent-protocol regression tests, and no Genesis/reseed.

## Definition of done

A new human can enter a room, understand it, express ordinary intent naturally, act through existing canonical mechanics, see the consequence, and encounter durable evidence of other Players — while an agent Controller continues using the same structured canonical world with no parser dependency.

> The Player perceives a place and its history before they perceive the runtime that produced it.
