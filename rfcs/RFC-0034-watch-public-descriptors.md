# RFC-0034 — GC3-S2 WATCH Public Descriptor Bands

## Status

**Accepted**

Specification-only. No new verbs. No `event-catalog/0.3`. No reputation scalar. GC3-S0 / GC3-S1 stay WATCH-empty.

## Problem

[SOCIAL-MEMORY.md](../docs/SOCIAL-MEMORY.md) pins that WATCH MAY show coarse public descriptor bands from already-public events, else silent. Without an executable slice an implementer would project private GC3-S0/S1 lines, invent `unknown` as a hint, or put `reliable` on WATCH from private trades.

## Proposed change

Accept GC3-S2:

- WATCH (and any Player's public PLAY) MAY show `dangerous` or `deceptive` bands derived only from already-public events
- Public evidence (closed): `CONTEST_RESOLVED` (always public); `CRIME_DETECTED`, `AGREEMENT_BROKEN`, contradicted public `ATTEST` only when `visibility=PUBLIC`
- `TRADE_ACCEPTED`, `TRADE_REJECTED`, `MESSAGE`, private/institutional visibility → no WATCH band
- No `reliable` / `unknown` WATCH band in this slice (no public recognition event; silence is not `unknown`)
- GC3-S0 / GC3-S1 catalogs stay `watch_projection: false`

Catalog: [`social-memory-catalog.gc3-s2.json`](../specs/social-memory-catalog.gc3-s2.json).  
Slice: [GC3-S2-WATCH-PUBLIC.md](../docs/GC3-S2-WATCH-PUBLIC.md).

## Alternatives rejected

| Alternative | Why |
|-------------|-----|
| Project S0 `reliable` on WATCH | Leaks private dyadic trade counts |
| Emit `unknown` when silent | Silence is absence, not a hint |
| WATCH titles from S1 danger | S1 is subject-only |
| New REMEMBER / REPUTE verb | Verb inflation |

## Compatibility

Additive public projection. S0/S1 private lines unchanged.

## Data / security

Rebuildable. Lines name a public handle only. No amounts, routes, hidden ids, contest form, crime method, or private MESSAGE text.

## Validation

`check_gc3_s2`: public contest → dangerous band; three accepted trades → WATCH empty; private breach → WATCH empty; no forbidden tokens.

## Rollback

Omit the public band. S0/S1 remain. WATCH stays silent.

## Unresolved

None of the remaining SOCIAL-MEMORY SPEC GAP items. Institution edges, decay, friction, and deceptive are RFC-0035–0038.
