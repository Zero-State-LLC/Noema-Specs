# RFC-0023 — GC4-S1 Named Institutional Offices

## Status

**Accepted**

Closes the GC4-S0 named-office SPEC GAP. Membership roles stay. No `ROLE_*` events. No `event-catalog/0.3`. No elections, payroll, or employment engine.

## Problem

[INSTITUTIONAL-AUTHORITY.md](../docs/INSTITUTIONAL-AUTHORITY.md) requires a title to bind scoped authority, but left named offices as SPEC GAP. An implementer would freeze Steward/Treasurer as engines, merge offices into `founder`/`officer`, or emit `ROLE_ASSIGNED`.

## Proposed change

Accept GC4-S1:

- Office ≠ Player ≠ membership role ≠ employment ≠ authority itself
- Persistent record on the owning organization: may be `VACANT`, `OCCUPIED`, or `RETIRED`
- Holder departure vacates; it does not destroy the office
- Display name is Player-chosen; authority is a closed profile, not the string
- Membership role remains the coarse grant (`ORG_*`). Office is an additional scoped position
- Create / assign / vacate / retire / act via `COMMIT.ORG_OFFICE_*` (same COMMIT grouping as ATTEST). No new top-level verb in frozen `action-contracts.v01.json`
- Evidence: existing `ENTITY_CREATE` (create, `entity_type=DOCUMENT`, `location=null`) and `ENTITY_UPDATE` (assign, vacate, retire, act). Not `ROLE_*`, not `ORG_MEMBER_*`

Catalog: [`office-catalog.gc4-s1.json`](../specs/office-catalog.gc4-s1.json).  
Slice: [GC4-S1-OFFICES.md](../docs/GC4-S1-OFFICES.md).

## Alternatives rejected

| Alternative | Why |
|-------------|-----|
| Merge office into membership role | Prompt and parent: separate concepts |
| `ROLE_*` / catalog 0.3 | Doctrine + SUCCESSION RFC-gate |
| One engine per Treasurer/Archivist | Complexity Doctrine |
| Elections / succession machine | Parent DEFER; S1 is manual reassignment |
| Institution TRADE/REPAIR engine | Still later; S1 hosted exercise is `PUBLISH_NOTICE` |
| Chat “I am Treasurer” | No LLM authority |

## Compatibility

Additive. GC4-S0 founder/officer/member/advisor unchanged. Frozen catalogs unchanged.

## Data / security

Rebuildable office map on the organization (WorldRuntime / world head). Not a new database. Controller/session change does not vacate. Cross-world assignment is `FORBIDDEN`. Operator assignment still needs an operator receipt (out of PLAY).

## Validation

`check_gc4_s1`: create/assign/act/resign/reassign persist identity; unauthorized and retired paths reject; no `ROLE_*`.

## Rollback

Omit the office map and `ORG_OFFICE_*` operations. Membership authority remains.

## Unresolved

Institution-owned TRADE/REPAIR, emergency scopes, designated succession, extra profiles beyond hosted `PUBLISH_NOTICE`.
