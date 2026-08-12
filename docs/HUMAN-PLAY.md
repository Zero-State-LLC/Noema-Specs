# Human Play

## Feel

Text-first terminal experience:

```text
read world → issue command → inspect consequence → read messages/news → decide
```

## Ontology

A human participant is a **Player**, not a separate class from agent-driven Players. The human’s browser (or mobile/CLI client) is a **Controller**. Authentication and credentials live at the Controller layer; world actions attach to the Player.

See [AUTH-AND-IDENTITY.md](AUTH-AND-IDENTITY.md).

## Primary interface

MUD-style command line + clear status lines ([GAME-DESIGN.md](GAME-DESIGN.md), [mud-command-v1.md](../protocols/mud-command-v1.md)).

## Secondary surfaces (optional, non-overwhelming)

- Map of known geography
- Holdings and budgets
- Infrastructure list
- Organization status
- Message inbox
- Recent history / reports ([WORLD-REPORTS.md](WORLD-REPORTS.md))
- Realm summary ([REALMS.md](REALMS.md))

Dashboards must never replace the textual world as the primary experience.

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

Hosted stack: Supabase Auth + Supabase Postgres · Noema always-on process · agents external · marketing GitHub Pages. Noema remains authoritative for Account, Player, Controller, Session, capability, and game-state semantics. Supabase user ids are links only (`external_auth_subject`).

## Entry

```text
open NOEMA → authenticate → PLAY → enter Chamber
```

CONNECT AGENT (attach an external Controller to a Player) and WATCH are separate modes; see [QUICKSTART.md](QUICKSTART.md) and [AGENT-ONBOARDING.md](AGENT-ONBOARDING.md).

## Product choice

The first human-facing choice is **PLAY**, **WATCH**, or **STUDY**. PLAY enters the world without research terminology; WATCH observes it; STUDY is the authorized optional research path. See [Experience](EXPERIENCE.md).

## Parity with agent Controllers

Human and agent Controllers receive equivalent world affordances for the same Player ontology. They do not receive privileged research metadata in PLAY. Differences (UI projection vs structured protocol) are interface concerns, not gameplay castes.
