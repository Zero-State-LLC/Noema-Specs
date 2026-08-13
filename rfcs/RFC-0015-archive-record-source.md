# RFC-0015 — GC6-S0 Archive-Record Source

## Status

**Accepted**

Names the hosted archive-record source for GC6-S0. No new verbs. No `event-catalog` expansion. No Genesis pack. No flavor-text inference.

## Problem

[RFC-0010](RFC-0010-discovery-contradiction.md) accepted the contradiction projection but left *how* a Chamber Player obtains `{subject_entity_id, claim ∈ DESTROYED|OPERATING, accessible_to}` as a SPEC GAP. [GC6-FIRST-SLICE.md](../docs/GC6-FIRST-SLICE.md) blocked the hosted adapter so an implementer would not invent a Perihelion destroyed-relay pack or parse artifact labels.

## Proposed change

An **accessible archive record** exists for a Player only when all of:

1. The Player successfully `INSPECT`s a co-located entity whose `entity_type` is `ARTIFACT`.
2. That entity already carries **both** explicit fields:
   - `archive_subject_entity_id` — an `entity_id`
   - `archive_claim` — exactly `DESTROYED` or `OPERATING`
3. The acting Player is then listed in that record’s `accessible_to`.

A **live inspect member** exists when the same Player successfully `INSPECT`s the subject entity itself. Hosted S0 observation is `OPERATING` when that entity is present in a room at inspect time.

Rebuild stays [RFC-0010](RFC-0010-discovery-contradiction.md): same subject, both members accessible, claims disagree → PLAY line `The archive and the live site do not agree.`

Missing either explicit field is **no archive record**. Absence is not `DESTROYED`.

### Hosted presence

Perihelion Reach `entity.archive-ledger` does **not** carry those fields. Therefore **no hosted archive record exists today** and the conflict line **stays unprojected** on that world.

The projection MAY ship as a rebuildable cache. It MUST remain silent until an entity already has both fields. This RFC does not populate them.

## Alternatives rejected

| Alternative | Why |
|-------------|-----|
| Parse label / description / scar / World Services / WATCH | Flavor-text inference |
| Genesis `DESTROYED` claim on Relay Seven | RFC-0010 + first-world content freeze |
| Default missing claim to `DESTROYED` | Invents product behavior |
| New `ARCHIVE_*` events or verbs | Catalog expansion |
| Projection writes the fields | GC projections are non-writers |

## Compatibility

Additive pin under existing `INSPECT`. Frozen `action-contracts.v01.json` and `event-types.0.2.json` are unchanged. [HISTORICAL-ARTIFACTS.md](../docs/HISTORICAL-ARTIFACTS.md) already separates “artifact exists” from “artifact claims X”; this RFC names the two explicit claim fields Chamber may read.

## Data / security

Fields are evidence on an existing ARTIFACT, not WorldState writers from this projection. PLAY must not include `known_truth_relationship`, quest wording, relay topology, or hidden rooms. WATCH stays empty.

## Validation

`check_gc6_s0` plus this RFC Accepted: source fields named; flavor-text and Genesis pack rejected; hosted records absent ⇒ line unprojected.

## Rollback

Omit the source pin. Adapter stays blocked as before this RFC.

## Unresolved

Who may later set the two explicit fields (not Genesis on Perihelion). GC6-S1 reconstruction.
