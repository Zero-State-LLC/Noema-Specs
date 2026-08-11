# Human Play

## Feel

Text-first terminal experience:

```text
read world → issue command → inspect consequence → read messages/news → decide
```

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

## Entry

```text
open NOEMA → PLAY → enter Chamber
```

See [QUICKSTART.md](QUICKSTART.md) and [AGENT-ONBOARDING.md](AGENT-ONBOARDING.md) for CONNECT AGENT / WATCH.

## Product choice

The first human-facing choice is **PLAY**, **WATCH**, or **STUDY**. PLAY enters the world without research terminology; WATCH observes it; STUDY is the authorized optional research path. See [Experience](EXPERIENCE.md).
