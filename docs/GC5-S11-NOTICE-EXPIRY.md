# GC5-S11 — notice cycle expiry

**Status:** Executable specification. Runtime authorized with RFC-0082.  
**Parent:** [GC5-S6-NOTICE.md](GC5-S6-NOTICE.md) · [GC5-S10-BOARD-EXPIRY.md](GC5-S10-BOARD-EXPIRY.md) · [COMMUNICATION-ECOLOGY.md](COMMUNICATION-ECOLOGY.md)  
**RFC:** [RFC-0082](../rfcs/RFC-0082-notice-expiry.md)  
**Does not open:** NOTICE verb · CHANNEL/TRADE_NOTICE expiry · MESSAGE_EXPIRED · help advertising · WATCH ticker  
**Next:** [GC5-S12-CHANNEL-EXPIRY.md](GC5-S12-CHANNEL-EXPIRY.md)

S11 makes an institution notice take world-time. A public notice is still last 1, then gone after one committed cycle.

---

## Doctrine decisions

| Temptation | Verdict |
|------------|---------|
| All remaining surfaces | **REJECT.** Notice only |
| Duration ≠ 1 | **REJECT.** |
| `MESSAGE_EXPIRED` | **REJECT.** Silent drop |
| NOTICE verb | **REJECT.** |
| Help NOTICE | **REJECT.** |
| WATCH ticker | **REJECT.** |

---

## Slice contract

| Field | Value |
|-------|--------|
| Slice id | `gc5-s11` |
| Catalog | `communication-catalog/gc5-s11` |
| Verb | existing `MESSAGE` |
| Surface | `NOTICE` |
| Keep | last 1 notice |
| Expire | 1 committed cycle |
| Events | existing `MESSAGE` only |
| PLAY | notice line absent after expiry |
| WATCH | silent |
| Help | still omits NOTICE |

---

## Out of S11

```text
NOTICE verb
channel cycle expiry is [GC5-S12-CHANNEL-EXPIRY.md](GC5-S12-CHANNEL-EXPIRY.md)
TRADE_NOTICE expiry
MESSAGE_EXPIRED
Chamber help NOTICE
WATCH ticker
```

---

## Runtime rule

Hosted Chamber MUST drop a public-room institution notice after 1 committed cycle, keep last-1 overwrite, and reject hidden-room notice. Isolated tests only. Help unchanged. No Genesis change.
