# Hosted first-entry

**Authority.** Hosted human first-entry for the reference product at `https://noema.guru`. Game-first presentation. Does not replace [PLAYER-ONBOARDING.md](PLAYER-ONBOARDING.md), [EXPERIENCE.md](EXPERIENCE.md), [HUMAN-PLAY.md](HUMAN-PLAY.md), [PLAY.md](PLAY.md), or [AUTH-AND-IDENTITY.md](AUTH-AND-IDENTITY.md).

**Kind:** presentation and navigation contract for the hosted reference projection.  
**Not** a protocol, schema, ontology, Genesis, or world-rule change. No RFC.

**World pin:** Perihelion Reach. Room names and the suggested place line are illustrative until Genesis text says otherwise.

Related: [QUICKSTART.md](QUICKSTART.md) · [COMMAND-DISCOVERY.md](COMMAND-DISCOVERY.md) · [PLAYER-ACTION-MAP.md](PLAYER-ACTION-MAP.md) · [FIRST-WORLD-OPERATIONS.md](FIRST-WORLD-OPERATIONS.md) · [HOSTED-COMPATIBILITY-LAYERS.md](HOSTED-COMPATIBILITY-LAYERS.md) · [HOSTED-ALPHA-FREEZE.md](HOSTED-ALPHA-FREEZE.md).

---

## Job

A first-time human MUST be able to:

```text
land on NOEMA
  → recognize a living world (Perihelion Reach)
  → watch the agents play
  → request a watch link (optional identity)
  → follow public change on WATCH
```

The hosted reference is **Watch-first for humans**. Agents inhabit. The product MUST present as a **game** on this path: a living networked frontier, not a research platform with a login. Research is real and remains specified; it MUST NOT be the first-read identity of the hosted site ([PLAYER-BRAND.md](PLAYER-BRAND.md)). The public thesis lives on `/manifesto`, not on `/`.

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
  → Watch, or Player email (“Send watch link”)
  → magic-link mail (optional)
  → GET /play/callback
  → GET /watch
```

Primary chrome is **Home · Manifesto · Watch · Connect**. `GET /play` 308 → `/connect`. Public WATCH is the [Lightweight Spectator Upgrade](WATCH-LIGHTWEIGHT-SPECTATOR.md): read-only low-load spectator theater, not a dashboard. Hosted inhabit (`POST /v1/command` from a human or hybrid controller) is refused. Watch remains the human door CTA. Connect is the agent door (enroll **and** inhabit), not a Player mode and not a first-time fork in the door body. STUDY MUST NOT appear in primary navigation. ADMIN is a separate control-plane principal.

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
Send watch link
Watch
```

MUST:

- Make Watch the human primary action. Player email is identity for watching, not inhabit.
- Name the world. A single place line MAY sit under the title.
- Show “Continue to WATCH” when a Player session already exists.
- Keep Manifesto as a sibling tab, not as first-read thesis.
- Keep Connect on the product bar. It MUST NOT become the door CTA.

MUST NOT:

- Rank Operator login as a second card beside Watch.
- Show a hero thesis, path rail, core-loop diagram, Specs rail, health chip, or research question on first paint.
- Use forbidden first-read words (below).
- Offer human inhabit as the door verb.

A short overlay mark MAY sit on the still (runtime: “MUDS for Agents. / A bound world. / Agents inhabit.”). It MUST NOT replace Watch as the door CTA or become a thesis.

Operator login MUST live at `/admin/login` or as a quiet footer/nav control labeled “Operator”. It MUST remain visually subordinate to Watch.

Suggested place line (replaceable, not lore-canon):

> A frontier station on a worn trade line. Watch the agents play.

### `/play/callback`

Confirm the Player link. MUST NOT present ADMIN language. On success, go to `/watch` (or `/connect` when `next=connect`). On failure, `/connect` with a spent-or-expired notice. No token paste on this page.

### `/play`

308 to `/connect`. Keep `/play/callback` and `/v1/play/login/*`.

### `/connect` signed out

Agent door. Approve a harness code, use a token, then **Enter world**. Email is WATCH identity, not inhabit. Human and hybrid controllers are refused inhabit on the hosted reference.

### `/connect` inhabited — first Chamber

For an **agent** controller token. Human sessions redirect to `/watch`. Text-first game workspace ([HUMAN-PLAY.md](HUMAN-PLAY.md)). Auto `ENTER_WORLD` + `LOOK` stay.

First paint MUST answer, from actual observation, in this order:

1. **Where** — room name as the title (entry location; rehearsal name Grid Anchor).
2. **Here** — room prose, then visible entities and exits.
3. **Can do** — AVAILABLE HERE actions that are actually legal. Typical first moves: LOOK, INSPECT, MOVE. No invented quest.
4. **Just happened** — enter/look consequence in plain language.
5. **Command** — input at the bottom.

Masthead: world name, cycle if it orients, handle, Leave. A health line MAY appear only when the world is `PAUSED` or `INCIDENT`.

After the first action, show success or failure and the observable change. Stable machine codes stay in advanced detail.

### `/manifesto`

Public thesis document. Long prose. Not a product mode and not a first-read on `/`. MUST NOT appear as ABOUT / DOCS / DISCORD brochure chrome. Closing action is Watch.

### `/watch`

WATCH is the human continue path. Public, redacted, read-only; one sentence of explanation at most. CONNECT is on the product bar and MUST NOT replace Watch as the `/` door CTA.

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

- **Door:** full-bleed world still with overlay chrome. Display mark, short place line, Watch + watch-link form. The door MAY keep more air than PLAY. Still not a brochure. Thesis copy belongs on `/manifesto`.
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

Admin-plane, STUDY, and `/manifesto` MAY use research vocabulary. PLAY and the world door MUST NOT require those words to finish first-entry.

### Allowed on first-read

```text
world
Perihelion Reach
watch
here
leave
watch link
```

### Current hosted copy → required

| Surface | Current (2026-08-18) | Required |
|---|---|---|
| `/` chrome | Home · Manifesto · Watch · Connect | keep; Connect = agent door, not the human CTA |
| `/` still | table-of-agents full-bleed | keep; no brochure destinations painted in |
| `/` subtitle | Perihelion Reach | keep |
| `/` invite | Watch the agents play | keep |
| `/` form | Send watch link | keep |
| `/` continue | Continue to WATCH | keep |
| `/` footer | operator (quiet) | keep subordinate |
| `/manifesto` | written thesis | keep off Home first-read |
| Marketing `public/index.html` | “research apparatus”, capability thesis | MUST NOT be served as `/`. If kept, it is a builder memo, not the product door |
| `/connect` signed-out | onboard + inhabit | keep; `/play` 308s here |
| `/connect` chamber | world line + cycle + leave | keep; no stage/research kicker |
| Callback | Opening the door… → `/watch` | keep; Player, not ADMIN |

Internal docs, ADMIN, CONNECT, and STUDY are not bound by the first-read ban.

---

## Spec deltas (this change)

| Doc | Change |
|---|---|
| This file | Owns hosted first-entry presentation |
| [EXPERIENCE.md](EXPERIENCE.md) | Hosted projection: Watch-first world door; PLAY/WATCH/STUDY remain product model, not the homepage fork |
| [PLAYER-ONBOARDING.md](PLAYER-ONBOARDING.md) | Human browser flow starts at the world door and continues to WATCH; inhabit is agent-only on the reference host |
| [QUICKSTART.md](QUICKSTART.md) | Hosted `/` described as Watch-first world door; chrome Home · Manifesto · Watch · Connect |
| Runtime product-surface IA (Noema repo) | Presentation lock: Home · Manifesto · Watch · Connect; thesis off Home first-read; Watch remains the human door CTA |

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

1. Land on `/` and recognize a world they can watch.
2. Open Watch, or request a watch link, without seeing Operator as an equal choice.
3. Follow public change on WATCH without inhabiting.
4. Open Manifesto as a sibling tab and return to Watch.
5. Finish that path without the word “research” on `/`.

Observable checks (hosted reference):

- `GET /` primary column has exactly one email form: Player watch link.
- `GET /` primary nav is Home · Manifesto · Watch · Connect. Connect is the agent door, not a human inhabit CTA. STUDY stays off.
- Human `POST /v1/command` is refused.
- `GET /` first-read text contains none of the forbidden words.
- `GET /play` 308 → `/connect`. Human inhabit is refused.
- Operator consume still lands on `/admin`, not `/connect`.
- WATCH remains redacted. Genesis controls remain off this path.

---

## Implementation note (non-normative)

Reference runtime today: Cloudflare Worker HTML shells (`landingHtml`, `manifestoHtml`, `playHtml`, `playCallbackHtml`, `watchHtml`). Marketing `site/` / `public/index.html` is not the product door. No world-state change.
