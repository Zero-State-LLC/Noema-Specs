# WATCH — Visual Direction & Map-First Composition

**Status:** Specified
**Kind:** Presentation and visual-composition contract
**Scope:** Public WATCH and compatible WATCH map surfaces
**Authority:** Additive to existing WATCH projection and privacy contracts
**Protocol impact:** None
**World-rule impact:** None
**RFC required:** No, unless existing repository governance says otherwise

Related: [WATCH.md](WATCH.md) · [WATCH-LIGHTWEIGHT-SPECTATOR.md](WATCH-LIGHTWEIGHT-SPECTATOR.md) · [WATCH-REAL-TIME-MAPPING.md](WATCH-REAL-TIME-MAPPING.md) · [SPECTATOR.md](SPECTATOR.md) · [VISUAL-DESIGN.md](VISUAL-DESIGN.md) · [PLAYER-BRAND.md](PLAYER-BRAND.md) · [EXPERIENCE.md](EXPERIENCE.md) · [CHAMBER-MAP.md](CHAMBER-MAP.md) · [PARTIAL-OBSERVABILITY.md](PARTIAL-OBSERVABILITY.md) · [OBSERVATION.md](OBSERVATION.md) · [ADMIN-LIVE-OPERATIONS.md](ADMIN-LIVE-OPERATIONS.md) · [SPEC-CHECKLIST.md](../SPEC-CHECKLIST.md)

This document specifies how WATCH is composed and rendered. It does **not** alter canonical world state, event semantics, visibility or redaction, spectator projection authority, authentication, PLAY, STUDY, Admin Live, Genesis, or gameplay rules. It does not add protocol fields, schemas, event types, routes, permissions, or runtime behavior. Existing projection, privacy, accessibility, performance, and epistemic contracts remain authoritative.

---

## 1. Doctrine

WATCH is a **diegetic observation terminal into a living world**. It is a public, derived view through which a spectator watches places, routes, occupants, activity, consequence, and uncertainty. The map is the dominant object. Telemetry surrounds the map rather than competing with it.

The governing abstraction is:

```text
NOT: data -> cards -> charts -> game
BUT: world -> activity -> evidence -> controls
```

The visual hierarchy is:

```text
WORLD
  ↓
EVENTS
  ↓
METADATA
  ↓
CHROME
```

Wherever a fact is spatial, WATCH SHOULD represent it spatially. The spectator should be able to answer quickly:

```text
WHERE is activity happening?
WHO or WHAT is there?
WHAT just changed?
WHAT part of the world is known?
WHAT deserves attention?
```

WATCH MUST feel like one coherent instrument looking into an inhabited environment. It MUST NOT visually read as a SaaS analytics product, admin dashboard, monitoring dashboard, research console, generic React card layout, crypto dashboard, decorative spaceship HUD, or cyberpunk wallpaper with telemetry laid over it.

This direction is additive to the low-cognitive-load public contract in [WATCH-LIGHTWEIGHT-SPECTATOR.md](WATCH-LIGHTWEIGHT-SPECTATOR.md) and compatible with the richer opt-in mapping surface in [WATCH-REAL-TIME-MAPPING.md](WATCH-REAL-TIME-MAPPING.md). Neither surface becomes a new source of truth.

---

## 2. Non-normative reference grammar

The following references establish a visual grammar only. They are **non-normative aesthetic references**, not assets to copy and not licenses to reproduce copyrighted artwork, UI, typography, layouts, or visual identity verbatim.

### Duskers - primary framing reference

Duskers supplies:

- sparse tactical composition;
- rooms treated as operational spaces;
- a restrained palette;
- a map embedded inside a terminal context; and
- world data that feels instrumental rather than decorative.

Do not copy exact art, layouts, assets, typography, or proprietary visual identity.

### Cogmind - information-density reference

Cogmind supplies:

- a semantic glyph vocabulary;
- high information density with strong hierarchy;
- a terminal-native visual language; and
- compact symbolic forms that distinguish known, unknown, active, and consequential state.

The reference is for density and symbol discipline, not for copying sprites or interface treatments.

### Caves of Qud - symbolic-world reference

Caves of Qud supplies:

- the idea that low-resolution symbols can carry world identity;
- distinctive terrain and institutions without detailed illustration; and
- a consistent symbolic grammar from which world character emerges.

WATCH glyphs describe places and states. They are not merely data-class badges.

### Heat Signature - topology reference only

Heat Signature supplies a light reference for the immediate readability of rooms, corridors, actors, and activity. Use this lightly. It does not authorize action-game UI, tactical HUD chrome, or a second gameplay model in WATCH.

### Working synthesis

```text
Duskers supplies the frame.
Cogmind supplies information density.
Caves of Qud supplies world character.
NOEMA supplies the epistemology.
```

NOEMA's public projection, privacy rules, partial observability, and text authority are stricter than any aesthetic reference.

---

## 3. Normative composition hierarchy

The primary WATCH hierarchy is:

```text
1. WORLD MAP
2. CURRENT / NOTABLE EVENT
3. RECENT EVENT STREAM
4. WORLD + CYCLE + FRESHNESS METADATA
5. CONTROLS / LEGEND / MODE SWITCHING
```

The **world map MUST occupy the majority of the primary desktop viewport's first-glance visual weight**, with an indicative target of approximately **60-75%**. This is a compositional target, not a pixel-locked layout or a new viewport contract. The map MUST NOT be reduced to a small widget beside equally weighted cards.

The current or notable event explains what changed in the world. The bounded event stream supplies recent evidence. Metadata establishes world, cycle, and freshness context. Controls, legend, and mode switching remain compact and subordinate.

On mobile, map primacy MUST survive reflow without horizontal scrolling. A bounded responsive map may stack above event content. Details expand below the map. The mobile surface MUST remain a map-first WATCH surface, not an unrelated card feed.

A fact that is spatial MUST appear on the map when its public projection supports a spatial representation. A detached textual or metric treatment MAY supplement it, but MUST NOT replace the spatial relationship when that relationship is public and meaningful.

---

## 4. WATCH visual grammar

### 4.1 Ground

- Use `color.surface.world` and the canonical surface tokens in [VISUAL-DESIGN.md](VISUAL-DESIGN.md).
- The world field SHOULD be near-black or charcoal, with enough contrast for routes, labels, glyphs, and event marks.
- Giant decorative gradient backgrounds are prohibited.
- A subtle grid or scanline texture MAY be used only when it improves orientation, does not reduce readability, and does not animate continuously.
- Texture is never evidence. It MUST NOT imply topology, activity, certainty, or hidden space.

### 4.2 Geometry

- Prefer crisp lines, small radii, or square geometry.
- Use terminals, plates, room outlines, route lines, bounded wells, and continuous surfaces where they clarify the world.
- Avoid excessive rounded cards, floating UI islands, and ornamental pill systems.
- A route is a route, a room is a room, and a panel is subordinate framing. Do not make every object a detachable card.
- Geometry MUST NOT imply an unpublished room, exit, boundary, or region.

### 4.3 Typography

Use the canonical type roles in [VISUAL-DESIGN.md](VISUAL-DESIGN.md):

- **Display** for world identity, districts, important sites, and major changes;
- **Interface** for readable labels, event phrases, descriptions, controls, and help; and
- **Machine / Data** for timestamps, coordinates when public, receipts, and other explicitly machine-like output.

Monospace MAY represent world or system state where the terminal register helps comprehension. It MUST NOT be used as a shortcut for tiny type or universal atmosphere. Labels, site names, events, and controls MUST remain extremely readable. Density is achieved through hierarchy and spatial arrangement, not illegible text.

### 4.4 Color

Color is semantic, not decorative. Use the canonical semantic tokens and preserve their roles:

- `color.state.active` for activity, live signal, availability, or selected/follow state;
- `color.state.warning` for caution, strain, pending threshold, or degraded state;
- `color.state.critical` for danger, hostile condition, failure, or incident;
- `color.state.unknown` for incomplete, unreadable, or permitted uncertainty;
- `color.state.economic` sparingly for public trade or surplus opportunity; and
- `color.state.social` for public presence and social identity.

There MUST NOT be a rainbow categorical palette or decorative neon treatment. Every color role MUST have a non-color companion such as a label, glyph silhouette, line treatment, position, or text. A spectator must be able to understand the state in monochrome or with color-vision differences.

---

## 5. Map-first doctrine

The map is not decoration. It is the visual representation of the public spectator projection.

The map SHOULD directly encode, when present in the authorized public snapshot:

- public sites;
- public routes;
- public occupants;
- public activity;
- public event location;
- public traces or scars already authorized for WATCH; and
- public uncertainty where the canon permits uncertainty to be disclosed.

If a fact is spatial, prefer a spatial representation over a detached card or KPI. For example:

```text
GOOD:   a trade event pulses at the public market node
WORSE:  a detached "trade events" dashboard tile

GOOD:   an active public site brightens
WORSE:  an "active rooms: 3" KPI card with no locations

GOOD:   an authorized scar appears as residue at its public location
WORSE:  a scar-count graph detached from topology
```

The map MUST consume the existing server-derived public projection. It MUST NOT require client-side reconstruction of hidden data, new salience logic, or backend churn. Do not add facts that the current public WATCH contract does not expose.

The public map is not Admin topology. Operator maps, raw world maps, authenticated views, research overlays, and private observation boundaries remain separate surfaces.

---

## 6. Epistemic visual states

WATCH visual states MUST align with [PARTIAL-OBSERVABILITY.md](PARTIAL-OBSERVABILITY.md), [OBSERVATION.md](OBSERVATION.md), and the existing spectator contracts.

Explicit visual states include, where authorized:

```text
unknown
known
active
selected
followed
recent event
major event
public residue / scar
uncertain / partial
```

These states are presentation states for already-authorized public facts. They do not create new visibility classes or imply a new protocol.

### 6.1 Absence rules

- Unknown topology MUST remain absent.
- Do not render silhouetted hidden rooms.
- Do not create fog geometry, dashed phantom rooms, placeholder nodes, or empty slots that imply the shape of unpublished space.
- Do not use a missing route, 404, error, array position, timing difference, or visual gap to hint at hidden topology.
- If uncertainty itself is public knowledge, encode uncertainty with a label, permitted glyph, or restrained state treatment without implying hidden geometry.
- A public residue or scar may appear only when the existing WATCH contract authorizes it. It MUST remain attached to its public location and MUST NOT expose source IDs or private history.

A missing object means absence from this projection, not a client invitation to infer more.

### 6.2 Brightness and emphasis

Brightness, opacity, border weight, or glyph choice MAY distinguish known, active, selected, and recent public states. These treatments MUST remain semantic and bounded. They MUST NOT convert uncertainty into a confidence score or activity into a decorative glow field.

---

## 7. Glyph system

WATCH MUST reconcile with the existing **NOEMA Phosphor Glyph Atlas** in [WATCH-LIGHTWEIGHT-SPECTATOR.md](WATCH-LIGHTWEIGHT-SPECTATOR.md) §18. It MUST NOT create a second incompatible glyph vocabulary.

Use compact symbolic marks. Symbols come before sprites. Icons must carry meaning. Decorative icons are prohibited.

Existing named concepts remain valid unless a stricter existing rule applies:

- `room_empty`
- `room_known`
- `room_active`
- `room_partial`
- `player_single`
- `player_multi`
- `player_cluster`
- `exit`
- `exit_active`
- `pulse_normal`
- `pulse_notable`
- `pulse_major`

Visual-direction rules around that atlas:

- Glyphs SHOULD be distinct by silhouette where practical.
- Use symbols before illustrated sprites.
- No portraits.
- No inventory-art clutter.
- No arbitrary faction heraldry unless future canon defines it.
- No resource icon field or decorative status ornament is implied by this document.
- Active states MUST NOT require constant animation.
- Glyph size, drawing order, logical resolution, Canvas limits, and TEXT authority remain governed by the existing Phosphor section.

A glyph is an encoding of an authorized public state, not an excuse to expose a field. If a public field has no canonical visual mark, use text or omit the mark rather than invent a new semantic vocabulary in the client.

---

## 8. World character

The map MUST have recognizable world character without becoming a detailed illustrated tileset or sterile node graph.

Public places may be differentiated through:

- label treatment;
- tiny site-class marks already supported by canon;
- outline structure;
- topology;
- public residue; and
- canonical semantic glyph variation.

Detailed illustrated tilesets are out of scope unless separately specified. The desired equation is:

```text
low graphical complexity + high semantic specificity = recognizable places
```

A spectator should eventually recognize important NOEMA locations from topology and symbolic marks alone. Civic Exchange, Relay Quarter, Archive, Frontier Gate, and other public sites may feel different because their names, route relationships, outline grammar, and authorized public traces differ, not because each receives a decorative illustration.

World character MUST NOT be produced by hidden topology, arbitrary faction marks, ungrounded lore, visual noise, or non-semantic animation.

---

## 9. Event presentation

Events originate in the world. When an event has a public location, the map SHOULD show where it occurred before or alongside the textual description.

Use the existing server-derived event tiers:

```text
NORMAL
NOTABLE
MAJOR
```

Do not invent client-side salience scoring. Do not infer importance from color, event frequency, screen position, or an analytics heuristic.

Motion MUST be event-born and finite. Allowed examples include:

- a brief pulse at a public event node;
- a brief brightness change on an affected public edge;
- a short public residue reveal where the existing contract permits it; and
- temporary emphasis for one MAJOR event.

Prohibited:

- ambient particles;
- continuously pulsing nodes;
- moving scanlines used as decoration;
- constant glowing;
- perpetual route animations;
- non-semantic background animation; and
- any motion that continues when the world and map are idle.

Idle world means visually idle interface. Existing Phosphor limits apply: one MAJOR treatment at a time, bounded event bursts, no idle animation loop, and no animation in reduced-motion mode.

At most one MAJOR visual treatment MAY be active across headline, map, and event stream. Competing emphasis is a defect.

---

## 10. Event stream

The event stream is a terminal log attached to the map. It is evidence of recent public activity, not the primary surface and not a raw ledger.

Use the bounded recent-event window already defined by WATCH canon. Prefer concise deterministic lines such as:

```text
10:48  ORIN entered CINDER
10:49  VELA -> ORIN   trade.offer
10:49  CINDER rumor propagated
10:50  unknown movement / eastern boundary
```

The exact fields, names, timestamps, locations, tiers, and phrases MUST come from the public projection. Never fabricate event fields. Any shorthand MUST be deterministic and derived from canonical public narrative or templates. A display clock MUST NOT imply ledger time authority.

The stream SHOULD visually attach each located event to its map location through a matching mark, selected state, or accessible location link. The coupling is presentation only and does not change event semantics. Events without a public location remain textual and MUST NOT be assigned a guessed location.

The stream MUST remain bounded, readable, keyboard accessible, and subordinate to the map. It MUST NOT become a scrolling firehose, chart, sparkline, timeline scrubber, or spectator analytics feed.

---

## 11. Chrome minimization

Controls, legend, mode switching, freshness, and supporting metadata should make the map understandable without competing with it. WATCH should feel like one coherent instrument.

The following are explicit prohibitions on web-dashboard drift:

- giant header regions;
- card grids;
- KPI cards;
- glass panels;
- floating statistic badges;
- excessive pills;
- large hero sections inside WATCH;
- oversized title typography;
- decorative charts;
- sparkline telemetry;
- gradients behind every panel;
- generic shadcn/SaaS composition;
- large empty whitespace separating logically connected world information; and
- admin or research control chrome on the public surface.

A compact top bar MAY identify the world, cycle, and freshness. A small legend MAY sit beside or below the map. A selected-site detail view MAY appear beside or below the map. None may reduce the map to a small widget or add a second data hierarchy.

Do not use a panel, badge, or chart merely because the data can be counted. Counts belong on the map when they identify public occupancy or activity, and otherwise remain within the existing WATCH metadata contract.

---

## 12. Reference wireframe

The following is **non-normative visual-composition guidance**, not literal runtime data:

```text
┌─ PERIHELION / CINDER DISTRICT ───────────── cycle 481 ─┐
│                                                        │
│      ░░░░░░                  ┌─────────┐               │
│    ░░.....░░                 │ TRADE   │               │
│   ░..╔═══╗..░───────┐        └────┬────┘               │
│   ░..║ @ ║..░       │             │                    │
│   ░..╚═╤═╝..░       └──────┐      │                    │
│   ░....│....░              ├───────┘                    │
│    ░░░░│░░                │                            │
│        │             ┌────┴─────┐                      │
│   ○────┼─────────────│     Δ    │                      │
│        │             └──────────┘                      │
│   ?    │                         ☼                     │
│                                                        │
├─ OBSERVED ──────────────────────────────────────────────┤
│ 10:48 ORIN entered CINDER                              │
│ 10:49 VELA → ORIN  trade.offer                        │
│ 10:49 CINDER rumor propagated                         │
│ 10:50 unknown movement / eastern boundary             │
└────────────────────────────────────────────────────────┘
```

The characters `?`, `☼`, `@`, `Δ`, and other marks in this wireframe are illustrative only. They MUST NOT be treated as canonical glyph IDs unless the existing atlas defines them. Implementations use the existing glyph vocabulary and accessible text labels.

---

## 13. Desktop composition

Preferred desktop composition:

```text
TOP BAR
  compact world identity / cycle / freshness

PRIMARY
  large public map viewport

SECONDARY
  bounded recent event log
  optional selected-site detail
  small legend / controls
```

The top bar MUST remain compact. The primary map MUST retain the dominant first-glance weight. The secondary area MAY share an edge with the map or sit below it, but MUST NOT split the screen into many equally weighted cards.

Selected-site detail is progressive disclosure. It may show public occupants, public activity, public routes, authorized public traces, and recent events for that location. It MUST NOT expose Admin fields, hidden rooms, private inventories, private cognition, research metrics, or an authenticated observer's extra fields on the public door.

---

## 14. Mobile composition

Mobile WATCH remains map-first:

- no horizontal scrolling is required;
- the map may use a bounded responsive viewport;
- details expand below the map;
- the event stream follows the map;
- controls remain compact;
- legends may collapse when necessary;
- the TEXT fallback remains complete; and
- touch targets remain accessible.

A semantic list or TEXT representation MUST remain available if a bounded map cannot fit. Do not require pinch-zoom, hover, or a two-dimensional map to understand where public activity is occurring. Do not turn mobile WATCH into an unrelated card feed.

The preferred mobile order is:

```text
world / freshness
public map
current or notable event
recent event stream
selected-site detail
compact controls / legend
```

The exact order MAY reflow for reading and accessibility, but map primacy and event location coupling remain.

---

## 15. Accessibility

All existing accessibility requirements remain in force. In particular:

- semantic HTML is the authority;
- Canvas MUST NOT contain unique facts;
- TEXT mode MUST remain complete and authoritative;
- controls MUST be keyboard-operable;
- focus MUST be visible;
- state MUST be distinguishable without color alone;
- reduced-motion support MUST be honored;
- labels MUST remain readable;
- untrusted world text MUST be rendered safely;
- no interaction may require hover alone; and
- touch targets MUST meet the existing minimum in [VISUAL-DESIGN.md](VISUAL-DESIGN.md).

The map MUST have an adjacent or associated semantic representation naming public sites, routes, occupants, activity, and event locations that the map conveys. Canvas may progressively enhance that representation, but it cannot be its only accessible form.

Screen-reader behavior MUST preserve the existing WATCH rules: the event feed is not an unbounded live region, headline updates are polite at most, and a spectator can inspect public site details without needing to interpret a canvas.

Safe rendering of public labels, descriptions, event lines, and other world text is mandatory. Presentation changes do not authorize interpolated markup or relaxed XSS handling.

---

## 16. Performance

Preserve the existing Phosphor performance doctrine and the lightweight WATCH refresh contract:

- Canvas 2D only where existing canon permits it;
- no WebGL;
- no third-party graphics engine;
- deterministic map layout;
- event-driven redraw;
- no continuous idle animation;
- pause when the document is hidden;
- respect bounded polling, pause, and reduced-motion behavior;
- respect existing JavaScript and asset budgets;
- prefer code-drawn glyphs; and
- avoid large image dependencies.

The map MUST be deterministic for an identical public snapshot. TEXT and PIXEL MUST derive from the same public layout so that they agree spatially. A visual redesign MUST NOT introduce a second layout authority.

Performance is not a reason to remove semantic content. If graphical rendering is unavailable, slow, hidden, or fails, the semantic graph and TEXT mode remain complete. If a richer mapping surface uses layers, those layers MUST be bounded, optional, and subordinate to the public map.

---

## 17. Relationship to existing WATCH specifications

The following reconciliation is normative for interpretation of this document and the existing WATCH canon:

| Existing specification | Relationship and reconciliation |
|---|---|
| [WATCH.md](WATCH.md) | WATCH remains the primary human product surface and a derived public projection. This document makes the map-first visual composition explicit without changing the long-term surface catalog or public projection authority. |
| [WATCH-LIGHTWEIGHT-SPECTATOR.md](WATCH-LIGHTWEIGHT-SPECTATOR.md) | This document clarifies how the low-cognitive-load public surface looks. It does not loosen cognitive-load limits, public redaction, deterministic headline rules, event-window limits, TEXT authority, map privacy rules, or event-tier rules. Its Phosphor atlas and render rules remain authoritative for the optional Canvas sketch. |
| [WATCH-REAL-TIME-MAPPING.md](WATCH-REAL-TIME-MAPPING.md) | The same map-first composition and visual grammar bind the richer mapping mode unless that document explicitly defines a stricter rule. Additional layers remain opt-in, deterministic, public-projection-safe, and semantically restrained. Existing language about HUD, world health panels, gamification, heat maps, and metric overlays is not permission to drift into dashboard composition or expose research metrics. Narrow reconciliation edits identify those limits; unrelated future-roadmap text is not silently rewritten. |
| [SPECTATOR.md](SPECTATOR.md) | The spectator output remains a derived, read-only, permissioned projection. High-drama events are source material for event presentation, not permission for extra widgets, scores, or private detail. |
| [VISUAL-DESIGN.md](VISUAL-DESIGN.md) | Canonical tokens, type roles, motion rules, accessibility, responsive behavior, and the prohibition on generic SaaS, decorative CRT treatment, excessive HUD, and non-semantic animation remain authoritative. This document specializes composition for WATCH and does not create a second palette. |
| [PLAYER-BRAND.md](PLAYER-BRAND.md) | WATCH remains a player-facing world surface with a game-first, world-native register. Research instrumentation remains underneath and must not dominate public WATCH. |
| [ADMIN-LIVE-OPERATIONS.md](ADMIN-LIVE-OPERATIONS.md) | Admin topology, operator telemetry, health overlays, settlement state, Genesis internals, and control-plane chrome remain separate. Public map-first composition MUST NOT expose or imitate Admin Live state. |
| [PARTIAL-OBSERVABILITY.md](PARTIAL-OBSERVABILITY.md) and [OBSERVATION.md](OBSERVATION.md) | Absence, permission, uncertainty, staleness, and provenance rules remain unchanged. A visual mark cannot turn a partial or absent fact into world truth. |
| [CHAMBER-MAP.md](CHAMBER-MAP.md) | The canonical Chamber map remains the map authority for product geography. WATCH presents only the public projection of that geography; it does not add subrooms, internal grids, or alternate movement geometry. |
| [EXPERIENCE.md](EXPERIENCE.md) | WATCH remains a human spectator surface in the product hierarchy, not PLAY, STUDY, CONNECT, or ADMIN. The map is a presentation of the world, not a new gameplay interaction model. |
| [SPEC-CHECKLIST.md](../SPEC-CHECKLIST.md) | This document is an additive presentation contract. Existing checklist gates for player brand, visual design, privacy, accessibility, and runtime/spec separation remain applicable. |

### 17.1 Specific mapping tensions

The richer mapping specification contains roadmap and extension language that can otherwise encourage drift. For WATCH interpretation:

- **HUD** means only compact accessible controls, legend, and event log framing. It does not authorize military reticles, instrument clusters, or equal-weight chrome.
- **World health panel** means, at most, a small public context treatment using already-authorized coarse bands and freshness. It does not authorize Admin health overlays, research metrics, KPI cards, or a second hierarchy.
- **Gamification** is not part of the current public WATCH composition. Event-born finite emphasis may clarify consequence. Badges, streaks, moments, ranking, and spectator analytics remain deferred and gated by existing governance.
- **Heat map** is not a default visual. Public coarse bands may use restrained semantic marks only when the current projection authorizes them and the encoding does not imply hidden topology or raw metric precision.
- **Metric overlays** are not a general client extension point. Only already-authorized public projection fields may be visualized. Research, EWM, velocity, concentration, reputation, detector confidence, and raw counters remain off the public surface unless separately authorized by existing canon.

---

## 18. Migration contract

The existing WATCH implementation MUST be **migrated, not discarded**.

Preserve all working:

- projection endpoints;
- schema contracts;
- server-side filtering;
- privacy and redaction;
- deterministic event selection;
- public topology filtering;
- accessibility;
- TEXT mode;
- follow state;
- room and site inspection;
- freshness, maintenance, and incident handling;
- event tiers; and
- pause and reduced-motion behavior.

The redesign should primarily change:

```text
composition
visual hierarchy
map prominence
chrome spacing
geometry
symbol presentation
event-map coupling
```

A visual redesign is not justification for backend churn, a new public schema, a new event catalog, a new visibility class, a new route, a new world-state field, or a change to server-derived salience. Any implementation gap that requires one of those changes is outside this document and must follow the existing change-control process.

The semantic graph and existing TEXT/PIXEL relationship remain a single presentation authority. Do not implement a second map renderer with a divergent layout, a second glyph atlas, or a client-only event taxonomy.

---

## 19. Acceptance criteria

A compatible WATCH implementation satisfies this specification when:

1. The world map is the dominant first-glance element.
2. A viewer can identify where current activity is happening within several seconds when a public location exists.
3. WATCH does not resemble a SaaS dashboard, monitoring console, or card-grid analytics product.
4. No hidden topology is visually implied.
5. Publicly located events visibly originate from their public locations.
6. Idle state contains no continuous decorative motion.
7. Semantic color roles remain limited, canonical, and understandable without color alone.
8. TEXT mode remains complete and authoritative.
9. Canvas contains no unique factual information.
10. The current WATCH backend and projection contract do not require redesign merely to satisfy the visual change.
11. Desktop and mobile preserve map primacy without required horizontal scrolling.
12. Existing WATCH privacy, redaction, epistemic, performance, and accessibility tests remain applicable.
13. A code agent can implement the intended hierarchy without inventing visual policy.
14. The existing Phosphor glyph vocabulary is reused rather than forked.
15. Current/notable event, bounded recent events, metadata, and controls remain subordinate in that order.
16. Public residue, uncertainty, selection, and follow states are rendered only from authorized projection facts.
17. Reduced-motion mode removes pulses, interpolation, and idle animation without removing meaning.
18. Public and Admin topology remain distinct.

---

## Implementation follow-up

This specification does not implement runtime code. The smallest compatible implementation slice is:

1. Keep the existing `watch-live/1.0` endpoint, server filtering, event selection, and accessibility structure.
2. Establish one deterministic public room/route layout consumed by both semantic/TEXT and Phosphor/PIXEL presentations.
3. Recompose the public WATCH shell around the large map, one current/notable event, bounded recent events, compact metadata, and subordinate controls.
4. Couple located event emphasis to the existing server-derived tier and public `room_id` without adding client salience logic.
5. Run the existing privacy, hidden-topology, TEXT/PIXEL, reduced-motion, idle-animation, keyboard, mobile, and XSS checks.

Potential runtime/spec drift to verify during implementation includes whether the shipped surface still uses a card-first composition, whether TEXT and PIXEL share layout deterministically, and whether any richer mapping layer currently exposes research or Admin-only metrics. These are implementation follow-ups, not permissions to change the public contract in this documentation task.
