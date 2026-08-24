# RFC-0070 — GC4-S7 INHERITED_BY_ORGANIZATION

## Status

**Accepted**

No `SUCCESSION_*` events. No institution-as-Player. No elections. No `event-catalog/0.3`.

## Problem

[SUCCESSION.md](../docs/SUCCESSION.md) lists `INHERITED_BY_ORGANIZATION`. GC4-S6 can auto-seat the next member. An implementer would retire the office, seat a person anyway, or make the org a Player.

## Proposed change

Accept GC4-S7. Reuse `COMMIT.ORG_SUCCESSION_RULE` with `rule_id=INHERITED_BY_ORGANIZATION`:

- Founder or officer of an ACTIVE org publishes it. Retired offices reject
- Publishing clears designated successors and `MEMBER_ORDER`
- On `ORG_OFFICE_VACATE` / holder leave-org: **do not auto-seat**. Office stays `VACANT` on the same org. It is not retired
- Founder/officer may still `ORG_OFFICE_ASSIGN` as today
- Cost: compute 1
- Events: `ENTITY_UPDATE` + `BUDGET_CONSUMED`. No `SUCCESSION_*`
- PLAY MAY say `The organization keeps {office}.` Vacate without a successor stays the existing resign/vacate line
- WATCH silent (no seat, no pulse)
- Human alias `succession rule <office> inherited` is accepted and **not** added to Chamber help

Catalog: [`authority-catalog.gc4-s7.json`](../specs/authority-catalog.gc4-s7.json).  
Slice: [GC4-S7-INHERITED.md](../docs/GC4-S7-INHERITED.md).

## Alternatives rejected

| Alternative | Why |
|-------------|-----|
| Institution-as-Player | ADMIN ≠ Player family |
| Auto-seat next member | That is `MEMBER_ORDER` |
| Retire the office | Org would lose the seat |
| Emergency inherit | Out of slice |
| `SUCCESSION_*` | Extra catalog |

## Compatibility

Additive rule id on the existing rule operation. `MEMBER_ORDER` and `DESIGNATED` unchanged when published instead.

## Data / security

`rule_id` on the office succession record. Hidden rooms store none. WATCH silent.

## Validation

`check_gc4_s7`: publish inherit; vacate stays vacant and unretired; unknown rule reject; no new events.

## Rollback

Ignore `rule_id=INHERITED_BY_ORGANIZATION` (`INVALID_REQUEST`).

## Unresolved

Other rule ids. Emergency inherit.
