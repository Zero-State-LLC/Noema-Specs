# Intent: One WATCH stage in 3D

**Status:** `draft`

**Next stage:** `specify/spec.md` patch, drafted as a new `specify/watch-single-3d-stage.md` amend.

**Author:** scrimshawlife-ctrl (drafted with Claude Code)

**Date:** 2026-11-10

This record is process only. It is not a spec, not a plan, and not an RFC. It does not authorize implementation.

## Problem

OBSERVED: the owner directed on 2026-11-10 that public `/watch` become one single 3D view with appropriate detail, instead of a rail of modes.

OBSERVED: `/watch` today ships four renderings of the same public topology behind a mode rail (runtime repo `Zero-State-LLC/Noema`, `workers/noema/src/`):

| Mode | Renderer | Asset | Status in contracts |
|---|---|---|---|
| TEXT | Semantic Places list + ASCII cartogram (`watch.ts:1093-1204`, `watch-phosphor.ts:538`) | none | named, always available |
| PIXEL | Canvas 2D Phosphor (`watch-phosphor.ts:932`) | inline | named, **default** |
| MAP | Three.js stage (`watch-map-gl-stage.ts`) | `watch-map-gl.js`, about 136 KB gzip | named, opt-in |
| 3D | Three.js fluid scene (`watch-fluid.js`, `watch-fluid-map.js`) | about 6 + 147 KB gzip | **not named in any spec** |

OBSERVED: two independent Three.js stacks ship for MAP and 3D. MAP lays rooms on a naive `i%4` grid (`watch-map.ts:115-119`), not the shared public layout that [WATCH-VISUAL-DIRECTION.md](../docs/WATCH-VISUAL-DIRECTION.md) line 612 requires ("not a second geography").

OBSERVED: the current 3D view lacks detail the other modes carry:

- Site names are truncated to 14 uppercase characters.
- Occupants show only as a count, never as handles.
- Exits have no direction or destination.
- Traces and per-site recent events are missing.
- There is no site inspection or site Follow, because the Places list is hidden in 3D (`watch.ts:327, 674`).
- The certainty glyphs, tiered pulses, scar, pressure and protocol bands, health strip and map key are all missing.

OBSERVED: the 3D prototype also departs from decisions already taken:

- It uses a 900 ms morph that also runs on load, against the 400 ms spectator-initiated cap in [watch-fluid-modes.md](../specify/watch-fluid-modes.md).
- It stacks cumulative event towers, against the transient-depth selection of 2026-10-15 (same file).
- It falls back to MAP rather than to PIXEL or TEXT (`watch.ts:624`).

OBSERVED: current contracts block a single 3D default:

- [WATCH-LIGHTWEIGHT-SPECTATOR.md](../docs/WATCH-LIGHTWEIGHT-SPECTATOR.md) line 763: "**Default is PIXEL when Canvas 2D is available.**"
- [WATCH-REAL-TIME-MAPPING.md](../docs/WATCH-REAL-TIME-MAPPING.md) lines 103-105:
  - TEXT: "No WebGL"
  - PIXEL: "Canvas 2D only … WebGL stays banned until a later explicit row"
  - MAP: WebGL MAY render "the MAP mode stage"
- [WATCH-REAL-TIME-MAPPING.md](../docs/WATCH-REAL-TIME-MAPPING.md) line 225: "`MAP` is not the default anything."
- [specify/spec.md](../specify/spec.md) lines 42-53 name three modes, with PIXEL as the default.

## Proposed outcome

SPECULATIVE. The proposed outcome has six parts:

1. **One stage.** `/watch` has a single graphical stage, the Chamber stage: one Three.js scene that replaces PIXEL, MAP and the unnamed 3D view as separate modes. It is what a spectator sees first whenever WebGL2 is available. The mode rail goes away.
2. **Detail parity.** The stage draws only from `watch-live/1.0` and the optional `watch-map/1.0` bands. It shows:
   - every public site by its full name;
   - public routes with their direction;
   - occupants as their public handles;
   - the site states in WATCH-VISUAL-DIRECTION §6: unknown, known, active, selected, followed, recent, major, residue, partial;
   - transient event pulses bound one to one to the §18.6 pulses, with no cumulative towers;
   - authorized traces as marks;
   - scar, pressure and protocol bands;
   - Direct-Camera and Follow.
3. **Readable labels.** Site names and handles are DOM text over the canvas, so they can be read, selected and translated, rather than texture glyphs.
4. **Text stays authoritative, but stops being a mode.** The semantic site list (Places, with Look closer, exits, handles and Follow) is always present beside the stage: as a side column on desktop, and as a section below the stage on narrow screens. Selecting a site in the list or on the stage selects it in both. Every fact on the stage is also in the list.
5. **One layout and one chunk.** The stage uses the shared public layout (`layoutPublicTopology`). A single Three.js chunk replaces `watch-map-gl.js`, `watch-fluid.js` and `watch-fluid-map.js`, and a size-budget test guards it.
6. **Fallbacks without a second renderer.** The stage is not mounted when any of these holds: no WebGL2, GL failure, or Low noise. The always-present list and the text cartogram carry the page instead. Under reduced motion, the stage draws on demand only: no pulses and instant camera moves.

## Affected users / systems

- HumanPrincipals watching public `/watch`.
- The hosted Worker WATCH presentation (`watch*.ts`, the built Three.js asset, and WATCH tests).
- Admin Watch keeps its Canvas 2D Phosphor view, which shares `watch-phosphor.ts`, and is out of scope.

No Controller, Player action, World Engine, STUDY, or projection contract changes are proposed.

## Constraints / non-goals

- No change to `watch-live/1.0` or `watch-map/1.0`. No new fields, verbs, events, visibility classes, research metrics, or client salience scoring.
- The canvas never carries a unique fact. TEXT completeness stays the accessibility authority (WATCH-LIGHTWEIGHT-SPECTATOR line 224).
- Motion stays event-born, and an idle world means an idle stage. The following stay banned:
  - ambient loops, particles and fog;
  - scanlines and military HUD;
  - Orbitron-class fonts;
  - KPI walls;
  - decorative WebGL;
  - more than one MAJOR treatment at a time.
- Camera and transition moves last at most 400 ms, start only from the spectator or an event, and never run on load or refresh.
- Hidden rooms, exits, entities and players are never drawn. Ids never appear on screen. Missing data stays absent.
- Persistent, cumulative or trace-derived depth stays out of scope, per the 2026-10-15 selection, unless it is reviewed separately.
- Keyboard and touch:
  - sites are reachable by Tab, Enter selects, Esc clears;
  - Follow and Clear are keyboard reachable;
  - targets are 44 px;
  - there is no horizontal scroll on mobile.
- The live region stays limited to the headline.
- The WATCH HTML gzip budget (under 180 KiB) is unchanged.
- No Worker publish is implied.
- Runtime sequencing: implementation starts after the open drafts `Zero-State-LLC/Noema#856` and `#848`, which edit `watch.ts`, have landed or been closed.

## Contracts to amend in the next stage

- [WATCH-LIGHTWEIGHT-SPECTATOR.md](../docs/WATCH-LIGHTWEIGHT-SPECTATOR.md):
  - lines 757 and 763: the PIXEL default and the TEXT/PIXEL toggle;
  - lines 59 and 679: unscoped WebGL out of scope or deferred;
  - line 110: no cinema or explore modes, to be scoped rather than removed.
- [WATCH-REAL-TIME-MAPPING.md](../docs/WATCH-REAL-TIME-MAPPING.md):
  - line 40;
  - lines 103-111, where the stage replaces the per-mode rows;
  - line 225.
- [WATCH-VISUAL-DIRECTION.md](../docs/WATCH-VISUAL-DIRECTION.md) lines 530-532: the graphics engine allowlist.
- [specify/spec.md](../specify/spec.md) lines 42-53: the mode list and the default.
- [specify/watch-fluid-modes.md](../specify/watch-fluid-modes.md): superseded once there are no modes to morph between.
- Runtime repo inventory `docs/WATCH-VISUAL-MAP.md`, and the privacy notice entry for the `noema.watch.mode` local key.

## Open questions

1. Is the 3D stage the only graphical view, and the default? The owner's direction says yes; it needs this amend accepted.
2. What happens without WebGL2? Recommended: the semantic list plus text cartogram only, because it is already compliant and keeps one renderer. The alternative is to keep Canvas 2D PIXEL as a second renderer.
3. Do `?mode=text|pixel|map|3d` links keep working? Recommended: `text` shows the list with the stage unmounted, and the other three open the stage. This keeps existing links and the 733 acceptance script working.
4. How much camera control does the spectator get? Recommended: a fixed oblique default, Direct-Camera to events and Follow targets, and bounded orbit and zoom with a keyboard-reachable reset.
5. What is the size budget for the single chunk? NOT_COMPUTABLE until measured. The two current chunks are about 136 KB and 147 KB gzip.

## Verified / assumed claims

| Claim | Label | Basis |
|---|---|---|
| Owner directed a single 3D WATCH view on 2026-11-10 | `OBSERVED` | Owner instruction in the drafting session |
| PIXEL is the specified default | `OBSERVED` | WATCH-LIGHTWEIGHT-SPECTATOR.md line 763 |
| TEXT and PIXEL are specified as no-WebGL | `OBSERVED` | WATCH-REAL-TIME-MAPPING.md lines 103-104 |
| "3D" is not a named mode in any spec | `OBSERVED` | Search of `docs/` and `specify/` on `main` |
| Two separate Three.js stacks ship for MAP and 3D | `OBSERVED` | Runtime `watch-map-gl-stage.ts`; `watch-fluid.js`, `watch-fluid-map.js` |
| The 3D view hides the Places list | `OBSERVED` | Runtime `watch.ts:327, 674` |
| One chunk can carry full detail within a gzip budget near today's MAP chunk | `SPECULATIVE` | Not measured |
| DOM labels over WebGL stay legible at 40+ sites on mobile | `SPECULATIVE` | Needs a prototype at current world size |
| A single stage lowers spectator load compared with four modes | `INFERRED` | Four renderings of one topology today; not user-tested |

## Author / date

- **Author:** scrimshawlife-ctrl (drafted with Claude Code)
- **Date:** 2026-11-10
