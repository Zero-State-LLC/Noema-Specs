# GC2-S13 — multi-cycle workshop CONSTRUCT

**Status:** Executable specification. Runtime authorized with RFC-0072.  
**Parent:** [GC2-S2-WORKSHOP.md](GC2-S2-WORKSHOP.md) · [GC2-S9-MULTICYCLE.md](GC2-S9-MULTICYCLE.md) · [CONSTRUCTION.md](CONSTRUCTION.md)  
**RFC:** [RFC-0072](../rfcs/RFC-0072-workshop-cycle.md)  
**Does not open:** remaining-class multi-cycle · STRUCTURE_* · help BUILD · project minigame · UPGRADE/REPURPOSE of a shell  
**Next:** remaining constructible classes that are still instant

S13 makes workshop CONSTRUCT take world-time. A public workshop starts `IN_PROGRESS` and becomes a live bench after one committed cycle.

---

## Doctrine decisions

| Temptation | Verdict |
|------------|---------|
| All remaining classes | **REJECT.** Workshop only |
| Duration ≠ 1 | **REJECT.** |
| New room | **REJECT.** |
| `STRUCTURE_*` | **REJECT.** |
| Help BUILD | **REJECT.** |
| Scar on in-progress salvage | **REJECT.** Never live |
| UPGRADE / REPURPOSE while in progress | **REJECT.** Never live |

---

## Slice contract

| Field | Value |
|-------|--------|
| Slice id | `gc2-s13` |
| Catalog | `construction-catalog/gc2-s13` |
| Verb | existing `BUILD` |
| Operation | `CONSTRUCT` `class=workshop` |
| Start | `IN_PROGRESS` entity; same `entity_id` |
| Promote | 1 committed cycle |
| Slot | occupies workshop slot immediately |
| Live discount | only after promotion |
| In-progress DISMANTLE | salvage; no live workshop; no scar |
| In-progress UPGRADE / REPURPOSE | `FORBIDDEN` |
| Events | `ENTITY_CREATE` / `ENTITY_UPDATE` / `ENTITY_DESTROY` / `BUDGET_CONSUMED` |
| PLAY | `A workshop is under construction.` |
| WATCH | silent |
| Help | still omits BUILD |

---

## Out of S13

```text
remaining-class multi-cycle
STRUCTURE_*
Chamber help BUILD
project minigame
UPGRADE / REPURPOSE of IN_PROGRESS
```

---

## Runtime rule

Hosted Chamber MUST create a public `workshop` CONSTRUCT as `IN_PROGRESS`, promote that same `entity_id` after 1 committed cycle, refuse UPGRADE and REPURPOSE while in progress, and salvage an in-progress workshop without leaving a live workshop or a scar. Isolated tests only. Help unchanged. No Genesis change.
