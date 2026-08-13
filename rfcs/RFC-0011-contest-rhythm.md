# RFC-0011 — GC7-S0 Existing Contest Rhythm

## Status

**Accepted**

Hosted runtime shipped (isolated declare → resolve). Does **not** mutate `event-catalog/0.2`. Does **not** add forms or Chamber help.

## Problem

[STRATEGIC-CONFLICT.md](../docs/STRATEGIC-CONFLICT.md) GC7 left the RECON→RECOVER rhythm and anti-HP fixtures as SPEC GAP. An implementation agent would add `SCAN`/`ATTACK`, a fifth form, or `event-catalog/0.3`.

## Proposed change

Accept GC7-S0: a closed stage→verb table over existing v0.1/v0.2 operations, the existing four contest forms, and rejection tests for combat verbs, catalog mutation, hidden-fact leak, and character death.

Catalog: [`conflict-catalog.gc7-s0.json`](../specs/conflict-catalog.gc7-s0.json).  
Slice: [GC7-FIRST-SLICE.md](../docs/GC7-FIRST-SLICE.md).

`contest-config.v02.json`, `action-contracts.v02.json`, and `event-types.0.2.json` are **not** part of this change.

## Alternatives rejected

| Alternative | Why |
|-------------|-----|
| New conflict canon | Parent: extend v0.2 |
| Silent 0.3 / new forms | Completeness plan + parent SPEC GAP |
| HP combat | Doctrine |
| Withdraw in S0 | Still SPEC GAP |

## Compatibility

Additive pin. Existing v0.2 trajectories remain valid. First-world Chamber PLAY is not blocked.

## Data / security

No new entity class. Contest projection must not include hidden ids, private holdings, or HP.

## Validation

`check_gc7_s0`: legal rhythm accepts; `ATTACK` forbidden; unknown form forbidden; hidden projection leaks; death forbidden; catalog still names `event-catalog/0.2`.

## Rollback

Omit the catalog. v0.2 contracts remain.

## Unresolved

GC7-S1: withdraw/de-escalate; information-target form (only with a later RFC); institution-as-party.
