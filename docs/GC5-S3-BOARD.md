# GC5-S3 — MESSAGE board surface

**Status:** Executable specification. Runtime authorized with RFC-0054.  
**Parent:** [GC5-S2-RUMOR.md](GC5-S2-RUMOR.md) · [COMMUNICATION-ECOLOGY.md](COMMUNICATION-ECOLOGY.md)  
**Next:** [GC5-S4-SHOUT.md](GC5-S4-SHOUT.md) · [GC5-S5-RETENTION.md](GC5-S5-RETENTION.md)  
**RFC:** [RFC-0054](../rfcs/RFC-0054-message-board.md)  
**Does not open:** BOARD/SHOUT verbs · rumor score · help advertising · hidden boards

S3 adds one MESSAGE surface. A board notice stays in the public room. It is not a shout verb.

---

## Doctrine decisions

| Temptation | Verdict |
|------------|---------|
| BOARD / SHOUT verb | **REJECT.** |
| Long-range board | **REJECT.** |
| Hidden-room board | **REJECT.** |
| WATCH ticker | **REJECT.** |
| Help board | **REJECT.** |

---

## Slice contract

| Field | Value |
|-------|--------|
| Slice id | `gc5-s3` |
| Catalog | `communication-catalog/gc5-s3` |
| Verb | existing `MESSAGE` |
| Surface | `BOARD` only |
| Place | current public room |
| Cost | compute 1 |
| Keep | last 3 notices |
| Events | `MESSAGE` only |
| PLAY | `A notice on the board: {text}.` |
| WATCH | silent |
| Help | still omits board / SHOUT |

---

## Out of S3

```text
SHOUT verb
long-range board
WATCH ticker
Chamber help board
```

---

## Runtime rule

Hosted Chamber MUST accept `MESSAGE surface=BOARD` in a public room and keep the last 3 notices for PLAY. Isolated tests only. Help unchanged. No Genesis change.

## Extension Points

Non-normative guidance; this section does not change the accepted contract or claim runtime completion.

### Board surface conformance

Extend public-room MESSAGE board examples and presentation tests without adding a BOARD command.

### Preserved invariants

The S3 baseline costs compute 1 and retains last 3 notices in the current public room. Hidden and long-range boards are excluded; WATCH remains silent and help omits board/SHOUT.

### Compatibility and promotion

RFC-0054 remains the S3 baseline. Later retention and expiry slices must be tested under their own catalog versions, not backported into this table. Changed cost, reach or wire behavior requires Accepted authority.

### Validation fixtures before adoption

Under S3, post four notices and assert only the newest three are shown with the existing board line. Compare public-room success with hidden-room and remote-room refusal; verify no new event type, help entry or WATCH projection.
