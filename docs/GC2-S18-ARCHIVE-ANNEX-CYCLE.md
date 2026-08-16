# GC2-S18 — multi-cycle archive_annex CONSTRUCT

**Status:** Executable specification. Runtime authorized with RFC-0077.  
**Parent:** [GC2-S4-ARCHIVE-ANNEX.md](GC2-S4-ARCHIVE-ANNEX.md) · [GC2-S9-MULTICYCLE.md](GC2-S9-MULTICYCLE.md) · [CONSTRUCTION.md](CONSTRUCTION.md)  
**RFC:** [RFC-0077](../rfcs/RFC-0077-archive-annex-cycle.md)  
**Does not open:** remaining-class multi-cycle · STRUCTURE_* · help BUILD/ATTEST · project minigame · S4 discount retune  
**Next:** remaining constructible class that is still instant (`route_link`)

S18 makes archive_annex CONSTRUCT take world-time. A public archive annex starts `IN_PROGRESS` and becomes live after one committed cycle. The S4 attention discount applies only after promotion.

---

## Doctrine decisions

| Temptation | Verdict |
|------------|---------|
| All remaining classes | **REJECT.** archive_annex only |
| Duration ≠ 1 | **REJECT.** |
| New room | **REJECT.** |
| `STRUCTURE_*` | **REJECT.** |
| Help BUILD / ATTEST | **REJECT.** |
| Scar on in-progress salvage | **REJECT.** Never live |
| Shell discounts attention | **REJECT.** Live only |
| Filter shell from slot | **REJECT.** Occupies immediately |
| Change −1 attention | **REJECT.** S4 closed |

---

## Slice contract

| Field | Value |
|-------|--------|
| Slice id | `gc2-s18` |
| Catalog | `construction-catalog/gc2-s18` |
| Verb | existing `BUILD` |
| Operation | `CONSTRUCT` `class=archive_annex` |
| Start | `IN_PROGRESS` entity; same `entity_id` |
| Promote | 1 committed cycle |
| Slot | occupies archive_annex slot immediately |
| Live discount | only after promotion; S4 INSPECT/ATTEST attention −1 |
| In-progress DISMANTLE | salvage; no live annex; no scar |
| Events | `ENTITY_CREATE` / `ENTITY_UPDATE` / `ENTITY_DESTROY` / `BUDGET_CONSUMED` |
| PLAY | `An archive annex is under construction.` |
| WATCH | silent |
| Help | still omits BUILD and ATTEST |

---

## Out of S18

```text
remaining-class multi-cycle
STRUCTURE_*
Chamber help BUILD ATTEST
project minigame
S4 discount retune
```

---

## Runtime rule

Hosted Chamber MUST create a public `archive_annex` CONSTRUCT as `IN_PROGRESS`, occupy the class slot immediately, refuse the S4 attention discount until that same `entity_id` is live after 1 committed cycle, and salvage an in-progress annex without leaving a live annex or a scar. Isolated tests only. Help unchanged. No Genesis change.
