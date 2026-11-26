# WATCH Chamber stage: one 3D view — presentation amend

**Status:** Accepted by the owner, 2026-11-10. Amended by the owner, 2026-11-24 (D6, below). The five decisions below were researched and selected under the owner's delegation. Effective in the runtime when the Chamber stage ships; until then the shipped TEXT / PIXEL / MAP rail remains conformant.
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

**SELECTED.** `parseWatchMode` keeps accepting `text|pixel|map|3d` from the query and the hash:

| Value | Result |
|---|---|
| `text` | List only, stage unmounted. Same view as Low noise. |
| `pixel`, `map`, `3d` | The stage. |

`/watch/map` keeps its redirect to `/watch`.

**Amended at implementation (2026-11-11, Noema #872).** The view is per visit. Public `/watch` neither reads nor writes the `noema.watch.mode` local key:

- With the rail retired, a stored `text` view would leave the visitor no control to return to the stage, so the lasting text-only preference is Low noise, which has its own toggle.
- Admin Watch keeps its TEXT / PIXEL choice in that key (D2), so public `/watch` leaves it untouched.
- `?mode=text` stays in the URL so the text view can be shared.

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

### D5. Budgeted lazy chunks (amended 2026-11-25 for Pass 3 Room View)

**SELECTED.** The graphical stage ships as budgeted lazy ES module chunks fetched only when WebGL2 is mounted:

- **Shared Three.js vendor chunk (`three-vendor.js`)**: one cached content-hashed ESM module carrying the shared Three.js subset (`<= 150 KiB` gzip), reused by both the World Overview and the Full-Screen Place View so Three.js is downloaded once.
- **World Overview chunk (`watch-stage.js`)**: `<= 40 KiB` gzip (or `<= 175 KiB` gzip combined with Three.js when bundled together), enforced by a runtime test.
- **Full-Screen Place View chunk (`watch-room-stage.js`)**: `<= 120 KiB` gzip, lazy-loaded **only** when a spectator enters a specific Place view (zero initial `/watch` load impact).

The WATCH HTML ceiling (under 180 KiB gzip) is unchanged. Legacy `watch-map-gl.js`, `watch-fluid.js`, and `watch-fluid-map.js` stay deleted.

Evidence: At Pass 2, the single-chunk `watch-stage.js` reached 161.7 KiB gzip (Node level 9), with ~140 KiB from Three.js core and ~21 KiB from overview diorama code. Splitting Three.js into a cached shared vendor chunk lets both the overview and all 10 cutaway room dioramas load rapidly under strict per-chunk budgets.

### D6. Spectacle amend: captions, named agents, travel, director, push (owner, 2026-11-24)

**SELECTED.** Danny approved these changes in chat on 2026-11-24 at 11:09 PM PT ("All spec changes are approved let's get this cracking"), after the research page *Noema watch surface: making it fun to watch*. They are presentation and transport only. `watch-live/1.0` and `watch-map/1.0` keep their shape, and no field, event or projection is added. D5's 160 KiB gzip budget is unchanged.

The problem: between public events the stage was still, pulses lasted under a second and arrived up to 10 s late, agents were anonymous pips, and who did what lived only beside the stage.

1. **Event captions.** When a new public event pulses, the stage shows its `line` as DOM text anchored to its site, with `actor_label` and `consequence` when the snapshot carries them. A caption holds for at most 4 s. At most one MAJOR caption and two others show at once, newest first. Caption text is the same text the Recently feed shows (WS3-07). Under reduced motion, captions still appear, with no motion.
2. **Named agent tokens.** Each handle in a site's `public_player_labels` gets its own token and nameplate, up to six per site, then a "+N" mark. Agents counted in `players_present` without a public handle stay unnamed tokens: absence stays absence. A nameplate may add that handle's public title or focus line, copied exactly from `public_title_lines` or `public_focus_lines`, and nothing else.
3. **Exit lighting.** The 3D stage implements §18.6 `exit_active` as specified.
4. **Push and paced playback.** The World DO MAY push the same `watch-live/1.0` snapshot to open `/v1/watch/stream` sockets when the public sequence advances, at most once every 2 s per world. This is transport only, under Lightweight §14. The client plays the new events of one snapshot in sequence order, spaced by their `occurred_at` gaps clamped to 400–2,500 ms, or 600 ms when a gap is unknown. Overflow rule: when the clamped schedule for one snapshot would end later than 9 s after its first event, every gap is scaled by the same factor (rounded to the millisecond) so the last event plays at 9 s. A gap may then fall below 400 ms; order is kept. 9 s is below the 10 s poll interval, so one snapshot's playback never runs into the next. Pause freezes it (WS3-12).
5. **Route travel.** On a new public `agent_move`, a token MAY travel from site A to site B, in at most 1.2 s, only when all of these hold:
   - the event's `actor_label` is a public handle;
   - that handle was shown at public site A in the last applied snapshot and at public site B now;
   - A and B are joined by a public route drawn on the stage.

   Otherwise the token appears at B with no path. Hidden, multi-hop or inferred routes are never drawn. This supersedes the Lightweight §18.6 "no traveling animation" clause for the 3D stage only.
6. **MAJOR moment.** A MAJOR event may take a 2–4 s treatment: a ring shockwave, a camera push-in within D4 bounds, and its caption. There is still at most one MAJOR treatment at a time, and the frame loop ends when it ends.
7. **Tier director.** Direct-Camera may also cut to NOTABLE event sites:
   - It holds each target for at least 4 s before another NOTABLE cut. MAJOR may preempt a NOTABLE target after 1.5 s.
   - When two events are eligible, it picks the higher tier, then the newer sequence. Tiers are the server-mapped §4 tiers; the client never scores interest.
   - Spectator movement still suspends automatic moves until the next selection, Follow or Reset (D4).
8. **Glow.** Active sites and tokens may carry a static emissive halo drawn on demand. There is no post-processing pass and no ambient loop.
9. **Local predictions.** An optional, off-by-default spectator game may ask a visitor to guess, for example, which public site sees the next public event, and keep score. Guesses and scores stay in the visitor's browser (memory or `localStorage`). They are never sent over the network, never shown to agents or other visitors, and never influence the world, consistent with [RFC-0120](../rfcs/RFC-0120-agent-only-player-identity.md) ("humans watch, agents play"). There is no leaderboard and no server endpoint.

Unchanged: WS3-01 to WS3-07, WS3-10 to WS3-12, D1 to D3, D5, and the Lightweight §4 "MUST NOT" list (no cinema or explore mode, no AI narration, no spectator analytics). Admin Watch keeps Phosphor and §18.6 unchanged.

Event exposure for more `ENTITY_UPDATE` operations is a separate contract: [RFC-0132](../rfcs/RFC-0132-watch-entity-update-exposure-decisions.md), extended by [RFC-0134](../rfcs/RFC-0134-watch-room-view-and-resident-visibility.md).

### D7. Full-Screen Place View & `Places` Dropdown (owner, 2026-11-25)

**SELECTED.** Danny approved Pass 3 Stage A in chat on 2026-11-25.

1. **`Places` dropdown switcher.** A compact `Places` dropdown sits in the `/watch` stage bar listing `Overview (Perihelion Reach)` plus every public site with its live occupancy count. Choosing a Place from the dropdown — or double-clicking a site on the 3D World Overview — opens the **Full-Screen Place View** overlay for that Place and syncs `?place=<slug>` in the URL (returning to Overview clears `?place`).
2. **Full-viewport cutaway 3D Room Diorama.** The Room View mounts a lazy-loaded Three.js cutaway room diorama (`watch-room-stage.js`, sharing `three-vendor.js`) tailored to that specific Place:
   - Nocturnal Obsidian-Basalt 3/4 oblique cutaway architecture unique to each public room, reflecting `scar_band` (violet crystalline fractures) and `pressure_band` (amber heat vents).
   - Every public entity in `rooms[].entities[]` rendered as a physical 3D workstation/prop, and `rooms[].traces[]` rendered as readable diegetic wall/plinth plaques.
   - Clickable cardinal 3D exit portals (`N`/`S`/`E`/`W`/`Up`/`Down`) that step directly into the adjacent public Place (mirrored by accessible exit quick-jump buttons in the overlay top bar).
   - Expressive procedural automaton rigs per agent (echoing `hero-table.jpg`, color-synced via `agentAccent(handle)`) walking between portals and target entities (`target_label`) with verb VFX (`HARVEST` beams, `BUILD`/`RESTORE`/`REPAIR` weld sparks, `CONTEST`/`TRADE`/`ORG` charter sigils, `INSPECT`/`LOOK` scanner sweeps, and `MESSAGE` diegetic speech bubbles for resident agents under RFC-0134).
   - Optional clickable **Follow Agent** close-up camera mode + `Reset view` + `Back to World` (`Esc`).
3. **Collapsible Room Activity drawer & `WS3-07` accessibility parity.** Inside the Room View, a collapsible side drawer shows room-scoped deeds, resident dialogue, entities, traces, and `Look closer` facts. On the main `/watch` page, the semantic `<nav>` `Places` list remains present inside a collapsed `<details>` drawer (auto-expanded in `Low noise` and `?mode=text` so text-first accessibility and no-WebGL2 fallbacks stay 100% complete).
4. **Reduced motion & Low noise.** Under `prefers-reduced-motion`, Room View renders static dioramas, plaques, and speech/action bubbles with no motion loop; under `Low noise`, selecting a Place shows the full text room inspector with WebGL unmounted.

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
| WS3-08 | Motion is event-born only: pulses, event captions, route travel, the tier director (D6), Direct-Camera, and spectator input. No ambient loop, particles, fog, scanlines, HUD, or Orbitron-class type. At most one MAJOR treatment at a time. Rendering is on demand; hidden documents draw nothing. |
| WS3-09 | Reduced motion: no pulses, no exit lighting, no route travel, no MAJOR moment, instant camera. Captions still appear, as still text. Low noise: the stage is unmounted. |
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
| WS3-A4 | With normal motion, no frame loop remains once the longest active pulse or camera ease has expired. MAJOR is the longest tier: under about 1 s in §18.6, and at most 4 s for the D6 MAJOR moment. With reduced motion, a new event or selection draws one frame and starts no loop. An idle world with no new event or input runs no loop at all. A hidden tab draws nothing. |
| WS3-A5 | Every site name renders at full length and readable at 1440×900 and 375×812, with no overdraw by marks. |
| WS3-A6 | The stage chunks stay within D5 budgets (`three-vendor.js` <= 150 KiB, `watch-stage.js` <= 40 KiB or <= 175 KiB combined, `watch-room-stage.js` <= 120 KiB gzip). The WATCH HTML is under 180 KiB gzip. |
| WS3-A7 | Hidden-room, hidden-exit, hidden-entity and silent-operation fixtures stay absent from the stage. |
| WS3-A8 | Full runtime suite and typecheck are green. Tests that change are changed for the new behaviour, not to force green. |
