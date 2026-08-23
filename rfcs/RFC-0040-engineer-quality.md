# RFC-0040 — GC1-S2 Same-Asset Engineer Quality

## Status

**Accepted**

No new verbs. No `event-catalog/0.3`. Not a level percent. Changes the frozen `REPAIR` condition write only when a world procedure applies.

## Problem

GC1-S1 makes a Player known to themselves as Engineer. Completeness scenario A also requires one world-native benefit. Adding +2 (or any bonus) to every `REPAIR` would be a class power. Leaving recognition as lines-only leaves scenario A incomplete.

## Proposed change

Accept GC1-S2:

- S1-recognized Engineer (`track.engineer.01`, 3 distinct repaired `entity_id`s)
- Successful `REPAIR` of an `entity_id` this **Player** already successfully repaired (any earlier success, including before recognition) writes condition **+20** (frozen +15 plus **+5**), cap **100**
- First repair of that asset stays +15
- Applies to personal pay **and** `acting_for` with occupied `OPERATE_NAMED_ASSET`; evidence is the acting Player
- Costs, targets, eligibility unchanged
- No WATCH titles; no decay; no other tracks

Catalog: [`mastery-catalog.gc1-s2.json`](../specs/mastery-catalog.gc1-s2.json).  
Slice: [GC1-S2-ENGINEER-QUALITY.md](../docs/GC1-S2-ENGINEER-QUALITY.md).

## Alternatives rejected

| Alternative | Why |
|-------------|-----|
| +N on every REPAIR | Level percent (RFC-0005) |
| Workshop-gated bonus | No workshop class on Perihelion |
| Only post-recognition prior work | Re-taxes work already done |
| Free / cheaper REPAIR cost | Naked cost discount |
| Public Engineer title | Leak; out of S1/S2 |

## Compatibility

Additive quality on a subset of REPAIR successes. Worlds ignoring S2 remain S1-conformant (+15 always).

## Data / security

Optional `quality_bonus: 5` on `ENTITY_UPDATE`. Rebuildable from engineer recognition `entity_id`s. WATCH MUST NOT narrate the bonus.

## Validation

`check_gc1_s2`: unrecognized or first-on-asset → 15; recognized + prior entity → 20; cap 100; no new verbs.

## Rollback

Always write +15.

## Unresolved

Decay / latent / public titles / other-track benefits remain later.
