# RFC-0089 — GC2-S24 SHARE family closeout

## Status

**Accepted**

Specification-only until hosted. No sixth stamp. No N-of-M roster. No `STRUCTURE_*`. No `event-catalog/0.3`. Help still omits BUILD. WR-S0 stays [RFC-0088](RFC-0088-world-report.md).

## Problem

[GC2-S23-FIFTH-CO-OWNER.md](../docs/GC2-S23-FIFTH-CO-OWNER.md) names five co-owners and lists later stamps as leftover. An implementer would add `co_owner_6_id`, then seven, forever. S20 already rejected a roster. The leftover is closed by stopping.

## Proposed change

Accept GC2-S24. The SHARE family is **done**:

- Cap stays **5** co-owners (`co_owner_id` … `co_owner_5_id`)
- A sixth SHARE stays `FORBIDDEN`
- N-of-M roster stays closed
- Owner still names. Co-owner still cannot SHARE
- No new field. No new verb. No new event
- WATCH silent. Chamber help still omits BUILD

Catalog: [`construction-catalog.gc2-s24.json`](../specs/construction-catalog.gc2-s24.json).  
Slice: [GC2-S24-SHARE-CLOSEOUT.md](../docs/GC2-S24-SHARE-CLOSEOUT.md).

## Alternatives rejected

| Alternative | Why |
|-------------|-----|
| `co_owner_6_id` | Treadmill |
| N-of-M roster | Extra machinery; S20 pin |
| Lower the cap | Would strand existing stamps |
| Help BUILD | S0 pin |

## Compatibility

No new stamp. Worlds at S23 already match this cap.

## Data / security

No new fields. Hidden rooms store none. WATCH silent.

## Validation

`check_gc2_s24`: family closed; max stays 5; sixth SHARE rejected; no roster; no new verbs.

## Rollback

Keep S23 catalog id (behavior identical).

## Unresolved

First-world PLAY advertising BUILD (forbidden).
