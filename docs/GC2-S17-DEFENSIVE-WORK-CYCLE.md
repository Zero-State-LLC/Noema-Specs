# GC2-S17 — multi-cycle defensive_work CONSTRUCT

**Status:** Executable specification. Runtime authorized with RFC-0076.  
**Parent:** [GC2-S3-DEFENSIVE-WORK.md](GC2-S3-DEFENSIVE-WORK.md) · [GC2-S9-MULTICYCLE.md](GC2-S9-MULTICYCLE.md) · [CONSTRUCTION.md](CONSTRUCTION.md)  
**RFC:** [RFC-0076](../rfcs/RFC-0076-defensive-work-cycle.md)  
**Does not open:** remaining-class multi-cycle · STRUCTURE_* · help BUILD · project minigame · S3 millipoint retune  
**Next:** remaining constructible classes that are still instant

S17 makes defensive_work CONSTRUCT take world-time. A public defensive work starts `IN_PROGRESS` and becomes live after one committed cycle. The S3 +50 contest-defense millipoints apply only after promotion.

---

## Doctrine decisions

| Temptation | Verdict |
|------------|---------|
| All remaining classes | **REJECT.** defensive_work only |
| Duration ≠ 1 | **REJECT.** |
| New room | **REJECT.** |
| `STRUCTURE_*` | **REJECT.** |
| Help BUILD | **REJECT.** |
| Scar on in-progress salvage | **REJECT.** Never live |
| Shell adds contest defense | **REJECT.** Live only |
| Filter shell from slot | **REJECT.** Occupies immediately |
| Change +50 millipoints | **REJECT.** S3 closed |

---

## Slice contract

| Field | Value |
|-------|--------|
| Slice id | `gc2-s17` |
| Catalog | `construction-catalog/gc2-s17` |
| Verb | existing `BUILD` |
| Operation | `CONSTRUCT` `class=defensive_work` |
| Start | `IN_PROGRESS` entity; same `entity_id` |
| Promote | 1 committed cycle |
| Slot | occupies defensive_work slot immediately |
| Live contest bonus | only after promotion; S3 +50 millipoints |
| In-progress DISMANTLE | salvage; no live work; no scar |
| Events | `ENTITY_CREATE` / `ENTITY_UPDATE` / `ENTITY_DESTROY` / `BUDGET_CONSUMED` |
| PLAY | `A defensive work is under construction.` |
| WATCH | silent |
| Help | still omits BUILD |

---

## Out of S17

```text
remaining-class multi-cycle
STRUCTURE_*
Chamber help BUILD
project minigame
S3 millipoint retune
```

---

## Runtime rule

Hosted Chamber MUST create a public `defensive_work` CONSTRUCT as `IN_PROGRESS`, occupy the class slot immediately, refuse the S3 contest-defense bonus until that same `entity_id` is live after 1 committed cycle, and salvage an in-progress work without leaving a live work or a scar. Isolated tests only. Help unchanged. No Genesis change.
