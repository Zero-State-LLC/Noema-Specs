# WATCH — Real-Time Mapping & Spectator System

**Version:** v0.1 (Draft)  
**Date:** 2026-08-21  
**Status:** Specs-first. Implementation follows review.  
**Kind:** Rich visual spectator projection layer (complements the lightweight theater surface).  
**Related:**
- [WATCH.md](WATCH.md)
- [WATCH-LIGHTWEIGHT-SPECTATOR.md](WATCH-LIGHTWEIGHT-SPECTATOR.md) (low-cognitive-load default)
- [SPECTATOR.md](SPECTATOR.md)
- [CHAMBER-MAP.md](CHAMBER-MAP.md)
- [VISUAL-DESIGN.md](VISUAL-DESIGN.md)
- [DEEP-TIME.md](DEEP-TIME.md) (scars, history as visual residue)
- [ECONOMY-EWM-SPEC.md](ECONOMY-EWM-SPEC.md)
- [DEEP-TIME-MECHANICS-UPDATE.md](DEEP-TIME-MECHANICS-UPDATE.md)

This document defines the **real-time mapping and dashboard-style spectator experience**. It is designed to be **easily expandable** over time while preserving immediate comprehension, visual pleasure, and fun for watchers.

## 1. Purpose & Boundaries

WATCH Real-Time Mapping provides a visually rich, glanceable, and engaging live view of the world that goes beyond the lightweight theater mode.

**It is:**
- A derived, read-only projection.
- Focused on immediate understanding + long-term engagement.
- Built on the same canonical event + state data as other spectator surfaces.
- Intentionally more visual and layered than the lightweight default.

**It is not:**
- A replacement for the lightweight spectator experience (see [WATCH-LIGHTWEIGHT-SPECTATOR.md](WATCH-LIGHTWEIGHT-SPECTATOR.md)).
- An admin or research analytics surface.
- A player HUD.
- A raw event firehose.

The two surfaces can coexist: the lightweight version remains the public default; the real-time mapping system is an opt-in richer mode (or separate route).

## 2. Core Principles (for Expandability)

1. **Immediate Comprehension** — A spectator must understand “what is happening, where, and at what intensity” within seconds.
2. **Layered & Modular** — New data sources, visual primitives, or interaction modes can be added without rewriting existing layers.
3. **Fun + Pleasing** — Micro-animations, narrative highlights, and light gamification elements are first-class but optional.
4. **History-Aware** — Deep Time elements (scars, traces, institutions) are visually persistent and meaningful.
5. **Composable** — Integrates with EWM metrics, semantic signals, and future mechanics via clear extension points.
6. **Accessible by Default** — Reduced-motion, high-contrast, and structured alternatives are built in.

## 3. Architecture (Designed for Extension)

### 3.1 Layer Model

The system is composed of independent, stackable layers. New layers can be inserted or extended without affecting others.

| Layer | Purpose | Current Content (v0.1) | Extension Hook |
|-------|---------|------------------------|----------------|
| Base Map | Spatial layout of rooms/regions | Room graph, clear labels, boundaries | Add new room types, procedural sub-structures |
| Activity Overlay | Movement & flow | Animated traces, recent paths | New flow types (influence, materials, belief) |
| State Overlays | Resource/pressure/scar heat | Subtle gradients for pressure, scars, attention | New metrics from EWM, Semantic, future systems |
| Entity Layer | Agents, objects, institutions | Role glyphs, size/glow by influence, scar residue | New entity classes, status effects, group formations |
| Event Layer | Recent significant changes | Icon + short consequence river | New event categories, importance scoring, grouping |
| Narrative Layer | Story beats & highlights | AI-assisted “what just happened” callouts | Custom narrative generators, spectator-voted moments |
| Health / Context | World-level glanceables | Velocity, concentration, reconstruction fidelity, scar activity | New composite health scores, phase indicators |
| Delight & Gamification | Fun feedback | Micro-animations, spectator badges, event “pops” | New rewards, streaks, community highlights |

### 3.2 Data Contract (Stable Core)

All layers consume a common derived projection (extends existing `watch-live/1.0` concepts):

- Rooms with position + metadata
- Entities (with role, position, visible state, scars)
- Recent events (typed, with grounding to canonical ledger)
- Aggregates (pressure, velocity, scar density, etc.)
- Timestamps for smooth interpolation

**Future-proofing:** New fields are added as optional extensions. Old clients ignore unknown fields.

### 3.3 Rendering & Animation

- Primary: Canvas/WebGL for performance on the map + smooth interpolated movement.
- UI chrome: HTML/CSS for panels, river, and HUD (easy accessibility).
- Animation contract: All movement and state changes use a shared easing/timing system. New visual primitives must declare their animation behavior.

## 4. Current Scope (v0.1)

- Live animated map with role glyphs and scar visualization.
- Event river with iconography and consequence text.
- Glanceable world health panel (EWM + Deep Time metrics).
- Subtle heat/flow overlays.
- Basic narrative highlights.
- Toggleable layers and filters.
- Spectator “moments” (light gamification).

## 5. Extension Points (for Future Growth)

This section is the primary mechanism for easy expansion.

### 5.1 Adding a New Visual Layer
1. Define the data schema extension (optional fields).
2. Register the layer in the rendering pipeline with priority and z-order.
3. Implement a toggle + legend entry.
4. Document impact on cognitive load and performance budget.

### 5.2 Adding New Metrics or Overlays
- Must provide both a raw value and a “glanceable” visual encoding.
- Must support reduced-motion and high-contrast variants.
- Recommended: Add to the Health/Context panel first, then promote to an overlay if needed.

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
- Event river + basic health panel
- Layer toggles

**Phase 1**
- Narrative highlight system
- Improved flow visualization
- Spectator badges / moments

**Phase 2**
- Advanced filters and search
- Event replay / scrubber
- Custom spectator layouts (saved configurations)

**Phase 3+ (Future Hooks)**
- Multi-map / realm comparison views
- AI-generated spectator summaries (research-grade toggle)
- Community highlight voting and “best moments” reels
- New visual primitives for future mechanics (e.g., belief diffusion, institution growth rings)
- Performance-adaptive rendering (auto-reduce detail on lower-end clients)

## 7. Accessibility & Cognitive Load

- Reduced motion mode (static updates + clear change indicators).
- High contrast + colorblind palettes.
- Keyboard navigation and screen-reader friendly labels for all major elements.
- “Summary mode” that collapses the map into a structured text + key metrics view.
- Always-visible legend and “what am I looking at” help.

## 8. Integration with Other Systems

- **Deep Time**: Scars appear as persistent visual residue. Reconstructions trigger visible “healing” animations.
- **EWM**: Pressure, velocity, stock health drive overlays and health panel.
- **Semantic Layer**: Reputation, drift, and grounded signals can influence glyph appearance or event salience.
- **Visual Design**: Must follow the player brand tokens and overall aesthetic direction.

## 9. Versioning & Stability

- This spec follows the same versioning as the broader WATCH surfaces but is explicitly versioned independently for the rich mapping experience.
- Breaking changes to data contracts or layer model require a new major version and migration notes.
- Cosmetic and additive changes (new layers, new delight elements) are minor.

## 10. Open Extension Contracts

- New event types must declare an icon, color, and short consequence template.
- New entity statuses must declare at least one visual encoding (color, size, particle, border).
- Performance budget: map rendering target 30–60 fps on target hardware even with moderate entity counts.

---

**This document is intentionally structured with clear tables, numbered layers, and an explicit “Extension Points” section so that future mechanics, visual primitives, and interaction modes can be added cleanly without architectural rewrites.**

See also the research notes on cognitive accessibility, glanceable interfaces, and real-time visualization patterns that informed the principles above.