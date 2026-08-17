# HUMAN-ORIENTATION-S0 — First-screen withhold

**Status:** Executable specification. Runtime authorized with RFC-0109.  
**Depends on:** [PLAYER-ONBOARDING.md](PLAYER-ONBOARDING.md) · [HOSTED-FIRST-ENTRY.md](HOSTED-FIRST-ENTRY.md) · [AGENT-ORIENTATION-S2.md](AGENT-ORIENTATION-S2.md)  
**RFC:** [RFC-0109](../rfcs/RFC-0109-human-orientation.md)  
**Does not open:** invented quests · tutorial room · arrival speech · WED / ATTEST help

S0 pins the **human first read**. The world door and first Chamber chrome MUST NOT brief a win. Place and available action stay visible. Meaning still comes from the live room.

---

## Doctrine decisions

| Temptation | Verdict |
|------------|---------|
| Door names the place | **ACCEPT.** |
| Thesis / win / “you should…” on first read | **REJECT.** Same withhold as agents |
| Tutorial room or fabricated quest | **REJECT.** |
| Human vs agent class picker | **REJECT.** |
| CONNECT as a first-time fork | **REJECT.** Secondary only |

---

## Slice contract

| Field | Value |
|-------|--------|
| Slice id | `human-orientation-s0` |
| Catalog | `human-orientation-catalog/s0` |
| Surfaces | `/` door · signed-out `/play` · `/play/callback` · first Chamber chrome |
| Must remain answerable | Where am I? What can I do here? |
| Forbidden | Win, point of the game, class, “you should…”, research objective, “being tested”, arrival speech, persistence lecture |
| New verbs / events | none |
| Help | Unchanged (still no WED / ATTEST) |

Live `situation` on LOOK is already S1. This slice is chrome and door copy only.

---

## Runtime rule

Hosted first-read HTML for `/`, signed-out `/play`, `/play/callback`, and Chamber chrome MUST pass the same thesis withhold as agent first `OBSERVE`. Isolated tests scan those surfaces. No Genesis change.
