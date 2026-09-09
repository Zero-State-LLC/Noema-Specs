# WATCH — Real-Time Mapping & Spectator System

**Version:** v0.1.3 (Draft)
**Date:** 2026-08-21 (reconciled 2026-08-21 evening; one-door amend 2026-09-09; MAP WebGL allowlist 2026-09-09)
**Status:** Specs-first. Implementation follows review.  
**Kind:** Rich visual spectator projection layer (`MAP` mode of the public `/watch` door).  
**Related:**
- [WATCH.md](WATCH.md)
- [WATCH-LIGHTWEIGHT-SPECTATOR.md](WATCH-LIGHTWEIGHT-SPECTATOR.md) (low-cognitive-load default)
- [SPECTATOR.md](SPECTATOR.md)
- [CHAMBER-MAP.md](CHAMBER-MAP.md)
- [VISUAL-DESIGN.md](VISUAL-DESIGN.md)
- [WATCH-VISUAL-DIRECTION.md](WATCH-VISUAL-DIRECTION.md) (map-first composition and visual grammar)
- [DEEP-TIME.md](DEEP-TIME.md) (scars, history as visual residue)
- [ECONOMY-EWM-SPEC.md](ECONOMY-EWM-SPEC.md)
- [DEEP-TIME-MECHANICS-UPDATE.md](DEEP-TIME-MECHANICS-UPDATE.md)

This document defines **`MAP` mode** on the public `/watch` door — a richer, layered live view of the same world heads. It is designed to be **easily expandable** over time while preserving immediate comprehension, visual pleasure, and fun for watchers. It is not a dashboard: the doctrinal exclusions of [WATCH-LIGHTWEIGHT-SPECTATOR.md](WATCH-LIGHTWEIGHT-SPECTATOR.md) §1 ("WATCH is not") bind every WATCH surface, this one included — the difference here is density and layering, never telemetry, scoring, or narration. It is not a second spectator application.

The map-first composition and visual grammar of [WATCH-VISUAL-DIRECTION.md](WATCH-VISUAL-DIRECTION.md) bind this surface unless this document explicitly defines a stricter rule. Additional layers MUST remain world-first, deterministic, public-projection-safe, and semantically restrained.

## 1. Purpose & Boundaries

WATCH Real-Time Mapping is the `MAP` mode of the one public spectator door (`/watch`). It provides a visually rich, glanceable, and engaging live view of the same world the TEXT and PIXEL modes already show.

**It is:**
- A derived, read-only projection. Never world truth.
- Focused on immediate understanding + long-term engagement.
- Built on the same `watch-live/1.0` world heads (`world_id`, `cycle`, `sequence`, `freshness`) as TEXT and PIXEL.
- Intentionally more visual and layered than the lightweight default.
- Progressive enhancement: optional `watch-map/1.0` bands overlay those same heads.

**It is not:**
- A second public spectator application or a second `/watch/map` app.
- A replacement for the lightweight spectator experience (see [WATCH-LIGHTWEIGHT-SPECTATOR.md](WATCH-LIGHTWEIGHT-SPECTATOR.md)).
- A dense telemetry dashboard or graph-heavy monitoring product (§1 doctrine of the lightweight contract applies).
- An admin or research analytics surface.
- A player HUD.
- A raw event firehose.
- The default cartography of `/watch`. PIXEL (Phosphor §18) stays the default first-glance map when Canvas 2D is available. `MAP` MUST NOT render beside the TEXT cartogram or the PIXEL canvas — one map at a time.

A historical `/watch/map` URL MAY redirect to `/watch` with `MAP` selected. It MUST NOT keep a separate live document or a different world head. Live dual surfaces (`/watch` and `/watch/map`) are observed runtime drift until that unify ships.

## 1.1 Privacy & Redaction (normative)

Every rule of [WATCH-LIGHTWEIGHT-SPECTATOR.md](WATCH-LIGHTWEIGHT-SPECTATOR.md) **§7** binds this surface verbatim — it is public WATCH. In particular:

- **No secret rooms/exits/entities/Players.** Derived overlays MUST be scoped to the rooms the public snapshot exposes, never to raw source maps (a pressure or scar map keyed by every room ever touched leaks hidden topology the moment a hidden room is touched).
- **Bands, never raw counters or amounts.** Per-room scar/pressure/protocol values serialize as coarse bands (`faint/marked/deep`, `low/moderate/high`). Raw floats and cumulative counters MUST NOT reach the wire. This is the shipped `watch-map/1.0` contract (Noema #488).
- **No research metrics.** Path-dependence, cascading-risk, velocity, and similar EWM/research scalars stay off the public payload.
- **No reputation.** `image_score` / `reputation_summary` / `second_order` never appear (GC3).
- **Untrusted world text.** All rendering via `textContent`/safe nodes; interpolated-markup assignment is a defect.
- **Server-side filtering only.** Redaction happens before JSON leaves the Worker; clients never re-derive hidden facts.

## 2. Core Principles (for Expandability)

1. **Immediate Comprehension** — A spectator must understand “what is happening, where, and at what intensity” within seconds.
2. **Layered & Modular** — New data sources, visual primitives, or interaction modes can be added without rewriting existing layers.
3. **Event-born emphasis** — Finite micro-animations and narrative highlights MAY clarify public change; gamification and spectator analytics are not part of the current WATCH composition.
4. **History-Aware** — Deep Time elements (scars, traces, institutions) are visually persistent and meaningful.
5. **Composable** — Integrates with EWM metrics, semantic signals, and future mechanics via clear extension points.
6. **Accessible by Default** — Reduced-motion, high-contrast, and structured alternatives are built in.

## 3. Architecture (Designed for Extension)

### 3.1 Layer Model

The system is composed of independent, stackable layers. New layers can be inserted or extended without affecting others.

| Layer | Purpose | Current Content (v0.1) | Extension Hook |
|-------|---------|------------------------|----------------|
| Base Map | Spatial layout of rooms/regions | Room graph, clear labels, boundaries | Add new room types, procedural sub-structures |
| Activity Overlay | Movement & flow | Static or brief event-born traces, recent public paths | New flow types only when publicly authorized |
| State Overlays | Resource/pressure/scar state | Restrained semantic marks for authorized coarse bands; no default heat map | New public-projection-safe state encodings |
| Entity Layer | Agents, objects, institutions | Role glyphs, public activity, scar residue | New entity classes or statuses with public visual contracts |
| Event Layer | Recent significant changes | Icon + short consequence river | New event categories via the server-side §4.E tier table only (client interest scoring is banned — [SPECTATOR.md](SPECTATOR.md)); deterministic grouping |
| Narrative Layer | Story beats & highlights | The server-derived deterministic headline (same selection as the lightweight §4.A — no AI narration) | Additional deterministic, evidence-grounded highlight rules; anything generative or voted requires a future RFC |
| Health / Context | World-level glanceables | World, cycle, freshness, public condition bands, authorized scar activity | New public context only; no research metrics |
| Event Emphasis | Consequence feedback | Event-born, finite emphasis | Badges, streaks, ranking, and spectator analytics remain deferred |

### 3.2 Data Contract (Stable Core)

All layers consume a common derived projection (extends existing `watch-live/1.0` concepts):

- Rooms with position + metadata
- Entities (with role, position, visible state, scars)
- Recent events (typed, with grounding to canonical ledger)
- Authorized public coarse bands and state marks only; raw research aggregates stay off public WATCH
- Event timestamps for bounded, event-born emphasis; no continuous interpolation requirement

**Future-proofing:** New fields are added as optional extensions. Old clients ignore unknown fields.

Optional extensions remain subject to existing schema, privacy, projection, and change-control rules. This document does not authorize new public fields or metrics by itself.

### 3.3 Rendering & Animation

**Public `/watch` graphics allowlist (reopen, 2026-09-09).** This row reopens the brand lock for the MAP mode stage only. It does not reopen PIXEL, PLAY, STUDY, or Admin Live. TEXT remains authority. Projection is not world truth. Canonical campaign note: [specify/watch-map-p0-gl-poi.md](../specify/watch-map-p0-gl-poi.md).

Impressiveness target is a unique blend, not pure cinema and not a raw MUD dump: MUD theater (TEXT authority; withheld/unknown is drama), living-stage MAP (WebGL / Three.js for depth and event-born Direct-Camera), civilization sports (glanceable Who / Where / Consequence, no KPI or esports HUD packing), and projection honesty (the chamber is a window, never omniscient world truth). Feel is **legible but with edges of experimental**: Gate D five slots, camera-to-action, and TEXT stay non-negotiable; uncanny depth, odd marks, and withheld-as-aesthetic stay fringe; muddy hierarchy, illegible type, and cosplay HUD remain defects. Visual grammar: [WATCH-VISUAL-DIRECTION.md](WATCH-VISUAL-DIRECTION.md) §1.

| Surface | Graphics |
|---|---|
| `TEXT` | Semantic HTML. No WebGL. |
| `PIXEL` | Canvas 2D only ([WATCH-LIGHTWEIGHT-SPECTATOR.md](WATCH-LIGHTWEIGHT-SPECTATOR.md) §18). WebGL stays banned until a later explicit row. |
| `MAP` | WebGL / Three.js (or equivalent) MAY render the MAP mode stage when every condition below holds. HTML/CSS layout remains equally compliant. Smooth interpolated movement is optional enhancement, never information. |

**MAP-stage MAY when all of the following hold:**

- Motion is event-born (finite, self-extinguishing; idle world is idle stage).
- Camera targets public `room_id` / public actors only (Direct-Camera).
- TEXT remains complete without GL. Canvas/GL never carries unique facts.

**Still banned on public WATCH:**

- Orbitron / sci-fi display fonts as brand voice
- CRT scanlines
- Military HUD packing
- Ambient particle / fog loops
- Dashboard KPI walls
- Fake depth that invents or implies hidden rooms/topology
- Decorative WebGL unrelated to a public event or follow target

**Unchanged:**

- Spectator ≠ world truth
- `prefers-reduced-motion` → hard cuts / no easing
- One map/stage at a time
- No new Player verbs or Genesis
- Access language only

UI chrome stays HTML/CSS for compact controls, legend, event log, and selected-site detail. New visual primitives MUST declare their animation behavior. Reduced-motion MUST replace easing with hard cuts.

### 3.4 MAP P0 acceptance intent (product, not implement)

A later runtime slice proves MAP stage quality against existing contracts. This repository does not implement that slice.

| Intent | Meaning | Existing authority |
|---|---|---|
| Direct-Camera | Camera targets only public `room_id` / public actors already on the snapshot. No invented rooms or hidden topology. | §3.3 allowlist; this document §1.1; lightweight §7 |
| Gate D five-slot | A spectator can still write the five public statements from `/watch`, including MAP. | [LCA-GATE-D-SCENARIO.md](LCA-GATE-D-SCENARIO.md) five-statement checklist |
| Follow-that-teaches | Follow remains one public Player or site; emphasis only; unrelated activity stays visible. MAP camera MAY track that follow target. | [WATCH-LIGHTWEIGHT-SPECTATOR.md](WATCH-LIGHTWEIGHT-SPECTATOR.md) §4.G |

## 4. Current Scope (v0.1)

- Live map with role glyphs, scar visualization, and finite event-born emphasis.
- Event river with iconography and consequence text.
- Compact public context line using existing world, cycle, freshness, and authorized bands.
- Restrained public state marks; no default heat map or research metric overlay.
- Basic narrative highlights.
- Toggleable layers and filters.
- Event-born emphasis only; spectator moments and gamification remain deferred.

## Extension Points

Non-normative future guidance; the binding privacy, motion and reconciliation rules above constrain every extension, including older layer-table suggestions.

### 5.1 Public projection and rendering seams

New layers may consume only server-filtered public snapshot data. Preserve the one `/watch` door, `MAP` as a mode of that door, lightweight public default, one-map-at-a-time, same world heads, deterministic server-selected events/headlines, and safe text nodes. Optional fields must remain compatible with existing `watch-map/1.0` consumers; breaking payload or layer-model changes need the major version and migration notes described in §9. A cosmetic extension cannot authorize a new source of public information.

- Requires separate authorization for the public projection; this document does not authorize raw values or new wire fields.
- Any public encoding must use an existing coarse, semantic role rather than a research scalar or dashboard metric.
- Must support reduced-motion and high-contrast variants.
- Recommended: keep authorized public context adjacent to the map; do not promote it into a competing overlay without reconciliation.

### 5.2 Redaction before visualization

Overlays must remain keyed to publicly exposed rooms and use permitted coarse bands. The earlier raw-value, velocity, reputation and composite-health suggestions are not permission to ship those values: §1.1 and the lightweight doctrine govern. Validate serialized payloads with hidden-room/entity fixtures, absent research scalars and reputation fields, and hostile world text. Compare old-client rendering with optional fields absent and present; no client may reconstruct hidden topology.

### 5.3 Promotion and interaction evidence

A proposed layer should identify its public source, deterministic derivation, legend and structured alternative. Verify pause actually stops polling, hidden documents skip polling, reduced-motion uses instant replacement, and refresh reserves layout space. Record the tested viewport and entity load rather than assuming the target frame rate proves usability. Scrubbers, analytics, badges, voting and generative summaries remain deferred behind a future RFC and lightweight §15 reconciliation row; this section does not reopen them.

## 6. Roadmap & Phasing (Expandable)

**Phase 0 (v0.1 — Current)**
- Core map + glyphs + scars
- Event river + compact public context
- Layer toggles
- **MAP P0 acceptance intent (product, not implement):** Direct-Camera, Gate D five-slot, and Follow-that-teaches (§3.4). This document does not implement the runtime slice.

**Phase 1**
- Narrative highlight system (deterministic, per §3.1)
- Improved flow visualization

**Phase 2** *(each item below overlaps the lightweight contract's §14 deferred list or §3 exclusions — none may proceed without a future RFC **and** a §15 reconciliation row there)*
- Advanced filters and search
- Event replay / scrubber
- Custom spectator layouts (saved configurations)
- Spectator badges / moments

**Phase 3+ (Future Hooks)** *(same gate: future RFC + reconciliation required)*
- Multi-map / realm comparison views
- AI-generated spectator summaries (research-grade toggle)
- Community highlight voting and “best moments” reels
- New visual primitives for future mechanics (e.g., belief diffusion, institution growth rings)
- Performance-adaptive rendering (auto-reduce detail on lower-end clients)

## 6.1 Motion & Refresh (normative)

The lightweight contract's §8 rules apply: bounded polling (8–12 s), a **pause control that stops the poll**, `document.hidden` skips polls, reserved heights (no layout jump on refresh), reduced-motion = instant replace. `MAP` mode without a pause control is a defect. Pause is shared with TEXT and PIXEL; it is not a second poller.

## 7. Accessibility & Cognitive Load

- Reduced motion mode (static updates + clear change indicators).
- High contrast + colorblind palettes.
- Keyboard navigation and screen-reader friendly labels for all major elements.
- “Summary mode” that collapses the map into a structured text + public context view.
- Always-visible legend and “what am I looking at” help.

## 8. Integration with Other Systems

- **Deep Time**: Scars appear as persistent visual residue. Publicly authorized changes MAY receive one finite event-born emphasis.
- **EWM**: Only already-authorized coarse public bands may drive WATCH marks; research scalars stay off the public surface.
- **Semantic Layer**: Only publicly authorized, grounded signals may influence glyph appearance or event presentation; reputation and private research signals stay out.
- **Visual Design**: Must follow the player brand tokens and overall aesthetic direction.

## 8.1 Reconciliation with WATCH-LIGHTWEIGHT-SPECTATOR

| Tension | Resolution |
|---|---|
| “dashboard” doctrine (§1 there forbids it) | This mode is layered density, not telemetry: no KPI grids beyond the small health panel, no charts/sparklines, no world-pressure meters, no spectator analytics. The self-description “dashboard-style” is retired. |
| One map at a time (§4.B.1 there) | Governs the public door `/watch` (TEXT cartogram / PIXEL phosphor / MAP). `MAP` is a mode of that door; it never embeds beside TEXT or PIXEL. A historical `/watch/map` URL MAY redirect to `/watch` with MAP selected. |
| Cognitive-load contract (§3 there) | Binds `/watch`. `MAP` carries its own restraint list (§1 “It is not” + §1.1 + §6.1) rather than §3's exact widget caps. |
| Phosphor default (§18 there) | Unchanged — the phosphor sketch remains the public door's default cartography. `MAP` is not the default anything. |
| Same world heads | `MAP` MUST display the same `world_id`, `cycle`, `sequence`, and `freshness` as TEXT and PIXEL. `watch-map/1.0` adds coarse bands only. A second head is a defect. |
| Client interest scoring (SPECTATOR.md) | Banned here too; tiers/importance are server-side only. |
| AI narration / voting / badges (§3/§14 there) | Not in v0.1; gated on future RFC + reconciliation (see §6 gates). |
| WebGL on public WATCH | Absolute ban retired for the MAP mode stage only (§3.3 allowlist). PIXEL stays Canvas 2D until a later explicit row. Anti-cosplay bans stay. |

## 9. Versioning & Stability

- This spec follows the same versioning as the broader WATCH surfaces but is explicitly versioned independently for the rich mapping experience.
- Breaking changes to data contracts or layer model require a new major version and migration notes.
- Cosmetic and additive changes (new layers, new delight elements) are minor.

## 10. Open Extension Contracts

- New event types must declare an icon, a brand-token color role, and a short deterministic consequence template.
- New entity statuses must declare at least one visual encoding (glyph, color, border, or finite event-born emphasis).
- Performance follows the existing WATCH and Phosphor budgets: deterministic event-driven redraw, no idle loop, and bounded bursts; no continuous 30–60 fps requirement.

---

**This document is intentionally structured with clear tables, numbered layers, and an explicit “Extension Points” section so that future mechanics, visual primitives, and interaction modes can be added cleanly without architectural rewrites.**

See also the research notes on cognitive accessibility, glanceable interfaces, and real-time visualization patterns that informed the principles above.
