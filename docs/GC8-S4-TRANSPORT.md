# GC8-S4 — Cargo MOVE Extra

**Status:** Executable specification. Runtime authorized with RFC-0048.  
**Parent:** [GC8-S3-SPOILAGE.md](GC8-S3-SPOILAGE.md) · [ECONOMIC-SPECIALIZATION.md](ECONOMIC-SPECIALIZATION.md)  
**RFC:** [RFC-0048](../rfcs/RFC-0048-cargo-move.md)  
**Does not open:** courier verb · route_link freight · currency · v0.6B · WATCH ticker

S4 makes carrying harvested lots cost one extra energy to move. Empty travel stays S0.

---

## Doctrine decisions

| Temptation | Verdict |
|------------|---------|
| Courier verb | **REJECT.** |
| route_link freight table | **REJECT.** Freight minigame |
| WATCH cargo feed | **REJECT.** |
| Currency | **REJECT.** |

---

## Slice contract

| Field | Value |
|-------|--------|
| Slice id | `gc8-s4` |
| Catalog | `economy-catalog/gc8-s4` |
| Empty | `storage` ≥ 16 → MOVE energy **1** |
| Carrying | `storage` < 16 → MOVE energy **2** |
| Signal | free storage below the default grant |
| PLAY | `Carrying lots costs extra to move.` |
| WATCH | silent |

---

## Out of S4

```text
courier verb
route_link freight engine
currency order book v0.6B
WATCH ticker
```

---

## Runtime rule

Hosted Chamber MUST charge MOVE 2 when free storage is below the grant. Isolated tests only. Help unchanged. No Genesis change.
