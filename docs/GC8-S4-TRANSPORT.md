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

## Extension Points

Non-normative guidance; this section does not change the accepted contract or claim runtime completion.

### Cargo threshold conformance

Extend MOVE budget examples around the free-storage threshold rather than adding freight mechanics.

### Preserved invariants

Free storage at least 16 costs MOVE energy 1; below 16 costs energy 2. WATCH stays silent; no courier verb, route_link freight, currency or v0.6B is opened.

### Compatibility and promotion

RFC-0048 owns the storage signal and costs. A different grant, threshold or carrying model requires Accepted authority and version review; descriptive PLAY copy cannot alter accounting. No Genesis change follows from this seam.

### Validation fixtures before adoption

Use storage 16 and 15 with sufficient energy and expect debits 1 and 2. Pair carrying storage with insufficient energy and verify canonical rejection without a partial debit. Check empty travel retains its baseline and no cargo WATCH feed appears.
