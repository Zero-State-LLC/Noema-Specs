# RFC-0028 — GC5-S2 Rumor Provenance

## Status

**Accepted**

Closes the GC5-S2 SPEC GAP. A rumor is a claim that travels on ordinary `MESSAGE` (and existing institutional notice) with preserved source lineage. Not truth. Not a rumor engine. No `event-catalog/0.3`.

## Problem

[GC5-S1-DELAY.md](../docs/GC5-S1-DELAY.md) left rumor provenance as SPEC GAP. An implementer would add `RUMOR` / `SPREAD_RUMOR`, a gossip score, or an omniscient truth labeler.

## Proposed change

Accept GC5-S2:

```text
RUMOR ≠ TRUTH ≠ WORLD EVENT ≠ HIDDEN BACKEND KNOWLEDGE ≠ REPUTATION SCORE
```

- Represent rumor as `Information(type=CLAIM)` plus transmissions. No first-class Rumor table.
- Propagate through existing `MESSAGE` / `MESSAGE_DELIVERED`. Institutional `PUBLISH_NOTICE` may originate a PUBLIC claim.
- Unchanged retelling = new transmission, same claim. Material text change = new claim with `derived_from`.
- Failed `MESSAGE` creates no receipt. Delayed long-range uses GC5-S1 timing.
- Duplicate ancestry is not independent corroboration.
- PLAY/WATCH never present a rumor as fact. No rumor score.

Catalog: [`communication-catalog.gc5-s2.json`](../specs/communication-catalog.gc5-s2.json).  
Slice: [GC5-S2-RUMOR.md](../docs/GC5-S2-RUMOR.md).

## Alternatives rejected

| Alternative | Why |
|-------------|-----|
| `RUMOR` / `SPREAD_RUMOR` verb | MESSAGE already addresses a Player |
| `RUMOR_CREATED` family | Silent catalog 0.3 |
| Truth probability / gossip level | Universal score; doctrine reject |
| Omniscient true/false scanner | Leaks backend world truth |
| Counting copies as witnesses | Same origin, three transmissions ≠ three sources |
| LLM similarity | Non-deterministic |

## Compatibility

Additive. GC5-S0/S1 bands and delay unchanged. Ordinary `MESSAGE` without claim fields stays a private DM. Frozen catalogs unchanged.

## Data / security

No new table or service. Claim cache is a non-writer projection of `MESSAGE` / `MESSAGE_DELIVERED` (and existing notice `ENTITY_UPDATE`). Cross-world refs rejected. Originator cannot be forged. Private text stays off WATCH. Research/admin origins rejected.

## Validation

`check_gc5_s2`: retell / drift / shared-source / independent corroboration / delay / fail-closed / leak / forge / duplicate fixtures.

## Rollback

Omit claim fields on `MESSAGE`. DMs remain as S1.

## Unresolved

Board / SHOUT surfaces. Multi-hop delay. Reconstruction evidence kind for held claims. GC3 relational judgment from repeated false reports.
