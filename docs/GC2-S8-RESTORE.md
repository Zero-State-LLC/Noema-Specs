# GC2-S8 — RESTORE

**Status:** Executable specification. Runtime authorized with RFC-0059.  
**Parent:** [GC2-S7-ABANDON.md](GC2-S7-ABANDON.md) · [CONSTRUCTION.md](CONSTRUCTION.md)  
**RFC:** [RFC-0059](../rfcs/RFC-0059-restore.md)  
**Does not open:** scar restore · CONNECT · help BUILD · STRUCTURE_* · stranger reclaim

S8 is the inverse of abandon. The owner may restore an UNCLAIMED public constructible. Scars stay dead.

---

## Doctrine decisions

| Temptation | Verdict |
|------------|---------|
| Restore GC10-S2 scars | **REJECT.** |
| Stranger reclaim | **REJECT.** |
| New class / new id | **REJECT.** |
| `STRUCTURE_RESTORED` | **REJECT.** |
| Help BUILD | **REJECT.** |

---

## Slice contract

| Field | Value |
|-------|--------|
| Slice id | `gc2-s8` |
| Catalog | `construction-catalog/gc2-s8` |
| Verb | existing `BUILD` |
| Operation | `RESTORE` |
| Target | public `UNCLAIMED` constructible the actor owns |
| Cost | that class’s CONSTRUCT cost |
| Condition | `min(current, 50)` |
| Identity | same `entity_id` and class |
| Events | `ENTITY_UPDATE` + `BUDGET_CONSUMED` |
| PLAY | `You restored the {label}.` |
| WATCH | silent |
| Help | still omits BUILD / restore |

---

## Out of S8

```text
CONNECT
scar restore
multi-cycle
STRUCTURE_*
Chamber help BUILD
```

---

## Runtime rule

Hosted Chamber MUST accept `BUILD.RESTORE` on an owned public UNCLAIMED constructible, clear `unclaimed`, and cap condition at 50. Isolated tests only. Help unchanged. No Genesis change.
