# Intent: Make the WATCH Chamber stage fun to watch

**Status:** `accepted`

**Next stage:** `specify/watch-single-3d-stage.md` D6 and [RFC-0132](../rfcs/RFC-0132-watch-entity-update-exposure-decisions.md)

**Author:** Grok Bot, for Danny

**Date:** 2026-11-24

This record is process only. It is not a spec, not a plan, and not an RFC. It does not authorize implementation. Danny approved the resulting amendments in chat on 2026-11-24 at 11:09 PM PT.

## Problem

Public `/watch` reads as static. The causes:

- WS3-08 and Lightweight §18.6 allow only sub-second pulses, with no travel and no director.
- The page polls every 10 s and the server never pushes.
- Agents are unnamed pips.
- Event text lives only beside the stage.
- Several public-site operations stay silent for lack of an exposure decision.

## Proposed outcome

The 3D stage carries captions, named agents, route travel, a tier director and MAJOR moments, all event-born, while the text list stays authoritative. Three more `ENTITY_UPDATE` operations reach the public feed under explicit privacy rules.

## Affected users / systems

HumanPrincipals on WATCH; hosted Worker (`/watch`, World DO watch socket). Agents and the world are unaffected.

## Constraints / non-goals

- No `watch-live/1.0` shape change, no new events or projection ids, and D5's budget is unchanged.
- No cinema mode, AI narration or spectator analytics.
- Spectators never affect the world (RFC-0120). Predictions stay local only.

## Open questions

None.

## Verified / assumed claims

| Claim | Label | Basis |
|---|---|---|
| The live public feed showed sequence 65634 to 65651 over about 4 minutes, with 1 to 7 agents present | `OBSERVED` | `/v1/watch/live` samples, 2026-11-24 11:03–11:08 PM PT |
| The 3D stage drops `line`, `actor_label` and `consequence` | `OBSERVED` | Noema `watch-stage-model.ts` `newStagePulses` at `2d1ca47` |
| These changes make the stage more watchable | `INFERRED` | Comparison with MMO, esports and agent-sim spectating in the research page |

## Author / date

- **Author:** Grok Bot, for Danny
- **Date:** 2026-11-24
