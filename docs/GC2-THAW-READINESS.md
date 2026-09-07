# GC2 thaw readiness — 2026-08-13

**Status:** Thawed. Hosted `BUILD` CONSTRUCT/DISMANTLE shipped (Noema #79). Chamber help names BUILD ([RFC-0090](../rfcs/RFC-0090-build-play-thaw.md)).  
**Authority:** [GC2-FIRST-SLICE.md](GC2-FIRST-SLICE.md) · [RFC-0006](../rfcs/RFC-0006-construction-existing-events.md)

| Topic | Status |
|-------|--------|
| Reducer owner | `ENTITY_CREATE` / `ENTITY_DESTROY` / `BUDGET_CONSUMED` (existing 0.1). No catalog 0.3 |
| Durable commitments | RFC-0016 head + RFC-0017 fence. SQL must be applied for reconstructable heads |
| World-time | S0 is single-cycle all-or-nothing. WAIT no longer advances `World.cycle` |
| Resource reservation | Same as HARVEST/TRADE: fail closed, no spend on reject |
| Asset lineage | `owner_id` = constructing Player; one live class per room |
| Location | Co-located; hidden rooms not targets |
| Events reused | `BUDGET_CONSUMED`, `ENTITY_CREATE`, `ENTITY_DESTROY` |
| Remaining runtime gaps | CONTEST / WED / ATTEST still omitted from help |

Hosted CONSTRUCT/DISMANTLE is live. Chamber help names BUILD (RFC-0090). Contest and WED shipped on their own slices; this document does not authorize their help text.

## Extension Points

Non-normative future guidance; this section does not authorize new behavior.

- Future readiness receipts can append evidence for hosted construction and BUILD help exposure while retaining this dated thaw assessment. Keep storage-head reconstruction, fail-closed reservation, co-location and owner lineage distinct from presentation readiness.
- Cite the runtime revision, accepted RFC and catalog for each new receipt; later slices do not retroactively alter S0. Recheck rejected actions without spend, reconstructable committed heads and BUILD help independently, without inferring CONTEST/WED/ATTEST exposure.
