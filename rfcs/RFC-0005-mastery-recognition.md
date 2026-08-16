# RFC-0005 — Mastery Recognition Projection (GC1-S1)

## Status

**Accepted**

Approved for specification-only implementation on 2026-08-13. Not a world-event catalog expansion. Not a mechanical-benefit RFC. Runtime may project recognized PLAY lines under [GC1-S1-RECOGNITION.md](../docs/GC1-S1-RECOGNITION.md).

## Problem

GC1-S0 shows that a Player has been practicing. Completeness scenario A also requires a **recognized specialization**. Recognition thresholds were left as SPEC GAP. A runtime agent must not invent them.

A first mechanical benefit would change frozen v0.1 `REPAIR` magnitudes. That is a different RFC (GC1-S2).

## Context

- [GC1-S1-RECOGNITION.md](../docs/GC1-S1-RECOGNITION.md)
- [GC1-FIRST-SLICE.md](../docs/GC1-FIRST-SLICE.md) (S0 shipped)
- [RFC-0004](RFC-0004-derived-mastery-projection.md) (**Accepted**)
- Live Perihelion Reach is **cycle 0**; recognition must not require cycle advance

## Proposed change

Accept GC1-S1 as derived recognition on the four S0 tracks:

- Distinct-unit thresholds: explorer 5 rooms, surveyor 5 entities, broker 3 trades, engineer 3 repaired entities
- Self-only PLAY line replacement
- No new events, verbs, costs, or WATCH projection

Exact rules live in [GC1-S1-RECOGNITION.md](../docs/GC1-S1-RECOGNITION.md).

## Alternatives

| Alternative | Why rejected |
|-------------|--------------|
| Recognition + REPAIR +2 now | Mutates frozen action-contract quality; split as S2 |
| Distinct-cycle anti-spike | Fails on cycle-0 worlds |
| Public titles | Leak / presentation; wait until self-recognition is stable |
| New `SPECIALIZATION_RECOGNIZED` event | Silent catalog expansion |

## Compatibility

Additive derived projection. S0 practicing lines remain for sub-threshold tracks. Worlds ignoring this RFC remain S0-conformant.

## Data impact

Optional extra derived fields (engineer `entity_id` set). No ledger rewrite. Pre-S1 hosted caches cannot reconstruct distinct repair targets (**NOT_COMPUTABLE**).

## Research impact

None on Lab / Compiler / LEARN. Recognition is not a capability claim.

## Security impact

Still Player-private. No affordance leak.

## Migration

S0 caches remain valid for practicing. Recognition starts empty until enough distinct units accrue after S1 implementation.

## Validation

- Catalog: [`specs/mastery-catalog.gc1-s1.json`](../specs/mastery-catalog.gc1-s1.json)
- Fixtures: [`examples/gc1-mastery/rebuild-s1-recognized.json`](../examples/gc1-mastery/rebuild-s1-recognized.json), [`examples/gc1-mastery/rebuild-s1-below-threshold.json`](../examples/gc1-mastery/rebuild-s1-below-threshold.json)
- Validator: `check_gc1_s1` executes the rebuild and forbids Engineer recognition from one-entity spam

## Rollback

Leave Draft or Reject. Runtime omits recognized lines.

## Unresolved questions

1. GC1-S2 opened as [RFC-0040](RFC-0040-engineer-quality.md) (same-asset procedure, not a level percent). Decay / public titles remain later.
