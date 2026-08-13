# GC2 thaw readiness — 2026-08-13

**Status:** Ready for an **explicit** thaw instruction. This document does **not** authorize `BUILD`.  
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
| Remaining runtime gaps | Chamber help still omits BUILD (required until thaw). No hosted CONSTRUCT/DISMANTLE yet |

Architecture is not a GC2 blocker once world-heads SQL is applied. Do not implement BUILD without an explicit thaw.
