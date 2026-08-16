# GC2-S12 — CONNECT dest pin

**Status:** Executable specification. Runtime authorized with RFC-0071.  
**Parent:** [GC2-S1-ROUTE-LINK.md](GC2-S1-ROUTE-LINK.md) · [GC2-S11-SHARED.md](GC2-S11-SHARED.md) · [CONSTRUCTION.md](CONSTRUCTION.md)  
**RFC:** [RFC-0071](../rfcs/RFC-0071-connect-dest.md)  
**Does not open:** new exits · CONNECT verb · hidden rooms · help BUILD · STRUCTURE_*

S12 lets a steward name where a public `route_link` faces. The destination must already be a two-way public neighbor. It is not a new exit.

---

## Doctrine decisions

| Temptation | Verdict |
|------------|---------|
| New exit | **REJECT.** |
| Distinct hidden-dest error | **REJECT.** Same `NOT_OBSERVABLE`. |
| Change S1 cargo waiver | **REJECT.** |
| CONNECT verb | **REJECT.** |
| Help BUILD | **REJECT.** |

---

## Slice contract

| Field | Value |
|-------|--------|
| Slice id | `gc2-s12` |
| Catalog | `construction-catalog/gc2-s12` |
| Verb | existing `BUILD` |
| Operation | `CONNECT` |
| Target | live public `route_link` the actor stewards |
| Dest | existing public two-way neighbor |
| Identity | same `entity_id`; `dest_room_id` stamped |
| Cost | compute 1 |
| Events | `ENTITY_UPDATE` + `BUDGET_CONSUMED` |
| PLAY | `The route link faces {dest}.` |
| Fail | `NOT_OBSERVABLE` for hidden / missing / one-way |
| WATCH | silent |
| Help | still omits BUILD |

---

## Out of S12

```text
new exits
CONNECT verb
hidden dest leak
cargo-waiver retune
STRUCTURE_*
Chamber help BUILD
```

---

## Runtime rule

Hosted Chamber MUST accept `BUILD.CONNECT` on a stewarded public `route_link` when `dest` is already a public two-way neighbor, stamp `dest_room_id`, and MUST NOT create an exit. Isolated tests only. Help unchanged. No Genesis change.
