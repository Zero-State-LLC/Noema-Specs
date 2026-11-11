# WATCH Chamber stage: one 3D view — presentation amend

**Status:** Accepted by the owner, 2026-11-10. The five decisions below were researched and selected under the owner's delegation. Effective in the runtime when the Chamber stage ships; until then the shipped TEXT / PIXEL / MAP rail remains conformant.
**Kind:** Presentation amend for the public `/watch` door.
**Date:** 2026-11-10
**Intent:** [One WATCH stage in 3D](../intent/2026-11-10-watch-single-3d-stage.md).
**Supersedes:** [watch-fluid-modes.md](watch-fluid-modes.md) mode-selection motion, once the stage ships. Its event-born depth selection (Danny, 2026-10-15) carries over unchanged.
**RFC:** None. No protocol, schema, security, world-rule, or event-catalog change.
**Version domains:** No version change. `watch-live/1.0` and `watch-map/1.0` remain unchanged.

## Workflows

1. A spectator opens `/watch`.
   - With WebGL2 available, the Chamber stage mounts beside the semantic site list.
   - Without WebGL2, on GL failure, or with Low noise, only the list and the text cartogram render.
2. The spectator reads the stage:
   - every public site by its full name, with occupants as public handles;
   - routes with their direction;
   - site states;
   - the current event pulse.

   The Who / Where / Consequence headline, the Recently feed and the Withheld band stay where they are.
3. The spectator selects a site on the stage or in the list. Both select it, and Look closer opens in the list. Follow on a site or handle works from either place; Clear works the same way.
4. A public event arrives:
   - its site pulses once, for the §18.6 pulse lifetime;
   - a MAJOR event takes the one MAJOR treatment;
   - Direct-Camera eases to a followed or MAJOR target, unless the spectator has moved the camera since the last selection.
5. The spectator orbits, zooms or pans within bounds, by pointer, touch or keyboard. "Reset view" returns to the default framing.
6. An old link with `?mode=` or `#mode` lands on the same door: `text` shows the list with the stage unmounted, and `pixel`, `map` and `3d` show the stage.

## Decisions

### D1. One stage, and it is the default

**SELECTED.** `/watch` mounts one WebGL2 Chamber stage. It replaces PIXEL, MAP and the unnamed 3D view as separate public modes, and the mode rail is retired. The stage is what a spectator sees first whenever WebGL2 is available. It is the map, not a cinema or explore mode, so [WATCH-LIGHTWEIGHT-SPECTATOR.md](../docs/WATCH-LIGHTWEIGHT-SPECTATOR.md) line 110 still holds.

Evidence:

- The owner directed it on 2026-11-10.
- WebGL2 reaches 97.29% of global users (caniuse, November 2026).
- The live world is 10 public sites and 24 exits, with names up to 20 characters (`/v1/watch/live`, 2026-11-11). That fits one readable scene.

### D2. No second graphical renderer on `/watch`

**SELECTED.** When the stage cannot mount (no WebGL2, context creation or loss failure, chunk load failure) or Low noise is on, `/watch` renders the always-present semantic site list plus the text cartogram. Lightweight §18 already names this as the failure path: "Canvas absence or failure falls back to TEXT".

Canvas 2D Phosphor is no longer mounted on public `/watch`. It stays in the codebase for Admin Watch, which shares `watch-phosphor.ts`.

Evidence:

- Support is not success: GPU blocklists and disabled hardware acceleration fail WebGL2 on supported browsers, so a text path is required either way.
- Keeping PIXEL as a fallback would leave two graphical renderers, against D1.
- Dropping the inline Phosphor client from `/watch` also lowers the page's gzip weight.

### D3. Old mode links keep working

**SELECTED.** `parseWatchMode` keeps accepting `text|pixel|map|3d` from query, hash and the `noema.watch.mode` local key:

| Value | Result |
|---|---|
| `text` | List only, stage unmounted. Same view as Low noise. |
| `pixel`, `map`, `3d` | The stage. |

`/watch/map` keeps its redirect to `/watch`. The local key keeps only the `text` preference.

Evidence: about 20 evidence records and runbooks in the runtime repo link `?mode=` URLs, including the Gate D packet and the 733 hosted-evidence docs. So does `scripts/acceptance-733.mjs`. Those URLs must keep reproducing.

### D4. Camera: bounded spectator control, event-born Direct-Camera

**SELECTED.**

- **Default framing.** An oblique view that fits every public site.
- **Spectator control is direct manipulation**, with no damping and no inertia, so no frame loop runs once input stops:
  - orbit, with the polar angle bounded between 20° and 70° from vertical;
  - zoom, bounded to the layout's extent;
  - pan, with the target clamped to the layout radius;
  - keyboard: arrow keys pan, Shift plus arrow keys orbit.
  - A visible "Reset view" control restores the default framing.
- **Direct-Camera** targets only public `room_id` and public actors already on the snapshot. It eases within the NOTABLE pulse lifetime: §18.6 tiers, 560 ms in the runtime today (`watch-phosphor.ts`). It runs on Follow, on selection, or on a newly observed MAJOR event: one whose sequence is newer than the last event this window has already applied. Polled snapshots and stream updates are where such events arrive, so an update that carries one may trigger the move. Loading the page, a manual refresh, or an update that only repeats state the window has already applied never moves the camera. The move is instant under reduced motion.
- **Spectator movement suspends automatic moves** until the next selection, Follow, or Reset.

Evidence: the bundled Three.js 0.186 `OrbitControls` provides polar and distance bounds, `maxTargetRadius`, and `listenToKeyEvents` with Shift-arrow rotation. Disabling damping keeps the "idle world is idle stage" rule (MAPPING §3.3).

### D5. One chunk, budgeted

**SELECTED.** One lazy ES module chunk carries the stage. It must stay at or under **160 KiB gzip**, enforced by a runtime test. It replaces `watch-map-gl.js`, `watch-fluid.js` and `watch-fluid-map.js`, which are deleted once the stage ships. The WATCH HTML ceiling (under 180 KiB gzip) is unchanged.

Evidence: a tree-shaken esbuild probe of the stage's Three.js surface measured 142,802 B gzip, about 139.5 KiB. It included the WebGL renderer, scene, cameras, instanced meshes, line and dashed-line materials, lights, raycaster, `OrbitControls` and `CSS2DRenderer`. That leaves about 20 KiB for stage code. Today a spectator who opens MAP and then 3D downloads 136,985 + 147,838 + 6,287 B gzip.

## Stage requirements

| ID | Requirement |
|---|---|
| WS3-01 | The stage uses the shared public layout (`layoutPublicTopology`) and nothing else. No second geography, and no naive grid. |
| WS3-02 | It draws only what is in `watch-live/1.0` and the optional `watch-map/1.0` bands for the same world head. Hidden rooms, exits, entities and Players never appear. Ids never appear on screen. Absence stays absence. |
| WS3-03 | Site names and occupant handles render as DOM text over the canvas (for example `CSS2DRenderer`), at full length, in the interface face, backed by a ground plate so marks never overdraw them (Lightweight §18 "Labels stay readable"). |
| WS3-04 | Encodes the site states of [WATCH-VISUAL-DIRECTION.md](../docs/WATCH-VISUAL-DIRECTION.md) §6 (unknown, known, active, selected, followed, recent, major, residue, partial) by form and label, never by colour alone. Uncertain routes are dashed. |
| WS3-05 | Routes show direction. Authorized traces appear as marks on their site. Scar, pressure and protocol bands may tint the site plate. Depth stays the transient §18.6-bound elevation (Danny, 2026-10-15); no cumulative towers. |
| WS3-06 | An HTML map key sits beside the stage and names every mark in plain language. |
| WS3-07 | The semantic site list stays present and complete: exits with direction, handles, entities, traces, Look closer, site and handle Follow. Every fact on the stage is also in the list, and selection is shared between the two. |
| WS3-08 | Motion is event-born only: pulses, Direct-Camera, and spectator input. No ambient loop, particles, fog, scanlines, HUD, or Orbitron-class type. At most one MAJOR treatment at a time. Rendering is on demand; hidden documents draw nothing. |
| WS3-09 | Reduced motion: no pulses, no exit lighting, instant camera. Low noise: the stage is unmounted. |
| WS3-10 | Keyboard and touch: sites are reachable through the list. Enter selects, Esc clears, and Follow and Clear are keyboard reachable. Stage controls and Reset view meet the 44 px target. No horizontal scroll at 375 px. |
| WS3-11 | `aria-live` stays limited to the headline. The canvas is `aria-hidden`, and the list is the accessible authority. |
| WS3-12 | Pause freezes the displayed head and the stage. Manual refresh and resume stay coherent. |

## Migration

1. Wait until runtime drafts `Zero-State-LLC/Noema#856` and `#848`, which edit `watch.ts`, land or close.
2. Build the stage as a new module and chunk behind the existing `?mode=3d` entry, until it meets WS3-01 to WS3-12.
3. Make the stage the default:
   - retire the mode rail;
   - apply D3's link mapping;
   - remove the PIXEL mount from `/watch`;
   - delete the MAP and fluid chunks;
   - update the affected runtime tests, inventory (`docs/WATCH-VISUAL-MAP.md`) and the privacy notice.
4. Keep Admin Watch on Phosphor.

## Acceptance evidence for the runtime slice

| ID | Observable check |
|---|---|
| WS3-A1 | On one public snapshot, stage and list show the same world head, sites, routes, handles and Recently feed. |
| WS3-A2 | No WebGL2, forced context loss, a blocked chunk and Low noise each leave the list and the text cartogram complete, with no uncaught error. |
| WS3-A3 | `?mode=text`, `?mode=pixel`, `?mode=map`, `?mode=3d`, `#text` and `/watch/map` resolve per D3. |
| WS3-A4 | With normal motion, no frame loop remains once the longest active pulse or camera ease has expired. MAJOR is the longest §18.6 tier, under about 1 s. With reduced motion, a new event or selection draws one frame and starts no loop. An idle world with no new event or input runs no loop at all. A hidden tab draws nothing. |
| WS3-A5 | Every site name renders at full length and readable at 1440×900 and 375×812, with no overdraw by marks. |
| WS3-A6 | The stage chunk is at or under 160 KiB gzip. The WATCH HTML is under 180 KiB gzip. |
| WS3-A7 | Hidden-room, hidden-exit, hidden-entity and silent-operation fixtures stay absent from the stage. |
| WS3-A8 | Full runtime suite and typecheck are green. Tests that change are changed for the new behaviour, not to force green. |
