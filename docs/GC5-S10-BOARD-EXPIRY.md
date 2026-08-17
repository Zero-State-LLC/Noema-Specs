# GC5-S10 — board cycle expiry

**Status:** Executable specification. Runtime authorized with RFC-0081.  
**Parent:** [GC5-S5-RETENTION.md](GC5-S5-RETENTION.md) · [GC5-S9-SHOUT-EXPIRY.md](GC5-S9-SHOUT-EXPIRY.md) · [COMMUNICATION-ECOLOGY.md](COMMUNICATION-ECOLOGY.md)  
**RFC:** [RFC-0081](../rfcs/RFC-0081-board-expiry.md)  
**Does not open:** BOARD verb · NOTICE/CHANNEL/TRADE_NOTICE expiry · MESSAGE_EXPIRED · help advertising · WATCH ticker  
**Next:** [GC5-S11-NOTICE-EXPIRY.md](GC5-S11-NOTICE-EXPIRY.md)

S10 makes board notices take world-time. A public board is still last 5, then those notices are gone after one committed cycle.

---

## Doctrine decisions

| Temptation | Verdict |
|------------|---------|
| All remaining surfaces | **REJECT.** Board only |
| Duration ≠ 1 | **REJECT.** |
| `MESSAGE_EXPIRED` | **REJECT.** Silent drop |
| BOARD verb | **REJECT.** |
| Help board | **REJECT.** |
| WATCH ticker | **REJECT.** |

---

## Slice contract

| Field | Value |
|-------|--------|
| Slice id | `gc5-s10` |
| Catalog | `communication-catalog/gc5-s10` |
| Verb | existing `MESSAGE` |
| Surface | `BOARD` |
| Keep | last 5 notices |
| Expire | 1 committed cycle |
| Events | existing `MESSAGE` only |
| PLAY | board lines absent after expiry |
| WATCH | silent |
| Help | still omits board / SHOUT |

---

## Out of S10

```text
BOARD verb
notice cycle expiry is [GC5-S11-NOTICE-EXPIRY.md](GC5-S11-NOTICE-EXPIRY.md)
channel cycle expiry is [GC5-S12-CHANNEL-EXPIRY.md](GC5-S12-CHANNEL-EXPIRY.md)
TRADE_NOTICE expiry
MESSAGE_EXPIRED
Chamber help board
WATCH ticker
```

---

## Runtime rule

Hosted Chamber MUST drop public-room board notices after 1 committed cycle, keep last-5 overwrite in the posting cycle, and reject hidden-room board. Isolated tests only. Help unchanged. No Genesis change.
