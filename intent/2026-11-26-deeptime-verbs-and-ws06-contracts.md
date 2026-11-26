# Intent: Deep Time Intervention Verbs, Multi-Agent Construction, Civic Contracts (WS06) & Mastery Track Expansion

**Status:** `accepted`

**Next stage:** [RFC-0137](../rfcs/RFC-0137-deeptime-interventions-and-joint-construction.md) and [RFC-0138](../rfcs/RFC-0138-ws06-civic-contracts-and-mastery-tracks.md)

**Author:** Antigravity, for Danny

**Date:** 2026-11-26

This record is process only. It is not a spec, not a plan, and not an RFC. Danny approved the Phase 3 roadmap (`orin_deeptime_mechanics_plan.md`) in chat on 2026-11-25.

## Problem

1. **Deep Time has no player-initiated stewardship verbs:** Once a room accumulates economic scars or crystallizes a `LoreAttractor` (`deep-time.ts`), players cannot actively remediate a pre-fossilization economic scar or commemorate a fossilized scar / crystallized lore basin into lasting civic memory.
2. **Multi-cycle construction is single-actor:** `construction.ts` already marks all 8 classes as `MULTI_CYCLE_CLASSES`, yet co-located allies cannot contribute materials or engineering progress to an in-progress public construction site.
3. **Contract Clerk WS06 has no escrowed civic work orders:** `world-services.ts` defines Contract Clerk WS06, but organizations cannot post bounded, escrowed civic contracts (e.g., repair/attest bounties) that external third-party agents and resident agents can fulfill without open-ended `TRADE` spam.
4. **Archivist and Herald/Speaker roles have no native mastery tracks:** `practice.ts` and `focus.ts` only cover `explorer`, `surveyor`, `broker`, and `engineer`.

## Proposed outcome

1. **`RFC-0137` (`COMMEMORATE`, `REMEDIATE`, `BUILD_CONTRIBUTE`):**
   - `COMMEMORATE` turns a crystallized `LoreAttractor` or fossilized scar into a permanent public commemorative trace/monument granting `-1` attention cost on historical/civic actions in that room (and rendering a golden monument beam on `/watch`).
   - `REMEDIATE` spends cargo + energy to accelerate pre-fossilization economic scar decay and restore `co_evolution.regen_mod` in over-harvested rooms (never altering irreversible `DISMANTLE` `scar: true` ruins from `RFC-0051`).
   - `BUILD_CONTRIBUTE` lets any co-located ally contribute progress to an `in_progress` construction site (reducing remaining cycles / advancing completion).
2. **`RFC-0138` (WS06 Civic Contracts + `archivist` & `herald` Mastery Tracks):**
   - Bounded, escrowed `CONTRACT_POST` / `CONTRACT_FULFILL` at Contract Clerk WS06 (max 3 open contracts per org, escrowed cargo or influence reward, verifiable deterministic completion predicate: entity condition target or room attestation count).
   - Two new derived practice & focus tracks: `track.archivist.01` (`RECONSTRUCT`/`ATTEST` mastery) and `track.herald.01` (`PUBLISH_NOTICE`/corroborated `rumor`/`BOARD` mastery), preserving all 4 existing tracks unchanged.

## Affected users / systems

Hosted World Engine (`deep-time.ts`, `construction.ts`, `practice.ts`, `focus.ts`, `actions.ts`, `world-actions.ts`, `watch-live.ts`, `watch-room-stage-client.js`), `noema-client`, `noema-orin`, and HumanPrincipals on `/watch`.

## Constraints / non-goals

- `RFC-0051` irreversible `DISMANTLE` `scar: true` ruins MUST remain unrepairable and un-remediable.
- All new mastery tracks remain rebuildable derived caches (`practice.ts`), never raw numeric XP scalars on `/watch`.
- Contracts are deterministic, bounded, and escrowed; no unbounded debt or free-text script execution.

## Verified / assumed claims

| Claim | Label | Basis |
|---|---|---|
| `construction.ts` marks all 8 infrastructure classes in `MULTI_CYCLE_CLASSES` | `OBSERVED` | `workers/noema/src/construction.ts` lines 129–138 |
| `world-services.ts` defines Contract Clerk `WS06` | `OBSERVED` | `workers/noema/src/world-services.ts` line 85 |
| `practice.ts` currently defines 4 tracks (`explorer`, `surveyor`, `broker`, `engineer`) | `OBSERVED` | `workers/noema/src/practice.ts` lines 10–47 |
| Escrowed civic contracts + active Deep Time verbs strengthen resident ↔ third-party agent cooperation | `INFERRED` | Approved `orin_deeptime_mechanics_plan.md` |

## Author / date

- **Author:** Antigravity, for Danny
- **Date:** 2026-11-26
