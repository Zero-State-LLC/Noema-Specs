# RFC-0053 — GC2-S4 archive_annex

## Status

**Accepted**

Specification-only until hosted. No new verbs. No `QUEST`. No oracle. No `event-catalog/0.3`.

## Problem

[CONSTRUCTION.md](../docs/CONSTRUCTION.md) lists `archive_annex` as a bounded class that changes record access. GC2-S0–S3 can build walls and workshops. INSPECT and ATTEST still cost full attention beside a reading room.

## Proposed change

Accept GC2-S4. Add constructible class `archive_annex` on existing `BUILD.CONSTRUCT` / `DISMANTLE`:

- Costs: energy 6, compute 4, storage 4, influence 2; salvage 2
- One live `archive_annex` per public room. Hidden rooms stay unbuildable
- Effect: while a live annex is in the room, **INSPECT** and **ATTEST** pay **−1 attention** (floor 0). Surveyor prior-work 0 stays 0
- No QUEST. No extra evidence invented. No reconstruction truth
- PLAY MAY say an archive annex is open. WATCH silent
- Chamber help still omits BUILD and ATTEST

Catalog: [`construction-catalog.gc2-s4.json`](../specs/construction-catalog.gc2-s4.json).  
Slice: [GC2-S4-ARCHIVE-ANNEX.md](../docs/GC2-S4-ARCHIVE-ANNEX.md).

## Alternatives rejected

| Alternative | Why |
|-------------|-----|
| QUEST / oracle | Doctrine |
| Extra invented evidence | Leak / oracle |
| Annex required to ATTEST | Soft-lock |
| WATCH annex ticker | Spectator leak |
| Help BUILD / ATTEST | S0 pins |

## Compatibility

Additive class. Worlds ignoring S4 keep S3 classes and full INSPECT/ATTEST attention.

## Data / security

Existing `ENTITY_CREATE` / `ENTITY_DESTROY`. Hidden rooms unbuildable.

## Validation

`check_gc2_s4`: class present; INSPECT/ATTEST attention −1 with annex; hidden reject; no QUEST; no new verbs.

## Rollback

Ignore `archive_annex`. Costs stay S3.

## Unresolved

UPGRADE/CONNECT. Abandonment. MESSAGE surface. Office eligibility.
