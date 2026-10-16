# WATCH fluid mode transitions — proposed presentation amend

**Status:** Draft for review. Not implementation authority.
**Kind:** Presentation proposal for the existing public `/watch` door.
**Date:** 2026-10-14
**Intent:** [Fluid WATCH mode transitions](../intent/2026-10-14-watch-fluid-modes.md).
**RFC:** None proposed. No protocol, schema, security, world-rule, or event-catalog change.
**Version domains:** No version change proposed. `watch-live/1.0` and `watch-map/1.0` remain unchanged.

The requirements below describe the proposed outcome. Existing canonical WATCH contracts remain binding until the maintainer accepts an amend. This document neither implements the frontend nor authorizes a Worker publish.

## Workflows

- **SKILL.ORIENT** — identify the existing WATCH authority and presentation-only scope.
- **SKILL.SPEC_CHANGE** — keep the amend separate from existing contracts until reviewed.
- **SKILL.EXPERIENCE** — preserve the public spectator projection and progressive disclosure.
- **SKILL.REVIEW** — review scope, semantic drift, privacy, accessibility, and acceptance coverage.
- **SKILL.VALIDATE** — run repository validation, link checks, and required-path checks.
- **Owner specialist:** WATCH public spectator presentation.
- **Existing Action:** reuse repository CI; no new workflow.

## Authority and scope

| Subject | Existing authority |
|---|---|
| One `/watch` door; TEXT / PIXEL / MAP | [One-door amend](spec.md) |
| MAP WebGL allowance | [MAP amend](watch-map-p0-gl-poi.md) and [mapping §3.3](../docs/WATCH-REAL-TIME-MAPPING.md#33-rendering--animation) |
| Semantic graph, public labels, Follow, motion, Phosphor | [Lightweight WATCH](../docs/WATCH-LIGHTWEIGHT-SPECTATOR.md) §4, §6–9, §18 |
| Preserve the implementation and one layout authority | [Visual direction §18](../docs/WATCH-VISUAL-DIRECTION.md#18-migration-contract) |
| Public descriptor lines | [GC3-S2](../docs/GC3-S2-WATCH-PUBLIC.md) |
| Explicit public event exposure; default silence | [Accepted RFC-0126](../rfcs/RFC-0126-watch-entity-update-exposure.md) |
| Human legibility evidence | [Gate D scenario](../docs/LCA-GATE-D-SCENARIO.md) |

Scope is a reviewed presentation proposal for switching the existing modes. It does not change server event selection, identity, public exposure, topology, or world state. No new endpoint, event family, public field, or second spectator application is proposed.

## Shared public view

1. Every mode MUST use the same `world_id`, `cycle`, `sequence`, and `freshness`. A mode switch MUST NOT fetch or construct a separate world head.
2. TEXT, PIXEL, and MAP MUST share the deterministic public-room and public-exit layout. Identical public inputs MUST produce identical placement; depth MUST NOT become a second geography.
3. At most one visible map or graphical stage may be painted at a time. Preparing the next mode offscreen MUST NOT display a second map.
4. Public site and Player selection, Follow, pause state, and the displayed feed MUST survive a mode switch. Switching modes MUST NOT create a public event or reselect the headline.
5. PIXEL stays the default when Canvas 2D is available. MAP stays opt-in. TEXT stays one keystroke away.

## Mode presentation and transitions

| Mode | Required presentation |
|---|---|
| TEXT | Complete semantic HTML and the existing optional static ASCII cartogram. No visible canvas or WebGL; the cartogram does not animate. |
| PIXEL | Existing Canvas 2D Phosphor layout, glyph vocabulary, logical resolution, key, and performance budgets. No WebGL or replacement atlas. |
| MAP | Optional richer stage under the existing MAP allowance, using the same public layout and complete semantic alternative. |

Proposed additional motion is limited to an explicit spectator mode selection. It is cosmetic interface motion, not a new world event or evidence of movement in the world.

- **APPROVED (Danny, 2026-10-15):** a spectator-initiated PIXEL↔MAP selection MAY interpolate for at most 400 ms using the existing MAP camera ease. TEXT entry and exit are always a hard cut. The transition MUST NOT delay input, focus, or ARIA state, and MUST NOT run on load, refresh, or stream update. It MUST stop when its target is reached and MUST respect the existing PIXEL drawing budget while PIXEL is painted. The View Transitions API MAY supply an optional crossfade only; where it is unavailable or reduced motion applies, the result is a hard cut, and it MUST NOT leave two maps visible after the transition. This is the only non-event motion permitted; Lightweight WATCH §18.6 remains otherwise binding.
- Entering TEXT MUST remove the graphical stage and present the static text view. It MUST NOT keep a canvas text surrogate visible or animate the ASCII cartogram.
- A later mode selection supersedes an unfinished transition. The result MUST match the latest selected mode and preserve one visible stage.
- `prefers-reduced-motion` MUST replace all interpolation with hard cuts. It MUST also preserve the existing zero-pulse and zero-exit-lighting rules.
- Hidden documents MUST stop transition drawing. No continuous idle animation, fog, particles, scanlines, or decorative camera motion is permitted.
- Ordinary public-event pulses remain governed by Phosphor §18.6, including tier mapping and concurrency limits. Mode selection MUST NOT manufacture or replay those pulses.

The mode-selection motion extension was approved by Danny on 2026-10-15 with the bounds above. Existing event-only motion rules are not otherwise replaced.

## Public identity and feed preservation

The frontend MUST display already-projected actor labels, room occupants, and public standing/descriptor lines according to their existing contracts. It MUST preserve public Player and site Follow controls and stored client-local preferences.

An absent actor label MUST remain absent. The frontend MUST NOT infer a name, recover an identity from another source, or substitute a remembered identity. Conversely, the proposal does not authorize removing a public handle that the server deliberately supplies.

Feed selection, ordering, tiers, phrasing, and consequences remain server-derived. Follow remains emphasis only; unrelated world activity stays visible. Private sites, motives, cognition, operator identities, and unprojected event operations remain withheld or silent under the existing contracts.

Names determining special Player shapes are a separate design idea. This proposal does not approve a new identity encoding or change the existing glyph atlas.

## Event-born MAP depth: review boundary

The prototype's event-born depth is a design reference, not an accepted world-state projection. Any proposed depth treatment MUST identify its already-public inputs, finite animation behavior, deterministic mapping, and equivalent semantic description.

Depth MUST NOT invent room geometry, imply hidden floors or sites, turn event receipt counts into progress or reputation, or claim that the current snapshot contains a complete event history. Public events received in one browser window are not a full ledger, world memory, or permanent construction record.

The renderer MUST NOT import local operator recordings or raw history to supply missing events. Optional public bands remain scoped to currently public rooms and the same world head. If a primitive needs a new history projection, public metric, or otherwise unauthorized fact, that primitive is outside this amend and requires separate review.

**SELECTED (Danny, 2026-10-15):** MAP depth is a transient elevation of a public room bound 1:1 to an existing §18.6 pulse (same sequence, tier, caps, and lifetime). It returns to a single uniform rest depth on expiry, is disabled under reduced motion, and encodes nothing absent from the feed. Persistent, cumulative, or trace-derived depth (for example from `rooms[].traces[]`) is out of scope and deferred to a separate reviewed row. A smooth-looking prototype or a passing renderer suite does not extend this selection.

## Accessibility, refresh, and failure

- The semantic public-site graph MUST remain available in every mode. Canvas MUST contain no unique factual information.
- Mode controls, site inspection, Follow, and clear-follow MUST remain keyboard- and touch-operable with visible focus. Site details and the map key MUST remain readable without interpreting a canvas.
- The mobile layout MUST retain map primacy without required horizontal scrolling; the optional ASCII cartogram follows its existing mobile fit rules.
- One shared refresh path MUST preserve bounded polling, pause, manual refresh, freshness, incident, and maintenance behavior. Stream updates received while paused MUST NOT advance the displayed head or animation.
- If MAP or its graphics chunk cannot load, the viewer MUST retain usable PIXEL or TEXT. If Canvas 2D is unavailable, it MUST retain complete semantic TEXT.
- Failure of the enhancement MUST leave the existing WATCH shell, public feed, controls, and site details functional.
- Public world text MUST use the existing safe-label path. A presentation amend does not relax escaping or privacy checks.

## Acceptance evidence for a later runtime slice

These checks are required evidence, not claims that this PR has executed a runtime implementation.

| ID | Observable check |
|---|---|
| FWM-01 | Switch TEXT → PIXEL → MAP → TEXT on one public snapshot; all displayed world-head fields remain equal and the feed is unchanged. |
| FWM-02 | Rapidly switch modes during loading and transitions; only one map is visible and the final selected mode wins. |
| FWM-03 | TEXT shows no visible canvas, retains the semantic graph, and adds no animated cartogram. |
| FWM-04 | PIXEL preserves the existing atlas, map key, logical resolution, event-pulse rules, and bounded frame budget; it loads no MAP graphics dependency. |
| FWM-05 | Reduced motion produces hard cuts and no pulses, interpolation, or exit lighting. An idle or hidden page has no drawing loop. No animation frame loop remains active ~400 ms after the last mode selection. TEXT entry/exit is a hard cut, and load, refresh, and stream updates start no mode transition. |
| FWM-06 | Public handles, public descriptor lines, Player/site Follow, clear-follow, and site inspection survive mode switches. Absent identities remain absent. |
| FWM-07 | Hidden-room/exit/entity/Player and silent-operation cases remain excluded from layout, feed, and every proposed depth primitive. |
| FWM-08 | Pause freezes the displayed head and all modes during incoming stream updates; manual refresh and resume remain coherent. |
| FWM-09 | Missing MAP chunk, unavailable Canvas 2D, and failed enhancement each leave a complete usable fallback without an uncaught startup error. |
| FWM-10 | Keyboard, screen-reader, and mobile checks preserve complete semantic content, visible focus, touch controls, and readable labels without horizontal overflow. |
| FWM-11 | Depth is born only from a §18.6 pulse and expires with it. Resting depth is identical for the same public snapshot regardless of prior events received. Reduced motion shows no depth change. Trace-derived or cumulative depth is absent pending a separate row. |
| FWM-12 | Run the complete affected runtime suite and typecheck before publishing its PR. Report failures; do not alter existing tests or fixtures to force green. |

The later runtime evidence MUST identify the tested commit, public inputs, commands, results, and applicable acceptance rows. Automated checks do not substitute for human legibility review under the existing Gate D scenario. This proposal does not reopen or promote Gate D, E, or F.

## Review and handoff

Both maintainer decisions (mode-selection motion; event-born depth) were made by Danny on 2026-10-15 and are recorded above. Runtime implementation and deployment still require separate approval. After acceptance, update only the affected canonical WATCH presentation paragraphs and preserve every stricter existing rule. Any approved contract movement must carry its required checklist, changelog, and version review.

Implementation and its plan belong in `Zero-State-LLC/Noema`. This Specs PR contains no frontend code, compiled assets, deployment instructions, private recordings, or production changes.
