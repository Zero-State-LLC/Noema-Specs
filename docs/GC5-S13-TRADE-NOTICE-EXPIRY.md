# GC5-S13 — trade-notice cycle expiry

**Status:** Executable specification. Runtime authorized with RFC-0084.  
**Parent:** [GC5-S8-TRADE-NOTICE.md](GC5-S8-TRADE-NOTICE.md) · [GC5-S12-CHANNEL-EXPIRY.md](GC5-S12-CHANNEL-EXPIRY.md) · [COMMUNICATION-ECOLOGY.md](COMMUNICATION-ECOLOGY.md)  
**RFC:** [RFC-0084](../rfcs/RFC-0084-trade-notice-expiry.md)  
**Does not open:** MARKET/TRADE_NOTICE verb · auto-TRADE · MESSAGE_EXPIRED · help advertising · WATCH ticker  
**Next:** fourth-and-later co-owners

S13 makes a public stall note take world-time. A trade notice is still last 1, then gone after one committed cycle.

---

## Doctrine decisions

| Temptation | Verdict |
|------------|---------|
| Duration ≠ 1 | **REJECT.** |
| `MESSAGE_EXPIRED` | **REJECT.** Silent drop |
| MARKET / TRADE_NOTICE verb | **REJECT.** |
| Auto-open TRADE | **REJECT.** |
| Help market | **REJECT.** |
| WATCH ticker | **REJECT.** |

---

## Slice contract

| Field | Value |
|-------|--------|
| Slice id | `gc5-s13` |
| Catalog | `communication-catalog/gc5-s13` |
| Verb | existing `MESSAGE` |
| Surface | `TRADE_NOTICE` |
| Keep | last 1 trade notice |
| Expire | 1 committed cycle |
| Events | existing `MESSAGE` only |
| PLAY | trade-notice line absent after expiry |
| WATCH | silent |
| Help | still omits market / TRADE_NOTICE |

---

## Out of S13

```text
MARKET / TRADE_NOTICE verb
auto-open TRADE
MESSAGE_EXPIRED
Chamber help market
WATCH ticker
```

---

## Runtime rule

Hosted Chamber MUST drop a public-room trade notice after 1 committed cycle, keep last-1 overwrite, and reject hidden-room stall. Isolated tests only. Help unchanged. No Genesis change.
