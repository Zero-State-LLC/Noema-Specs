# RFC-0014 — GC10-S0 Seeded Mild Relay Pressure

## Status

**Accepted**

Specification-only. No new event types. No Frontier schema reuse. No Admin spawn. No runtime implementation in this RFC.

## Problem

[WORLD-EVENT-DIRECTOR.md](../docs/WORLD-EVENT-DIRECTOR.md) and [STARTING-CONDITIONS.md](../docs/STARTING-CONDITIONS.md) require a mild deterministic schedule after a few cycles, but left the catalog, preview, and “no forced outcome” fixtures as SPEC GAP. An implementation agent would add `WED_*` types, share Frontier IDs, or script Player responses.

## Proposed change

Accept GC10-S0:

- One class: `infrastructure_failure`
- Seeded schedule at cycle 4
- `ENTITY_UPDATE` condition −15 on a named live relay
- Preview digest equals activation
- No required Player response
- `SITUATION_INJECTED` and Frontier request IDs stay out

Catalog: [`pressure-catalog.gc10-s0.json`](../specs/pressure-catalog.gc10-s0.json).  
Slice: [GC10-FIRST-SLICE.md](../docs/GC10-FIRST-SLICE.md).

## Alternatives rejected

| Alternative | Why |
|-------------|-----|
| New pressure events | Silent catalog expansion |
| `SITUATION_INJECTED` as WED | Frontier type; parent forbids shared IDs |
| Script REPAIR as the answer | Forces a research outcome |
| Drop below condition 25 | Not mild; would slam GC5 long-range |

## Compatibility

Additive pin of existing `ENTITY_UPDATE`. `event-catalog/0.1` and Frontier schemas are not rewritten.

## Data / security

Audit receipt is operator/research. PLAY must not include pressure class names. Admin Live must not grow a spawn control.

## Validation

`check_gc10_s0`: cycle-4 schedule drop 70→55; preview matches; forced response, PLAY label, Player authorizer, and Frontier ID reuse rejected.

## Rollback

Omit the schedule. Seeded relay condition remains as genesis.

## Unresolved

GC10-S1: other product classes; operator confirm path details; irreversible scars; first-20 later bands.
