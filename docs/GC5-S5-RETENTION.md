# GC5-S5 — MESSAGE board retention

**Status:** Executable specification. Runtime authorized with RFC-0063.  
**Parent:** [GC5-S3-BOARD.md](GC5-S3-BOARD.md) · [COMMUNICATION-ECOLOGY.md](COMMUNICATION-ECOLOGY.md)  
**RFC:** [RFC-0063](../rfcs/RFC-0063-board-retention.md)  
**Does not open:** BOARD/SHOUT verbs · cycle expiry · unlimited boards · help advertising · shout last-1 change  
**Next:** [GC5-S6-NOTICE.md](GC5-S6-NOTICE.md)

S5 widens the S3 board. A public room keeps the last 5 notices. It is not an archive.

---

## Doctrine decisions

| Temptation | Verdict |
|------------|---------|
| Unlimited board | **REJECT.** |
| Cycle expiry | **REJECT.** |
| Last 7 / last 10 | **REJECT.** Smallest step past 3 is 5. |
| Change shout last-1 | **REJECT.** |
| Help board | **REJECT.** |

---

## Slice contract

| Field | Value |
|-------|--------|
| Slice id | `gc5-s5` |
| Catalog | `communication-catalog/gc5-s5` |
| Verb | existing `MESSAGE` |
| Surface | `BOARD` (S3) |
| Place | current public room |
| Cost | compute 1 |
| Keep | last **5** notices |
| Events | `MESSAGE` only |
| PLAY | `A notice on the board: {text}.` |
| WATCH | silent |
| Help | still omits board / SHOUT |
| Shout | last 1 (S4 unchanged) |

---

## Out of S5

```text
SHOUT / BOARD verb
shout cycle expiry is [GC5-S9-SHOUT-EXPIRY.md](GC5-S9-SHOUT-EXPIRY.md)
board cycle expiry is [GC5-S10-BOARD-EXPIRY.md](GC5-S10-BOARD-EXPIRY.md)
channel cycle expiry is [GC5-S12-CHANNEL-EXPIRY.md](GC5-S12-CHANNEL-EXPIRY.md)
trade-notice cycle expiry is [GC5-S13-TRADE-NOTICE-EXPIRY.md](GC5-S13-TRADE-NOTICE-EXPIRY.md)
unlimited board
Chamber help board
```

---

## Runtime rule

Hosted Chamber MUST keep the last 5 `MESSAGE surface=BOARD` notices in a public room for PLAY. Hidden rooms still reject. Isolated tests only. Help unchanged. No Genesis change.
