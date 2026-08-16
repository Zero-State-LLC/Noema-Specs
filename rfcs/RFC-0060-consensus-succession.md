# RFC-0060 — GC4-S5 CONSENSUS succession

## Status

**Accepted**

Specification-only until hosted. No `SUCCESSION_*` events. No elections. No `RULE_BASED`. No `event-catalog/0.3`.

## Problem

[SUCCESSION.md](../docs/SUCCESSION.md) lists `CONSENSUS` as a closed mechanism. GC4-S4 only fills a vacancy from a predeclared list. An empty office with no eligible designate stays vacant unless a founder assigns.

## Proposed change

Accept GC4-S5. Members of an ACTIVE org may consent a candidate onto a **VACANT** office:

- Operation: `COMMIT.ORG_SUCCESSION_CONSENT` with `office_id` and `candidate_id`
- Actor and candidate must be current members in this world
- Occupied / retired offices reject
- Latest consent per member wins
- Seat when distinct live consents for one candidate ≥ `ceil(members/2)`. A tie seats no one
- GC1-S5 `requires_track` still applies
- Cost: compute 1
- Events: `ENTITY_UPDATE` + `BUDGET_CONSUMED`. No `SUCCESSION_*`
- PLAY MAY say the consent was recorded, or that consensus filled the office
- On seat, reuse the existing WATCH pulse `A designated successor has taken an institution office.` Consent-only updates are WATCH silent
- Human alias `consent <office> <player>` is accepted and **not** added to Chamber help

Catalog: [`authority-catalog.gc4-s5.json`](../specs/authority-catalog.gc4-s5.json).  
Slice: [GC4-S5-CONSENSUS.md](../docs/GC4-S5-CONSENSUS.md).

## Alternatives rejected

| Alternative | Why |
|-------------|-----|
| Elections / parties | Out |
| RULE_BASED | Needs a rule language |
| Occupied-office vote | Not a recall |
| Emergency-scope consensus | Out of this slice |
| `SUCCESSION_*` | Extra catalog |
| New WATCH title | Reuse existing pulse |

## Compatibility

Additive. DESIGNATED succession still fires first on vacate.

## Data / security

Consents live on the office. Dropped when the member leaves or the office seats/retires. WATCH silent until seat.

## Validation

`check_gc4_s5`: threshold seats; short of majority records only; occupied / non-member reject; no new events.

## Rollback

Ignore `ORG_SUCCESSION_CONSENT` (`INVALID_REQUEST`).

## Unresolved

RULE_BASED. Institution-owned constructibles. Multi-cycle.
