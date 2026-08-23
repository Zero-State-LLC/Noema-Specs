# RFC-0051 — GC10-S2 Irreversible Scar

## Status

**Accepted**

No new verbs. No `event-catalog/0.3`. No Admin spawn. No hidden-room leak.

## Problem

[WORLD-EVENT-DIRECTOR.md](../docs/WORLD-EVENT-DIRECTOR.md) lists an irreversible scar class. GC2-S0 `DISMANTLE` erases the asset. Later Players cannot see that something stood there. An implementer would add `SCAR_*` events or repair the leftover.

## Proposed change

Accept GC10-S2:

- Public `DISMANTLE` still emits `ENTITY_DESTROY` (S0)
- Then `ENTITY_CREATE` leaves a `RUIN` with `scar=true` in that room
- Label is `scarred-{class}` (class token only; no hidden ids)
- A scar is **not** repairable. The class slot is free (scars are not live infrastructure)
- Hidden rooms leave **no** scar
- Scheduled pressure stays recoverable (S0/S1 floors). Pressure does not scar
- PLAY MAY say `A scar remains.` WATCH silent
- Chamber help still omits BUILD

Catalog: [`pressure-catalog.gc10-s2.json`](../specs/pressure-catalog.gc10-s2.json).  
Slice: [GC10-S2-SCAR.md](../docs/GC10-S2-SCAR.md).

## Alternatives rejected

| Alternative | Why |
|-------------|-----|
| `SCAR_*` events | New catalog |
| Replace DESTROY with UPDATE | Breaks GC2-S0 |
| Scar from S0/S1 pressure | Those floors stay recoverable |
| Repairable ruin | Not irreversible |
| Admin spawn | Doctrine |
| WATCH scar ticker | Spectator leak |

## Compatibility

Additive leftover after DESTROY. Worlds ignoring S2 keep empty-room dismantle.

## Data / security

Optional `scar` on a public RUIN. Hidden `room_id` MUST NOT be stored on a scar.

## Validation

`check_gc10_s2`: dismantle leaves scar; scar not repairable; hidden dismantle empty; no new events; pressure does not scar.

## Rollback

Skip the CREATE. DESTROY remains.

## Unresolved

Artifact emergence. Institutional crisis. Unknown signal. Operator receipt schema.
