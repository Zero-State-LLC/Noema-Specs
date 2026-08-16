# RFC-0055 — GC1-S5 office eligibility

## Status

**Accepted**

Specification-only until hosted. No new verbs. No `ROLE_*`. No `event-catalog/0.3`. No WATCH titles. No class discounts.

## Problem

[MASTERY-SPECIALIZATION.md](../docs/MASTERY-SPECIALIZATION.md) lists office eligibility as a closed benefit family. GC1-S4 still treats it as SPEC GAP. An implementer would freeze Treasurer as an Engineer class, emit titles on WATCH, or discount office costs.

## Proposed change

Accept GC1-S5. A named office MAY require a recognized track. Assignment uses existing `ORG_OFFICE_ASSIGN`.

- `ORG_OFFICE_CREATE` MAY set `requires_track` to `engineer` or `broker` only
- Absent `requires_track` stays unrestricted (existing offices)
- `ORG_OFFICE_ASSIGN` and designated succession seat only a Player **recognized** on that track
- LATENT still counts (recognition is not wiped). Do not evict on rust
- Explorer / Surveyor cannot be required in this slice
- Events remain `ENTITY_CREATE` / `ENTITY_UPDATE` / `BUDGET_CONSUMED`
- PLAY MAY say `That office requires a recognized Engineer.` (or Broker) on reject
- Public office lines and WATCH stay silent on the requirement. No titles
- Human `requires=engineer|broker` on `office create` is accepted and **not** added to Chamber help

Catalog: [`mastery-catalog.gc1-s5.json`](../specs/mastery-catalog.gc1-s5.json).  
Slice: [GC1-S5-OFFICE-ELIGIBILITY.md](../docs/GC1-S5-OFFICE-ELIGIBILITY.md).

## Alternatives rejected

| Alternative | Why |
|-------------|-----|
| Gate every `OPERATE_NAMED_ASSET` / treasury office | Changes unrestricted existing seats |
| WATCH / public titles | Leak |
| Class discounts on office or verb costs | Forbidden family |
| Evict when LATENT | Extra cycle machinery; recognition remains |
| `ROLE_*` / new assign verb | Extra catalog |
| Explorer / Surveyor required tracks | Out of this slice |

## Compatibility

Additive field. Worlds ignoring S5 keep assigning any member.

## Data / security

`requires_track` is an office property, not a Player title. Private recognition is consulted only at assign / designate / succession. WATCH does not carry it.

## Validation

`check_gc1_s5`: recognized Engineer/Broker may sit the matching office; unrecognized and wrong track reject; unrestricted stays open; LATENT still sits; no new verbs; no WATCH titles.

## Rollback

Ignore `requires_track` (treat every office as unrestricted).

## Unresolved

Focus as ledger. Public titles. Parameter-access upgrades.
