# WATCH — Lightweight Spectator Upgrade

**Status:** Specified. Not a product-version pin.  
**Surface nickname:** WATCH v1.5 (informal).  
**Canonical label:** WATCH — Lightweight Spectator Upgrade.  
**Milestone:** v0.1 Chamber hosted experience ([ROADMAP.md](ROADMAP.md)).  
**Kind:** public spectator presentation contract.  
**Not** a protocol, event-catalog, Genesis, or world-rule change. No RFC.

Does not replace [WATCH.md](WATCH.md), [SPECTATOR.md](SPECTATOR.md), [SPECTATOR-ONBOARDING.md](SPECTATOR-ONBOARDING.md), or [spectator-projection.schema.json](../specs/spectator-projection.schema.json).

Related: [EXPERIENCE.md](EXPERIENCE.md) · [HOSTED-FIRST-ENTRY.md](HOSTED-FIRST-ENTRY.md) · [PARTIAL-OBSERVABILITY.md](PARTIAL-OBSERVABILITY.md) · [OBSERVATION.md](OBSERVATION.md) · [CHAMBER-MAP.md](CHAMBER-MAP.md) · [WORLD-OPERATIONS.md](WORLD-OPERATIONS.md) · [INCIDENT-RECOVERY.md](INCIDENT-RECOVERY.md) · [ADMIN-LIVE-OPERATIONS.md](ADMIN-LIVE-OPERATIONS.md) · [SECURITY.md](SECURITY.md) · [PLAYER-ACTION-MAP.md](PLAYER-ACTION-MAP.md).

Hosted reference (non-normative): `https://noema.guru/watch` · `GET /v1/watch/live`.

---

## 1. Doctrine

WATCH is a **low-cognitive-load, read-only spectator window** into the live MUD. It is **enhanced world theater**: readable, atmospheric, low-noise, immediately understandable. It uses the player brand tokens ([VISUAL-DESIGN.md](VISUAL-DESIGN.md)) at a lower information density than PLAY.

A spectator MUST be able to answer, without opening PLAY:

```text
WHAT IS HAPPENING?
WHERE IS IT HAPPENING?
WHO OR HOW MANY PLAYERS ARE INVOLVED?
```

Deeper information requires explicit interaction.

### WATCH is not

WATCH MUST NOT become:

- a dense telemetry dashboard
- an admin/operator surface
- a research analytics UI
- a scrolling firehose of every event
- a Twitch-like broadcast system
- a graph-heavy monitoring product
- a visually noisy cyberpunk interface
- an RPG HUD
- a replacement for PLAY or STUDY

Admin Live topology, Operator Digests, and STUDY overlays remain other planes ([ADMIN-LIVE-OPERATIONS.md](ADMIN-LIVE-OPERATIONS.md), [OPERATOR-DIGESTS.md](OPERATOR-DIGESTS.md), [STUDY.md](STUDY.md)). Admin topology is an operator graphics exception and MUST NOT be the Player/WATCH map ([SPEC-CHECKLIST.md](../SPEC-CHECKLIST.md)).

### WATCH is

```text
A public, derived, permissioned projection.
Never world truth.
Never a writer.
Text-first Chamber theater.
```

Preserve the text-first doctrine ([EXPERIENCE.md](EXPERIENCE.md), [MUD-DESIGN-CANON.md](MUD-DESIGN-CANON.md)). WATCH stays low-load relative to PLAY; that is not a mandate for empty PLAY ([PLAYER-BRAND.md](PLAYER-BRAND.md)). Small functional graphics MAY be used only when they improve glance comprehension. WebGL, portrait grids, decorative motion, and Admin-style topology remain out of scope. The only permitted canvas on public `/watch` is optional **NOEMA Phosphor Cartography** (§18): progressive enhancement of the same `watch-live/1.0` snapshot. TEXT remains complete and authoritative.

---

## 2. Version placement

Product versions remain `0.1` Chamber … `0.7` LEARN ([VERSIONING.md](VERSIONING.md)). **`v1.5` is not a product, spec-pin, or world-rules version.**

This upgrade is a **hosted public WATCH surface revision** under v0.1 Chamber experience. Implementations MAY expose a presentation pin:

```text
watch-live/1.0
```

That pin names the public live snapshot envelope in §6. It MUST NOT bump `spectator-projection/1.0`, `event-catalog/*`, or `world/v1`.

---

## 3. Cognitive-load contract

At a normal moment WATCH MUST show at most:

1. one primary **current/notable event**
2. one **world graph** (public sites + activity)
3. one **bounded recent-events** surface
4. small status metadata (world, cycle, sequence, freshness, public player count)
5. optional **room detail** only after explicit interaction

At most **one MAJOR** visual treatment MAY be active. Competing emphasis is a defect.

WATCH MUST NOT add, in this upgrade:

- KPI grids beyond the metadata in (4)
- charts, sparklines, large metric sets
- animated backgrounds
- player portrait grids
- story-thread systems
- world-pressure meters
- semantic audio
- cinema/explore modes
- AI narration
- spectator analytics

Those are **deferred** (§14), not forbidden forever.

---

## 4. Presentation surfaces (six features)

### A. Current / notable event

One prominent headline. Example:

```text
> VESPER-7 refuses MARROW's trade.
  Chamber Market · 8 sec ago
```

Rules:

- Exactly one headline, or the empty fallback.
- MUST use only public/redacted projection data.
- MUST NOT fabricate motives or unsupported prose.
- MUST NOT rotate on every poll.
- Routine NORMAL events MUST NOT constantly replace a NOTABLE or MAJOR headline.

**Selection (deterministic):**

1. Consider the server-derived `recent_events` window (newest first, max 16 candidates).
2. If `freshness` is `incident`, treat a synthetic world-status item as MAJOR: “World incident — projection is stale.”
3. If `freshness` is `maintenance`, treat as NOTABLE: “World is in maintenance.”
4. Rank candidates by presentation tier `MAJOR` > `NOTABLE` > `NORMAL`, then by descending `sequence`.
5. **Hold:** keep the current headline unless:
   - a strictly higher-tier candidate arrives, or
   - the current headline’s source `sequence` is older than 8 newer public sequences, or
   - the current headline is no longer in the candidate window.
6. Fallback when the window is empty: “The Chamber is quiet.” If `players_present > 0`, append the public count as a secondary line, not a fake event.

No scoring engine. No AI director.

### B. World graph

Replace the flat “Known sites” tile grid as the **primary spatial surface**. Represent only publicly known sites and known public connections.

**Chosen rendering:** semantic HTML in monospace, arranged as a compact terminal graph. Not canvas. Not a sole ASCII blob.

```text
Primary (accessible):
  <nav> / list of public sites
  each site: name, public player count if > 0, public exits as text
  active sites get a restrained marker (e.g. trailing *)

Optional atmosphere (aria-hidden="true"):
  a compact <pre> generated from the same public graph
  only when public site count ≤ 8 and no node degree > 3
  otherwise omit the <pre>
```

Hidden rooms, hidden exits, and unpublished topology MUST NOT appear. Runtime evidence (`redactedPublicWorld` currently lists every Chamber room) is **not** authority when it conflicts with this rule.

Mobile: drop the `<pre>` if it would require horizontal scrolling. Keep the semantic list. Do not require a two-dimensional map to understand “where people are.”

### C. Location activity

Each publicly exposed site MAY show:

- site/room name
- public player count (`0` omitted or shown as inactive)
- active / inactive presentation (count > 0 or a recent public event in that room)

MUST NOT expose hidden Players, hidden entities, system-actor lists, or admin presence splits.

### D. Recent events

Bounded feed, **5–8** visible items, newest first.

- Concise public phrasing (existing projection narratives or the templates in §5).
- Older items visually quieter (opacity / faint color — not color-only).
- No infinite scroll by default.
- No raw event dump.
- At most **two** NORMAL movement items (`agent_move`) in the visible window. Extra movement is dropped, keeping the newest.
- NOTABLE and MAJOR may receive restrained emphasis.

### E. Event presentation tiers

| Tier | Meaning | Treatment |
|------|---------|-----------|
| `NORMAL` | Routine activity | standard or muted text; no animation beyond insert |
| `NOTABLE` | Interesting social or world activity | stronger type emphasis; eligible as headline |
| `MAJOR` | Rare meaningful world event | temporary terminal banner/pulse; no persistent flash |

Mapping is a **canonical table** from public `projection_id` (and a few world-status cases) to tier. Implementations MUST NOT invent client-side interest scores.

| Source | Tier |
|--------|------|
| `agent_move` | NORMAL |
| `harvest` | NORMAL |
| `message_notice` | NORMAL |
| `production` | NORMAL |
| `resource_change` (public scarcity flag only) | NORMAL |
| `trade` | NOTABLE |
| `organization` | NOTABLE |
| `organization_response` | NOTABLE |
| `market_shift` | NOTABLE |
| `agreement_formed` / `agreement_broken` | NOTABLE |
| `contest_declared` | NOTABLE |
| `infrastructure` band `degraded` | NOTABLE |
| `communication_disrupted` | NOTABLE |
| `conflicting_reports` (public “reports conflict” only) | NOTABLE |
| `harvest` is NOT MAJOR | — |
| `discovery` | MAJOR |
| `contest_resolved` | MAJOR |
| `infrastructure` / `infrastructure_disrupted` band `failed` | MAJOR |
| `shortage` | MAJOR |
| `world_pressure` / `frontier_pressure` (public wording only) | MAJOR |
| `crime_detected` when already PUBLIC_HISTORY | MAJOR |
| `access_changed` | MAJOR |
| `freshness=incident` world-status line | MAJOR |
| public culture / emergency / reconstruction **pulses** already allowed by their GC specs | NOTABLE unless that GC spec says empty |

Unlisted public projection ids default to NORMAL.

**Extension point:** a later pin MAY add rows to this table. It MUST NOT add a scoring subsystem in this upgrade.

MAJOR banner example (temporary, ≤ 2 poll cycles or until replaced by a newer MAJOR):

```text
──────────────────────────
   RELAY SIGNAL DETECTED
──────────────────────────
```

Copy MUST come from the public narrative/template. MUST NOT invent a “signal” that the source event does not support.

### F. Room detail

Explicit inspect of one public site without leaving WATCH.

**Chosen UX:** native `<details>` / disclosure attached to the site node. No modal stack. Esc and a visible close/summary toggle return to the graph.

Contents, public only:

```text
<SITE NAME>

Players:   public display labels in that room, or “none visible”
Visible:   public entity labels already on the live snapshot
Recent:    up to 3 recent_events whose room_id matches
```

MUST NOT become a full inspector. MUST NOT show admin/debug, inventories, amounts, private messages, or hidden entities.

Keyboard: focusable summary, Enter/Space toggle, visible focus. Mobile: full-width expansion below the graph, not a desktop-only drawer.

---

## 5. Event phrasing

Phrases are **derived presentation**, never ledger text.

Prefer existing public narratives from [SPECTATOR.md](SPECTATOR.md). When composing a short line, use only public fields:

```text
<public_label> entered <public_site>
<public_label> offered a trade
<public_label> refused a trade
<n> players gathered at <public_site>
<public_site> is degraded
```

MUST NOT assert intent (“wants”, “plots”, “is afraid”).  
MUST NOT name hidden destinations.  
`narrative` on a spectator projection remains non-authoritative ([SPECTATOR.md](SPECTATOR.md)).

---

## 6. Public data contract (`watch-live/1.0`)

Server-derived public snapshot. Prefer this envelope over sending raw `WorldEvent` records.

Hosted evidence today (`GET /v1/watch/live`): `world_id`, `cycle`, `sequence`, `freshness`, `world_status`, `players_present`, `rooms[]` (id, name, description, entities, exits), `public_pulses[]` (strings, truncated), `projection`, `note`.

| Field | Status | Notes |
|-------|--------|--------|
| `projection` | existing | `"public"` |
| `world_id` | existing | |
| `cycle` | existing | |
| `sequence` | existing | ledger sequence; not a refresh counter |
| `world_status` | existing | `ACTIVE` / `PAUSED` / `INCIDENT` / … |
| `freshness` | existing | `live` / `stale` / `maintenance` / `incident` |
| `players_present` | existing | public count of live entered Players |
| `note` | existing | spectator-is-not-truth line |
| `public_pulses` | existing | optional GC pulse strings; not the event feed |
| `rooms[].room_id` | existing | public sites only |
| `rooms[].name` | existing | |
| `rooms[].description` | existing | public description only |
| `rooms[].entities[]` | existing | public entities only (`label`, `entity_type`) |
| `rooms[].exits[]` | existing | **public exits to public rooms only** |
| `rooms[].players_present` | **new** | public count in that room; `0` allowed |
| `rooms[].active` | **derivable** | `players_present > 0` or a recent event in room |
| `rooms[].public_player_labels[]` | **new** / redaction-sensitive | public handles only; omit if none |
| `recent_events[]` | **new** | 5–8 visible; server MAY compute from last 16 |
| `recent_events[].sequence` | **new** | ordering key |
| `recent_events[].cycle` | **new** | |
| `recent_events[].tier` | **new** | `NORMAL` \| `NOTABLE` \| `MAJOR` |
| `recent_events[].projection_id` | **new** | existing spectator `projection_id` or `world_status` |
| `recent_events[].line` | **new** | short public phrase; actor names use the same public-handle rule as `rooms[].public_player_labels[]`. `smoke-*` / `op.*` / `operator.*` stay “A player” |
| `recent_events[].room_id` | optional | public room or omitted |
| `recent_events[].occurred_at` | optional | display clock; MUST NOT imply ledger time authority |
| `notable_event` | **derivable** | selected headline object or `null` |
| `source_event_ids` | optional | for audit; MUST NOT expand hidden payloads |

**Redaction-sensitive:** player labels, room membership, exits, entity lists. Server MUST apply public filters before JSON leaves the Worker.

Client MUST NOT reconstruct hidden topology by combining 404s, error strings, or missing rooms.

`public_pulses` remain allowed as atmospheric GC lines. They MUST NOT replace `recent_events`. Implementations SHOULD map a pulse into `recent_events` when a `projection_id` exists; otherwise treat as NOTABLE text with no fake actor.

Additive fields are compatible. Removing or redefining existing public room/exit leakage is a **tightening** required by this spec (hidden topology MUST NOT ship).

---

## 7. Security, privacy, epistemic boundaries

WATCH remains a **derived projection** ([SPECTATOR.md](SPECTATOR.md) hard rules, ADR-002, ADR-004).

| Rule | Requirement |
|------|-------------|
| Read-only | No command, no ledger append, no world mutation |
| Not truth | Copy MUST keep “projection / not world truth” available |
| Redaction | Public observers see public spectator rows only |
| No secret rooms | Omit unpublished / hidden rooms |
| No hidden exits | Omit hidden/blocked/unpublished exits |
| No hidden entities | Public labels already permitted on the snapshot |
| No hidden Players | No stealth, unentered, or system-actor lists |
| No Admin data | No operator session, settlement internals, Genesis inputs |
| No private cognition | No prompts, plans, or agent reasoning |
| No research metrics | No anomaly scores, detector confidence, cohorts |
| No raw payloads | No internal event `payload` objects |
| No client inference | Missing data is absence, not a hint |
| No private social memory | Coarse public descriptor bands only, and only from already-public events; else silent ([SOCIAL-MEMORY.md](SOCIAL-MEMORY.md)). Reaffirms [PARTIAL-OBSERVABILITY.md](PARTIAL-OBSERVABILITY.md) |

Agent POV and authenticated-observer modes stay defined in [SPECTATOR-ONBOARDING.md](SPECTATOR-ONBOARDING.md). This upgrade specifies the **public / anonymous** WATCH door. It MUST NOT widen Agent POV or research overlays.

XSS: public labels and descriptions are untrusted world text. Implementations MUST render via `textContent` / safe nodes. `innerHTML` of interpolated labels is a defect (current hosted `watch.ts` interpolates with an escape helper; the next runtime pass MUST keep that fail-closed and MUST NOT regress PLAY/STUDY/ADMIN).

---

## 8. Motion and refresh

Existing architecture: bounded HTTP poll of `GET /v1/watch/live`. **Polling is sufficient.** An optional `GET /v1/watch/stream` WebSocket MAY carry the same `watch-live/1.0` snapshot; it MUST NOT add fields. Clients that cannot hold a socket MUST keep polling.

| Rule | Requirement |
|------|-------------|
| Feel live | Poll every **8–12 s** while the document is visible and not paused |
| No layout jump | Reserve headline, graph, and feed heights; replace in place |
| Subtle ordinary updates | New rows MAY start brighter, then settle within one interval |
| Old events quieter | Visual fade only; no deletion flash |
| MAJOR | Temporary banner ≤ 2 intervals; no loop, no strobe |
| `prefers-reduced-motion` | Instant replace; no brightness pulse; no banner animation |
| Pause | Existing pause control remains; poll MUST stop |
| Background tabs | `document.hidden` MUST skip polls |
| Incident / stale | Show marker; continue read-only; do not invent activity |

Do not make the entire feed `aria-live`. At most the **headline** MAY be `aria-live="polite"`. Feed insertions are silent. Status tag changes (`live` / `paused` / `stale` / `incident` / `unavailable`) MAY be polite.

---

## 9. Accessibility

- Keyboard: tab order header → headline → pause/refresh → graph sites → `<details>` summaries → feed (static).
- Visible focus on all controls (existing product focus ring).
- Room detail is a real `<details>`/`<summary>` (or equivalent button+region with `aria-expanded`).
- Topology alternative: semantic list of public sites and public exits (required even if a `<pre>` exists).
- Tiers MUST NOT be color-only: prefix or marker (`>` notable, `!` major) plus type weight.
- Contrast follows the player brand token set ([VISUAL-DESIGN.md](VISUAL-DESIGN.md)): bone on graphite; `color.state.active` for emphasis, not sole meaning. Legacy copper is superseded.
- Periodic updates MUST NOT flood AT. No live region on the feed.
- Reduced motion as §8.

---

## 10. Responsive layout

**Desktop (optional two column):**

```text
header (world · cycle · seq · freshness · players)
notable event
[ world graph ] [ recent events ]
room detail expands under the graph
```

**Mobile (single column, no required horizontal scroll):**

1. world/status header  
2. current notable event  
3. compact world graph (list fallback)  
4. recent events  
5. optional room detail  

If public topology is wider than the viewport, use the stacked-site fallback. MUST NOT require pinch-zoom to read names or counts.

---

## 11. Failure and empty states

| State | Presentation |
|-------|----------------|
| Offline / HTTP fail | “Projection unavailable.” No fake rooms or events |
| No players | Headline fallback; graph still shows known public sites |
| No known sites | “No public sites exposed yet.” |
| No recent events | Empty feed line: “Nothing public yet.” |
| Stale | freshness tag `stale`; last snapshot remains |
| Incident | freshness `incident`; MAJOR headline from §4.A.2 |
| Maintenance / `PAUSED` | freshness `maintenance`; WATCH MAY continue |
| Malformed optional fields | Ignore the field; keep required metadata |
| Partial topology | Show known public nodes; omit unknown edges |
| Room with no visible entities | “no visible objects” |
| Paused updates | Tag `paused`; last snapshot frozen |

Atmospheric, clear, **no fake activity**.

---

## 12. Implementation slices

Runtime work belongs in `Zero-State-LLC/Noema`. This repository does not implement it.

### Slice 1 — projection contract

| | |
|--|--|
| Inputs | Live world + existing public filters |
| Outputs | `watch-live/1.0` fields in §6 (`recent_events`, per-room counts/labels, public-only exits) |
| Surfaces | `GET /v1/watch/live` (or equivalent) |
| Tests | Hidden rooms/exits/players absent; labels redacted; schema/shape |
| Privacy | Server-side filter only |
| Rollback | Clients ignore unknown fields; old clients keep `public_pulses` |

### Slice 2 — event presentation

| | |
|--|--|
| Inputs | Slice 1 `recent_events` + `notable_event` |
| Outputs | Headline + 5–8 line feed + tier styling |
| Surfaces | `/watch` |
| Tests | Deterministic tier table; headline hold; movement cap; XSS of `line` |
| Privacy | No raw payloads |
| Rollback | Remove feed CSS; leave snapshot |

### Slice 3 — world graph

| | |
|--|--|
| Inputs | Public rooms + exits + per-room counts |
| Outputs | Semantic graph + optional `<pre>` |
| Surfaces | `/watch` |
| Tests | No hidden edges; mobile fallback; SR list present |
| Privacy | Public graph only |
| Rollback | Revert to site cards |

### Slice 4 — room details

| | |
|--|--|
| Inputs | Selected public `room_id` + snapshot |
| Outputs | `<details>` panel |
| Surfaces | `/watch` only |
| Tests | Keyboard; no admin fields; close returns to graph |
| Privacy | Public labels only |
| Rollback | Remove `<details>`; sites remain |

### Slice 5 — polish

| | |
|--|--|
| Inputs | Slices 2–4 |
| Outputs | 8–12 s poll, pause, `document.hidden`, reduced motion, empty/error |
| Surfaces | `/watch` |
| Tests | Pause; hidden tab; reduced motion; incident/stale; PLAY/STUDY/ADMIN unchanged |
| Privacy | None new |
| Rollback | Restore prior interval |

---

## 13. Tests (normative expectations)

Runtime MUST cover:

- hidden rooms, exits, entities, Players never appear
- tier mapping deterministic for the §4.E table
- notable headline selection deterministic given the same window
- visible recent-events count in 5–8
- stale / offline / incident / zero-player / no-sites
- topology with missing connections (no invented edges)
- mobile: no required horizontal scroll for names/counts
- keyboard room inspection
- `prefers-reduced-motion`
- paused refresh (no poll)
- XSS-safe labels/descriptions/`line`
- screen-reader: feed not a live region; headline polite at most
- regression: `/play` unchanged
- regression: `/study` unchanged
- regression: Admin Live / operator surfaces unchanged
- WATCH remains non-mutating ([TESTING.md](TESTING.md))

---

## 14. Deferred (not this upgrade)

- richer spectator filtering
- story/thread grouping
- audio / semantic sound
- scoring or “interest” engines
- richer world visualization (WebGL, 3D, Admin-style topology, cinema). Optional Phosphor §18 is specified separately.
- richer push semantics beyond the same `watch-live/1.0` snapshot (optional `/v1/watch/stream` is transport only)
- authenticated-observer extra fields on the public door
- Agent POV chrome on `/watch`
- Deep Time TIMELINE drama beyond existing HISTORY/GC pulses
- cinema mode, Spectator Director, Story Engine, World Pressure Engine

---

## 15. Contradictions reconciled

| Tension | Resolution |
|---------|------------|
| Informal “WATCH v1.5” vs product `0.1`…`0.7` | Informal nickname only. Canonical label is this document’s title. No product bump. |
| [WATCH.md](WATCH.md) lists LIVE/REALMS/MAP/ECONOMY/… | Those remain the **long-term spectator surface catalog**. This upgrade specifies the **public hosted door** (`/watch`) as one LIVE window. It does not implement ECONOMY/DIPLOMACY chrome. |
| [SPECTATOR.md](SPECTATOR.md) high-drama list vs six features | Drama list is **source material for the tier table**, not extra widgets. |
| Runtime `/v1/watch/live` emits all Chamber rooms | Specs win: public-known sites and public exits only. |
| Runtime headline is a player-count sentence | Specs replace it with §4.A selection. Count stays in metadata. |
| Runtime poll 4 s | Specs set 8–12 s. |
| Runtime `public_pulses` cap 4 unstructured strings | Keep pulses; add structured `recent_events`. |
| Admin Live topology vs WATCH graph | Admin topology stays operator-only. WATCH graph is a **public, incomplete, text-first** site sketch. |
| GC6-S0 “WATCH empty” for contradiction | Unchanged. This upgrade MUST NOT add a contradiction pulse those slices forbid. |

---

## 16. NOT_COMPUTABLE

- Exact Perihelion public-vs-hidden room set after Genesis vs runtime dump: **NOT_COMPUTABLE** from Specs alone; implementation MUST apply the live world’s public-visibility flags, not this document’s Chamber-map names.
- Precise `occurred_at` wall clock vs cycle/sequence: prefer `sequence`; wall clock is display-only if the runtime has a trustworthy timestamp.
- Whether a given Player handle is public in all deployments: follow existing public-name policy; if absent, show counts only.

---

## 17. Runtime implementation prompt (next run)

Implement **WATCH — Lightweight Spectator Upgrade** in `Zero-State-LLC/Noema` against this document. Do not implement deferred features. Do not change PLAY, STUDY, or Admin Live. Do not reseed Genesis. Extend `GET /v1/watch/live` additively, filter hidden topology, derive `recent_events` and headline server-side, then update `workers/noema/src/watch.ts` through the five slices. Verify with the §13 tests and `prefers-reduced-motion`. Optional Phosphor (§18) MAY follow; it MUST NOT become a second authority.

---

## 18. Optional — NOEMA Phosphor Cartography

**Status:** Specified optional layer. Not a product-version pin.  
**Pin:** none. Uses `watch-live/1.0` only.  
**Hosted reference (non-normative):** TEXT default on `https://noema.guru/watch`; PIXEL is a spectator opt-in.

Phosphor is a **Canvas 2D sketch of the same public snapshot**. It MUST NOT replace the semantic HTML graph. It MUST NOT add fields to `watch-live/1.0`. It MUST NOT appear on PLAY, STUDY, or Admin Live.

Atmospheric stills (hero, spectator plate, legends) MAY dress the public door. They MUST NOT become a second map. The spectator key explains function (site, route, player category, signal), not hidden world facts.

### Doctrine

| Law | Requirement |
|-----|-------------|
| Symbol-before-sprite | 8×8 (preferred) or 12×12 glyphs. Larger forbidden. No portraits. |
| Topology-before-scenery | Nodes and public exits only. No decorative ground. |
| Motion-as-events only | Pulses from new `recent_events`. No ambient loop. |
| Resolution-as-knowledge | Brightness/opacity = public certainty (`partial` / `known` / `active`). |
| Brightness-as-activity | Active public rooms read brighter. Hidden rooms omitted. |
| Text-authority | Canvas never carries unique information. TEXT mode is complete. |
| No-hidden-state-leakage | Hidden rooms, exits, entities, and players never enter layout or draw. |
| One MAJOR | At most one MAJOR pulse at a time. |

Palette: `color.surface.world` ground; `color.state.active` / `color.state.warning` marks only. Legacy copper/amber hex values below are **superseded** as brand; token remap is normative. Pixel-level atlas redraw is DEFERRED ([VISUAL-DESIGN.md](VISUAL-DESIGN.md)).

### Render rules

- Canvas 2D only. No WebGL. No engines.
- Fixed low logical resolution (320×180 class). `image-rendering: pixelated` (or equivalent).
- Event-driven redraw. ≤20 FPS bursts. Zero continuous `requestAnimationFrame` when idle or `document.hidden`.
- Deterministic layout from public `rooms[]` + public exits only.
- TEXT / PIXEL toggle, keyboard-accessible. **Default is TEXT.**
- `prefers-reduced-motion` → no pulses, no interpolation, snap positions.
- Failure / no-canvas / TEXT → pure text. Semantic graph always present.

### 18.5 Glyph Atlas (assets)

**Name:** NOEMA Phosphor Glyph Atlas v0.1  
**Cell size:** 8×8 logical pixels (preferred). 12×12 permitted only if 8×8 is illegible. Larger forbidden.  
**Color model:** transparent + dim/full `color.state.active` + `color.state.warning` for caution marks. Legacy copper hex retained only until the atlas is redrawn.

```text
GROUND  color.surface.world     (#0E1114 reference; legacy #0a0e14 permitted until redraw)
DIM     color.state.active @ 45%
FULL    color.state.active      (#3DDCFF reference)
BRIGHT  color.state.warning     (#FFB020 reference)
LEGACY  #c47a3a / #e8a050       SUPERSEDED; do not use in new assets
```

**Delivery preference:**

1. Pure code (`ImageData` or direct Canvas 2D path drawing). Zero external files preferred.
2. Optional tiny base64 data-URI only if necessary. Total cartography assets remain < 200 KB. Cartography JS < 100 KB.

**Required named glyphs:**

| ID | Purpose | Visual form |
|----|---------|-------------|
| `room_empty` | Known public site, quiet | hollow square |
| `room_known` | Known public site | soft filled square |
| `room_active` | Known + public activity | bright filled square |
| `room_partial` | Partial public knowledge (rare) | three-sided open square |
| `player_single` | Exactly one public player | small diamond |
| `player_multi` | 2–9 public players | two stacked diamonds |
| `player_cluster` | ≥10 public players | 4×4 solid + brighter 2×2 core |
| `exit` | Public exit | 1 px line |
| `exit_active` | Exit used by recent public move | brighter 1 px line (transient) |
| `pulse_normal` | Transient NORMAL event | soft expand (generated at draw time) |
| `pulse_notable` | Transient NOTABLE event | stronger expand |
| `pulse_major` | Transient MAJOR event | sharp ring + short afterimage |

**Hard rules:**

- Every glyph MUST remain identifiable at logical cell size with no anti-aliasing.
- No portraits, resource icons, faction marks, or decorative flourishes.
- No pre-baked animation frames. Pulses are generated at draw time from scale + alpha.
- Certainty and activity are expressed only by glyph choice + brightness/alpha.
- **Drawing order:** exits → rooms → players → pulses.

**Epistemic mapping (mandatory):**

```text
not in public snapshot     → omit entirely
known, quiet               → room_empty / room_known, dim
known, active              → room_active, brighter
recent public event        → corresponding pulse over the room
player count > 0           → player_* glyph at the node
```

**Example public fragment** (illustrative labels only; live worlds use their own public rooms):

```text
A  active + player_multi (3)
B  room_known
C  active + player_single
D  room_empty
Exits: A–B, A–C, B–D

        [A]────[C]
         │
        [B]
         │
        [D]
```

A is brightest. C carries a single diamond. B is medium fill. D is hollow. Lines are dim copper; a recent public move on an edge lights it briefly as `exit_active`.

### Tests

- Hidden rooms / exits / players never appear in canvas layout
- Deterministic layout for an identical public snapshot
- Reduced-motion: no pulses, no rAF
- TEXT and canvas-failure leave semantic HTML fully usable
- Idle = no continuous animation frames
- Budgets respected
- WATCH remains non-mutating; PLAY / STUDY / Admin Live unchanged
