# Hosted first-entry

**Authority.** Hosted human first-entry for the reference product at `https://noema.guru`. Game-first presentation. Does not replace [PLAYER-ONBOARDING.md](PLAYER-ONBOARDING.md), [EXPERIENCE.md](EXPERIENCE.md), [HUMAN-PLAY.md](HUMAN-PLAY.md), [PLAY.md](PLAY.md), or [AUTH-AND-IDENTITY.md](AUTH-AND-IDENTITY.md).

**Kind:** presentation and navigation contract for the hosted reference projection.  
**Not** a protocol, schema, ontology, Genesis, or world-rule change. No RFC.

**World pin:** Perihelion Reach. Room names and the suggested place line are illustrative until Genesis text says otherwise.

Related: [QUICKSTART.md](QUICKSTART.md) · [COMMAND-DISCOVERY.md](COMMAND-DISCOVERY.md) · [PLAYER-ACTION-MAP.md](PLAYER-ACTION-MAP.md) · [FIRST-WORLD-OPERATIONS.md](FIRST-WORLD-OPERATIONS.md).

---

## Job

A first-time human MUST be able to:

```text
land on NOEMA
  → recognize a living world (Perihelion Reach)
  → request a Player link
  → complete the managed callback
  → see the first Chamber screen
  → perform one supported action
  → understand the observable consequence
```

The product MUST present as a **game** on this path: a living networked frontier, not a research platform with a login. Research is real and remains specified; it MUST NOT be the first-read identity of the hosted site ([PLAYER-BRAND.md](PLAYER-BRAND.md)).

This is a usability acceptance target, not a timer ([EXPERIENCE.md](EXPERIENCE.md)).

---

## Non-goals

- New auth protocols, new verbs, or new Chamber mechanics
- Genesis activate / reseed / force-supersede
- Invented quests, lore, metrics, or testimonials
- Teaching PLAY / WATCH / STUDY as the first decision
- Particle fields, generic neon HUD chrome, CRT scanlines, or maps-as-art inside PLAY
- Merging ADMIN into PLAY
- Changing claim labels, evidence rules, or WATCH redaction

---

## Path

```text
GET /
  → Player email
  → magic-link mail
  → GET /play/callback
  → GET /play (auto ENTER + LOOK)
  → AVAILABLE HERE
  → one real action
```

WATCH and CONNECT remain secondary routes. Public WATCH is the [Lightweight Spectator Upgrade](WATCH-LIGHTWEIGHT-SPECTATOR.md): read-only low-load spectator theater, not a dashboard. STUDY MUST NOT appear in primary navigation. ADMIN is a separate control-plane principal.

The browser MUST NOT ask the person to choose `human` vs `agent` as gameplay classes.

---

## Surfaces

### `/` — world door

`/` remains a **door**, not a brochure and not a dual-plane login slab.

Required first paint:

```text
NOEMA
Perihelion Reach
<one line of place>

[ email ]
Send play link
```

MUST:

- Make Player email the only primary action.
- Name the world. A single place line MAY sit under the title.
- Show “Continue to PLAY” when a Player session already exists.

MUST NOT:

- Rank Operator login as a second card beside Play.
- Show a hero thesis, path rail, core-loop diagram, Specs rail, health chip, or research question on first paint.
- Use forbidden first-read words (below).

Operator login MUST live at `/admin/login` or as a quiet footer/nav control labeled “Operator”. It MUST remain visually subordinate to Play.

Suggested place line (replaceable, not lore-canon):

> A frontier station on a worn trade line. Enter the world.

### `/play/callback`

Confirm the Player link. MUST NOT present ADMIN language. On success, go to `/play` and enter the world. On failure, `/play` with a spent-or-expired notice. No token paste on this page.

### `/play` signed out

Same Player door as `/`, without Operator. Handle field stays. Advanced controller-token paste stays collapsed. Verb: **Enter world**. CONNECT MAY appear as a quiet link, not a class choice.

### `/play` signed in — first Chamber

Text-first game workspace ([HUMAN-PLAY.md](HUMAN-PLAY.md)). Auto `ENTER_WORLD` + `LOOK` stay.

First paint MUST answer, from actual observation, in this order:

1. **Where** — room name as the title (entry location; rehearsal name Grid Anchor).
2. **Here** — room prose, then visible entities and exits.
3. **Can do** — AVAILABLE HERE actions that are actually legal. Typical first moves: LOOK, INSPECT, MOVE. No invented quest.
4. **Just happened** — enter/look consequence in plain language.
5. **Command** — input at the bottom.

Masthead: world name, cycle if it orients, handle, Leave. A health line MAY appear only when the world is `PAUSED` or `INCIDENT`.

After the first action, show success or failure and the observable change. Stable machine codes stay in advanced detail.

### `/watch` and `/connect`

Secondary. WATCH: public, redacted, read-only; one sentence of explanation at most. CONNECT: attach an external Controller; not a Player mode. Neither is a first-time fork on `/`.

### `/study`

Stays out of primary nav. Honest stub if the route exists. Not part of first-entry.

---

## Visual voice

Canonical visual system: [VISUAL-DESIGN.md](VISUAL-DESIGN.md). Do not invent a second brand.

The 2026-08-14 Chamber token set below is **superseded** as player brand. It remains a historical first-entry decision. New implementation follows semantic tokens and three type voices.

| Role | Current authority |
|---|---|
| Surfaces | `color.surface.world` / `.panel` / `.band` |
| Primary text | `color.text.primary` (bone) |
| Active / available | `color.state.active` (electric cyan) |
| Display | Syne (or role-equivalent) — world and region marks |
| Interface | IBM Plex Sans — prose, controls, help |
| Machine | IBM Plex Mono — command syntax, receipts, timestamps only |

Door and Chamber:

- **Door:** large world name (Display), short place line (Interface), one form. The door MAY keep more air than PLAY. Still not a brochure.
- **Chamber:** location title in Display, world text in Interface, command input in Machine. Semantic color on the world-state strip. Available actions use `color.state.active`.
- Motion only with semantic purpose ([VISUAL-DESIGN.md](VISUAL-DESIGN.md) §6). Honor `prefers-reduced-motion`.
- No particle canvas, no research diagram, no fake 3D, no military HUD, no scanline overlay.

**Superseded (do not reimplement):** night ledger / copper accent / Fraunces / Source Sans 3 as the player system; “more air, less card stack” as a universal PLAY rule; teal-on-copper as the accent pair.

---

## Copy inventory

### Forbidden on first-read (`/`, signed-out `/play`, callback)

```text
apparatus
ledger
conformance
capability
evidence
evidence boundary
humans & agents
stage 0
NOTICE
TEST
CAPTURE
LEARN
research
experimental
```

Admin-plane and STUDY pages MAY use research vocabulary. PLAY and the world door MUST NOT require those words to finish first-entry.

### Allowed on first-read

```text
world
Perihelion Reach
enter
look
here
leave
watch
play link
```

### Current hosted copy → required

| Surface | Current (2026-08-14) | Required |
|---|---|---|
| `/` kicker | `strategy world · stage 0` | omit, or world/place only |
| `/` subtitle | Perihelion Reach | keep |
| `/` footer | `humans & agents are both Players` | omit from first-read |
| `/` layout | Play card + Operator card | Play only; Operator subordinate |
| `/` meta/title | Home · NOEMA | MAY become Perihelion Reach · NOEMA |
| Marketing `public/index.html` | “research apparatus”, capability thesis | MUST NOT be served as `/`. If kept, it is a builder memo, not the product door |
| `/play` signed-out | Play email + handle + advanced token | keep; drop any remaining brochure lead |
| `/play` masthead | world line + cycle + leave | keep; no stage/research kicker |
| Callback | Opening PLAY… | keep; Player, not ADMIN |

Internal docs, ADMIN, CONNECT, and STUDY are not bound by the first-read ban.

---

## Spec deltas (this change)

| Doc | Change |
|---|---|
| This file | Owns hosted first-entry presentation |
| [EXPERIENCE.md](EXPERIENCE.md) | Hosted projection: world door, game-first first-read; PLAY/WATCH/STUDY remain product model, not the homepage fork |
| [PLAYER-ONBOARDING.md](PLAYER-ONBOARDING.md) | Human browser flow starts at the world door; STUDY is not a first fork |
| [QUICKSTART.md](QUICKSTART.md) | Hosted `/` described as world door + Player email |
| Runtime product-surface IA (Noema repo) | Presentation lock updates: `/` stays a door; Operator leaves the primary column; no research thesis. Auth APIs unchanged |

Unchanged owners:

| Doc | Still owns |
|---|---|
| PLAYER-ONBOARDING | Minimum authenticate → first action path |
| HUMAN-PLAY / PLAY | Chamber information priority, text-first rule |
| PLAYER-BRAND / VISUAL-DESIGN | Public identity, tokens, type, screens |
| EXPERIENCE | Product model PLAY → NOTICE → TEST → CAPTURE → LEARN (not homepage chrome) |
| AUTH-AND-IDENTITY | Principals, tokens, admin ≠ player |
| FIRST-WORLD-OPERATIONS | Perihelion pin, world lifecycle |
| ADMIN-LIVE-OPERATIONS | Operator plane |

---

## Acceptance

A first-time human can:

1. Land on `/` and recognize a world they can enter.
2. Request a play link without seeing Operator as an equal choice.
3. Arrive in Chamber, name the room from the title, and see at least one available action.
4. Perform one supported action and understand what changed.
5. Finish that path without the word “research”.

Observable checks (hosted reference):

- `GET /` primary column has exactly one email form: Player.
- `GET /` first-read text contains none of the forbidden words.
- `GET /play` signed-in first paint includes room name, at least one available action, and a command input.
- Operator consume still lands on `/admin`, not `/play`.
- WATCH remains redacted. Genesis controls remain off this path.

---

## Implementation note (non-normative)

Reference runtime today: Cloudflare Worker HTML shells (`landingHtml`, `playHtml`, `playCallbackHtml`) plus Chamber tokens. Marketing `site/` / `public/index.html` is not the product door. Implementation belongs in the runtime repo after this spec is accepted. No world-state change.
