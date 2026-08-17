# GC5-S6 — MESSAGE institution notice

**Status:** Executable specification. Runtime authorized with RFC-0064.  
**Parent:** [GC5-S5-RETENTION.md](GC5-S5-RETENTION.md) · [GC4-S1-OFFICES.md](GC4-S1-OFFICES.md) · [COMMUNICATION-ECOLOGY.md](COMMUNICATION-ECOLOGY.md)  
**RFC:** [RFC-0064](../rfcs/RFC-0064-institution-notice.md)  
**Does not open:** NOTICE/BOARD/SHOUT verbs · long-range notice · help advertising · hidden notices  
**Next:** [GC5-S7-CHANNEL.md](GC5-S7-CHANNEL.md)

S6 adds one MESSAGE surface. An occupied `PUBLISH_NOTICE` office may utter in the public room. It is not a notice verb.

---

## Doctrine decisions

| Temptation | Verdict |
|------------|---------|
| NOTICE verb | **REJECT.** |
| Org-member channel | **REJECT.** |
| Long-range / all-rooms | **REJECT.** |
| Hidden-room notice | **REJECT.** |
| WATCH ticker | **REJECT.** |
| Help NOTICE | **REJECT.** |
| Replace OFFICE_ACT | **REJECT.** |

---

## Slice contract

| Field | Value |
|-------|--------|
| Slice id | `gc5-s6` |
| Catalog | `communication-catalog/gc5-s6` |
| Verb | existing `MESSAGE` |
| Surface | `NOTICE` only |
| Authority | occupied `PUBLISH_NOTICE` office |
| Place | current public room |
| Cost | compute 1 |
| Keep | last 1 institution notice |
| Events | `MESSAGE` only |
| PLAY | `A notice from {org}: {text}.` |
| WATCH | silent |
| Help | still omits NOTICE as a comms verb |

---

## Out of S6

```text
NOTICE verb
long-range notice
WATCH ticker
Chamber help NOTICE
notice cycle expiry is [GC5-S11-NOTICE-EXPIRY.md](GC5-S11-NOTICE-EXPIRY.md)
```

---

## Runtime rule

Hosted Chamber MUST accept `MESSAGE surface=NOTICE` from a holder of an occupied `PUBLISH_NOTICE` office in a public room and keep the last 1 institution notice for PLAY. Vacant / non-holder fail closed. Hidden rooms reject. Isolated tests only. Help unchanged. No Genesis change.
