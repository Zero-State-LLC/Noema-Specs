# GC2-S14 — multi-cycle generator CONSTRUCT

**Status:** Executable specification. Runtime authorized with RFC-0073.  
**Parent:** [GC2-S9-MULTICYCLE.md](GC2-S9-MULTICYCLE.md) · [GC2-S13-WORKSHOP-CYCLE.md](GC2-S13-WORKSHOP-CYCLE.md) · [CONSTRUCTION.md](CONSTRUCTION.md)  
**RFC:** [RFC-0073](../rfcs/RFC-0073-generator-cycle.md)  
**Does not open:** remaining-class multi-cycle · STRUCTURE_* · help BUILD · project minigame  
**Next:** remaining constructible classes that are still instant

S14 makes generator CONSTRUCT take world-time. A public generator starts `IN_PROGRESS` and becomes live after one committed cycle.

---

## Doctrine decisions

| Temptation | Verdict |
|------------|---------|
| All remaining classes | **REJECT.** Generator only |
| Duration ≠ 1 | **REJECT.** |
| New room | **REJECT.** |
| `STRUCTURE_*` | **REJECT.** |
| Help BUILD | **REJECT.** |
| Scar on in-progress salvage | **REJECT.** Never live |

---

## Slice contract

| Field | Value |
|-------|--------|
| Slice id | `gc2-s14` |
| Catalog | `construction-catalog/gc2-s14` |
| Verb | existing `BUILD` |
| Operation | `CONSTRUCT` `class=generator` |
| Start | `IN_PROGRESS` entity; same `entity_id` |
| Promote | 1 committed cycle |
| Slot | occupies generator slot immediately |
| Live | only after promotion |
| In-progress DISMANTLE | salvage; no live generator; no scar |
| Events | `ENTITY_CREATE` / `ENTITY_UPDATE` / `ENTITY_DESTROY` / `BUDGET_CONSUMED` |
| PLAY | `A generator is under construction.` |
| WATCH | silent |
| Help | still omits BUILD |

---

## Out of S14

```text
remaining-class multi-cycle
STRUCTURE_*
Chamber help BUILD
project minigame
```

---

## Runtime rule

Hosted Chamber MUST create a public `generator` CONSTRUCT as `IN_PROGRESS`, promote that same `entity_id` after 1 committed cycle, and salvage an in-progress generator without leaving a live generator or a scar. Isolated tests only. Help unchanged. No Genesis change.

## Extension Points

Non-normative extension guidance; this section does not change accepted behavior or prove runtime completion.

- Extend generator lifecycle fixtures around restart and cycle settlement. Preserve immediate generator-slot occupancy, one entity_id and IN_PROGRESS→live only after one committed cycle, not elapsed wall time.

- Keep generator-only scope, accepted ENTITY_* and BUDGET_CONSUMED events, WATCH silence and omitted BUILD help. In-progress salvage leaves neither a live generator nor a scar; no new room, STRUCTURE_* event or project minigame is implied.

- Pin construction-catalog/gc2-s14 and RFC-0073. Another class, duration or exposure change needs its own accepted authority; this seam does not change Genesis or the isolated-test rule.

- Validate a slot conflict while IN_PROGRESS, restart before promotion, duplicate cycle settlement and pre-promotion DISMANTLE. Assert one stable identity, no premature live effect and no post-salvage promotion.
