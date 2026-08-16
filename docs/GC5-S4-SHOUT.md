# GC5-S4 — MESSAGE shout surface

**Status:** Executable specification. Runtime authorized with RFC-0062.  
**Parent:** [GC5-S3-BOARD.md](GC5-S3-BOARD.md) · [COMMUNICATION-ECOLOGY.md](COMMUNICATION-ECOLOGY.md)  
**RFC:** [RFC-0062](../rfcs/RFC-0062-message-shout.md)  
**Does not open:** SHOUT/BOARD verbs · long-range shout · help advertising · hidden shouts · board retention change

S4 adds one MESSAGE surface. A shout is heard in the public room. It is not a shout verb.

---

## Doctrine decisions

| Temptation | Verdict |
|------------|---------|
| SHOUT / BOARD verb | **REJECT.** |
| Long-range / adjacent shout | **REJECT.** |
| Hidden-room shout | **REJECT.** |
| WATCH ticker | **REJECT.** |
| Help shout | **REJECT.** |
| Change board last-3 | **REJECT.** |

---

## Slice contract

| Field | Value |
|-------|--------|
| Slice id | `gc5-s4` |
| Catalog | `communication-catalog/gc5-s4` |
| Verb | existing `MESSAGE` |
| Surface | `SHOUT` only |
| Place | current public room |
| Cost | compute 1 |
| Keep | last 1 shout |
| Events | `MESSAGE` only |
| PLAY | `A shout: {text}.` |
| WATCH | silent |
| Help | still omits board / SHOUT |

---

## Out of S4

```text
SHOUT verb
long-range shout
WATCH ticker
Chamber help shout
board retention beyond 3
```

---

## Runtime rule

Hosted Chamber MUST accept `MESSAGE surface=SHOUT` in a public room and keep the last 1 shout for PLAY. Isolated tests only. Help unchanged. No Genesis change.
