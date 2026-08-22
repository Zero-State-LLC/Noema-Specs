# Visual Design / Brand System

**Authority.** Canonical visual design, information architecture, component taxonomy, motion, accessibility, responsive behavior, and representative screen contracts for player-facing NOEMA.

**Kind:** presentation contract.  
**Not** a protocol, schema, Genesis, or world-rule change. No RFC.

Does not replace [PLAYER-BRAND.md](PLAYER-BRAND.md), [PLAY.md](PLAY.md), [HUMAN-PLAY.md](HUMAN-PLAY.md), [HOSTED-FIRST-ENTRY.md](HOSTED-FIRST-ENTRY.md), or [WATCH-LIGHTWEIGHT-SPECTATOR.md](WATCH-LIGHTWEIGHT-SPECTATOR.md). Those remain authoritative for product model, first-entry path, and WATCH information load. This document owns **how those surfaces look and are composed**.

Related: [EXPERIENCE.md](EXPERIENCE.md) · [EXPERIENCE-TERMINOLOGY.md](EXPERIENCE-TERMINOLOGY.md) · [PLAYER-BRAND-IMPLEMENTATION.md](PLAYER-BRAND-IMPLEMENTATION.md) · [ADMIN-LIVE-OPERATIONS.md](ADMIN-LIVE-OPERATIONS.md) · [PLAYER-ONBOARDING.md](PLAYER-ONBOARDING.md).

---

## 1. Doctrine

NOEMA is a **text-first MUD**. Graphics reinforce text. They do not replace it.

The visual system targets **medium-high information density**. NOEMA is not minimalist. Complexity MUST remain structured.

A player SHOULD be able to answer, within seconds:

```text
Where am I?
What is happening?
What matters?
What can I do?
What changed because of me?
```

This extends the PLAY usability questions in [EXPERIENCE.md](EXPERIENCE.md) and [PLAY.md](PLAY.md). The interface MUST make the persistent world feel active even while the player is reading text.

### Base visual language

Use:

- dark industrial surfaces
- layered information panels
- contextual status bands
- environmental state
- local world information
- signals and events
- faction / institution identity
- economic conditions
- contextual actions
- communications traffic
- world-state indicators
- atmospheric texture
- selective motion

Do not treat decorative graphics as a substitute for gameplay information.

### Forbidden visual modes

- sterile minimalism / empty night sky with one input
- generic SaaS cards and marketing hero
- generic neon cyberpunk
- 1980s CRT nostalgia, scanline overlays, phosphor bloom as chrome
- hacker-cosplay terminal skins
- excessive military HUD (reticles, compass roses, targeting brackets)
- glitch-effect overload
- cheesy sci-fi display fonts (stencil, chrome, orbitron-class)
- decorative complexity that does not encode gameplay meaning

WATCH remains **low-load theater** relative to PLAY ([WATCH-LIGHTWEIGHT-SPECTATOR.md](WATCH-LIGHTWEIGHT-SPECTATOR.md)). That is a cognitive-load contract, not a license to make PLAY visually empty.

The 2026-08-14 first-entry visual voice (night ledger paper, copper accent, Fraunces display, “more air, less card stack”) is **superseded** as the player brand. See [PLAYER-BRAND.md](PLAYER-BRAND.md) § Supersession.

---

## 2. Color semantics

Colors mean system state. They are not decoration.

Implementations MUST bind UI to **semantic tokens**. Hex values below are the **reference palette**. They MAY be adjusted if contrast, accessibility, or display calibration requires it, provided the semantic role is preserved and the result does not drift into neon-cyberpunk or warm-SaaS cream.

### Tokens

| Token | Role | Reference |
|---|---|---|
| `color.surface.world` | Environment / page ground | graphite `#0E1114` |
| `color.surface.panel` | Layered panel | gunmetal `#161B20` |
| `color.surface.band` | Status / world-state strip | smoke `#1C232B` |
| `color.surface.inset` | Recessed well (command, logs) | `#0A0C0E` |
| `color.surface.raised` | Hover / selected panel | `#1F262E` |
| `color.text.primary` | Primary information | bone `#E8E4DC` |
| `color.text.secondary` | Supporting copy | `#A8A39A` |
| `color.text.machine` | Machine / data voice | cold steel `#9BB8C4` |
| `color.text.inverse` | Text on saturated state fills | `#0E1114` |
| `color.state.active` | System active, live signal, available action | electric cyan `#3DDCFF` |
| `color.state.warning` | Warning, strain, pending threshold | hot amber `#FFB020` |
| `color.state.critical` | Hostile, failure, danger | red-orange `#FF4D2E` |
| `color.state.unknown` | Anomalous, incomplete, unreadable | ultraviolet `#9B6DFF` |
| `color.state.economic` | Opportunity, trade, surplus | acid-lime `#C6FF3D` |
| `color.state.social` | Human / social presence | warmer sand `#C4A882` |
| `color.border.subtle` | Panel rules | `#2A333C` |
| `color.border.focus` | Keyboard focus | `color.state.active` |
| `color.overlay.scrim` | Modal / consent separation | `#0E1114` at 72% |

### Semantic use rules

- Environment / base: graphite, gunmetal, smoke.
- Primary information: bone / cold white.
- Active system: cyan, never as a full-bleed background.
- Warning: amber. Used for strain, expiry, contested, degraded play.
- Critical: red-orange. Used for hostile, `INCIDENT`, failed vital infrastructure, broken agreements that affect the player.
- Unknown: ultraviolet. Used for incomplete history, unreadable records, anomalous signals. Not a “magic” decoration.
- Economic: acid-lime, **sparingly**. Trade index up, available surplus, open desk. Not a general accent.
- Social: warmer neutrals for handles, messages, presence. Distinguishes people from machines without cartoon warmth.

Color MUST NOT be the only carrier of meaning. Pair with label, icon, or text.

Do not introduce a second accent (legacy copper) on player surfaces. WATCH Phosphor Cartography remaps former copper marks to `color.state.active` and former amber-only marks to `color.state.warning` ([WATCH-LIGHTWEIGHT-SPECTATOR.md](WATCH-LIGHTWEIGHT-SPECTATOR.md) §18). Pixel-level phosphor redraw is **DEFERRED**; the token remapping is normative.

Admin surfaces use the same tokens. They MAY use more `color.text.machine` and denser tables. They MUST NOT invent a separate rainbow.

---

## 3. Typography

Three voices. No fourth default.

### Display

**Use:** NOEMA identity, regions, districts, institutions, major events, consequential state changes.

**Direction:** engineered, slightly unfamiliar, speculative, highly legible. Wide tracking on short marks (`NOEMA`, world name). Not military stencil, not 1970s chrome, not literary serif.

**Default pin:** [Syne](https://fonts.google.com/specimen/Syne) (variable, weight 600–800 for marks; 500 for region titles). Substitutable if the substitute preserves the role.

### Interface

**Use:** gameplay, navigation, dialogue, descriptions, controls, general information.

**Direction:** modern, clean, highly readable grotesk / sans.

**Default pin:** [IBM Plex Sans](https://fonts.google.com/specimen/IBM+Plex+Sans) (400 body, 500 labels, 600 emphasis). Substitutable if the substitute preserves the role.

### Machine / Data

**Use only for:** telemetry, coordinates, hashes, timestamps, command syntax, canonical receipts, machine/system output, logs where appropriate.

**Default pin:** [IBM Plex Mono](https://fonts.google.com/specimen/IBM+Plex+Mono) (400 / 500).

Monospace MUST NOT be the universal NOEMA font. Command **input** MAY use Machine voice because it is command syntax. Room prose, dialogue, rumors, and help MUST use Interface voice.

### Scale (reference)

| Role | Voice | Size / line |
|---|---|---|
| Identity mark `NOEMA` | Display | 28–40 / 1.05 |
| World / region title | Display | 22–28 / 1.15 |
| Location title | Display or Interface 600 | 20–24 / 1.2 |
| Body / room prose | Interface | 16 / 1.45 |
| Strip / meta | Interface 500 | 13–14 / 1.3 |
| Controls | Interface 500 | 14–16 / 1.2 |
| Machine / command / receipt | Machine | 13 / 1.4 |
| Legal / consent secondary | Interface | 13 / 1.4 |

Root size 16px. Do not ship a 12px-body “hacker terminal” as PLAY.

---

## 4. Spacing and layout

### Density

Medium-high. Panels share edges. The World-State Strip is always present in PLAY. Empty vertical luxury (“more air”) is **superseded** except on the world door, which remains a door and not a brochure.

### Scale

4px base. Use 8 / 12 / 16 / 24 / 32. Avoid arbitrary 7/11/13 spacing.

### PLAY desktop hierarchy (≥960px)

```text
┌─────────────────────────────────────────────────────────────┐
│ WORLD HEADER          NOEMA // PERIHELION     handle  Leave │
├─────────────────────────────────────────────────────────────┤
│ WORLD-STATE STRIP   cycle · pressure · relay · trade · pop  │
├───────────────────────────────┬─────────────────────────────┤
│ LOCATION PANEL                │ SIGNAL FEED                 │
│ region / room title           │ recent events / rumors      │
│ environmental prose           │                             │
│ entities · routes             │ INSTITUTION / TRADE peek    │
├───────────────────────────────┤                             │
│ CONTEXT ACTION RAIL           │ PLAYER STATE                │
│ AVAILABLE HERE                │ attention compute energy …  │
├───────────────────────────────┴─────────────────────────────┤
│ COMMAND INPUT                                      COMMS ▾  │
└─────────────────────────────────────────────────────────────┘
```

This is a **required information hierarchy**, not a pixel-locked wireframe. Implementations MAY reflow columns but MUST preserve the priority in [PLAY.md](PLAY.md):

1. location
2. what matters here
3. entities
4. routes
5. contextual actions
6. relevant status
7. recent activity
8. command input

### Progressive disclosure

Default PLAY shows the current region, strip, local prose, available actions, and a short signal list.

Collapsed until asked or until relevant:

- full communications history
- archive / archaeology
- advanced receipts and canonical IDs
- complete help catalog
- STUDY
- operator surfaces

A new player MUST NOT face every panel at full depth.

---

## 5. Component taxonomy

Reuse existing ubiquitous language. Do not invent a parallel widget catalog.

| Component | Existing canon | Job |
|---|---|---|
| World Header | PLAY masthead | Identity, world name, handle, leave |
| Region Header | location title | Where am I |
| World-State Strip | status lines + world report cues | Cycle, pressure, relay, trade, population/activity |
| Location Panel | LOOK prose + entities + exits | Here, visible, routes |
| Signal Feed | recent activity / world report | What is happening |
| Rumor Card | GC5 rumor | Uncertain social information |
| Institution Card | org / World Service desk | Named institution, stance, entry action |
| Event Card | public event line | Discrete happening |
| Pressure Indicator | strip + condition | Scarcity / strain / instability |
| Trade / Economy Indicator | strip + TRADE | Opportunity or contraction |
| Player State Panel | resource line | Attention, compute, energy, influence, storage |
| Context Action Rail | `AVAILABLE HERE` | What I can do now |
| Command Input | MUD command line | Authoritative text action |
| Communications Feed | MESSAGE / BOARD / NOTICE / … | Social traffic |
| Archive Entry | INSPECT artifact / scar | Historical memory |
| Threshold Event | MAJOR / consequential change | Decision or pressure crossed |
| System Receipt | advanced detail | Machine confirmation, IDs, codes |
| Admin Telemetry Panel | Admin Live | Operator-precision instrumentation |

Rules:

- Contextual controls and commands resolve to the same canonical action ([PLAYER-ACTION-MAP.md](PLAYER-ACTION-MAP.md)).
- Do not add a Minimap component that reveals hidden geography.
- Do not add a Quest Log.
- Do not add a Capability Score widget.
- WATCH uses a subset: World Header, Signal Feed (one notable), Event Cards, optional public graph. No Action Rail, no Command Input, no Player State.

### Motif → component

| Motif | Components |
|---|---|
| Signal | Signal Feed, Rumor Card, Communications Feed, relay on the strip |
| Head | World Header world name; operators see receipts / revision on Admin |
| Threshold | Threshold Event |
| Archive | Archive Entry, Location Panel scars |
| Pressure | Pressure Indicator, World-State Strip, critical/warning bands |
| Network | Institution Card, Trade Indicator, Communications Feed, presence |

---

## 6. Motion

Motion communicates meaning. It is not atmosphere filler.

Permitted purposes:

- state transition
- incoming signal
- environmental change
- threshold crossing
- danger
- world update
- communication activity

Forbidden:

- constant glitching
- gratuitous scanlines
- excessive flashing
- decorative animation
- effects that reduce readability

Reference timings (full motion):

| Event | Motion |
|---|---|
| Panel / route change | 160ms fade or short slide, no bounce |
| Incoming signal | 200ms cyan edge on the new feed row, then settle |
| Threshold | 240ms amber band, then the new steady state |
| Critical / danger | band appears; **no** strobe; optional 1-shot 200ms pulse |
| World update (cycle) | strip values tick; no page reload flash |
| Comms activity | social-tone pip, not a bounce |

`prefers-reduced-motion: reduce` is mandatory: instant state, no pulses, no auto-playing canvas animation. WATCH Phosphor, if present, freezes on the last frame or falls back to text.

---

## 7. Accessibility

Mandatory on all player and admin surfaces:

- WCAG 2.2 AA contrast for text and essential controls
- visible keyboard focus (`color.border.focus`)
- full keyboard operation of PLAY, door, and WATCH
- state not conveyed by color alone
- semantic headings and landmarks
- name, role, value for contextual actions
- 44px minimum touch target on narrow viewports
- `prefers-reduced-motion` honored
- text remains selectable and copyable; PLAY is still a text game
- no autoplaying audio
- error text in Interface voice, exact codes in Machine voice under advanced detail

Admin tables MUST remain usable with a screen reader. Charts, if any, require a text equivalent.

---

## 8. Responsive behavior

| Viewport | Behavior |
|---|---|
| ≥960px | Two-column PLAY as in §4. Strip is one line. |
| 640–959px | Single column. Strip wraps to two lines. Signal Feed stacks under Location. Player State collapses to a compact resource row. |
| <640px | World door: mark, place line, email, one button. PLAY: Region Header, two-line strip, Location prose, Action Rail, Command Input. Signal, comms, institutions, archive behind explicit disclosures. |

Narrow screens MUST keep:

```text
location
what matters
available actions
command input
recent consequence
```

Secondary status and history MAY collapse ([HUMAN-PLAY.md](HUMAN-PLAY.md)). Horizontal pan of a fake HUD is a defect.

WATCH on narrow: notable event, cycle/player count, then recent events. Graph MAY hide behind “sites”.

---

## 9. Game-oriented communication

The visual system MUST make these conditions perceptible without opening STUDY:

| Condition | How it reads |
|---|---|
| Danger | `color.state.critical` band + Interface label (restricted, contested, failed) |
| Opportunity | sparing `color.state.economic` on trade/surplus + available action |
| Uncertainty | `color.state.unknown` + hedging copy (“records missing”, rumor card) |
| Social presence | `color.state.social` on handles / occupancy |
| Local history | Archive Entry, scars, age/condition in Location Panel |
| Scarcity | Pressure Indicator, resource values, hoarding/report lines |
| Institutional activity | Institution Card, strip, world-report lines |
| Player consequence | consequence block immediately after the action, before new chrome |
| Changing world | strip ticks, Signal Feed prepends, Threshold Event when earned |

Minimal graphical elements (condition glyphs, route ticks, org marks) remain acceptable. The **design itself** MUST NOT be visually empty.

---

## 10. Representative screens

Do not implement these screens in this specification run. Each contract is sufficient to implement without inventing brand decisions.

Shared empty / loading / error language:

| State | Treatment |
|---|---|
| Loading | Interface “Listening…” or “Entering…”. No skeleton shimmer carnival. Machine timestamp optional. |
| Empty | Direction, not mood. “No public signals this cycle.” / “No desk is open here.” |
| Error | Interface what happened + what to do. Machine code in advanced detail. `color.state.warning` or `.critical` by severity. |
| Unknown | `color.state.unknown` + “incomplete” / “unreadable”. Never fabricate. |

Shared a11y: §7. Shared type: §3. Shared color: §2.

---

### 10.1 Login / world entry

**Purpose.** Recognize a living world and watch it. Not a brochure, not a dual-plane login slab.

**Hierarchy.** Display mark `NOEMA` → world name → one place line → Watch + watch-link form → quiet Operator.

**Primary.** Perihelion Reach (or the pinned world). Watch. Player email as “Send watch link” / “Continue to WATCH” if a session exists.

**Secondary.** Manifesto, Play (agent inhabit door), and Connect (enroll) on the product bar. They MUST NOT become the door CTA. Operator control visually subordinate ([HOSTED-FIRST-ENTRY.md](HOSTED-FIRST-ENTRY.md)).

**Actions.** Open Watch. Submit watch-link email. Continue existing session. Open Manifesto, Play, or Connect from the bar. Open Operator only as subordinate.

**State indicators.** None required. If the world is `PAUSED` or `INCIDENT`, a warning/critical band may appear; do not show research health chips.

**Responsive.** Full-bleed world still with overlay chrome. More air is allowed **only here**. No card stack. Narrow: headlines and pills stack, 16px inset.

**Empty / loading / error.** Invalid email: Interface guidance. Mail sent: “Check the signal.” Spent link: return to door with warning.

**Color.** `surface.world`, `text.primary`, active on the single primary control. No lime, no ultraviolet decoration.

**Type.** Display for NOEMA and world name. Interface for place line and form. No monospace on this screen except an optional Machine timestamp in the footer.

**Terminology.** world, watch, watch link. Forbidden first-read list in [HOSTED-FIRST-ENTRY.md](HOSTED-FIRST-ENTRY.md) plus [PLAYER-BRAND.md](PLAYER-BRAND.md) § Forbidden.

**A11y.** One `h1`, labelled email field, visible focus, no auto-rotating atmosphere.

---

### 10.2 New-player onboarding

**Purpose.** Establish identity and arrive in the world as a game, not as a subject.

**Hierarchy.** World confirmed → handle field → enter → first Chamber frame (10.3) with extra emptiness in Signal Feed.

**Primary.** Handle. Enter world.

**Secondary.** Consent / data / research-participation disclosure as a **separate** sheet or route, never as the hero thesis. CONNECT is a quiet link, not a class picker.

**Actions.** Choose handle (collision visible and retryable). Enter. Dismiss or accept required disclosures.

**State indicators.** Handle available / taken.

**Responsive.** Same as the door, then PLAY mobile stack.

**Empty / loading / error.** Collision: “That name is already in the Reach.” Callback spent: warning, return to door.

**Color.** Social tone on the handle. Active on Enter.

**Type.** Display world name. Interface form. Machine only for any session id in advanced detail (hidden by default).

**Terminology.** player, handle, enter. Not subject, participant class, controller ID.

**A11y.** Disclosures are readable and dismissible by keyboard. Required legal text is not hidden in a canvas.

---

### 10.3 Main world / player screen

**Purpose.** Inhabit. Answer the five questions.

**Hierarchy.** World Header → World-State Strip → Location Panel → Action Rail → Signal Feed / Player State → Command Input.

**Primary.** Room name, local prose, what matters, `AVAILABLE HERE`, command input, last consequence.

**Secondary.** Strip metrics, short signal list, compact resources, comms disclosure.

**Actions.** Contextual actions and equivalent commands. Leave. Open comms, archive, help as disclosures.

**State indicators.** Pressure, relay integrity, trade index, cycle, resource budgets, `PAUSED`/`INCIDENT` if live.

**Responsive.** §8. Command input stays reachable without scrolling past a novel.

**Empty / loading / error.** First entry may have a quiet Signal Feed. Failed command: consequence block in Interface voice.

**Color.** Strip uses semantic tokens per value. Available actions: `state.active`. Consequence success: primary text. Failure: warning/critical.

**Type.** Display region/room. Interface prose and actions. Machine command input and any receipt.

**Terminology.** location, cycle, pressure, signal, available here. No research chrome.

**A11y.** Landmarks: banner (header+strip), main (location+actions), complementary (signals), form (command).

---

### 10.4 Location / district view

**Purpose.** Deepen “here” without becoming a map product.

**Hierarchy.** Region Header → environmental state → entities → routes → local institutions → local pressure.

**Primary.** Named district/room, prose, visible entities with human-readable roles, exits.

**Secondary.** Age/condition of infrastructure, scars, local desks.

**Actions.** INSPECT, MOVE, desk entry, other available verbs.

**State indicators.** Condition %, restricted exits (`state.warning`/`critical`), unknown gaps (`state.unknown`).

**Responsive.** Routes as a vertical list on narrow. No pinch-zoom map required.

**Empty / loading / error.** Hidden exits stay hidden. “Some records missing” is valid content.

**Color.** Restricted = warning/critical. Historic/scar = unknown or secondary, not critical unless dangerous.

**Type.** Display place name. Interface prose. Machine only for coordinates if a Player-visible coordinate exists.

**Terminology.** district, room, route, condition. Not node, graph, topology.

**A11y.** Exits as a list of named links/buttons, not an unlabeled canvas.

---

### 10.5 Signal / event feed

**Purpose.** What is happening, ranked without becoming a firehose.

**Hierarchy.** Threshold/notable first if present → recent public events → rumors.

**Primary.** Event cards from public/redacted projection and world-report lines.

**Secondary.** Age stamps, room names, “records incomplete”.

**Actions.** Open an event for location context if public. No admin inspect.

**State indicators.** NORMAL / NOTABLE / MAJOR as display rank only ([WATCH-LIGHTWEIGHT-SPECTATOR.md](WATCH-LIGHTWEIGHT-SPECTATOR.md)). MAJOR uses Threshold treatment. At most one MAJOR emphasis.

**Responsive.** Full width under location on narrow. Cap visible rows; older behind “earlier signals”.

**Empty / loading / error.** “No public signals this cycle.” Loading: “Listening…”.

**Color.** Active edge on new rows. Warning/critical only when the event is strain/danger. Unknown for rumor/incomplete.

**Type.** Interface headlines. Machine timestamps.

**Terminology.** signal, record, rumor. Not observation, telemetry dashboard, metric.

**A11y.** Live region for incoming signals; polite, not assertive spam. Reduced motion: no edge pulse.

---

### 10.6 Institution interaction

**Purpose.** Meet a named institution or World Service desk as a place in the world.

**Hierarchy.** Institution name (Display) → stance/condition → what this desk can prepare → player-confirmable actions.

**Primary.** Name, public role, available institutional actions that map to canonical verbs.

**Secondary.** Offices if public, inheritance/scar if observable, agreement state if the player is a party.

**Actions.** Only Player-confirmed canonical actions ([WORLD-SERVICES.md](WORLD-SERVICES.md)). No LLM desk authority.

**State indicators.** ACTIVE / strained / contested / restricted using semantic colors.

**Responsive.** Card becomes a full sheet on narrow.

**Empty / loading / error.** “No desk is open here.” Unauthorized: FORBIDDEN in Interface voice.

**Color.** Institutional identity via name + one mark, not a rainbow faction palette. Economic lime only for trade desks with open opportunity.

**Type.** Display institution name. Interface body. Machine for contract ids in receipts.

**Terminology.** institution, desk, office, agreement. Not org_id, capability grant.

**A11y.** Actions are buttons with names matching the verb help text.

---

### 10.7 Trade / economy interaction

**Purpose.** Execute or inspect trade and local economic condition.

**Hierarchy.** Trade Index / local condition → offer or desk → costs/reservation → confirm.

**Primary.** What is offered, what it costs, what becomes true if accepted.

**Secondary.** Preferential-trade agreement if any, spoilage/transport constraints when in scope.

**Actions.** TRADE and related available verbs. Cancel.

**State indicators.** Trade Index on the strip. Surplus/opportunity = economic. Contraction = warning. Blocked = critical or forbidden.

**Responsive.** Form stacks. Confirm stays visible.

**Empty / loading / error.** No partner: “No trade is open here.” Insufficient resources: warning + remaining decision.

**Color.** Acid-lime **only** on positive opportunity. Do not lime the whole panel.

**Type.** Interface for terms. Machine for integer costs and reservations.

**Terminology.** trade, index, cost, reservation. Not order book, metric, evaluation.

**A11y.** Numeric fields labelled. Confirmation restates the terms.

---

### 10.8 Communications / social view

**Purpose.** Read and send world-native communications.

**Hierarchy.** Channel/surface name → recent messages (retention rules apply) → compose.

**Primary.** Visible BOARD / NOTICE / SHOUT / CHANNEL / TRADE_NOTICE / MESSAGE per existing ecology ([COMMUNICATION-ECOLOGY.md](COMMUNICATION-ECOLOGY.md)).

**Secondary.** Expiry, reach (same-room vs relay), membership.

**Actions.** Send if available. Open a named player or institution if public.

**State indicators.** Relay integrity from the strip. Unreachable = warning, no topology leak.

**Responsive.** Feed + compose. Header compact.

**Empty / loading / error.** “No traffic on this board.” UNREACHABLE in Interface voice.

**Color.** Social tone for speakers. Active for new incoming. Warning for expiry/unreachable.

**Type.** Interface message bodies. Machine timestamps and handles if handle is the public name (handles may also be Interface).

**Terminology.** message, board, notice, channel, shout. Not observation stream.

**A11y.** Compose labelled. History as a log. Incoming polite live region.

---

### 10.9 Archive / history view

**Purpose.** Read persistent memory without treating lore as truth.

**Hierarchy.** Archive Entry title → what the record says → gaps → inspect actions.

**Primary.** Artifact or scar text, age, condition, missing pieces.

**Secondary.** Source hedging (“a record says…”), contradiction if specified.

**Actions.** INSPECT, ATTEST only if available and in help scope. No QUEST.

**State indicators.** Incomplete = unknown. Damaged = warning. Contradictory = unknown + Interface hedge, not a truth meter.

**Responsive.** Long text first; metadata strip above.

**Empty / loading / error.** Perihelion may have no artifacts. “No archive is open here.”

**Color.** Ultraviolet for unreadability. Do not paint history as critical unless the site is dangerous.

**Type.** Display for named artifact/place. Interface for claims. Machine for record ids in advanced detail.

**Terminology.** archive, record, scar. Not dataset, evidence bundle, claim label.

**A11y.** Hedging language is in text, not only color.

---

### 10.10 Major threshold / event state

**Purpose.** Make a consequential world change unmistakable.

**Hierarchy.** Threshold band → what changed → what is now possible or blocked → return to PLAY.

**Primary.** One sentence of world change derived from public evidence. Example shape: “The eastern relay failed.” / “The Ash Meridian agreement is broken.”

**Secondary.** Local pressure change, newly available or withdrawn actions.

**Actions.** Contextual actions that exist after the change. Dismiss/acknowledge returns to 10.3; it does not consume a world action unless a verb exists.

**State indicators.** Single MAJOR treatment. Strip updates to the new steady state.

**Responsive.** Band spans the content width. Do not full-screen cinema.

**Empty / loading / error.** If evidence does not support a threshold, do not show one. Competing MAJOR treatments are a defect.

**Color.** Warning or critical according to the event. Then settle. No loop.

**Type.** Display for the threshold mark. Interface for the sentence. Machine for cycle stamp.

**Terminology.** event, threshold language in copy (“the line is crossed”, “the relay fails”). Not evaluation, experiment, lesion.

**A11y.** Assertive live region once. Reduced motion: static band, no pulse.

---

### 10.11 Mobile / narrow viewport

**Purpose.** Same game, one column, no missing core.

**Hierarchy.** Header → two-line strip → location → actions → command → disclosures.

**Primary.** The five questions.

**Secondary.** Signals, comms, institutions, archive behind toggles labelled in Interface voice.

**Actions.** Same verbs. Larger tap targets.

**State indicators.** Strip wraps; pressure and location never drop.

**Responsive.** This *is* the <640px contract in §8.

**Empty / loading / error.** Same language as 10.3.

**Color.** Same tokens. No high-saturation full-bleed.

**Type.** Display room name may drop one step (20px) but remains Display or Interface 600. Body stays ≥16px.

**Terminology.** Unchanged.

**A11y.** Command input not covered by a fixed keyboard without a way to see the last consequence. Focus order: location, actions, command.

---

### 10.12 Admin / operator dashboard relationship

**Purpose.** Operate the world without playing it, in a sibling visual register.

**Hierarchy.** Operator mark (not the world door) → world health → canonical head / revision → event stream / digests → interventions.

**Primary.** Is the world operating. What is blocked. What intervention is legal.

**Secondary.** Telemetry, settlement receipts, cognition / emergence analysis, experiment classifications, provenance.

**Actions.** OBSERVE, INSPECT, DIAGNOSE, OPERATE, AUDIT only as specified ([ADMIN-LIVE-OPERATIONS.md](ADMIN-LIVE-OPERATIONS.md)). No PLAY verbs.

**State indicators.** Health overlay `HEALTHY` / `DEGRADED` / `PLAY_BLOCKED` / `RECOVERY_REQUIRED` using semantic colors. Schema names visible.

**Responsive.** Tables scroll. Topology exception remains Admin-only.

**Empty / loading / error.** Fail closed. SECRET never reaches the browser.

**Color.** Same token set. More machine text. No social-lime play dressing. Critical reserved for operational danger, not lore.

**Type.** Interface for operator prose. Machine for ids, hashes, catalogs, receipts. Display only for `NOEMA` / `OPERATOR` marks — not for room fantasy.

**Terminology.** operator, admin, head, revision, telemetry, digest. Player-facing words are wrong here when precision is required.

**A11y.** Same as §7. Charts need text equivalents. Redaction classes remain enforced.

**Relationship to player brand.** Same materials, same type roles, same tokens. Different information, different vocabulary, different density. A spectator who glances at Admin MUST NOT think they are in PLAY. A player who glances at PLAY MUST NOT think they are in a lab.

---

## 11. Acceptance criteria (visual)

Testable statements (see also [PLAYER-BRAND.md](PLAYER-BRAND.md)):

1. A first paint of `/` is recognizable as a science-fiction world door, not a research console or SaaS login.
2. Ordinary PLAY contains no dominant research terminology.
3. At ≥960px, PLAY shows header, strip, location, actions, and command without a blank canvas.
4. Pressure, warning, critical, unknown, economic, and social states use the named tokens and a non-color label.
5. Room prose and help are not monospace; command syntax, receipts, hashes, and timestamps are.
6. A MAJOR/threshold change is visually distinct from a normal signal row.
7. The five questions are answerable from first paint of PLAY.
8. No scanline overlay, no neon grid, no glitch loop, no military reticle, no Orbitron-class display.
9. <640px keeps location, what matters, actions, command, last consequence.
10. LOOK/INSPECT text remains the primary world representation.
11. STUDY and Admin remain reachable to authorized users and remain precise.
12. Human and agent Players share world mechanics; only projection differs.
13. An implementer can bind components to tokens and copy maps without choosing a new accent or display face.

---

## 12. Remaining ambiguities

| Item | Status | Notes |
|---|---|---|
| Semantic tokens + reference hex | RESOLVED | Hex adjustable for contrast |
| Display / Interface / Machine roles + default pins | RESOLVED | Substitutable if role preserved |
| PLAY information hierarchy | RESOLVED | Extends PLAY.md |
| Component taxonomy | RESOLVED | Mapped to existing canon |
| Twelve representative screens | RESOLVED | Contracts, not mock bitmaps |
| Motion + reduced motion | RESOLVED | |
| Accessibility floor | RESOLVED | WCAG 2.2 AA |
| Responsive breakpoints | RESOLVED | 960 / 640 |
| Player vs Admin register | RESOLVED | |
| Exact licensed display-font purchase | DEFERRED | Syne is the default open pin |
| Full icon SVG set | DEFERRED | Motifs specified; drawings not required to start layout |
| Phosphor cartography pixel redraw | DEFERRED | Token remap is normative now |
| Marketing site beyond the world door | DEFERRED | Door contract is enough |
| Per-institution mark language | DEFERRED | One mark per public institution when art exists; names work without marks |
| Audio identity | DEFERRED | No autoplay; not required for gate |

None of the DEFERRED items block `NOEMA_PLAYER_BRAND_SPEC_COMPLETE`.
