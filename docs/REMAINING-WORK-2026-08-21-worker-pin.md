# Remaining work — 2026-08-21 evening

**Status:** Honest snapshot after Noema `#487` on `main` (official client pin) and Specs RFC-0120 restore `#237`.  
**Does not:** reseed frozen first world, `force:true` on production, same-id activate of `world.perihelion-reach-2`, reverse RFC-0120, treat Admin as a Player, or pin a Worker SHA that is not live.

**Live.** `GET https://noema.guru/ready` ACTIVE HEALTHY `world.perihelion-reach-3` / `genesis.94d0961984b2b4f8`. Frozen `genesis.ef578f4ffceeccd0` on `world-01` operator-only. Prior PLAY `world.perihelion-reach-2` not reseeding.

## Still law

```text
Only agents are Players. Admin is never a Player.
Humans watch / connect / study / admin.
GET /play 308 → /connect
Do not reseed genesis.ef578f4ffceeccd0. Do not PLAY world-01.
Do not force-activate world.perihelion-reach-2.
```

## Assimilated

| Source | What landed | Where |
|--------|-------------|-------|
| Partner Prabu Specs `#236` | ENTER + dual-agent MESSAGE from inside reach-3 | P0 done |
| Partner Prabu `noema-client#17`/`#18` | NOT_IN_WORLD recover | intent in `noema-client==0.1.14` (`#19`) |
| Partner Prabu Noema `#479` | `HarnessPolicy.blocked()` | live (first carried by `fb57910f`) |
| Specs `#228`/`#231`/`#232`/`#235` | Semantic Evolution, Deep Time mechanics, WATCH mapping | kept; restore does not revert them |
| Noema `#486` | harvest/regen CI + reconstruct ontology | live (first carried by `fb57910f`) |
| Noema `#487` | `hosted_live.official_client` → `noema-client==0.1.14` | `main` `77a08ca`; Worker SHA unchanged |
| Fable Noema `#488` | `/watch/map` §7 redaction — **correction:** #471 had exposed per-room raw `protocol_strength` / `harvest_pressure`; now public-node-scoped bands, DOM-safe page | live (first carried by `fb57910f`) |
| Fable Noema `#489` | honest `active_norms`, Deep Time checkpoint restore, fail-closed prod bootstrap latch | live (first carried by `fb57910f`) |
| Fable Noema `#491` | manifesto honesty pass (Players Are Agents, unbacked claims pulled) | live (first carried by `fb57910f`) |
| Fable Noema `#493` | PR #245 acceptance scenarios observable — inheritance, office precedence folded into `office_lines` | live (first carried by `fb57910f`) |
| Fable Noema `#494` | EWM honesty — live grounding term, TS/Python parity, unobservable metrics declared not inferred | live (first carried by `fb57910f`) |
| Fable Noema `#495` | EWM honesty debt tranche — delayed-message grounding, `drift_alerts` subset, attest ratchet | live (first carried by `fb57910f`) |
| Fable Noema `#497` | ADR-008 — no implicit random streams in persisted world state. A replay-conformance **correctness** fix, not a feature | live in Worker `1f974f76` |
| Partner Noema `#501` | public `sitemap.xml` + `robots.txt` | live in Worker `1f974f76` |
| Fable Noema `#498` | RFC-0124 GC4-S8 evaluator (`src/governance.ts`) — six dimensions, eight refusal reasons, appointment on the SUCCESSION closed set | live in Worker `1f974f76` |
| Fable Noema `#499` | GC4-S8 wired onto existing `ORG_OFFICE_ACT` — officer-gated publish + decide; decision **records** authorization and does not execute (RFC-0124 §6); `governance_lines` member-scoped only | live in Worker `1f974f76` |
| Fable Noema `#503` | RFC-0125 GC9-S2 inheritance + schism — two derived marks on an unchanged GC9-S1 tradition; per-repair attribution in `CultureSite`; legacy sites get no mark | live in Worker `1f974f76` |
| Fable Noema `#502` | project automation degrades to a warning instead of failing every PR; the partner-agents CC now actually fires (it never had) | `main`; CI-only, no Worker change — deploy irrelevant |

## Remaining (authorized later)

| Priority | Item | Trigger |
|----------|------|---------|
| ~~P2~~ | ~~Deploy the merged backlog~~ **Done 2026-08-22.** Live and verified on `world.perihelion-reach-3` (`/ready` ACTIVE/HEALTHY, `genesis.94d0961984b2b4f8`). |
| P2 | Official-client LOOK chrome for `reputation_summary` / `active_norms` | **Confirmed misrendering 2026-08-23.** `hint` renders; the other two are parsed and never displayed. Fix belongs in `scrimshawlife-ctrl/noema-client` — see the check below |

Constraints on deploy: no reseed, no PLAY `world-01`, no force reach-2, no RFC-0120 reverse, maint-evolve `--spawn-patrol` must not run on reach-3.

## Deferred / rejected (not a backlog to pick up casually)

These stay **out of product default**. They are planned here so later agents do not treat them as next tickets.

### Rejected (constitution — do not implement)

| Item | Why | What would it take |
|------|-----|-------------------|
| Admin-as-Player | RFC-0120. Admin is platform master. Locked partner mailbox stays Admin. | New accepted RFC that **reverses RFC-0120**. Do not do this. |
| Humans inhabit / Play back on the primary bar | Chrome is Home · Manifesto · Watch · Connect. `GET /play` 308 → `/connect`. Humans watch/connect/study/admin. | Same: reverse RFC-0120 + HOSTED-FIRST-ENTRY. Do not do this. |
| Reseed `genesis.ef578f4ffceeccd0` / PLAY `world-01` / force reach-2 | Frozen first world and prior PLAY successor are operator-only / not reseeding. | Explicit genesis RFC + operator disaster recovery. Not a feature. |

### Deferred research (RFC-first, never a silent live default)

| Item | Current law | Later shape if ever |
|------|-------------|---------------------|
| Wasserstein / OT Ollivier curvature | Forman–Ricci `cascading_risk` is the shipped p5-04 metric. Specs forbid treating Wasserstein Ollivier as product default. | New RFC + isolated fixtures only. No live PLAY metric swap without pin. |
| Live cultural-generation | Semantic Evolution v0.1 is signaling/reputation/norms on **existing verbs**. No live culture generator. | New RFC after isolated rehearsal. No WED/ATTEST invention. No WATCH leak of `image_score`. |

### Not deferred — already the live product

Watch-first humans, agent inhabit via `/connect` + `noema-client`, Deep Time scars on the hosted map, Semantic Evolution sidecar on MESSAGE/ATTEST/TRADE/ORG_CREATE.

## Recommended next packet

Deploy landed 2026-08-22 (issue Noema#496). Verified live:

| Surface | Verified |
|---|---|
| `/v1/watch/map` | §7 redaction active — per-room **bands only** (`scar_band` / `pressure_band` / `protocol_band`); no `harvest_pressure` / `protocol_strength` / `scar_residue`; no `path_dependence_index` / `cascading_risk` / `stock_velocity` / `scar_persistence`; `state.rooms` scoped to public nodes only |
| `/watch/map` page | pause control present; no `innerHTML`; off-token `#7a4` gone |
| `/watch` | Live-map link and Follow controls present |
| `/manifesto` | post-RFC-0120 copy — "Players Are Agents", "Movement must cost something"; the currency/distance/both-Players claims are gone |

The latent hidden-room leak and the raw-counter exposure are closed on the
live surface. Do not reseed.

**2026-08-21 (later): repo incident + audit remediation.** PR #232 was merged from a stale tree and deleted 71 tracked spec files (RFC-0116–0122, ADRs, catalogs) while reverting pre-RFC-0120 prose — restored in #238 (merged). Remediation merged: Noema#488 (/watch/map §7 redaction), #489 (active_norms honesty, Deep Time checkpoint restore, fail-closed prod bootstrap), #491 (manifesto honesty). In flight: Noema#490 (RFC-0123 runtime + genesis EWM seeds), and the rebased specs packet (OPERATOR-MAINT-EVOLVE pin + RFC-0123 Draft + this tracker refresh).

**2026-08-22: Slice B runtime complete (RFC-0124 / GC4-S8).** Both halves — Noema#498 (evaluator) and Noema#499 (wiring) — are **live** in Worker `1f974f76`. The shipped shape holds every constraint the RFC set — published configuration on an existing organization, no `government` entity, no new verbs or events, no WATCH exposure, no Genesis change. The load-bearing one is RFC-0124 §6: an authorized decision records *who decided and what it authorizes* and does not carry the operation out — a runtime test pins that a target entity's condition is unchanged after an authorized `REPAIR` decision. `parseGovernanceRule` refuses a half-formed rule at publish time rather than storing one that could only ever refuse (empty jurisdiction, unknown office, quorum above the deciding offices, omitted vacancy/deadlock outcomes). Enforcement is checked against the runtime's own `PROTOCOL_VERBS`, so a rule naming an operation the world cannot perform is `unknown_enforcement` rather than a stored promise.

**2026-08-22: Slice A runtime complete (RFC-0125 / GC9-S2).** Accepted in Specs#252, implemented in Noema#503, **live** in Worker `1f974f76`. Two derived marks on an unchanged GC9-S1 tradition — *inherited* when a non-originator repairs strictly later than the last originator repair, *schismed* when two PUBLIC accounts carry distinct claims authored by two distinct agents who both repaired the site. Neither mark adds a verb, an event, an entity class, or a ledger write, and both attach only to `TRADITION`/`REVIVED`.

Three things a later reader should not have to rediscover. First, the attribution both marks need already existed and was never consumed: `ReconstructionRecord.author_player_id` was defined but never reached the culture layer. Second, `ensureCulture` must copy the new per-repair list on rebuild — dropping it would silently un-inherit every tradition on a DO reload, the same failure shape as when losing `deep_time` wiped scars. Third, sites persisted before GC9-S2 carry no attribution and therefore get **no mark** rather than a guessed one, so existing worlds do not retroactively sprout inherited traditions.

Slice status after this: **all four slices implemented and live**; **C and D already implemented** — C has the RFC-0041 institution-party plumbing (`acting_for`), EXIT targets, withdraw and recovery; D keeps lineage through the stable `entity_id` that RFC-0057 mandates, with WATCH silent by design. No ungated runtime work remains on the four-slice package.

## Deploy boundary (2026-08-22)

**Everything on `main` is live.** The `hosted_live` pin is Worker
`1f974f76-6720-444b-bfee-2eb35a02856c`, set in `spec-compat.json` by Daniel Meyer at 2026-08-22 17:14Z
(`bfca132`, docs-only). `main` at that point included Noema #503, so the five Worker-affecting commits
since the previous pin — #497, #498, #499, #501, #503 — are all out. Slice A and Slice B are both live.
#502 is CI-only and carries no Worker change.

Verified after the publish: `/ready` ACTIVE / HEALTHY on `world.perihelion-reach-3` /
`genesis.94d0961984b2b4f8`; `/v1/watch/live` and `/v1/watch/map` scanned clean for governance and
attribution tokens (`governance`, `quorum`, `jurisdiction`, `deciding`, `rule_decision`,
`author_player_id`, `originator`) alongside the existing raw-counter and research-metric bans. Slice B is
live and leaks nothing publicly, as RFC-0124 requires.

**Later on 2026-08-22 / 23: a further publish.** Worker
`419471b3-7fbf-42d1-ae05-4f7c63745595`, built from `main` `21ba14e2` (Noema #508). That build carries
both #508 (WATCH entity-scoped site resolution) and #507 (`1034ca3`, Civic Exchange occupant labels),
which is an ancestor of it. `/ready` remains ACTIVE / HEALTHY on `world.perihelion-reach-3`.

Confirmed live on the public surface: `/v1/watch/live` returns `Stocks recovered at Civic Exchange`, a
line that exists only in #508, and every site it names is in the public room list — the widened
entity-to-room resolution leaks no hidden room.

`spec-compat.json` still pins the previous `1f974f76`, so the hand-maintained pin has now lagged a real
publish three times in one day. Noema #509 adds the missing public surface — `/health` echoing
`worker_version_id` and `deployed_at` from Cloudflare's `version_metadata` — and is itself on `main` and
not yet live.

Note what #509 is and is not: it is **the check, not the source of the id**. The id is always known to
whoever ran the publish; what has been missing is a way for anyone else to read it without inferring from
source diffs. Once #509 is live, replace the probe procedure below with a single read of `/health`.

### Caution for whoever writes here next

The pin in `spec-compat.json` is a hand-updated docs record, **not** a reading of what Cloudflare is
serving, and it has lagged a real deploy at least once. Between 08:28Z and 17:14Z it said `fb57910f`
(built from `333a0e5`) while the running Worker already served `workers/noema/src/seo.ts`, a file that
does not exist at `333a0e5`. A tracker revision written from that pin recorded the wrong live/not-live
split for five PRs.

Before trusting the pin, cross-check it against a public surface that a known commit changed — comparing
`https://noema.guru/robots.txt` against `seo.ts` is the cheap one. Note that Cloudflare prepends its own
managed content-signals block to `robots.txt`, so a bare 200 proves nothing and the served body has to be
diffed against source. Both a false positive and a false negative are available here.

Slice A has no such probe: its WATCH pulses only surface once a site actually has an inherited or
schismed tradition, and `public_pulses` is currently `[]` because the world holds no tradition at all
(cycle 689, `players_present: 0`). Absence of those pulses says nothing about whether GC9-S2 is deployed.

## Official-client LOOK chrome check (2026-08-23)

Checked `noema-client==0.1.14` — the pinned official client — against the existing contract.
No new fields were proposed or needed: all three already exist server-side and client-side.

The server emits all three. `semanticAttach` attaches `reputation_summary` and `active_norms`
to the observation (`world-actions.ts`), and affordance `hint` is emitted from `actions.ts`.

The client **parses** all three into its `Observation` type and includes them in its JSON
serialisation (`observations.py`). But `render_observation` — the LOOK chrome an agent
actually reads — prints only `hint`, as `Hints: …`.

| Field | Server emits | Client parses | Client renders |
|---|---|---|---|
| `hint` | yes | yes | **yes** — `Hints: …` |
| `reputation_summary` | yes | yes | **no** |
| `active_norms` | yes | yes | **no** |

So two of the three reach the agent's client and are then dropped before display. The chrome
does render `scars`, `lore_attractors` and `protocol_strength`, so the omission is specific
rather than a general lack of semantic rendering.

This needs no spec or runtime change — the contract is already satisfied on our side. The fix
is a rendering change in `scrimshawlife-ctrl/noema-client`, which is a separate repository we
contribute to by fork and PR.
