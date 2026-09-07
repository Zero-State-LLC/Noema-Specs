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
trade-notice cycle expiry is [GC5-S13-TRADE-NOTICE-EXPIRY.md](GC5-S13-TRADE-NOTICE-EXPIRY.md)
MESSAGE_EXPIRED
Chamber help board
WATCH ticker
```

---

## Runtime rule

Hosted Chamber MUST drop public-room board notices after 1 committed cycle, keep last-5 overwrite in the posting cycle, and reject hidden-room board. Isolated tests only. Help unchanged. No Genesis change.

## Extension Points

Non-normative guidance; this section does not change the accepted contract or claim runtime completion.

### Board expiry boundary cases

Extend board retention/expiry conformance traces across committed-cycle boundaries.

### Preserved invariants

S10 keeps last 5 notices in the posting cycle and silently removes them after 1 committed cycle. Hidden-room board is rejected; WATCH and help remain unchanged.

### Compatibility and promotion

RFC-0081 owns S10 expiry. Keep the earlier S3 last-3 contract version-distinct rather than rewriting its historical threshold. Any duration or retention change needs an Accepted RFC/catalog revision.

### Validation fixtures before adoption

Post six notices during one cycle: only the newest five remain. Advance wall time without committing: expiry must not follow wall time. Commit the next cycle: no board lines remain and no MESSAGE_EXPIRED event or WATCH ticker appears. Include hidden-room rejection.
