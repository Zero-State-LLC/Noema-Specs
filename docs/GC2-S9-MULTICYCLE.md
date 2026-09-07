# GC2-S9 — multi-cycle relay CONSTRUCT

**Status:** Executable specification. Runtime authorized with RFC-0061.  
**Parent:** [GC2-S8-RESTORE.md](GC2-S8-RESTORE.md) · [CONSTRUCTION.md](CONSTRUCTION.md)  
**RFC:** [RFC-0061](../rfcs/RFC-0061-multicycle-construct.md)  
**Does not open:** CONNECT · other-class multi-cycle · STRUCTURE_* · help BUILD · project minigame  
**Next:** [GC2-S10-INSTITUTION.md](GC2-S10-INSTITUTION.md)

S9 makes one CONSTRUCT take world-time. A public relay starts `IN_PROGRESS` and becomes live after one committed cycle.

---

## Doctrine decisions

| Temptation | Verdict |
|------------|---------|
| All classes | **REJECT.** Relay only |
| Duration ≠ 1 | **REJECT.** |
| New room | **REJECT.** |
| `STRUCTURE_*` | **REJECT.** |
| Help BUILD | **REJECT.** |
| Scar on in-progress salvage | **REJECT.** Never live |

---

## Slice contract

| Field | Value |
|-------|--------|
| Slice id | `gc2-s9` |
| Catalog | `construction-catalog/gc2-s9` |
| Verb | existing `BUILD` |
| Operation | `CONSTRUCT` `class=relay` |
| Start | `IN_PROGRESS` entity; same `entity_id` |
| Promote | 1 committed cycle |
| Slot | occupies relay slot immediately |
| Live comms | only after promotion |
| In-progress DISMANTLE | salvage; no live relay; no scar |
| Events | `ENTITY_CREATE` / `ENTITY_UPDATE` / `ENTITY_DESTROY` / `BUDGET_CONSUMED` |
| PLAY | `A relay is under construction.` |
| WATCH | silent |
| Help | still omits BUILD |

---

## Out of S9

```text
CONNECT
other-class multi-cycle
STRUCTURE_*
Chamber help BUILD
project minigame
```

---

## Runtime rule

Hosted Chamber MUST create a public `relay` CONSTRUCT as `IN_PROGRESS`, promote that same `entity_id` after 1 committed cycle, and salvage an in-progress relay without leaving a live relay or a scar. Isolated tests only. Help unchanged. No Genesis change.


## Extension Points

Non-normative guidance for future maintenance; this section changes no current behavior or promotion status.

- Construction lifecycle examples can expand settlement and recovery coverage for a relay moving from IN_PROGRESS to live. Preserve one entity_id, immediate slot occupancy, and promotion after one committed cycle rather than elapsed wall time.

- Duration, other-class construction, and visibility changes belong to their own accepted slices and catalog pins, not a rewrite of RFC-0061 examples. The S9 boundary keeps WATCH silent and does not add STRUCTURE_* events or a project-management system.

- Exercise restart before promotion, repeated settlement, slot contention, and dismantle before the cycle commits. Compare replayed state and event order; an in-progress relay must neither carry live communications nor leave a scar when salvaged.
