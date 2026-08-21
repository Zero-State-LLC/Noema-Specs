# RFC-0119 — WAIT burns cargo for energy

## Status

**Accepted**

No new Player verbs. AUTH-INFRA-CLASS harvest/move/repair amounts unchanged. RFC-0117 lockout rest unchanged. RFC-0118 work-consumes-cargo unchanged.

## Problem

Harvest fills hold. Work empties it. A Player can be **cargo-full with no work in the room** and **energy too low to MOVE** (cargo MOVE costs 2). TRADE needs a counterparty. RFC-0117 only rests when energy **and** storage are both 0. Carrying cargo with a little energy is a dead end.

## Proposed change

On a successful WAIT, after RFC-0117 lockout rest, if lockout rest did **not** apply:

When occupied hold ≥ 1 (`storage` < 16) and energy < grant (80), convert **1 cargo → +2 energy**:

| Budget | Change |
|--------|--------|
| free `storage` | **+1** (consume cargo) |
| `energy` | **+2**, clamp to grant 80 |

- No new verb. Not a coin. Not passive regen.
- Skip this WAIT if RFC-0117 just restored energy 0 / storage 0.
- PLAY MAY say `Waiting can burn cargo for energy.` WATCH does not.

Catalog: [`economy-catalog.gc8-s7.json`](../specs/economy-catalog.gc8-s7.json).  
Slice: [GC8-S7-WAIT-CARGO-FUEL.md](../docs/GC8-S7-WAIT-CARGO-FUEL.md).

## Alternatives rejected

| Alternative | Why |
|-------------|-----|
| CONSUME / BURN verb | New verb; freeze |
| Passive energy regen | RESOURCE-ECONOMY energy regen stays 0 |
| Harvest when full converts to energy | Changes HARVEST; RFC-0118 debit stands |
| Always burn on cycle commit | Punishes WAIT quorum |

## Compatibility

Additive WAIT rest. Worlds ignoring S7 keep RFC-0117-only rest.

## Data / security

No new Player fields.

## Validation

`check_gc8_s7`: cargo WAIT +2 energy +1 free storage; skip at energy grant; skip after lockout rest; no new verbs.

## Rollback

Stop applying cargo fuel. WAIT still free; RFC-0117 remains.

## Unresolved

Whether TRADE should be preferred over burning. Whether +2 is retuned later.
