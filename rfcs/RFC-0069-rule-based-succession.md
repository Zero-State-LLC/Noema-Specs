# RFC-0069 — GC4-S6 RULE_BASED succession

## Status

**Accepted**

Specification-only until hosted. No `SUCCESSION_*` events. No elections. No rule language. No implicit jump. No `event-catalog/0.3`.

## Problem

[SUCCESSION.md](../docs/SUCCESSION.md) lists `RULE_BASED`. GC4-S4 needs a name list. GC4-S5 needs live consents. An implementer would invent a rule language or seat the oldest member without a published rule.

## Proposed change

Accept GC4-S6. One published rule on an office, exclusive of `DESIGNATED` successors:

- Operation: `COMMIT.ORG_SUCCESSION_RULE` with `office_id` and `rule_id=MEMBER_ORDER`
- Actor is founder or officer of an ACTIVE org. Retired offices reject
- Publishing clears any designated successor list. Designating later clears the rule
- On `ORG_OFFICE_VACATE` / holder leave-org: walk **current** `members` in stored order. Seat the first entered member who is not the departed holder and meets `requires_track`
- Zero eligible → office stays `VACANT`. No implicit jump
- Emergency scopes stay `DESIGNATED` only
- Cost: compute 1
- Events: `ENTITY_UPDATE` + `BUDGET_CONSUMED`. No `SUCCESSION_*`
- PLAY MAY say the rule was published, or that a successor was seated
- On seat, reuse `A designated successor has taken an institution office.` Publish-only is WATCH silent
- Human alias `succession rule <office> member_order` is accepted and **not** added to Chamber help

Catalog: [`authority-catalog.gc4-s6.json`](../specs/authority-catalog.gc4-s6.json).  
Slice: [GC4-S6-RULE.md](../docs/GC4-S6-RULE.md).

## Alternatives rejected

| Alternative | Why |
|-------------|-----|
| General rule language | Extra machinery |
| Implicit oldest / nearest | GC4-S4 implicit-jump reject |
| Elections | Out |
| Emergency-scope rules | Out of slice |
| `SUCCESSION_*` | Extra catalog |
| New WATCH title | Reuse existing pulse |

## Compatibility

Additive. DESIGNATED still fires when a successor list is present. CONSENSUS still fills a vacant office with no live designate/rule seat.

## Data / security

`rule_id` lives on the office succession record. Hidden rooms store none. WATCH silent until seat.

## Validation

`check_gc4_s6`: publish MEMBER_ORDER; vacate seats first remaining eligible member; none eligible stays vacant; unknown rule reject; no new events.

## Rollback

Ignore `ORG_SUCCESSION_RULE` (`INVALID_REQUEST`).

## Unresolved

`INHERITED_BY_ORGANIZATION` is [RFC-0070](RFC-0070-inherited-org.md). Other rule ids.
