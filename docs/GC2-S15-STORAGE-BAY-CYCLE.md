# GC2-S15 — multi-cycle storage_bay CONSTRUCT

**Status:** Executable specification. Runtime authorized with RFC-0074.  
**Parent:** [GC2-S9-MULTICYCLE.md](GC2-S9-MULTICYCLE.md) · [GC2-S6-REPURPOSE.md](GC2-S6-REPURPOSE.md) · [CONSTRUCTION.md](CONSTRUCTION.md)  
**RFC:** [RFC-0074](../rfcs/RFC-0074-storage-bay-cycle.md)  
**Does not open:** remaining-class multi-cycle · STRUCTURE_* · help BUILD · project minigame · REPURPOSE-as-shell  
**Next:** remaining constructible classes that are still instant

S15 makes storage_bay CONSTRUCT take world-time. A public storage bay starts `IN_PROGRESS` and becomes live after one committed cycle. REPURPOSE of a live workshop still yields a live bay.

---

## Doctrine decisions

| Temptation | Verdict |
|------------|---------|
| All remaining classes | **REJECT.** storage_bay CONSTRUCT only |
| Duration ≠ 1 | **REJECT.** |
| New room | **REJECT.** |
| `STRUCTURE_*` | **REJECT.** |
| Help BUILD | **REJECT.** |
| Scar on in-progress salvage | **REJECT.** Never live |
| REPURPOSE yields IN_PROGRESS | **REJECT.** S6 live conversion |

---

## Slice contract

| Field | Value |
|-------|--------|
| Slice id | `gc2-s15` |
| Catalog | `construction-catalog/gc2-s15` |
| Verb | existing `BUILD` |
| Operation | `CONSTRUCT` `class=storage_bay` |
| Start | `IN_PROGRESS` entity; same `entity_id` |
| Promote | 1 committed cycle |
| Slot | occupies storage_bay slot immediately |
| Live | only after promotion |
| In-progress DISMANTLE | salvage; no live bay; no scar |
| REPURPOSE | still live `storage_bay` |
| Events | `ENTITY_CREATE` / `ENTITY_UPDATE` / `ENTITY_DESTROY` / `BUDGET_CONSUMED` |
| PLAY | `A storage bay is under construction.` |
| WATCH | silent |
| Help | still omits BUILD |

---

## Out of S15

```text
remaining-class multi-cycle
STRUCTURE_*
Chamber help BUILD
project minigame
REPURPOSE-as-shell
```

---

## Runtime rule

Hosted Chamber MUST create a public `storage_bay` CONSTRUCT as `IN_PROGRESS`, promote that same `entity_id` after 1 committed cycle, and salvage an in-progress bay without leaving a live bay or a scar. Isolated tests only. Help unchanged. No Genesis change.
