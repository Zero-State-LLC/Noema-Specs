# GC2-S2 — workshop

**Status:** Executable specification. Runtime authorized with RFC-0050.  
**Parent:** [GC2-S1-ROUTE-LINK.md](GC2-S1-ROUTE-LINK.md) · [CONSTRUCTION.md](CONSTRUCTION.md)  
**RFC:** [RFC-0050](../rfcs/RFC-0050-workshop.md)  
**Does not open:** recipes · mastery discounts · help BUILD · hidden rooms

S2 adds a bench. A live `workshop` saves one storage on CONSTRUCT and REPAIR in that room.

---

## Doctrine decisions

| Temptation | Verdict |
|------------|---------|
| Recipe book | **REJECT.** |
| Mastery cheaper builds | **REJECT.** |
| Workshop required to build | **REJECT.** Soft-lock |
| Help BUILD | **REJECT.** |

---

## Slice contract

| Field | Value |
|-------|--------|
| Slice id | `gc2-s2` |
| Catalog | `construction-catalog/gc2-s2` |
| Class | `workshop` |
| Construct | energy 6, compute 3, storage 5, influence 0 |
| Salvage | 2 |
| Slot | one live per public room |
| Effect | in-room CONSTRUCT and REPAIR storage −1 (floor 0) |
| PLAY | `A workshop is open.` |
| WATCH | silent |
| Help | still omits BUILD |

---

## Out of S2

```text
defensive_work archive_annex
UPGRADE CONNECT recipes
Chamber help BUILD
```

---

## Runtime rule

Hosted Chamber MUST accept `BUILD.CONSTRUCT class=workshop` in a public room and discount in-room CONSTRUCT/REPAIR storage by 1. Isolated tests only. Help unchanged. No Genesis change.
