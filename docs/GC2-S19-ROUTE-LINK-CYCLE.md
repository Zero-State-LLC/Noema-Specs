# GC2-S19 — multi-cycle route_link CONSTRUCT

**Status:** Executable specification. Runtime authorized with RFC-0078.  
**Parent:** [GC2-S1-ROUTE-LINK.md](GC2-S1-ROUTE-LINK.md) · [GC2-S12-CONNECT.md](GC2-S12-CONNECT.md) · [GC2-S9-MULTICYCLE.md](GC2-S9-MULTICYCLE.md) · [CONSTRUCTION.md](CONSTRUCTION.md)  
**RFC:** [RFC-0078](../rfcs/RFC-0078-route-link-cycle.md)  
**Does not open:** new exits · CONNECT verb · STRUCTURE_* · help BUILD · project minigame · S1 waiver retune  
**Next:** third-and-later co-owners · comms cycle expiry

S19 makes route_link CONSTRUCT take world-time. A public route link starts `IN_PROGRESS` and becomes live after one committed cycle. The S1 cargo waiver applies only after promotion. CONNECT dest stays the S12 pin.

---

## Doctrine decisions

| Temptation | Verdict |
|------------|---------|
| New exit | **REJECT.** |
| Duration ≠ 1 | **REJECT.** |
| `STRUCTURE_*` | **REJECT.** |
| Help BUILD | **REJECT.** |
| Scar on in-progress salvage | **REJECT.** Never live |
| Shell waives cargo | **REJECT.** Live only |
| Filter shell from slot | **REJECT.** Occupies immediately |
| Change cargo extra | **REJECT.** S1 closed |
| CONNECT as new exit | **REJECT.** S12 dest pin |

---

## Slice contract

| Field | Value |
|-------|--------|
| Slice id | `gc2-s19` |
| Catalog | `construction-catalog/gc2-s19` |
| Verb | existing `BUILD` |
| Operation | `CONSTRUCT` `class=route_link` |
| Start | `IN_PROGRESS` entity; same `entity_id` |
| Promote | 1 committed cycle |
| Slot | occupies route_link slot immediately |
| Live waiver | only after promotion; S1 cargo extra waived on departing MOVE |
| CONNECT | S12 dest pin on a **live** public link only |
| In-progress DISMANTLE | salvage; no live link; no scar |
| Events | `ENTITY_CREATE` / `ENTITY_UPDATE` / `ENTITY_DESTROY` / `BUDGET_CONSUMED` |
| PLAY | `A route link is under construction.` |
| WATCH | silent |
| Help | still omits BUILD |

---

## Out of S19

```text
new exits
CONNECT verb
STRUCTURE_*
Chamber help BUILD
project minigame
S1 cargo-waiver retune
```

---

## Runtime rule

Hosted Chamber MUST create a public `route_link` CONSTRUCT as `IN_PROGRESS`, occupy the class slot immediately, refuse the S1 cargo waiver until that same `entity_id` is live after 1 committed cycle, refuse CONNECT dest on a shell, and salvage an in-progress link without leaving a live link or a scar. Isolated tests only. Help unchanged. No Genesis change.

## Extension Points

Non-normative guidance for future work; existing authorities and closed-slice boundaries remain unchanged.

- **Seam and invariants.** Lifecycle fixtures can expand around the route-link shell, promotion and in-progress salvage without creating a project subsystem. Preserve immediate slot occupancy, the same entity_id and promotion after one committed cycle.
- **Compatibility and validation.** Cover duplicate cycle delivery, MOVE before/after promotion, CONNECT rejection on a shell and dismantle before completion without a scar. Pin S19 together with S1/S12 dependencies; changing duration or waiver rules requires accepted versioned contracts, not a scheduler shortcut.
