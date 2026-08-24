# RFC-0043 — GC1-S3 Mastery Decay

## Status

**Accepted**

No new verbs. No `event-catalog/0.3`. No WATCH titles. No other-track benefits.

## Problem

[MASTERY-SPECIALIZATION.md](../docs/MASTERY-SPECIALIZATION.md) leaves LATENT after inactivity as SPEC GAP. After GC1-S2 the Engineer bonus never rusts, so recognition is a permanent class power.

## Proposed change

Accept GC1-S3:

- A recognized track goes **LATENT** after **12** cycles with no qualifying work on that track (same window as GC3-S4)
- LATENT PLAY uses a was-known line. Recognition evidence is not wiped
- **3** qualifying successes while LATENT restore MAINTAINED (same restitution count as GC3-S4)
- Engineer same-asset +5 applies only while Engineer is MAINTAINED
- First works during LATENT stay +15 even on a known asset
- No WATCH titles. No Explorer/Surveyor/Broker benefits. No `SPECIALIZATION_*` events

Catalog: [`mastery-catalog.gc1-s3.json`](../specs/mastery-catalog.gc1-s3.json).  
Slice: [GC1-S3-DECAY.md](../docs/GC1-S3-DECAY.md).

## Alternatives rejected

| Alternative | Why |
|-------------|-----|
| Wipe recognition | Ledger never forgets |
| 1-work restore | Makes decay a flicker |
| Decay all tracks into one timer | Tracks are independent |
| Public LATENT title | WATCH leak |

## Compatibility

Additive latency on existing practice cache. Worlds ignoring S3 stay S2-conformant (bonus never rusts).

## Data / security

Cache MAY store `last_work_cycle` and `latent_progress` per track. Rebuildable from qualifying events + `world.cycle`. WATCH stays silent.

## Validation

`check_gc1_s3`: idle 12 → LATENT, bonus 15; 11 idle stays 20; 3 rehab works restore 20; no new verbs or WATCH titles.

## Rollback

Ignore latency (S2 bonus whenever recognized + prior asset).

## Unresolved

Focus declaration. Public titles. Other-track benefits.
