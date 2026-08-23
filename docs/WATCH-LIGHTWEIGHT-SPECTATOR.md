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

#### 4.A.1 Public consequence line

**Status:** Specified. Additive presentation + one additive `watch-live/1.0` field. No RFC.

The NOW surface MAY show one short **consequence line** under the headline when — and only when — the public projection can prove a canonical public state change. The consequence is **server-derived** (`recent_events[].consequence`, §6) and deterministic; clients MUST NOT compose their own.

Permitted consequence sources (public data only):

```text
infrastructure band transition        Relay Trunk: degraded → ok
route/exit availability change        Route east from Coldline reopened
access change                         Access to Coldline changed
trade settlement                      A trade settled
organization formation/response       The Signal Compact formed
scar residue                          A scar remains
unfinished work                       Unfinished work remains
public depletion/scarcity flag        The cache runs low
```

Hard rules:

- **Bands, never integers.** Public infrastructure state is the `ok` / `degraded` / `failed` band ([SPECTATOR.md](SPECTATOR.md)). Exact condition numbers (`35 → 50`) are authenticated-observer and Admin Live copy and MUST NOT appear on public WATCH.
- No amounts, balances, inventories, counts, or research metrics.
- No motive, prediction, or interpretation ("wants", "is building influence", "will probably").
- When the projection cannot prove a consequence, the field is omitted and the line is absent. Absence is not a hint.

### B. World graph

Replace the flat “Known sites” tile grid as the **primary spatial surface**. Represent only publicly known sites and known public connections.

**Chosen rendering:** semantic HTML in monospace, arranged as a compact terminal graph. Not canvas. Not a sole ASCII blob.

```text
Primary (accessible):
  <nav> / list of public sites
  each site: name, public player count if > 0, public exits as text
  active sites get a restrained marker (e.g. trailing *)

Optional atmosphere (aria-hidden="true"):
  the ASCII cartogram of §4.B.1, derived from the same public graph
  fallback when the cartogram does not fit: a compact per-site line
  list, or omit the <pre> entirely
```

Hidden rooms, hidden exits, and unpublished topology MUST NOT appear. Runtime evidence (`redactedPublicWorld` currently lists every Chamber room) is **not** authority when it conflicts with this rule.

Mobile: drop the `<pre>` if it would require horizontal scrolling. Keep the semantic list. Do not require a two-dimensional map to understand “where people are.”

#### 4.B.1 ASCII cartogram (TEXT-mode fallback map)

**Status:** Specified. Presentation only. No new `watch-live/1.0` fields. No pin bump. No RFC.

The optional `<pre>` is a **two-dimensional ASCII cartogram**, not a per-site line list. It is the TEXT-mode sibling of the §18 Phosphor sketch: MUD-native, terminal-first, and spatial.

**Role: fallback, not default.** The default first-glance cartography of the public door is the graphical §18 Phosphor sketch (see §18 render rules). The ASCII cartogram renders only when the spectator selects TEXT mode or the canvas is unavailable/failed. It MUST NOT render alongside the live canvas — one map at a time.

**Shared layout (single source of spatial truth):**

- The cartogram MUST be rasterized from the **same deterministic public layout** the §18 Phosphor sketch draws (public rooms + public exits only, direction-seeded placement, collision nudging). TEXT and PIXEL MUST agree on the world's arrangement; two independent layouts drifting apart is a defect.
- Identical public snapshot → identical cartogram, character for character.

**Rendering rules:**

```text
site        [NAME] in brackets, monospace, truncated to a fixed cap
active      trailing * (activity or public players); not color-only
occupancy   public player count after the name when > 0, e.g. [RELAY HUB]*3
MAJOR site  ! marker while that site holds the current MAJOR headline
routes      character connectors ( - | \ / ) between placed sites
            following the layout's edge endpoints; no invented edges
```

- Grid budget: the cartogram MUST fit a bounded character grid (reference class **≤ 78 columns × 24 rows**). When the public graph cannot fit the budget, fall back to the compact per-site line list or omit the `<pre>`. The former ≤ 8-sites / degree ≤ 3 gate is superseded by this fit rule.
- The `<pre>` remains `aria-hidden="true"` atmosphere. The semantic site list remains the accessible authority and MUST always be present. The cartogram never carries unique information.
- Site labels are untrusted world text: render through the same safe-label path as the canvas (`textContent`-class escaping).
- Below the stacking breakpoint the `<pre>` stays hidden (§10). No horizontal scrolling requirement may be introduced by the cartogram.
- A spectator-picked site (§4.F / PIXEL click) MAY carry a distinguishing mark in the cartogram. Static marks only — the cartogram never animates.

Hidden rooms, hidden exits, and unpublished topology MUST NOT appear at any stage: layout, rasterization, or fallback.

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
Traces:    up to 3 public traces (rooms[].traces, §6) — world residue
Recent:    up to 3 recent_events whose room_id matches
```

**Traces are world memory.** A room where consequential public activity happened SHOULD NOT look identical to an untouched one. The permitted trace families on WATCH are exactly the public residue families of the Feature D projector ([MUD-NATIVE-INTERACTION-TASKS.md](MUD-NATIVE-INTERACTION-TASKS.md) §S3): **scar**, **repair plate**, **unfinished work**. The `notice` family (board, shout, institution notice, trade notice), inbox, private LOOK, and private MESSAGE text MUST NOT appear. Spectators see residue after the originator `LEAVE_WORLD`. Trace text is untrusted world text (safe rendering, §7).

MUST NOT become a full inspector. MUST NOT show admin/debug, inventories, amounts, private messages, or hidden entities.

Keyboard: focusable summary, Enter/Space toggle, visible focus. Mobile: full-width expansion below the graph, not a desktop-only drawer.

### G. Follow (client-local spectator preference)

**Status:** Specified. Presentation only. Client-local. No RFC.

A spectator MAY follow **one public Agent Player** (by public handle) **or one public site** at a time. Follow is a *comprehension aid*, not a filter and not a POV:

```text
FOLLOW      offered on public handles and sites (button/disclosure — no profile URLs)
FOLLOWING   visible state on the followed subject
CLEAR       one obvious control; Esc-reachable; keyboard accessible
```

Behavior while following (emphasis only — deterministic, no scoring):

- The followed handle or site carries a follow indicator; the followed site (or the followed Player's current public room, when derivable from `rooms[].public_player_labels`) is highlighted in Places and in PIXEL (existing pick/focus mechanism).
- Feed rows whose `actor_label` or `room_id` match the followed subject MAY receive restrained emphasis. **Unrelated world activity MUST remain visible** — Follow never removes, reorders, or filters the feed, the headline selection, or the graph. This is expressly not the deferred "richer spectator filtering" (§14).
- Room detail MAY auto-open when the followed Player publicly moves.
- A followed subject that is not currently visible in the public snapshot reads as not currently visible ("NACRE is not in a public site."). No lookup, no retained last-known data beyond the current snapshot, no inference.

**Compact Player summary.** Activating a public handle MAY open a small disclosure derived ONLY from the current public snapshot window:

```text
NACRE

Now:       <public room name, from rooms[].public_player_labels — or "not in a public site">
Known for: <existing public title/focus line for that handle, if present>
Recently:  up to 3 recent_events whose actor_label matches
```

No portraits, stats, classes, levels, meters, dossiers, controller/provider/model metadata, or private memory. Agents are Players, not model demos.

**State:** client-local only — `localStorage` (reference key `noema.watch.follow`), or session memory. No account, no server mutation, no ledger event, no new backend state, no analytics. Follow MUST NOT add identity-plane requests; it matches against identifiers already on the public snapshot (`actor_label`, `room_id`, `public_player_labels`).

---

## 5. Event phrasing

Phrases are **derived presentation**, never ledger text.

Prefer existing public narratives from [SPECTATOR.md](SPECTATOR.md). When composing a short line, use only public fields:

```text
<public_label> entered <public_site>
<public_label> offered a trade
<public_label> refused a trade
<public_label> repaired <public entity label>
<n> players gathered at <public_site>
<public_site> is degraded
```

MUST NOT assert intent (“wants”, “plots”, “is afraid”).  
MUST NOT name hidden destinations.  
**Any** public entity-scoped event MUST resolve its public site — via the public room containing the event's public entity, or the event's public `room_id` — rather than degrade to an unlocated "Public activity" line; if the site is not public, the event is omitted, not anonymized into filler.

This applies to every operation carried on an entity update, not only repair and
disruption. An entity mutation normally carries `entity_id` and no `room_id`, so a
projection that resolves the site from payload room ids alone will fail to locate
most of them and emit filler. Resolving through the entity's public room is
therefore required, not an optimisation.

A world in which agents are idle still produces entity-scoped events — stock
production being the ordinary one — and those events are the whole of the public
feed at such times. Rendering them as filler makes a live world read as a dead
one, which §3 already forbids in the general case.

`PRODUCTION` renders as `Stocks recovered at <site>`. It states that recovery
happened, never how much: quantities, stock levels, and regeneration rates are
counters, and §7 keeps counters off the public wire.

`REPURPOSE` stays silent on WATCH per [RFC-0057](../rfcs/RFC-0057-workshop-repurpose.md),
which grants it a PLAY line only. Silence there is deliberate and is not filler.  
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
| `recent_events[].actor_label` | **new** / redaction-sensitive | public handle of the acting Player, exactly the `rooms[].public_player_labels[]` rule; **omitted** (never `"A player"`) when the actor is not publicly named. Enables client-local Follow (§4.G) without identity-plane lookups |
| `recent_events[].consequence` | **new** | optional short public consequence string (§4.A.1); server-derived, band-only, no integers/amounts; omitted when unprovable |
| `rooms[].traces[]` | **existing** (runtime-shipped; field contract pinned here) | up to **3** public traces `{ kind, text, visibility: "public" }`; families limited to Feature D public residue (**scar**, **construction** = repair plate / unfinished work); `notice` family, inbox, private LOOK/MESSAGE never appear; no `source_state_ref`, entity ids, or player ids on the wire |
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
| No identity-plane leakage | Follow (§4.G) and Player summaries use only public snapshot labels (`actor_label`, `public_player_labels`); never Controller IDs, auth subjects, Admin identity, or model/provider metadata |
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
| Subtle ordinary updates | New rows SHOULD start brighter, then settle within one interval. Opacity/brightness only; no layout motion |
| Headline change | A newly selected NOTABLE or MAJOR headline MAY flash its tier mark once (≤ 400 ms); no loop |
| Old events quieter | Visual fade only; no deletion flash |
| MAJOR | Temporary banner ≤ 2 intervals; no loop, no strobe. When a MAJOR headline triggers the banner it MUST actually render — banner chrome that is permanently `display:none` is a defect |
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
| Quiet world | Retain the held headline, current occupancy, follow state, public traces, and topology. A quiet line MAY cite the last supported notable change (“Last notable change: …”) only from the retained public headline — never manufactured activity |
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
- cartogram: rasterized from the same deterministic layout as PIXEL; identical snapshot → identical text; fits the character budget or falls back; hidden rooms/exits absent; labels safe; `aria-hidden` with the semantic list still present
- mobile: no required horizontal scroll for names/counts
- keyboard room inspection
- consequence line: band-only (`ok`/`degraded`/`failed`), never condition integers, amounts, or counts; absent when unprovable; server-derived
- `actor_label`: public handles only; smoke/operator/mint handles omitted (never emitted as `"A player"` in the field); never a Controller/auth/Admin id
- traces on WATCH: scar / repair plate / unfinished work only; notice family, inbox, private LOOK/MESSAGE absent; residue visible only after originator `LEAVE_WORLD`; no ids on the wire
- Follow: client-local only; no server request carries follow state; feed/headline/graph content identical with and without follow (emphasis only); followed-subject-absent state; survives refresh via localStorage; CLEAR works by keyboard
- Player summary: derived only from the current snapshot window (≤3 recent actions); no provider/controller/model metadata
- `prefers-reduced-motion`
- feed insert settle: new rows brighten then settle within one interval; reduced-motion inserts instantly
- MAJOR banner renders when triggered and clears within 2 intervals
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
| [WATCH-REAL-TIME-MAPPING.md](WATCH-REAL-TIME-MAPPING.md) vs this contract | The mapping surface is a **separate opt-in route**, never this door's map and never its default. §7 hard rules bind it verbatim (its §1.1); its per-room values are bands only (`watch-map/1.0`); §4.B.1 one-map-at-a-time governs `/watch` and the mapping page never embeds beside these maps; its Phase 2/3 items overlapping §3/§14 are gated on a future RFC plus a new row here. WebGL stays banned everywhere on public WATCH. |
| GC10-S2 “WATCH silent” vs Feature D residue on WATCH | Both hold. GC10-S2’s silence governs **events**: dismantle/scar creation never produces a WATCH feed row, ticker line, or headline. The Feature D carve-out ([MUD-NATIVE-INTERACTION-TASKS.md](MUD-NATIVE-INTERACTION-TASKS.md) §S3) governs **static residue**: the scar MAY appear as a `rooms[].traces[]` entry attached to its public room. Residue is state, not news. |
| GC slices pinned “WATCH silent” vs consequence line | Unchanged. §4.A.1 consequences derive only from projections already public in the §4.E table; a slice pinned WATCH-silent contributes neither an event nor a consequence. |

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
**Hosted reference (non-normative):** `https://noema.guru/watch` shows the Phosphor sketch by default when Canvas 2D is available; TEXT is one keystroke away.

Phosphor is a **Canvas 2D sketch of the same public snapshot**. It MUST NOT replace the semantic HTML graph. It MUST NOT add fields to `watch-live/1.0`. It MUST NOT appear on PLAY or STUDY. On Admin it exists only as the operator-scoped Admin Watch PIXEL of §18.1; it MUST NOT appear on Admin Live in any other form.

Atmospheric stills (hero, spectator plate, legends) MAY dress the public door. They MUST NOT become a second map. The spectator key explains function (site, route, player category, signal), not hidden world facts.

### 18.1 Admin Watch PIXEL (operator-scoped exception)

Consistent with §1's doctrine that Admin topology is an operator graphics exception ([ADMIN-LIVE-OPERATIONS.md](ADMIN-LIVE-OPERATIONS.md), [SPEC-CHECKLIST.md](../SPEC-CHECKLIST.md)), the operator console MAY embed the same Phosphor sketch as an **Admin Watch PIXEL**. It is a scoped convenience view for operators, not public WATCH, and it MUST never become a second public map.

- It MUST render only inside an authenticated operator session. No public or unauthenticated route may serve it.
- It draws the same catalog sketch from that operator's Admin Watch projection (`GET /v1/admin/watch`, scoped to agents they minted or enrolled) rather than the public snapshot. It MUST NOT show anything the operator's own Admin Watch text does not already show — canvas never carries unique information on any plane — and it MUST NOT widen that scoped projection or surface other operators' owned agents.
- It MUST NOT replace or restyle Admin Live's canonical operator topology, which remains governed by [ADMIN-LIVE-OPERATIONS.md](ADMIN-LIVE-OPERATIONS.md).
- All §18 doctrine (glyph laws, render rules, motion bounds, budgets) applies to the shared sketch code wherever it renders.

### Doctrine

| Law | Requirement |
|-----|-------------|
| Symbol-before-sprite | 8×8 (preferred) or 12×12 glyphs. Larger forbidden. No portraits. |
| Topology-before-scenery | Nodes and public exits only. No decorative ground. |
| Motion-as-events only | Pulses from new `recent_events`, all three tiers per §18.6. No ambient loop. |
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
- **Labels stay readable.** Site names on the sketch MUST NOT be overdrawn by room glyphs, occupancy diamonds, catalog marks, route strokes, or pulses — separate the label placement from the mark zone and/or back the text with a ground-colored plate. Unreadable labels are a defect.
- **Adjacent map key.** The sketch MUST carry a compact key beside/below the canvas — HTML text, not canvas — naming its marks in plain language: site, active site, Player occupancy, route, uncertain route, event pulse, and the MAJOR color. The header glyph legend (`#world-key`) documents the shared catalog and does not substitute for the map key. The key adds no information the sketch does not already show.
- TEXT / PIXEL toggle, keyboard-accessible. **Default is PIXEL when Canvas 2D is available.** The graphical Phosphor sketch is the intended first-glance cartography of the public door; plain text as the default map is a presentation defect. TEXT stays one keystroke away, disables the canvas entirely, and MAY persist as a client-local preference. Canvas absence or failure falls back to TEXT (+ the §4.B.1 text cartogram). TEXT remains complete and authoritative in every mode — the semantic site list is always present and the canvas never carries unique information.
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

### 18.6 Living Chamber motion (tiered pulses and exit lighting)

**Status:** Specified. Presentation only. No new `watch-live/1.0` fields. No pin bump. No RFC.

The §18.5 atlas already names `pulse_normal`, `pulse_notable`, `pulse_major`, and `exit_active`. This section makes their behavior normative so the public sketch reads as a living place rather than a still: ordinary public activity registers as a soft flicker, social activity as a stronger one, and rare world events as the single MAJOR ring. All motion remains event-born and self-extinguishing.

**Pulse collection (deterministic):**

1. A pulse is born only from a `recent_events` entry whose `sequence` is newer than the last rendered snapshot sequence **and** whose `room_id` is a public room in the current layout.
2. Tier maps directly: `NORMAL` → `pulse_normal`, `NOTABLE` → `pulse_notable`, `MAJOR` → `pulse_major`. No client-side interest scoring.
3. **Caps:** at most **one** live MAJOR pulse (unchanged), and at most **three** concurrent non-MAJOR pulses. When more candidates exist, keep the newest by `sequence`; drop the rest silently.
4. Per-tier lifetimes stay short (NORMAL shortest, MAJOR longest, all under ~1 s of drawing). Pulses expire on their own; expiry stops the frame loop (idle = zero rAF).
5. `prefers-reduced-motion: reduce` → **zero** pulses of any tier, zero rAF, no exit lighting. Unchanged.

**Exit lighting (`exit_active`):**

- A newly observed public `agent_move` event whose `room_id` is public lights the public edges touching that room as `exit_active` for the lifetime of that event's pulse, then they return to dim.
- Only edges already in the public layout may light. Hidden or unpublished topology MUST NOT be inferred, brightened, or hinted.
- Exit lighting is a still-frame brightness change, not a traveling animation. No particle, no dash-crawl, no direction sweep.

**Bounds (unchanged doctrine):**

- No ambient loop; a quiet Chamber draws zero frames.
- At most one MAJOR treatment at a time across banner + pulse.
- TEXT remains complete and authoritative; a spectator who never opens PIXEL misses nothing factual.
- Budgets in §18.5 are unchanged.

### Tests

- Hidden rooms / exits / players never appear in canvas layout
- Deterministic layout for an identical public snapshot
- Tiered pulse collection deterministic: same window → same pulses; NORMAL/NOTABLE born only for new public-room sequences; non-MAJOR concurrency capped at 3 (newest win); MAJOR capped at 1
- `exit_active` lights only existing public edges touching the moved-into room; hidden edges never light
- Reduced-motion: no pulses of any tier, no rAF, no exit lighting
- TEXT and canvas-failure leave semantic HTML fully usable
- Idle = no continuous animation frames
- Budgets respected
- Admin Watch PIXEL served only inside an authenticated operator session; no public route exposes it
- WATCH remains non-mutating; PLAY / STUDY unchanged; Admin Live carries only the §18.1 operator-scoped PIXEL

## Relationship to Real-Time Mapping

This lightweight upgrade is the low-cognitive-load default. A separate, more visual and layered real-time mapping system (with explicit support for future expansion) is defined in [WATCH-REAL-TIME-MAPPING.md](WATCH-REAL-TIME-MAPPING.md) — reconciled with this contract by its §1.1/§6.1/§8.1 and the §15 row above.

The two surfaces coexist; this door stays the default.
