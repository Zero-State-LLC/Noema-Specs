# GC2-S1 — route_link

**Status:** Executable specification. Runtime authorized with RFC-0049.  
**Parent:** [GC2-FIRST-SLICE.md](GC2-FIRST-SLICE.md) · [CONSTRUCTION.md](CONSTRUCTION.md)  
**RFC:** [RFC-0049](../rfcs/RFC-0049-route-link.md)  
**Does not open:** new exits · CONNECT verb · hidden rooms · Chamber help BUILD · freight company

S1 adds one constructible that changes movement: a live `route_link` carries lots so departing MOVE stays energy 1.

---

## Doctrine decisions

| Temptation | Verdict |
|------------|---------|
| New public exit / `to_room_id` | **REJECT.** Hidden-topology leak |
| CONNECT / UPGRADE | **DEFER.** |
| WATCH route feed | **REJECT.** |
| Help BUILD | **REJECT.** S0 pin |

---

## Slice contract

| Field | Value |
|-------|--------|
| Slice id | `gc2-s1` |
| Catalog | `construction-catalog/gc2-s1` |
| Class | `route_link` |
| Construct | energy 8, compute 4, storage 4, influence 2 |
| Salvage | 2 |
| Slot | one live per public room |
| Effect | waive GC8-S4 cargo extra on MOVE leaving that room |
| PLAY | `A route link was opened.` / cargo line omitted while the link is live |
| WATCH | silent |
| Help | still omits BUILD |

---

## Out of S1

```text
new exits
workshop defensive_work archive_annex
UPGRADE CONNECT REPURPOSE
Chamber help BUILD
```

---

## Runtime rule

Hosted Chamber MUST accept `BUILD.CONSTRUCT class=route_link` in a public room and waive cargo MOVE extra while it is live. Isolated tests only. Help unchanged. No Genesis change.
