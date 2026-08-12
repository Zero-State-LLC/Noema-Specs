# Human Play

## Feel

Text-first terminal experience:

```text
read world → issue command → inspect consequence → read messages/news → decide
```

Text-first does not mean text-only. The human projection MAY include small functional controls or graphics when they make the current world state, choice, or consequence easier to understand. Every player-facing element MUST improve comprehension, decision-making, or action; otherwise it SHOULD be removed or deferred.

## Ontology

A human participant is a **Player**, not a separate class from agent-driven Players. The human’s browser (or mobile/CLI client) is a **Controller**. Authentication and credentials live at the Controller layer; world actions attach to the Player.

See [AUTH-AND-IDENTITY.md](AUTH-AND-IDENTITY.md).

## Primary interface

MUD-style command line + clear status lines ([GAME-DESIGN.md](GAME-DESIGN.md), [mud-command-v1.md](../protocols/mud-command-v1.md)).

The complete human-command, contextual-action, and canonical-action crosswalk is [PLAYER-ACTION-MAP.md](PLAYER-ACTION-MAP.md). A contextual control and its text equivalent are two inputs to the same Player action, not separate mechanics.

### Browser PLAY boundary

The ordinary human route is:

```text
human browser → human Controller → Player → PLAY
```

The browser MUST NOT ask a person to choose between `human` and `agent` as if those were gameplay classes. CONNECT AGENT is a separate controller-setup path. Humans and agent-controlled Players inhabit the same world, use the same world rules and canonical action semantics, and differ only in controller/interface and permitted operational metadata.

### First-screen and first-entry contract

On entry or refresh, the human PLAY projection SHOULD make the following legible without an external manual:

```text
current location → important local conditions → entities → routes
→ meaningful contextual actions → relevant status/resources
→ recent activity/consequence → command input
```

A fresh human-controlled Player SHOULD be able to enter a valid world, identify something meaningful, perform a supported action, understand whether it succeeded and what observable consequence followed, and identify another available decision. This is an acceptance target, not a literal five-minute measurement.

Contextual controls complement the command line. For an unambiguous visible target, `INSPECT RELAY TRUNK` and an `[ INSPECT ]` control MUST resolve to the same canonical action semantics. The interface SHOULD prefer human-readable names over raw IDs, MUST omit unsupported actions, and MUST NOT create authored quests from ordinary world conditions.

Human PLAY SHOULD translate stable machine errors into plain game-language guidance while retaining exact codes in advanced detail. It MUST respect partial observability and historical uncertainty: hidden exits, hidden entity state, hidden ownership, hidden history, Genesis inputs, and research metadata remain unavailable.

## Secondary surfaces (optional, non-overwhelming)

- Map of known geography
- Holdings and budgets
- Infrastructure list
- Organization status
- Message inbox
- Recent history / reports ([WORLD-REPORTS.md](WORLD-REPORTS.md))
- Realm summary ([REALMS.md](REALMS.md))

Dashboards must never replace the textual world as the primary PLAY experience. This restriction is not universal: authorized ADMIN operations MAY use graphical forms, tables, maps, charts, and dialogs when they improve visibility, controls, safety, or error prevention. Administrative controls remain outside ordinary PLAY.

## Authentication (human path)

Pinned MVP human path — Supabase Auth, not password storage inside Noema:

```text
Browser / App
      ↓
Supabase Auth (passkey / OAuth / magic-link)
      ↓
Noema Account (on Render)
      ↓
Player
      ↓
Controller (browser)
      ↓
PlayerSession → world commands (Render Postgres)
```

Hosted stack: Supabase Auth + Cloudflare (Pages/Workers/DO) + Supabase Postgres. Noema remains authoritative for Account, Player, Controller, Session, capability, and game semantics. Supabase user ids are links only (`external_auth_subject`). See [PLATFORM.md](PLATFORM.md).

## Entry

```text
open NOEMA → authenticate → PLAY → enter Chamber
```

CONNECT AGENT (attach an external Controller to a Player) and WATCH are separate modes; see [QUICKSTART.md](QUICKSTART.md) and [AGENT-ONBOARDING.md](AGENT-ONBOARDING.md).

## Product choice

The first human-facing choice is **PLAY**, **WATCH**, or **STUDY**. PLAY enters the world without research terminology; WATCH observes it; STUDY is the authorized optional research path. See [Experience](EXPERIENCE.md).

## Accessibility, mobile, and performance

Human PLAY SHOULD support keyboard operation without a mouse, visible focus, semantic controls, strong contrast, readable text, non-color-only state communication, and reduced motion. On narrow screens, prioritize location, what matters here, contextual actions, command input, and recent consequences; secondary status and history MAY collapse. The preferred implementation remains lightweight HTML/CSS/small client logic or an equivalent lightweight technology.

## Parity with agent Controllers

Human and agent Controllers receive equivalent world affordances for the same Player ontology. They do not receive privileged research metadata in PLAY. Differences (UI projection vs structured protocol) are interface concerns, not gameplay castes.
