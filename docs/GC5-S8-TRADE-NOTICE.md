# GC5-S8 — MESSAGE trade notice

**Status:** Executable specification. Runtime authorized with RFC-0066.  
**Parent:** [GC5-S7-CHANNEL.md](GC5-S7-CHANNEL.md) · [COMMUNICATION-ECOLOGY.md](COMMUNICATION-ECOLOGY.md)  
**RFC:** [RFC-0066](../rfcs/RFC-0066-trade-notice.md)  
**Does not open:** MARKET/TRADE_NOTICE verbs · auto-TRADE · price oracle · help advertising · hidden stalls · cycle expiry  
**Next:** cycle expiry is [GC5-S13-TRADE-NOTICE-EXPIRY.md](GC5-S13-TRADE-NOTICE-EXPIRY.md)

S8 adds one MESSAGE surface. A trade notice is heard in the public room. It is not a trade verb.

---

## Doctrine decisions

| Temptation | Verdict |
|------------|---------|
| MARKET / TRADE_NOTICE verb | **REJECT.** |
| Auto-open TRADE | **REJECT.** |
| Certified prices | **REJECT.** |
| Long-range stall | **REJECT.** |
| Hidden-room stall | **REJECT.** |
| WATCH ticker | **REJECT.** |
| Help market | **REJECT.** |

---

## Slice contract

| Field | Value |
|-------|--------|
| Slice id | `gc5-s8` |
| Catalog | `communication-catalog/gc5-s8` |
| Verb | existing `MESSAGE` |
| Surface | `TRADE_NOTICE` only |
| Place | current public room |
| Cost | compute 1 |
| Keep | last 1 trade notice |
| Events | `MESSAGE` only |
| PLAY | `A trade notice: {text}.` |
| WATCH | silent |
| Help | still omits market / TRADE_NOTICE |

---

## Out of S8

```text
MARKET / TRADE_NOTICE verb
auto-open TRADE
price oracle
WATCH ticker
Chamber help market
cycle expiry is [GC5-S13-TRADE-NOTICE-EXPIRY.md](GC5-S13-TRADE-NOTICE-EXPIRY.md)
```

---

## Runtime rule

Hosted Chamber MUST accept `MESSAGE surface=TRADE_NOTICE` in a public room and keep the last 1 trade notice for PLAY. Hidden rooms reject. Isolated tests only. Help unchanged. No Genesis change.
