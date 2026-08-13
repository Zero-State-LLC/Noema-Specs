# RFC-0008 — GC4-S0 Existing Roles as Bounded Authority

## Status

**Accepted**

Specification-only. No new verbs. No `event-catalog` expansion. No named-office freeze. No runtime implementation in this RFC.

## Problem

[INSTITUTIONAL-AUTHORITY.md](../docs/INSTITUTIONAL-AUTHORITY.md) forbids titles without authority and LLM assignment, but left the v0.1 role table as a SPEC GAP. [ACTION-CONTRACTS.md](../docs/ACTION-CONTRACTS.md) says `ORG_MEMBER_REMOVE` authorizer is “permitted” without naming the set. An implementation agent would invent Steward/Treasurer engines or `ROLE_*` events.

## Proposed change

Accept GC4-S0: treat `founder` / `officer` / `member` / `advisor` as closed authority configurations over existing `COMMIT.ORG_*` operations.

- Invite and non-self remove: `founder` or `officer` only
- Assignable invite roles: `officer`, `member`, `advisor` — never `founder`
- Self-leave required for every member role
- Last-founder guard: cannot remove the only founder while other members remain
- Cosmetic titles have zero authority

Catalog: [`authority-catalog.gc4-s0.json`](../specs/authority-catalog.gc4-s0.json).  
Slice: [GC4-FIRST-SLICE.md](../docs/GC4-FIRST-SLICE.md).

## Alternatives rejected

| Alternative | Why |
|-------------|-----|
| Freeze Steward / Treasurer names | Parent spec: capability is scopes, not the string |
| `ROLE_*` / event-catalog/0.3 | Silent catalog expansion; SUCCESSION already RFC-gates those types |
| New APPOINT verb | Verb inflation |
| Chat assignment | No LLM authority |
| Drop `advisor` | v0.1 role list already includes it; collapsing it to officer would invent power |

## Compatibility

Additive pin of existing v0.1 membership. Worlds already using founder/officer invite remain valid. Advisor stays non-authorizing for invite/remove.

## Data / security

No new entity class. No wallet or external office registry. Audit remains the existing `ORG_*` events (`actor` / `by`, org, target, role).

## Validation

`check_gc4_s0`: officer add accepted; member and advisor add forbidden; self-leave accepted; founder assign forbidden; last-founder remove forbidden; Steward title on a member does not authorize.

## Rollback

Omit the catalog. v0.1 contracts remain; “permitted” stays underspecified.

## Unresolved

GC4-S1: named offices as scope configs; institution-owned TRADE/REPAIR; vacancy / succession events if an RFC admits them.
