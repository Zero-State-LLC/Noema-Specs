# RFC-0010 — GC6-S0 Archive vs Live Inspect

## Status

**Accepted**

Specification-only. No new verbs. No `event-catalog` expansion. No quest UI. No runtime implementation in this RFC.

## Problem

[SYSTEMIC-DISCOVERY.md](../docs/SYSTEMIC-DISCOVERY.md) forbids authored quests but left the Relay Seven pattern (archive says destroyed, entity operating) and oracle-leak fixtures as SPEC GAP. An implementation agent would add a quest log or tell PLAY which signal is true.

## Proposed change

Accept GC6-S0: a derived, self-only PLAY contradiction when the same Player holds an accessible archive claim and a live `INSPECT` of the same entity that disagree on `{DESTROYED, OPERATING}`.

- Reuse contradiction-set semantics: `resolution_status=open`, `agent_visible_relationship=unresolved`
- One PLAY line; WATCH empty
- `known_truth_relationship` stays research-only
- Discovery state `investigated`, never `understood`
- No events, no ledger write

Catalog: [`discovery-catalog.gc6-s0.json`](../specs/discovery-catalog.gc6-s0.json).  
Slice: [GC6-FIRST-SLICE.md](../docs/GC6-FIRST-SLICE.md).

## Alternatives rejected

| Alternative | Why |
|-------------|-----|
| QUEST verb / quest log | Doctrine: no quest engine |
| Engine names the true signal | Parent + contradiction-set research partition |
| DISCOVERY_* events | Silent catalog expansion |
| WATCH pulse in S0 | Leak / presentation risk |
| Genesis “destroyed relay” pack | First-world content freeze |

## Compatibility

Additive derived projection. Existing `INSPECT` and Deep Time archive/contradiction schemas stay authoritative.

## Data / security

Rebuildable cache. PLAY must not include `known_truth_relationship`, quest wording, or hidden entity internals. Private to the subject who holds both members.

## Validation

`check_gc6_s0`: Relay Seven pair shows the conflict line; inspect-only is silent; agreeing pair is silent; third party and WATCH empty; research truth tokens forbidden in PLAY.

## Rollback

Omit the projection.

## Unresolved

GC6-S1: Player-compiled historical reconstruction; settled-for-Player vs settled-for-world; public contradiction WATCH without oracle leak.
