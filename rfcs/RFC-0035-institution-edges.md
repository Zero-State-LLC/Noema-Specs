# RFC-0035 — GC3-S3 Institution→Player Edges

## Status

**Accepted**

Specification-only. No new verbs. No `ROLE_*`. No `event-catalog/0.3`. WATCH empty.

## Problem

[SOCIAL-MEMORY.md](../docs/SOCIAL-MEMORY.md) allows Institution→Player memory from records the institution is authorized to hold, but left the edge as SPEC GAP. Scenario B requires institutional expectation change after a public breach. An implementer would copy private Player edges onto the org, emit `ROLE_*`, or put institutional standing on WATCH.

## Proposed change

Accept GC3-S3:

- Derived directed `org_id` → `player_id` edges rebuilt from that org's authorized ledger
- Evidence (closed): `TRADE_ACCEPTED` with `acting_for=org`; `ORG_MEMBER_ADD` / `ORG_MEMBER_REMOVE` for that org; `CONTEST_RESOLVED` where the org is defender/`acting_for`; `AGREEMENT_BROKEN` where the org is a party
- Officers (founder/officer) see the org's PLAY lines. A member sees only their own standing with that org. Other Players and WATCH empty
- A successor inherits the **institution's** edges, not another Player's private S0/S1 edges

Catalog: [`social-memory-catalog.gc3-s3.json`](../specs/social-memory-catalog.gc3-s3.json).  
Slice: [GC3-S3-INSTITUTION-EDGES.md](../docs/GC3-S3-INSTITUTION-EDGES.md).

## Alternatives rejected

| Alternative | Why |
|-------------|-----|
| Copy private Player edges onto the org | Unauthorized knowledge |
| `ROLE_*` / catalog 0.3 | RFC-0008 / RFC-0023 |
| WATCH institutional titles | Leak / presentation |
| Player→Institution private opinion as WorldState | Interpretation stays private; not this slice |

## Compatibility

Additive derived projection. GC4 offices and RFC-0029 institution TRADE/REPAIR already exist.

## Data / security

Rebuildable cache. No amounts, hidden ids, or other orgs' records.

## Validation

`check_gc3_s3`: org-acted trade credits the org; personal trade does not; WATCH empty; non-officer third party empty.

## Rollback

Omit the institutional projection. S0/S1/S2 remain.

## Unresolved

Decay/rehab of these edges is RFC-0036. Friction from them is RFC-0037.
