# GC2-S3 — defensive_work

**Status:** Executable specification. Runtime authorized with RFC-0052.  
**Parent:** [GC2-S2-WORKSHOP.md](GC2-S2-WORKSHOP.md) · [CONSTRUCTION.md](CONSTRUCTION.md) · [STRATEGIC-CONFLICT.md](STRATEGIC-CONFLICT.md)  
**RFC:** [RFC-0052](../rfcs/RFC-0052-defensive-work.md)  
**Does not open:** HP · new contest form · help BUILD/CONTEST · hidden rooms

S3 adds a wall. A live `defensive_work` adds 50 millipoints of defense to contests in that room.

---

## Doctrine decisions

| Temptation | Verdict |
|------------|---------|
| Hit points | **REJECT.** |
| New contest form | **REJECT.** |
| Mutate S0 weights | **REJECT.** |
| Help BUILD / CONTEST | **REJECT.** |

---

## Slice contract

| Field | Value |
|-------|--------|
| Slice id | `gc2-s3` |
| Catalog | `construction-catalog/gc2-s3` |
| Class | `defensive_work` |
| Construct | energy 7, compute 3, storage 4, influence 3 |
| Salvage | 2 |
| Slot | one live per public room |
| Effect | +50 defense millipoints on contests in that room |
| PLAY | `A defensive work stands.` |
| WATCH | silent |
| Help | still omits BUILD and CONTEST |

---

## Out of S3

```text
archive_annex (closed in GC2-S4)
UPGRADE CONNECT HP
Chamber help BUILD CONTEST
```

---

## Runtime rule

Hosted Chamber MUST accept `BUILD.CONSTRUCT class=defensive_work` in a public room and add 50 defense millipoints to contests there. Isolated tests only. Help unchanged. No Genesis change.
