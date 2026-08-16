# GC2-S16 — multi-cycle production_node CONSTRUCT

**Status:** Executable specification. Runtime authorized with RFC-0075.  
**Parent:** [GC2-S9-MULTICYCLE.md](GC2-S9-MULTICYCLE.md) · [CONSTRUCTION.md](CONSTRUCTION.md)  
**RFC:** [RFC-0075](../rfcs/RFC-0075-production-node-cycle.md)  
**Does not open:** remaining-class multi-cycle · STRUCTURE_* · help BUILD · project minigame  
**Next:** remaining constructible classes that are still instant

S16 makes production_node CONSTRUCT take world-time. A public production node starts `IN_PROGRESS` and becomes live after one committed cycle.

---

## Doctrine decisions

| Temptation | Verdict |
|------------|---------|
| All remaining classes | **REJECT.** production_node only |
| Duration ≠ 1 | **REJECT.** |
| New room | **REJECT.** |
| `STRUCTURE_*` | **REJECT.** |
| Help BUILD | **REJECT.** |
| Scar on in-progress salvage | **REJECT.** Never live |

---

## Slice contract

| Field | Value |
|-------|--------|
| Slice id | `gc2-s16` |
| Catalog | `construction-catalog/gc2-s16` |
| Verb | existing `BUILD` |
| Operation | `CONSTRUCT` `class=production_node` |
| Start | `IN_PROGRESS` entity; same `entity_id` |
| Promote | 1 committed cycle |
| Slot | occupies production_node slot immediately |
| Live | only after promotion |
| In-progress DISMANTLE | salvage; no live node; no scar |
| Events | `ENTITY_CREATE` / `ENTITY_UPDATE` / `ENTITY_DESTROY` / `BUDGET_CONSUMED` |
| PLAY | `A production node is under construction.` |
| WATCH | silent |
| Help | still omits BUILD |

---

## Out of S16

```text
remaining-class multi-cycle
STRUCTURE_*
Chamber help BUILD
project minigame
```

---

## Runtime rule

Hosted Chamber MUST create a public `production_node` CONSTRUCT as `IN_PROGRESS`, promote that same `entity_id` after 1 committed cycle, and salvage an in-progress node without leaving a live node or a scar. Isolated tests only. Help unchanged. No Genesis change.
