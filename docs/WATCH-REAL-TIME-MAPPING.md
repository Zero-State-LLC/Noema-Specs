# WATCH — Real-Time Mapping & Spectator System

**Version:** v0.1.1 (Draft)  
**Date:** 2026-08-21 (reconciled 2026-08-21 evening)  
**Status:** Specs-first. Implementation follows review.  
**Kind:** Rich visual spectator projection layer (complements the lightweight theater surface).  
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

This document defines the **real-time mapping spectator surface** — a richer, layered live view. It is designed to be **easily expandable** over time while preserving immediate comprehension, visual pleasure, and fun for watchers. It is not a dashboard: the doctrinal exclusions of [WATCH-LIGHTWEIGHT-SPECTATOR.md](WATCH-LIGHTWEIGHT-SPECTATOR.md) §1 ("WATCH is not") bind every WATCH surface, this one included — the difference here is density and layering, never telemetry, scoring, or narration.

The map-first composition and visual grammar of [WATCH-VISUAL-DIRECTION.md](WATCH-VISUAL-DIRECTION.md) bind this surface unless this document explicitly defines a stricter rule. Additional layers MUST remain world-first, deterministic, public-projection-safe, and semantically restrained.

## 1. Purpose & Boundaries

WATCH Real-Time Mapping provides a visually rich, glanceable, and engaging live view of the world that goes beyond the lightweight theater mode.

**It is:**
- A derived, read-only projection.
- Focused on immediate understanding + long-term engagement.
- Built on the same canonical event + state data as other spectator surfaces.
- Intentionally more visual and layered than the lightweight default.

**It is not:**
- A replacement for the lightweight spectator experience (see [WATCH-LIGHTWEIGHT-SPECTATOR.md](WATCH-LIGHTWEIGHT-SPECTATOR.md)).
- A dense telemetry dashboard or graph-heavy monitoring product (§1 doctrine of the lightweight contract applies).
- An admin or research analytics surface.
- A player HUD.
- A raw event firehose.
- The public door's map: `/watch` keeps its own §4.B/§18 cartography; this surface lives on its own opt-in route and MUST NOT render alongside them.

The two surfaces can coexist: the lightweight version remains the public default; the real-time mapping system is an opt-in richer mode (or separate route).

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

- Primary: **Canvas 2D** (WebGL remains banned on public WATCH — lightweight §18). HTML/CSS layout (the shipped v0.1 renderer) is equally compliant; smooth interpolated movement is optional enhancement, never information.
- UI chrome: HTML/CSS for compact controls, legend, event log, and selected-site detail (easy accessibility).
- Animation contract: All movement and state changes use a shared easing/timing system. New visual primitives must declare their animation behavior.

## 4. Current Scope (v0.1)

- Live map with role glyphs, scar visualization, and finite event-born emphasis.
- Event river with iconography and consequence text.
- Compact public context line using existing world, cycle, freshness, and authorized bands.
- Restrained public state marks; no default heat map or research metric overlay.
- Basic narrative highlights.
- Toggleable layers and filters.
- Event-born emphasis only; spectator moments and gamification remain deferred.

## 5. Extension Points (for Future Growth)

This section is the primary mechanism for easy expansion.

### 5.1 Adding a New Visual Layer
1. Define the data schema extension (optional fields).
2. Register the layer in the rendering pipeline with priority and z-order.
3. Implement a toggle + legend entry.
4. Document impact on cognitive load and performance budget.

### 5.2 Adding New Metrics or Overlays
- Requires separate authorization for the public projection; this document does not authorize raw values or new wire fields.
- Any public encoding must use an existing coarse, semantic role rather than a research scalar or dashboard metric.
- Must support reduced-motion and high-contrast variants.
- Recommended: keep authorized public context adjacent to the map; do not promote it into a competing overlay without reconciliation.

### 5.3 Adding New Interaction Modes
- Define as a “Mode” with clear entry/exit and data requirements.
- Examples of planned future modes: “Director View”, “Timeline Scrub”, “Story Follow”, “Comparison Mode”.

### 5.4 Integrating New Game Mechanics
When a new system is added (e.g., new semantic signals, new Deep Time features, new resource types):
- Add a corresponding data field to the common projection.
- Define at least one visual primitive (glyph modification, overlay, or event type).
- Update the “immediate comprehension” test cases.

### 5.5 Performance & Density Controls
- Global density slider (low / medium / high).
- Per-layer enable/disable.
- Automatic aggregation when entity or event count exceeds thresholds.

## 6. Roadmap & Phasing (Expandable)

**Phase 0 (v0.1 — Current)**
- Core map + glyphs + scars
- Event river + compact public context
- Layer toggles

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

The lightweight contract's §8 rules apply: bounded polling (8–12 s), a **pause control that stops the poll**, `document.hidden` skips polls, reserved heights (no layout jump on refresh), reduced-motion = instant replace. A mapping page without a pause control is a defect.

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
| “dashboard” doctrine (§1 there forbids it) | This surface is layered density, not telemetry: no KPI grids beyond the small health panel, no charts/sparklines, no world-pressure meters, no spectator analytics. The self-description “dashboard-style” is retired. |
| One map at a time (§4.B.1 there) | Governs the public door `/watch` (semantic list / cartogram / phosphor). This surface is a **separate opt-in route**; it never embeds beside those maps, and `/watch` MAY link to it as plain text. |
| Cognitive-load contract (§3 there) | Binds `/watch`. This surface carries its own restraint list (§1 “It is not” + §1.1 + §6.1) rather than §3's exact widget caps. |
| Phosphor default (§18 there) | Unchanged — the phosphor sketch remains the public door's default cartography. This surface is not the default anything. |
| Client interest scoring (SPECTATOR.md) | Banned here too; tiers/importance are server-side only. |
| AI narration / voting / badges (§3/§14 there) | Not in v0.1; gated on future RFC + reconciliation (see §6 gates). |

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
