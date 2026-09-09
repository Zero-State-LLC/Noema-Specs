# One public spectator door (`/watch`)

**Kind:** thin presentation amend. Plan and docs only in this repository.  
**Status:** Specified. One-door unify shipped. Gate D COMPLETE is recorded in [LCA-GATE-D-PROMOTION-2026-09-09.md](../docs/LCA-GATE-D-PROMOTION-2026-09-09.md), not in this amend.
**Date:** 2026-09-09  
**RFC:** No. No new verbs, events, protocol fields, or gates.  
**Authority to patch:** [WATCH-LIGHTWEIGHT-SPECTATOR.md](../docs/WATCH-LIGHTWEIGHT-SPECTATOR.md), [WATCH-REAL-TIME-MAPPING.md](../docs/WATCH-REAL-TIME-MAPPING.md), and the WATCH pointers they name.  
**Campaign pointer:** [LCA-GATE-D-SCENARIO.md](../docs/LCA-GATE-D-SCENARIO.md)

This file is a proposed patch to existing WATCH presentation contracts. It does not replace those contracts. It does not authorize a Worker publish.

## Workflows

- **google-developer-style** — lead with the task, use short present-tense sentences, prefer tables over prose, do not invent jargon.
- **SKILL.SPEC_CHANGE** — edit the smallest canonical WATCH surface, then pointers, checklist, and changelog.
- **SKILL.EXPERIENCE** — keep PLAY, WATCH, and STUDY separate; WATCH stays a derived spectator projection.
- **Owner specialist:** WATCH public spectator door.
- **Existing Action:** reuse repository validation (`.github/workflows/` unchanged). Do not add a workflow.
- Do not invent an RFC, skill, bot, verb, or gate.

## Goal

The public spectator door is one `/watch`.

`TEXT`, `PIXEL`, and `MAP` are modes of that door. Mapping is progressive enhancement of the same world heads. It is not a second app.

Phosphor rules stay unchanged. Spectator projection is not world truth.

## Current drift (OBSERVED)

| Surface | Observation |
|---|---|
| Live product (at amend) | `/watch` and `/watch/map` were dual public pages |
| Specs before this amend | Mapping is a separate opt-in route |
| Gate D runtime score | PASS recorded in Noema [#679](https://github.com/Zero-State-LLC/Noema/pull/679) (Danny human-yes on the score) |
| Runtime unify | Noema [#680](https://github.com/Zero-State-LLC/Noema/pull/680) `39d4856abd857b79aedd4304987ef6d7593d000a` Deployed; live Worker `592c06a4-fa8c-40f6-bec7-21cbc45689f9` |
| Specs Gate D | COMPLETE recorded in [LCA-GATE-D-PROMOTION-2026-09-09.md](../docs/LCA-GATE-D-PROMOTION-2026-09-09.md). This amend specified the door; it is not the promotion packet |

## Decision

1. Name `/watch` as the only public spectator door.
2. Name three modes on that door:

   | Mode | Role | Authority |
   |---|---|---|
   | `TEXT` | Semantic HTML graph plus optional ASCII cartogram | Complete and authoritative |
   | `PIXEL` | NOEMA Phosphor Cartography | [WATCH-LIGHTWEIGHT-SPECTATOR.md](../docs/WATCH-LIGHTWEIGHT-SPECTATOR.md) §18, unchanged |
   | `MAP` | Richer layered mapping | [WATCH-REAL-TIME-MAPPING.md](../docs/WATCH-REAL-TIME-MAPPING.md); same world heads |

3. Keep one map at a time. The TEXT cartogram, PIXEL canvas, and MAP canvas MUST NOT render together.
4. Keep `PIXEL` as the default first-glance cartography when Canvas 2D is available. `MAP` is opt-in enhancement. `TEXT` stays one keystroke away and remains complete.
5. Treat `GET /v1/watch/map` (`watch-map/1.0`) as an optional band payload, not a second spectator app. MAP mode MUST show the same `world_id`, `cycle`, `sequence`, and `freshness` as `GET /v1/watch/live`.
6. A historical `/watch/map` URL MAY redirect to `/watch` with MAP selected. It MUST NOT remain a second public application with a separate world head.
7. Do not change Phosphor glyph, motion, privacy, or TEXT-authority rules.
8. Do not change spectator-is-not-truth copy or redaction.

## Plan (runtime repository; not this tree)

Implement the unify in `Zero-State-LLC/Noema`. This repository does not implement it.

1. Keep `/watch` as the only public spectator HTML door.
2. Add or extend the existing TEXT / PIXEL control so MAP is a third mode of the same page.
3. Feed MAP from the same `watch-live/1.0` snapshot used by TEXT and PIXEL. Add `watch-map/1.0` bands only as overlay data for the same heads.
4. Redirect `/watch/map` to `/watch` (MAP). Do not keep a second live document.
5. Leave Phosphor §18 behavior in place. Leave PLAY, STUDY, and Admin Live unchanged.
6. Prove same-head identity across modes, one-map-at-a-time, hidden-topology omission, pause / reduced-motion, and “projection / not world truth.”
7. After that unify shipped, a separate Danny human-yes Continue flipped Specs Gate D to COMPLETE in [LCA-GATE-D-PROMOTION-2026-09-09.md](../docs/LCA-GATE-D-PROMOTION-2026-09-09.md). This file does not Deploy and does not pass Gate E or Gate F.

## Non-goals

- Deploy, Gate E/F COMPLETE, hosted STUDY, or RFC-0130 from this amend
- New Player verbs, events, gates, or protocol fields
- Phosphor redesign
- WebGL, dashboards, AI narration, or spectator analytics
- Hosted STUDY, Deploy, or RFC-0130
- Runtime code in this repository

## Acceptance (this Specs change)

- WATCH docs name one `/watch` door and TEXT / PIXEL / MAP modes.
- Mapping is progressive enhancement of the same world heads.
- Phosphor §18 and spectator-is-not-truth language remain in force.
- Campaign docs record Noema #679 PASS and the later COMPLETE promotion packet.
- This amend remains the one-door contract; COMPLETE lives in the promotion packet.
- `python3 validation/validate_all.py` PASSes.
