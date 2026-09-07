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


## Extension Points

Non-normative guidance for future maintenance; this section changes no current behavior or promotion status.

- Route-facing examples can add combinations of steward authority and existing two-way public neighbors. CONNECT remains BUILD.CONNECT stamping dest_room_id on the same live route_link; it never creates geography or changes the cargo waiver.

- Any change to destination eligibility, costs, or failure disclosure needs review against RFC-0071 and construction-catalog/gc2-s12. Later construction slices do not retroactively change the S12 fixture boundary or authorize a standalone CONNECT verb.

- Validate success preserves entity_id and the exit set, charges compute once, and leaves WATCH silent. Pair hidden, missing, and one-way destinations with the same NOT_OBSERVABLE outcome; test non-stewards and replay/retry without a second debit.
