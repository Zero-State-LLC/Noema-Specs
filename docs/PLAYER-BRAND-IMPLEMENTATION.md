# Player Brand Implementation Plan

**Authority.** Ordered implementation architecture for the player-facing brand specified in [PLAYER-BRAND.md](PLAYER-BRAND.md) and [VISUAL-DESIGN.md](VISUAL-DESIGN.md).

**Kind:** presentation implementation plan.  
**Not** a protocol, schema, Genesis, world-rule, or frontend rewrite. No RFC. **Do not implement the redesign in the same change as this document.**

**Runtime pin (closeout):** `Zero-State-LLC/Noema` `origin/main` @ `c5a9bc0` (ACCESS_POLICY S3; brand Slices 0–9 already on main). Hosted surface: `workers/noema` at `https://noema.guru`.  
**Specs pin:** this tree, including `NOEMA_PLAYER_BRAND_SPEC_COMPLETE` and `NOEMA_PLAYER_BRAND_IMPLEMENTED`.

Does not replace [HOSTED-FIRST-ENTRY.md](HOSTED-FIRST-ENTRY.md), [HUMAN-PLAY.md](HUMAN-PLAY.md), [PLAY.md](PLAY.md), [ADMIN-LIVE-OPERATIONS.md](ADMIN-LIVE-OPERATIONS.md), or [WATCH-LIGHTWEIGHT-SPECTATOR.md](WATCH-LIGHTWEIGHT-SPECTATOR.md). Those remain product contracts. This document says **how the existing Worker HTML will migrate**.

Related: [EXPERIENCE-TERMINOLOGY.md](EXPERIENCE-TERMINOLOGY.md) · [PLAYER-ONBOARDING.md](PLAYER-ONBOARDING.md) · [UI handoff (runtime)](https://github.com/Zero-State-LLC/Noema/blob/main/docs/UI-HANDOFF.md).

---

## Status

```text
SPECIFIED     NOEMA_PLAYER_BRAND_SPEC_COMPLETE
READY         NOEMA_PLAYER_BRAND_IMPLEMENTATION_READY
IMPLEMENTED   NOEMA_PLAYER_BRAND_IMPLEMENTED
VERIFIED      brand-visual-qa + brand-baseline + live /play tokens (hosted)
```

Historical: coding started at Slice 0 after this plan was accepted. Slices 0–9 are shipped on the Worker. This document remains the migration map. Do not reopen the redesign.

**Closeout (2026-08-18).** Hosted tokens are phosphor (`color.surface.world` `#0E1114`, `color.state.active` `#3DDCFF`, Syne / IBM Plex). Copper / Fraunces / Source Sans 3 are historical — do not reimplement. Product chrome is Home · Manifesto · Play · Watch · Connect (Play = agent inhabit door). The §2 divergence table describes the pre-slice Worker and is historical.

---

## 1. Specification gate (verified)

The status marker is not the proof. The required authorities exist and are implementable:

| Required | Authority | Verdict |
|---|---|---|
| Brand doctrine | [PLAYER-BRAND.md](PLAYER-BRAND.md) | specified |
| Player / research semantic separation | [PLAYER-BRAND.md](PLAYER-BRAND.md) · [EXPERIENCE-TERMINOLOGY.md](EXPERIENCE-TERMINOLOGY.md) | specified |
| Terminology mappings | [EXPERIENCE-TERMINOLOGY.md](EXPERIENCE-TERMINOLOGY.md) | specified |
| Visual language | [VISUAL-DESIGN.md](VISUAL-DESIGN.md) §1 | specified |
| Semantic color | [VISUAL-DESIGN.md](VISUAL-DESIGN.md) §2 | specified |
| Typography roles | [VISUAL-DESIGN.md](VISUAL-DESIGN.md) §3 | specified |
| Layout / IA | [VISUAL-DESIGN.md](VISUAL-DESIGN.md) §4 · [PLAY.md](PLAY.md) | specified |
| Component taxonomy | [VISUAL-DESIGN.md](VISUAL-DESIGN.md) §5 | specified |
| Motion | [VISUAL-DESIGN.md](VISUAL-DESIGN.md) §6 | specified |
| Responsive | [VISUAL-DESIGN.md](VISUAL-DESIGN.md) §8 | specified |
| Accessibility | [VISUAL-DESIGN.md](VISUAL-DESIGN.md) §7 | specified |
| Player / admin split | [PLAYER-BRAND.md](PLAYER-BRAND.md) · [ADMIN-LIVE-OPERATIONS.md](ADMIN-LIVE-OPERATIONS.md) | specified |
| Onboarding | [PLAYER-ONBOARDING.md](PLAYER-ONBOARDING.md) · [HOSTED-FIRST-ENTRY.md](HOSTED-FIRST-ENTRY.md) | specified |
| Representative screens | [VISUAL-DESIGN.md](VISUAL-DESIGN.md) §10 | specified |
| Acceptance | [PLAYER-BRAND.md](PLAYER-BRAND.md) · [VISUAL-DESIGN.md](VISUAL-DESIGN.md) §11 | specified |

DEFERRED items from the brand spec (licensed display font, icon SVG set, phosphor pixel redraw, marketing site, audio) do **not** invalidate the gate. This plan owns those as later slices or asset work.

Process note: as of this audit the brand commit lives on `feat/player-brand-doctrine` ([Noema-Specs#144](https://github.com/Zero-State-LLC/Noema-Specs/pull/144)). Implementation MUST treat these documents as authority even if merge is still in flight. Do not code against `origin/main` specs that still say “research apparatus”.

---

## 2. Runtime architecture (actual)

Runtime reality wins. The hosted product is **not** a React/Next/Tailwind SPA.

```text
BROWSER
  GET  / /play /watch /connect /study /admin
       Worker returns complete HTML (string templates)
  POST /v1/command            PLAY actions (Bearer)
  GET  /v1/watch/live         public snapshot watch-live/1.0
  POST /v1/play/login/*       Player magic link
  /v1/admin/*                 operator plane

CLOUDFLARE WORKER  workers/noema
  src/index.ts                routing
  src/shell.ts                shared product CSS + chrome
  src/landing.ts              world door
  src/play.ts                 PLAY HTML + embedded client
  src/play-ui.ts              presentation helpers (testable)
  src/play-login-html.ts      email gate markup
  src/watch.ts + watch-live.ts + watch-phosphor.ts
  src/connect.ts
  src/study.ts                honest stub
  src/admin.ts                separate CSS/chrome (duplicated tokens)
  src/world-do.ts             live world
  public/assets/*             raster stills + phosphor sheets
```

| Topic | Reality |
|---|---|
| Framework | None. TypeScript Worker, HTML string templates, inline `<script>` |
| CSS | CSS custom properties in `shell.ts` `PRODUCT_CSS`; per-page `EXTRA` strings. Root `tokens.css` / `site/design.md` are **Hallmark ledger** (copper / Fraunces) and are **not** imported by the Worker |
| Tailwind | Absent |
| Components | Functions that return HTML strings (`renderLookHtml`, `fillStatusRows`, …). No component framework |
| State | PLAY: in-page `state` object + `sessionStorage` / `localStorage`. No store library |
| API | `POST /v1/command` with `{ command, arguments: { line } }` → `{ observation, settled, … }` |
| Auth | Supabase magic link (PLAY vs ADMIN separate). Dev-token mint local only |
| Tests | Vitest on HTML strings and helpers (`play-ui.test.ts`, `product-surface.test.ts`, `play-chamber.test.ts`, `watch-phosphor.test.ts`). **No Playwright / screenshot / axe CI** |
| Deploy | `workers/noema` Wrangler + Worker `[assets]`. Cloudflare Pages is not the live host |
| Python monolith | `src/noema` / `noema-serve` is the local modular monolith, **not** noema.guru |

### PLAY composition today

```text
#play-door          email + handle + Enter world
#play-chamber       full viewport after session
  .ch-mast          NOEMA · world_name · Cycle N · handle · Leave
  .ch-scroll        WHERE + room prose + condition + #trail
  .ch-rail          HERE entities, players, desks, bonds, exits, opportunities, STATUS
  .ch-cmd           command input (Machine voice already)
```

This already answers the five questions, at low visual density, in the superseded copper/Fraunces voice.

### Divergence vs brand spec

| Spec | Runtime |
|---|---|
| Medium-high density, World-State Strip | Masthead + STATUS list; no strip |
| Syne / Plex Sans / semantic tokens | Fraunces / Source Sans 3 / copper / teal |
| Operator subordinate on `/` | **Already true** on `origin/main` (door + footer operator) |
| Forbidden first-read “stage 0 / humans & agents” | **Already removed** from shell footer/nav |
| Monospace only for machine data | Masthead, rail headings, WATCH sites, and nav remnants still mono |
| Signal Feed / rumor / comms panels | `report_lines` folded into STATUS/trail; rumor/board/shout/channel/notice lines **on observation, not rendered** |
| Admin shares tokens | `admin.ts` duplicates copper CSS |
| Glyph legend | Raster `legend.png` exists; PLAY unused; WATCH phosphor uses copper atlas |

---

## 3. Drift classification

| Finding | Class | Action |
|---|---|---|
| Copper / Fraunces / Source Sans 3 / night-ledger tokens in `shell.ts`, `admin.ts`, mail HTML, phosphor colors | `MIGRATION_REQUIRED` | Slice 1 remaps to semantic tokens |
| Hard-coded hex in phosphor + email templates | `MIGRATION_REQUIRED` | Bind to tokens; phosphor pixel redraw `DEFERRED` |
| Monospace on masthead, rail H3, WATCH site list, some nav | `MIGRATION_REQUIRED` | Interface voice; Machine only for command/ids/timestamps |
| PLAY STATUS dumps raw counts (Mail / Trades / Orgs) | `MIGRATION_REQUIRED` | Player view-model labels |
| Observation fields bound straight into HTML in `play.ts` | `MIGRATION_REQUIRED` | `toPlayerView(obs)` adapter |
| `BACKEND_GAPS = ["ACCESS_POLICY"]` | `SAFE_TO_RETAIN` | Real hosted gap; do not fake a UI |
| Existing `play-ui.ts` helpers, trail, humanizeError, command equivalence | `SAFE_TO_RETAIN` | Extend, do not replace |
| Chamber grid (mast / scroll / rail / cmd) | `SAFE_TO_RETAIN` | Become the gameplay shell |
| World door (Perihelion + email, operator footer) | `SAFE_TO_RETAIN` | Token + type pass only |
| STUDY stub | `SAFE_TO_RETAIN` | Keep out of primary nav |
| Admin separate principal + Genesis | `SAFE_TO_RETAIN` | Share tokens only |
| WATCH phosphor + `watch-live/1.0` | `SAFE_TO_RETAIN` | Token remap; no WebGL |
| Raster stills (`hero-phosphor.jpg`, `play-chamber.jpg`, topology-bg) | `SAFE_TO_RETAIN` then `DEFERRED` replace | Atmosphere only; never world truth |
| Raster glyph sheets / `legend.png` | `MIGRATION_REQUIRED` → SVG/CSS in Slice 4 | Color-only meaning forbidden |
| Grid overlay / copper glow in older shells | `MIGRATION_REQUIRED` | Remove decorative grid if still present; `origin/main` already quieter |
| `prefers-reduced-motion` in `shell.ts` | `SAFE_TO_RETAIN` | Keep; extend to phosphor (already snaps) |
| No screenshot / a11y CI | `MIGRATION_REQUIRED` | Slice 0 establishes; Slice 9 gates |
| Python `noema-serve` HTML (if any) | `DEFERRED` | Hosted Worker is the product |
| `site/` marketing Pages | `DEFERRED` | Not noema.guru |
| Inventing Pressure / Trade Index / Population scalars | `BLOCKING` if coded | Must stay `NOT_COMPUTABLE` until a derived contract exists |
| Changing `/v1/command`, settlement, Genesis, auth | `BLOCKING` | Out of scope |

Nothing in the current Worker **blocks** starting Slice 0–1. Inventing missing world indices **would** block readiness.

---

## 4. Presentation architecture

Do not introduce a new UI framework.

```text
DOMAIN DATA          Observation, watch-live/1.0, admin JSON
        ↓
PRESENTATION ADAPTER toPlayerView / toWatchView / toOperatorView
        ↓
PLAYER SEMANTICS     terms.ts  (register: player | operator | research)
        ↓
DESIGN TOKENS        theme/tokens.ts → CSS variables
        ↓
COMPONENTS           play-ui render/fill functions
        ↓
SCREEN COMPOSITION   play.ts / landing.ts / watch.ts / admin.ts
```

Forbidden:

```text
obs.report_lines[i]  →  innerHTML
emergent_capability_metric  →  PLAY label
```

### 4.1 Semantic presentation layer

**Choice:** one typed view-model + a closed dictionary. Not a CMS, not scattered aliases.

New files (runtime):

```text
workers/noema/src/presentation/terms.ts
workers/noema/src/presentation/player-view.ts
workers/noema/src/theme/tokens.ts
```

`terms.ts` is the executable subset of [EXPERIENCE-TERMINOLOGY.md](EXPERIENCE-TERMINOLOGY.md):

```ts
type Register = "player" | "operator" | "research" | "schema";
function label(concept: ConceptId, register: Register): string
```

`toPlayerView(obs: Observation): PlayerWorldView` is the only PLAY binding. It may **omit** fields that are `NOT_COMPUTABLE`. It MUST NOT invent pressure, population, or trade-index numbers.

Admin continues to read schema names. STUDY, when opened, uses the research register.

### 4.2 Design tokens

Implement [VISUAL-DESIGN.md](VISUAL-DESIGN.md) §2–4 as CSS variables in `theme/tokens.ts`, inlined by `shell.ts` and `admin.ts`.

```text
--color-surface-world
--color-surface-panel
--color-surface-band
--color-surface-inset
--color-surface-raised
--color-text-primary
--color-text-secondary
--color-text-machine
--color-state-active
--color-state-warning
--color-state-critical
--color-state-unknown
--color-state-economic
--color-state-social
--color-border-subtle
--color-border-focus

--font-display    /* Syne, role-substitutable */
--font-interface  /* IBM Plex Sans */
--font-machine    /* IBM Plex Mono */

--space-1 … --space-8     /* 4px base */
--radius-panel            /* 2px — keep the existing geometry */
--shadow-panel            /* restrained; not SaaS elevation stack */
```

Effects: no decorative glow, no scanlines, no noise overlay as chrome. Optional 1-shot pulse on incoming signal / threshold, gated by `prefers-reduced-motion`.

Delete `--copper` from player CSS after the remap. Admin MAY keep a `--operator-accent` alias of `--color-state-warning` if it improves scanability; it MUST NOT reintroduce copper as a second brand.

### 4.3 Component architecture

Do not rename working functions to React-like files. Map taxonomy → existing helpers:

| Target role | Existing | Action |
|---|---|---|
| World Header | `.ch-mast` / `.top` | `MODIFY` |
| Region Header | `#room-name` + `renderLookHtml` | `MODIFY` |
| World-State Strip | absent (STATUS rows + cycle) | `NEW` derive from `PlayerWorldView.strip` |
| Location Panel | `#loc-card` | `MODIFY` |
| Signal Feed | `#trail` world items + `report_lines` | `MODIFY` extract |
| Signal Item / Event Card | trail `kind=world` | `MODIFY` |
| Rumor Card | `rumor_lines` unrendered | `NEW` (data exists) |
| Institution Card | `renderServiceDesksHtml` + orgs in bonds | `MODIFY` |
| Pressure Indicator | `NOT_COMPUTABLE` as scalar | **omit** or show derived infra condition **as text**, never “SEVERE” unless specified |
| Economy Indicator | open trades + `trade_notice_lines` | `NEW` from existing fields; no index % |
| Player State Panel | STATUS budgets | `MODIFY` include influence |
| Action Rail | `#opp-list` + affordances | `MODIFY` bind `affordances` not only derived opportunities |
| Command Input | `#cmd-form` | `KEEP` (already Machine) |
| Communications Feed | bonds messages + unused board/shout/channel | `MODIFY` / `NEW` |
| Archive Entry | `discovery_lines` / reconstruction | `MODIFY` |
| Threshold Event | WATCH MAJOR; PLAY none | `NEW` from contest resolve / report / PAUSED |
| System Receipt | `#advanced` mono ids | `KEEP` |
| Admin Telemetry | `admin.ts` | `MODIFY` tokens only |
| Legend / Key | `legend.png` unused in PLAY | `NEW` SVG/CSS Slice 4 |

For each reusable unit, keep the existing data contract (`LocationObs`, `Observation`, …). Add `PlayerWorldView` fields rather than changing Observation schema.

---

## 5. Main gameplay shell

Priority target: PLAY chamber. Five questions map to **existing** data:

| Question | Runtime source | Gap |
|---|---|---|
| Where am I? | `location.name`, `location.description`, `world_name` | none |
| What is happening? | `report_lines`, `contests`, `consequence`, trail | rumor/comms unrendered |
| What matters? | `location.condition`, entity condition, contests, culture_lines | no Pressure enum |
| What can I do? | `affordances`, `available_actions`, opportunities | rail does not list structured affordances fully |
| What changed? | `consequence`, `#trail` | threshold treatment missing |

### World-State Strip — honest contents

Show only what exists:

```text
NOEMA // {world_name}
{location.name} · Cycle {cycle}
Relay: {best public relay condition}%     if an INFRASTRUCTURE relay is visible or in report_lines
Local: {location.condition}               already derived
Presence: {players_here.length} here      room-local only
```

Do **not** show:

| Spec example | Status | Why |
|---|---|---|
| Population 417 | `NOT_COMPUTABLE` | No world population. WATCH has `players_present` (live Players only). |
| Pressure: SEVERE | `NOT_COMPUTABLE` | No pressure band on Observation. WED/GC10 mutate entity condition / access. |
| Trade Index: −12% | `NOT_COMPUTABLE` | No index. Open trades + trade notices only. |
| Relay Integrity: 83% | **Derived** | Use visible/public infra `condition` or `"{label} condition {n}."` report line. Frontend derivation only. |

If product later wants Pressure / Trade Index / Population as first-class strip fields, that is a **GAMEPLAY_SPEC_GAP** — specify a derived projection, then implement. Do not invent them in JSX/HTML.

---

## 6. Data dependency matrix

| UI field | Source | Available? | Derived? | API change? | Domain change? | Notes |
|---|---|---|---|---|---|---|
| World name | `obs.world_name` | yes | no | no | no | Perihelion Reach |
| Cycle | `obs.cycle` | yes | no | no | no | |
| Sequence | `obs.sequence` | yes | no | no | no | Advanced only |
| Location name/prose | `obs.location` | yes | no | no | no | |
| Local condition | `location.condition` + `deriveLocalCondition` | yes | yes | no | no | Presentation only |
| Entities / exits | location | yes | no | no | no | |
| Player budgets | `obs.budgets` | yes | no | no | no | Influence not shown today |
| Available actions | `affordances` / `available_actions` | yes | no | no | no | Underused in HTML |
| Consequence | `obs.consequence` | yes | no | no | no | |
| World report | `obs.report_lines` | yes | yes (server) | no | no | WR-S0–S6; last-1 every 5 cycles |
| Practice / ties / culture / discovery | `*_lines` | yes | yes | no | no | Partially in STATUS |
| Rumors | `rumor_lines` | **yes, unrendered** | no | no | no | Slice 3 |
| Board / shout / notice / channel / trade notice | `*_lines` | **yes, unrendered** | no | no | no | Slice 3 |
| Offices | `office_lines` / org.offices | partial | no | no | no | Bonds only |
| Reconstructions | `reconstruction_lines` | **yes, unrendered** | no | no | no | Archive |
| Unclaimed works | `unclaimed_lines` | **yes, unrendered** | no | no | no | |
| Contests | `obs.contests` | yes | no | no | no | Not a dedicated card |
| Services / desks | `obs.services` | yes | no | no | no | |
| Players here | `obs.players_here` | yes | no | no | no | Room only |
| World player count | WATCH `players_present` | PLAY **no** | — | optional | no | Do not fake 417 |
| Mail / trades / orgs | obs arrays | yes | no | no | no | |
| Relay integrity | entity.condition / report | derived | **frontend** | no | no | Only if public relay known |
| Pressure band | — | **no** | — | no | **GAMEPLAY_SPEC_GAP** if required | |
| Trade index | — | **no** | — | no | **GAMEPLAY_SPEC_GAP** if required | |
| Population | — | **no** | — | no | **GAMEPLAY_SPEC_GAP** if required | |
| Canonical head | admin / settle | admin only | no | no | no | Never PLAY |
| Cognition metrics | research | no on PLAY | no | no | no | Correct |

---

## 7. Admin / operator isolation

```text
COMMON  theme/tokens.ts + focus/skip/reduced-motion + primitive buttons/fields
├── PLAYER   landing / play / watch / connect   world-native terms
└── OPERATOR admin.ts + admin APIs              schema terms, head, health, Genesis
```

Shared: tokens, type roles, radius, focus ring, skip link.  
Different: density, IDs, telemetry, lifecycle controls, digest tables.

Do not diegeticize Admin. `OPERATOR` mark, not `NOEMA // PERIHELION` fantasy.

---

## 8. Responsive architecture

Keep the existing 900px / 540–760px breakpoints; align names to the spec’s 960 / 640 **behavior**, not a pixel fight.

| Viewport | PLAY |
|---|---|
| ≥900px | mast + two-column (location \| rail) + sticky command |
| <900px | single column; exits line in location; rail below; command sticky |
| <640px | strip wraps 2 lines; Signal / comms / archive behind disclosures; 44px targets |

Command input stays sticky and ≥16px to avoid iOS zoom. Do not hide it behind the keyboard without a visible last consequence.

---

## 9. Accessibility (implementation requirements)

Carry [VISUAL-DESIGN.md](VISUAL-DESIGN.md) §7 into tests:

- Keyboard: door form, chamber actions, command, leave, WATCH pause/refresh
- `:focus-visible` uses `--color-border-focus`
- Landmarks already present (`header`, `main`, `aside`, command `footer`); keep them
- Live regions: `#trail` is `aria-live="polite"`; threshold uses **one** assertive update
- State not color-only (label + token)
- Contrast AA on bone/graphite; verify cyan/lime on graphite
- `prefers-reduced-motion` already global; phosphor already snaps
- Errors: `humanizeError` primary in Interface voice; code in `#err-advanced`
- Legend: `aria-label` on every glyph; text fallback

Slice 0 records a manual a11y checklist. Slice 9 is the gate.

---

## 10. Performance budget

Hosted PLAY is already a single HTML document + Google fonts. Keep it that way.

| Budget | Limit | Notes |
|---|---|---|
| PLAY HTML+inline JS+CSS | 180 KB gzip | reject React/SPA |
| WATCH phosphor JS | 100 KB (already `PHOSPHOR_JS_BUDGET`) | keep |
| Phosphor assets | 200 KB (already) | keep |
| Fonts | 3 families, 2–3 weights each | Syne + Plex Sans + Plex Mono |
| Still images on door | 1 image ≤ 250 KB | existing hero-phosphor |
| Trail / signal list | cap 18 (already) | do not unbounded-render report history |
| PLAY rerender | per command only | no 8s PLAY poll |
| WATCH poll | keep 8–12s | no rAF when idle |
| Animation | ≤200–240ms, 0 continuous loops | spec motion |

No new WebGL. No particle fields. CSS/SVG first.

---

## 11. Graphical layer

Text remains primary. Allowed later (Slice 4 / 7):

- compact SVG glyphs (legend)
- 1px state band on strip
- optional still on the **door only** (already)
- phosphor on WATCH only

Forbidden: sprite sheets as PLAY content, 3D, cinematic full-screen threshold, decorative canvas on PLAY.

---

## 12. Glyph and legend system

Start with **14** marks. Do not use the 20+ raster player sheet as PLAY vocabulary.

| name | meaning | form (direction) | category | accessible label | color | fallback | usage |
|---|---|---|---|---|---|---|---|
| `loc` | here | notched square | LOCATION | Location | text.primary | “here” | Region header |
| `player` | a Player | small upright mark | PLAYER | Player | state.social | handle initial | presence |
| `org` | institution | bracketed bar | INSTITUTION | Institution | text.primary | name | desk/org |
| `trade` | trade/opportunity | two chevrons | TRADE | Trade | state.economic | “trade” | trades, notices |
| `danger` | hostile/contest | sharp wedge | DANGER | Danger | state.critical | “danger” | contest, crime report |
| `distress` | strain/failing infra | cracked bar | DISTRESS | Distress | state.warning | “strained” | low condition |
| `rumor` | uncertain claim | open diamond | RUMOR | Rumor | state.unknown | “rumor” | rumor_lines |
| `unknown` | incomplete | hollow mark | UNKNOWN | Unknown | state.unknown | “?” | missing records |
| `comms` | message/board | tick + bar | COMMUNICATION | Signal | state.active | “message” | comms |
| `infra` | infrastructure | block | INFRASTRUCTURE | Works | text.machine | type word | entities |
| `resource` | harvest/stock | small tally | RESOURCE | Resource | text.secondary | resource name | harvestable |
| `threshold` | consequential change | long bar | THRESHOLD | Threshold | state.warning | “change” | MAJOR / strip |
| `economy` | economic change | lime tick | ECONOMIC CHANGE | Economy | state.economic | “trade” | surplus/contraction |
| `event` | world event | short dash | WORLD EVENT | Event | state.active | report line | Signal Feed |

Rules: meaning never color-alone; 16×16 SVG viewBox; CSS currentColor; desktop legend in a `details` “Key”; mobile same disclosure; keyboard + tooltip `title` + `aria-label`.

Existing `legend.png` / glyph PNGs: `DEFERRED` retirement after SVG lands. Phosphor atlas stays WATCH-only until its token remap.

---

## 13. Onboarding map

Current runtime already matches the operational path:

```text
/  door + email
/play/callback
/play  handle + Enter world → auto ENTER + LOOK
chamber  AVAILABLE HERE / opportunities + command
```

Keep it. Fantasy sequence is presentation, not a new wizard.

| Step | Runtime | Change |
|---|---|---|
| ENTER | door + magic link | tokens/type only |
| ORIENT | LOOK card | strip + location hierarchy |
| ACT | command / chips | Action Rail from affordances |
| OBSERVE | trail + notice | consequence block stays first |
| SIGNAL | report_lines in STATUS | move to Signal Feed |
| INTERACT | desks / players / trade | Institution / comms Slice 3 |
| EXPAND | help, unrendered lines | progressive disclosure |

Do not add a lore dump. Do not lead with STUDY. Consent/legal stays a separate sheet if required.

---

## 14. File migration map

Paths relative to `workers/noema/`.

| File | Action | Why |
|---|---|---|
| `src/shell.ts` | `MODIFY` | Token + type remap; keep chrome structure |
| `src/landing.ts` | `MODIFY` | Door already correct; drop decorative still if it fights density, keep place line |
| `src/play.ts` | `MODIFY` | Compose `PlayerWorldView`; add strip; do not rewrite command path |
| `src/play-ui.ts` | `MODIFY` | Keep helpers; consume view-model |
| `src/play-login-html.ts` | `MODIFY` | Copy/tokens only |
| `src/watch.ts` | `MODIFY` | Type + tokens; keep watch-live binding |
| `src/watch-live.ts` | `KEEP` | Projection contract |
| `src/watch-phosphor.ts` | `MODIFY` | Color constants → tokens; pixel redraw `DEFERRED` |
| `src/connect.ts` | `MODIFY` | Tokens; CONNECT is not a class picker |
| `src/study.ts` | `KEEP` | Stub |
| `src/admin.ts` | `MODIFY` | Import shared tokens; keep operator vocabulary |
| `src/admin-mail.ts` / `play-mail.ts` | `MODIFY` | Token hex in email |
| `src/theme/tokens.ts` | `NEW` | Semantic tokens |
| `src/presentation/terms.ts` | `NEW` | Dual-register labels |
| `src/presentation/player-view.ts` | `NEW` | `toPlayerView` |
| `src/presentation/glyphs.ts` | `NEW` | Slice 4 |
| `src/index.ts` | `KEEP` | Routes stay |
| `src/world-actions.ts` / `world-do.ts` / settle / auth | `KEEP` | No mechanics change |
| `src/types.ts` Observation | `KEEP` | Do not pretty-print schema |
| `public/assets/*` | `KEEP` then selective `DELETE` | Stills ok; PNG glyphs after SVG |
| `public/index.html` / `memo.html` | `KEEP` | Not product door |
| `site/` | `DEFERRED` | Marketing |
| `tokens.css` (repo root) | `MODIFY` or leave | Do not let Hallmark copper remain implied authority |
| `docs/UI-HANDOFF.md` | `MODIFY` | Point at brand + this plan |
| Tests listed in §16 | `MODIFY` / `NEW` | |

---

## 15. Implementation slices

Each slice was one PR-sized runtime change. **All slices below are SHIPPED** on `Zero-State-LLC/Noema` (PRs #221–#230). Specs remain the contract; do not re-run the campaign.

### Slice 0 — Baseline capture

- **Scope:** Record current UI, routes, tests, performance. Add screenshot/a11y harness stubs. No visual change.
- **Deps:** none
- **Files:** `docs/UI-HANDOFF.md` (runtime), new `workers/noema/test/brand-baseline.test.ts` (HTML contracts that must not regress: `/v1/command`, door email, no STUDY in nav, admin ≠ play)
- **Acceptance:** vitest green; route inventory written; optional manual screenshots attached to the PR
- **Tests:** existing `product-surface`, `play-ui`, `play-chamber`, `first-entry`
- **Rollback:** delete harness only

### Slice 1 — Foundation

- **Scope:** `theme/tokens.ts`, font pins, `terms.ts`, `toPlayerView` used by STATUS/look only. Remap CSS variables. No layout rewrite.
- **Deps:** Slice 0
- **Files:** `theme/tokens.ts` `NEW`; `presentation/*` `NEW`; `shell.ts` `admin.ts` `play.ts` `play-ui.ts` `MODIFY`
- **Acceptance:** no `--copper` on player surfaces; room prose not mono; command still mono; `toPlayerView` unit tests; command/auth still pass
- **Tests:** new `presentation/player-view.test.ts`; update `product-surface` forbidden-word list
- **Rollback:** revert token PR; helpers stay compatible

### Slice 2 — Gameplay shell

- **Scope:** World Header, Location, World-State Strip (honest fields), Signal Feed from `report_lines` + trail world items, Action Rail from `affordances`, keep command
- **Deps:** Slice 1
- **Files:** `play.ts` `play-ui.ts`
- **Acceptance:** five questions answerable; no invented Pressure/Population/Trade Index; influence visible
- **Tests:** `play-ui` strip contents; first-entry still LOOK + action
- **Rollback:** feature-flag or revert play composition; command path untouched

### Slice 3 — Gameplay systems

- **Scope:** Render existing unused lines: rumors, board/shout/notice/channel/trade notice, desks, contests, archive/reconstruction, unclaimed. Progressive disclosure.
- **Deps:** Slice 2
- **Files:** `play.ts` `play-ui.ts` only (no Observation schema change)
- **Acceptance:** rumor uses unknown token + hedge; comms retention rules unchanged
- **Tests:** render tests with fixture observations
- **Rollback:** hide panels

### Slice 4 — Glyph + legend

- **Scope:** 14 SVG glyphs + Key disclosure. Wire to Signal / entity / presence. No color-only meaning.
- **Deps:** Slice 2
- **Files:** `presentation/glyphs.ts` `NEW`; PLAY/WATCH `MODIFY`
- **Acceptance:** legend keyboard-accessible; text fallback; PNG sheets unused by PLAY
- **Tests:** glyph accessible-name tests
- **Rollback:** hide Key

### Slice 5 — Onboarding

- **Scope:** Door/type polish; first consequence emphasis; no research lecture; handle default empty (not `player1`) if tests allow
- **Deps:** Slice 1
- **Files:** `landing.ts` `play.ts` `play-login-html.ts` email templates
- **Acceptance:** [HOSTED-FIRST-ENTRY.md](HOSTED-FIRST-ENTRY.md) still holds; forbidden words stay gone
- **Tests:** `product-surface` `play-email-login` `first-entry`
- **Rollback:** copy revert

### Slice 6 — Responsive / mobile

- **Scope:** <640 disclosures; 44px targets; sticky command; strip wrap
- **Deps:** Slice 2
- **Files:** `play.ts` `shell.ts` CSS
- **Acceptance:** five questions without horizontal HUD pan
- **Tests:** HTML class/media contracts; manual matrix in Slice 9
- **Rollback:** CSS revert

### Slice 7 — Motion / atmosphere

- **Scope:** Semantic 160–240ms transitions; signal edge; threshold band; reduced-motion
- **Deps:** Slice 2
- **Files:** `shell.ts` `play.ts` CSS
- **Acceptance:** no loop, no glitch, no scanline
- **Tests:** reduced-motion CSS present
- **Rollback:** CSS revert

### Slice 8 — Admin relationship

- **Scope:** Admin imports shared tokens; remains operator-precise; no PLAY fantasy
- **Deps:** Slice 1
- **Files:** `admin.ts` mail
- **Acceptance:** health, head, Genesis still visible; SECRET still absent
- **Tests:** `admin-email-login` `ops`
- **Rollback:** isolated

### Slice 9 — Visual QA

- **Scope:** Viewport screenshots, contrast, keyboard, performance, spec acceptance checklist
- **Deps:** Slices 1–8 as landed
- **Files:** test docs / optional CI screenshot job
- **Acceptance:** [PLAYER-BRAND.md](PLAYER-BRAND.md) 14 statements testable
- **Rollback:** n/a (verification)

Do not combine Slice 1 layout work with Slice 2. Do not open settlement or command-semantics PRs in this campaign.

---

## 16. Test strategy

| Layer | How |
|---|---|
| Functional | Existing vitest: `/v1/command`, first-entry ENTER/LOOK/MOVE, auth, admin ≠ play, WATCH redaction |
| Visual | Slice 0 manual shots; Slice 9 matrix: 360 / 390 / 768 / 1280 / 1440, empty/loading/error, PAUSED, MAJOR |
| A11y | Keyboard scripts; contrast check; live-region audit; reduced-motion |
| Responsive | Slice 6 + 9 |
| Performance | gzip size of `playHtml()` / `watchHtml()`; phosphor budgets already asserted |
| Regression | **No** changes to `world-actions`, settle, fence, Genesis, diplomacy reducers in brand slices |

If a slice seems to need a world-report or Observation field change, stop. That is a **GAMEPLAY_SPEC_GAP**, not a CSS fix.

---

## 17. Asset-production plan

Do not generate assets in the first implementation slices. Specify, then produce in Slice 4+ or a dedicated art pass.

| asset_id | purpose | dim | format | variants | meaning | usage | a11y fallback | ceiling |
|---|---|---|---|---|---|---|---|---|
| `wordmark.noema` | identity | SVG | SVG | 1 | NOEMA | header/door | text “NOEMA” | 8 KB |
| `glyph.*` (14) | legend | 16 viewBox | SVG | currentColor | §12 | PLAY/WATCH | label | 1 KB each |
| `legend.key` | Key panel | CSS+SVG | — | 1 | all 14 | details | definition list | 8 KB |
| `texture.world` | optional ground | CSS only | — | — | atmosphere | surface.world | none | 0 raster |
| `still.door` | door still | ≤1600×900 | jpg | 1 | atmosphere | `/` only | empty alt | 250 KB |
| `phosphor.atlas` | WATCH PIXEL | 8×8 cells | canvas | copper→token | WATCH | WATCH | TEXT mode | existing |

Prefer SVG/CSS. Raster only for photographic stills. Do not put `study-traces.jpg` on PLAY.

---

## 18. GAMEPLAY_SPEC_GAP (do not solve in frontend)

```text
GAMEPLAY_SPEC_GAP  first-class Pressure band on PLAY observation
GAMEPLAY_SPEC_GAP  world Population / activity index
GAMEPLAY_SPEC_GAP  Trade Index scalar
GAMEPLAY_SPEC_GAP  ACCESS_POLICY verb (already hosted TIER3 gap)
```

Frontend may show **raw existing lines** (`relay-7 condition 83.`, `{form} is contested.`, `{type} is agreed.`). It may not mint SEVERE / −12% / 417.

---

## 19. Risks

| Risk | Mitigation |
|---|---|
| Settlement / command regression | Brand slices touch HTML/CSS/presentation only |
| Coupling Observation → HTML | `toPlayerView` in Slice 1 before layout |
| Terminology leakage | `terms.ts` + forbidden-word tests |
| A11y loss from sci-fi chrome | tokens + non-color labels + Slice 9 |
| Mobile command unusable | sticky input, 16px+, Slice 6 |
| Performance (fonts + stills) | 3 families; one door still; no SPA |
| Data gaps dressed as brand | `NOT_COMPUTABLE` in view-model |
| Unmerged brand specs | Land Specs #144 before Slice 1 pixels |
| Phosphor copper leftover | token remap; pixel art `DEFERRED` |

---

## 20. Readiness

```text
NOEMA_PLAYER_BRAND_IMPLEMENTATION_READY
NOEMA_PLAYER_BRAND_IMPLEMENTED
```

Campaign closed. Hosted PLAY/WATCH/Admin on `noema.guru` serve the Slice 0–9 contracts. Phosphor pixel-art copper remap remains **DEFERRED** (not a brand-campaign reopen).

### Next executable slice

```text
none — player brand
```

Gameplay continues from ACCESS_POLICY S3 (RFC-0104). WED / ATTEST help stay parked. Do not invent ACCESS_POLICY S4.
