# Player Onboarding

**Authority.** First-world path from authentication to a first meaningful action and visible consequence.

This document does not replace [PLAY.md](PLAY.md), [HUMAN-PLAY.md](HUMAN-PLAY.md), [AGENT-ONBOARDING.md](AGENT-ONBOARDING.md), [PLAYER-ACTION-MAP.md](PLAYER-ACTION-MAP.md), or [PLAYER-LIFECYCLE.md](PLAYER-LIFECYCLE.md). It settles the **minimum** Perihelion Reach entry path.

Related: [QUICKSTART.md](QUICKSTART.md) · [COMMAND-DISCOVERY.md](COMMAND-DISCOVERY.md) · [AUTH-AND-IDENTITY.md](AUTH-AND-IDENTITY.md) · [EXPERIENCE.md](EXPERIENCE.md) · [HOSTED-FIRST-ENTRY.md](HOSTED-FIRST-ENTRY.md) · [FIRST-WORLD-OPERATIONS.md](FIRST-WORLD-OPERATIONS.md).

---

## First-player path

```text
authenticate
  ↓
create/select Player
  ↓
enter world
  ↓
orient
  ↓
see WHAT MATTERS HERE
  ↓
see AVAILABLE HERE
  ↓
perform first meaningful action
  ↓
see consequence
  ↓
continue
```

No tutorial wall. No research-stack lecture. No Genesis controls.

Fantasy sequence (the session should *feel* like this):

```text
enter world
  → establish identity
  → understand immediate situation
  → take an action
  → observe consequence
  → encounter another player, institution, or signal
  → discover deeper systems progressively
```

Legal auth, consent, and data policy remain required where applicable. They are structurally separate from the game fantasy ([PLAYER-BRAND.md](PLAYER-BRAND.md)).

This is a usability acceptance target, not a literal timer ([PLAY.md](PLAY.md), [EXPERIENCE.md](EXPERIENCE.md)).

---

## Human onboarding

Minimum browser flow:

```text
open NOEMA
  → world door (Perihelion Reach + Player email)
  → request Player email link
  → managed auth callback
  → create or reuse Player (choose handle)
  → enter Perihelion Reach
  → first screen
  → AVAILABLE HERE + command input
```

WATCH and CONNECT MAY appear as secondary links. STUDY MUST NOT be a first-time fork. Hosted presentation: [HOSTED-FIRST-ENTRY.md](HOSTED-FIRST-ENTRY.md).

A new human-controlled Player MUST NOT need to understand:

```text
controller IDs
PlayerPrincipal
protocols
Genesis
research stack
settlement
```

They SHOULD understand:

```text
identity
world
location
actions
consequences
```

### First screen

On entry or refresh, the human projection SHOULD make these answers obvious:

```text
WHERE AM I?
WHAT IS HERE?
WHAT MATTERS HERE?
WHAT CAN I DO?
WHAT JUST HAPPENED?
```

Information priority remains [PLAY.md](PLAY.md): location, local significance, entities, routes, contextual actions, relevant status, recent activity, command input.

For Perihelion Reach, first entry is the approved world's entry location (rehearsal: Grid Anchor). Do not invent a tutorial room.

The browser MUST NOT ask the person to choose `human` vs `agent` as gameplay classes. CONNECT is a separate controller-setup path linked from product entry and optionally from PLAY; it is not a gameplay class.

### What the first action may be

Any supported, available action is valid. Typical first-world first actions are `LOOK`, `INSPECT`, or `MOVE` when those affordances are actually available. The interface MUST NOT fabricate a quest or mark an action available if the deployment cannot execute it.

After the action, show the action, success or failure, and observable consequence in plain language. Exact codes stay in advanced detail.

---

## Agent onboarding

Minimum agent-controller flow:

```text
enroll controller
  → receive credential
  → discover protocol / capabilities
  → connect
  → receive observation
  → submit action
  → resume
```

Canonical protocol path remains [AGENT-ONBOARDING.md](AGENT-ONBOARDING.md):

```text
device enrollment (or issued credential)
  → HELLO → AUTH → REGISTER → ENTER_WORLD → OBSERVE → ACT
```

An agent operator MUST be able to complete that path without parsing the human command grammar. Structured actions use Agent Protocol v1 and [`agent-action/1.0`](../specs/agent-action.schema.json).

Capability advertisement and `AVAILABLE_ACTIONS` are the agent discovery surface. Human `help` text is not required.

Agents MUST NOT receive human browser passwords or sessions. Private prompts are never required.

---

## Player naming

Settled in [PLAYER-LIFECYCLE.md](PLAYER-LIFECYCLE.md):

- Humans choose a unique `handle` at first Player creation.
- `display_name` MAY default to that handle.
- Ordinary surfaces show the public name, not `player_id`.
- Collision is visible and retryable.
- Rename is not required for first-world go-live.

Do not ask a new human to name Controllers, credentials, or sessions.

---

## Command discovery

Canonical first-world discovery contract: [COMMAND-DISCOVERY.md](COMMAND-DISCOVERY.md). Verb catalog: [PLAYER-ACTION-MAP.md](PLAYER-ACTION-MAP.md).

---

## Surfaces the new Player should not see

Ordinary first-world onboarding MUST NOT expose:

- Genesis Profile, Story Seeds, world seed, Cycle 0 acceptance;
- Admin Live;
- Lab / Compiler / LEARN internals;
- controller and session IDs as required fields;
- research claim labels as gameplay UI.

WATCH and STUDY remain available as **separate** entry choices, not steps in the PLAY tutorial. Research-participation disclosure, if legally required, is a separate sheet — not the first-read identity.

---

## Acceptance

1. A new human can authenticate, name a Player, enter, see `AVAILABLE HERE`, act, and understand the consequence without reading this repository.
2. An agent operator can enroll, authenticate, connect, observe, act, and resume on the structured protocol.
3. First help does not dump the entire verb list.
4. No tutorial wall, no GM_PLAYER, no Genesis controls on PLAY.

---

## Non-goals

- Scripted quests
- Character-creation stats
- A second human command language
- Requiring agents to parse MUD grammar
- Multi-world world-picker UX (first world is Perihelion Reach)
