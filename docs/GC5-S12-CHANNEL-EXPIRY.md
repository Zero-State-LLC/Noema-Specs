# GC5-S12 — channel cycle expiry

**Status:** Executable specification. Runtime authorized with RFC-0083.  
**Parent:** [GC5-S7-CHANNEL.md](GC5-S7-CHANNEL.md) · [GC5-S11-NOTICE-EXPIRY.md](GC5-S11-NOTICE-EXPIRY.md) · [COMMUNICATION-ECOLOGY.md](COMMUNICATION-ECOLOGY.md)  
**RFC:** [RFC-0083](../rfcs/RFC-0083-channel-expiry.md)  
**Does not open:** CHANNEL verb · TRADE_NOTICE expiry · MESSAGE_EXPIRED · help advertising · WATCH ticker · membership leak  
**Next:** [GC5-S13-TRADE-NOTICE-EXPIRY.md](GC5-S13-TRADE-NOTICE-EXPIRY.md)

S12 makes an org channel note take world-time. A member note is still last 1, then gone after one committed cycle.

---

## Doctrine decisions

| Temptation | Verdict |
|------------|---------|
| TRADE_NOTICE in this slice | **REJECT.** Channel only |
| Duration ≠ 1 | **REJECT.** |
| `MESSAGE_EXPIRED` | **REJECT.** Silent drop |
| CHANNEL verb | **REJECT.** |
| Distinct outsider fail | **REJECT.** Same `NOT_ADDRESSABLE` |
| Help CHANNEL | **REJECT.** |
| WATCH ticker | **REJECT.** |

---

## Slice contract

| Field | Value |
|-------|--------|
| Slice id | `gc5-s12` |
| Catalog | `communication-catalog/gc5-s12` |
| Verb | existing `MESSAGE` |
| Surface | `CHANNEL` |
| Keep | last 1 note per org |
| Expire | 1 committed cycle |
| Events | existing `MESSAGE` only |
| PLAY | channel line absent after expiry |
| Fail | `NOT_ADDRESSABLE` for unknown / non-member |
| WATCH | silent |
| Help | still omits CHANNEL |

---

## Out of S12

```text
CHANNEL verb
trade-notice cycle expiry is [GC5-S13-TRADE-NOTICE-EXPIRY.md](GC5-S13-TRADE-NOTICE-EXPIRY.md)
MESSAGE_EXPIRED
Chamber help CHANNEL
WATCH ticker
membership leak
```

---

## Runtime rule

Hosted Chamber MUST drop an org channel note after 1 committed cycle, keep last-1 overwrite, reject hidden-room send, and use one non-leaking fail for unknown org and non-member. Isolated tests only. Help unchanged. No Genesis change.
