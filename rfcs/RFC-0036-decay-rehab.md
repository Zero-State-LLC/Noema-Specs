# RFC-0036 — GC3-S4 Decay and Rehabilitation Weights

## Status

**Accepted**

Specification-only. No wipe verb. Ledger never forgets. No reputation scalar.

## Problem

[SOCIAL-MEMORY.md](../docs/SOCIAL-MEMORY.md) says old evidence loses weight and contrary public evidence can rehabilitate, but left floors as SPEC GAP. An implementer would delete ledger rows, sell a wipe, or auto-clear danger after one trade.

## Proposed change

Accept GC3-S4 as a **weight overlay** on GC3-S0/S1/S3/S6 derived lines:

- `decay_cycles = 12`: if no new evidence of that family toward that object arrives for 12 cycles, the family's PLAY/WATCH line is omitted (weight 0). Events remain in history
- Rehab: 3 distinct `TRADE_ACCEPTED` with that object **after** the last danger/deceptive evidence id → omit the hostile line. Trade lines may remain
- No paid wipe. No `FORGIVE` verb
- `CONTESTED` remains when a live positive family and a live hostile family both have weight > 0 (both lines may show)

Catalog: [`social-memory-catalog.gc3-s4.json`](../specs/social-memory-catalog.gc3-s4.json).  
Slice: [GC3-S4-DECAY-REHAB.md](../docs/GC3-S4-DECAY-REHAB.md).

## Alternatives rejected

| Alternative | Why |
|-------------|-----|
| Delete or rewrite ledger events | Deep Time / historical persistence |
| Paid wipe / FORGIVE verb | Doctrine + verb inflation |
| Decay on first idle cycle | Too fast; scars must last a season |
| Rehab on one trade | Too cheap; matches S0 reliable floor of 3 |

## Compatibility

Overlay only. Event catalogs unchanged. S0/S1 thresholds unchanged.

## Data / security

Rebuild takes `as_of_cycle`. No new stored facts. Lines still forbid leak tokens.

## Validation

`check_gc3_s4`: danger at cycle 0 is omitted at cycle 13 with no new evidence; three later trades omit danger and keep the trade line.

## Rollback

Ignore weights; project S0/S1/S3/S6 at full weight forever.

## Unresolved

None for decay/rehab. Trade-friction uses **live** (non-decayed) edges only (RFC-0037).
