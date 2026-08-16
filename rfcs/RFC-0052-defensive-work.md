# RFC-0052 — GC2-S3 defensive_work

## Status

**Accepted**

Specification-only until hosted. No new verbs. No `event-catalog/0.3`. No HP. No new contest form.

## Problem

[CONSTRUCTION.md](../docs/CONSTRUCTION.md) lists `defensive_work` as a bounded class that changes contest resistance. GC2-S0–S2 can build production and workshops. Contests still ignore walls.

## Proposed change

Accept GC2-S3. Add constructible class `defensive_work` on existing `BUILD.CONSTRUCT` / `DISMANTLE`:

- Costs: energy 7, compute 3, storage 4, influence 3; salvage 2
- One live `defensive_work` per public room. Hidden rooms stay unbuildable
- Effect: a live work in the contest room adds **50 millipoints** of defense on existing forms (subtracted from the published score like infra condition)
- No HP. No new form. No change to S0 arithmetic when no work is present
- PLAY MAY say a defensive work stands. WATCH silent
- Chamber help still omits BUILD

Catalog: [`construction-catalog.gc2-s3.json`](../specs/construction-catalog.gc2-s3.json).  
Slice: [GC2-S3-DEFENSIVE-WORK.md](../docs/GC2-S3-DEFENSIVE-WORK.md).

## Alternatives rejected

| Alternative | Why |
|-------------|-----|
| Hit points | Doctrine |
| New contest form | event-catalog / help |
| Change published S0 weights | Breaks GC7-S0 fixtures |
| WATCH fort ticker | Spectator leak |
| Help BUILD / CONTEST | S0 pins |

## Compatibility

Additive class. Worlds ignoring S3 keep S2 classes and S0 contest scores.

## Data / security

Existing `ENTITY_CREATE` / `ENTITY_DESTROY`. Hidden rooms unbuildable.

## Validation

`check_gc2_s3`: class present; +50 defense with work; S0 score unchanged without; hidden reject; no HP/new form.

## Rollback

Ignore `defensive_work`. Scores stay S0.

## Unresolved

`archive_annex`. UPGRADE/CONNECT. Abandonment.
