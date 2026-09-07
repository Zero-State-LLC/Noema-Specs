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
trade-notice cycle expiry is [GC5-S13-TRADE-NOTICE-EXPIRY.md](GC5-S13-TRADE-NOTICE-EXPIRY.md)
MESSAGE_EXPIRED
Chamber help NOTICE
WATCH ticker
```

---

## Runtime rule

Hosted Chamber MUST drop a public-room institution notice after 1 committed cycle, keep last-1 overwrite, and reject hidden-room notice. Isolated tests only. Help unchanged. No Genesis change.

## Extension Points

Non-normative maintenance and integration guidance; the contracts cited above remain authoritative.

### Document-specific seam

Extend notice projection tests around last-1 overwrite and removal after one committed cycle. A viewer should recompute from the committed head, not preserve an expired notice because a browser timer or cache has not refreshed.

### Compatibility and promotion

RFC-0082 is NOTICE-only under MESSAGE; no MESSAGE_EXPIRED event, NOTICE verb, help advertising, or WATCH ticker is introduced. CHANNEL and TRADE_NOTICE expiry belong to their accepted successor slices. World time, not elapsed wall-clock time, determines this boundary.

### Verification before adoption

Compare the visible notice before and after the next commit, overwrite twice within the valid window, and restart at expiry. Confirm hidden-room notice rejection, last-1 behavior, and no expiry event. A translated or accessible empty state must not quote expired/private content or imply deletion of canonical message history.
