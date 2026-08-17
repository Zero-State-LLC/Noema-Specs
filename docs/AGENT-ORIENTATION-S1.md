# AGENT-ORIENTATION-S1 — First OBSERVE situation fields

**Status:** Executable specification. Runtime authorized with RFC-0107.  
**Depends on:** [AGENT-ORIENTATION-S0.md](AGENT-ORIENTATION-S0.md)  
**RFC:** [RFC-0107](../rfcs/RFC-0107-agent-orientation-situation.md)  
**Does not open:** CONNECT/skill thesis lock · human first-screen · arrival speech · invented strain

S1 makes **where** and **strain-if-present** first-class on the same first `OBSERVE`. It restates live room facts. It does not brief a goal.

---

## Doctrine decisions

| Temptation | Verdict |
|------------|---------|
| `situation.place` = live room name | **ACCEPT.** |
| `situation.strain` only when the room already shows strain | **ACCEPT.** |
| Quiet room omits `strain` | **ACCEPT.** |
| New thesis / “you should…” | **REJECT.** S0 still binds |
| Arrival speech | **REJECT.** |
| Invent strain | **REJECT.** |
| CONNECT/skill lock | **DEFER** (S2) |

---

## Slice contract

| Field | Value |
|-------|--------|
| Slice id | `agent-orientation-s1` |
| Catalog | `agent-orientation-catalog/s1` |
| `situation.place` | Existing `LOCATION` name |
| `situation.strain` | Existing damage/stock/report fact, or omitted |
| New verbs / events | none |
| Arrival speech | false |
| Invent strain | false |
| WATCH | no `situation` |
| Help | Unchanged (still no WED / ATTEST) |

---

## Runtime rule

Hosted first `OBSERVE` / `LOOK` MUST attach `situation.place` from the current room name. Attach `situation.strain` only from live room facts (worn infrastructure, empty stock, or an already-true public report). Isolated world `test.hosted-canonical.agent-orient-s1`. No Genesis change.
