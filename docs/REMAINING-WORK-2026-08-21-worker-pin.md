# Remaining work — 2026-08-21 evening

**Status:** Honest snapshot after Noema `#487` on `main` (official client pin) and Specs RFC-0120 restore `#237`.  
**Does not:** reseed frozen first world, `force:true` on production, same-id activate of `world.perihelion-reach-2`, reverse RFC-0120, treat Admin as a Player, or pin a Worker SHA that is not live.

**Live as of 2026-08-21** (verified still current 2026-08-24; the authority is `/ready` and `hosted_live`, not this line). `GET https://noema.guru/ready` ACTIVE HEALTHY `world.perihelion-reach-3` / `genesis.94d0961984b2b4f8`. Frozen `genesis.ef578f4ffceeccd0` on `world-01` operator-only. Prior PLAY `world.perihelion-reach-2` not reseeding. The live Worker is `GET https://noema.guru/version`, not a SHA named below.

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
| Partner Prabu Noema `#479` | `HarnessPolicy.blocked()` | **offline harness only.** `#479` touches four files under `src/noema/harness/` and one Python test — **no `workers/` file at all**, so no Worker build carries it and `fb57910f` never did. It runs in the Python Controller harness beside an agent, not in the hosted Worker |
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
| ~~P2~~ | ~~Official-client LOOK chrome for `reputation_summary` / `active_norms`~~ **Fixed 2026-08-23** in `noema-client` [#20](https://github.com/scrimshawlife-ctrl/noema-client/pull/20) (0.1.15), open for review. `render_observation` now prints both. Nothing to do here — see the pin trigger below |
| ~~P3~~ | ~~Move `hosted_live.official_client` to `noema-client==0.1.15`~~ **Done 2026-08-24.** PyPI has 0.1.15; pinned in Noema #522. The trigger fired as written — the pin waited for the release rather than the merge |

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

**2026-08-22: everything on `main` was live.** The `hosted_live` pin was Worker
`1f974f76-6720-444b-bfee-2eb35a02856c`, set in `spec-compat.json` by Daniel Meyer at 2026-08-22 17:14Z
(`bfca132`, docs-only). `main` at that point included Noema #503, so the five Worker-affecting commits
since the previous pin — #497, #498, #499, #501, #503 — were all out. Slice A and Slice B were both live.
#502 is CI-only and carries no Worker change. That Worker is not current; later dated publishes follow.

Verified after the publish: `/ready` ACTIVE / HEALTHY on `world.perihelion-reach-3` /
`genesis.94d0961984b2b4f8`; `/v1/watch/live` and `/v1/watch/map` scanned clean for governance and
attribution tokens (`governance`, `quorum`, `jurisdiction`, `deciding`, `rule_decision`,
`author_player_id`, `originator`) alongside the existing raw-counter and research-metric bans. Slice B is
live and leaks nothing publicly, as RFC-0124 requires.

## Specs / runtime reconciliation (2026-08-24)

Audited the two repositories against each other rather than each against itself. Findings,
in the order they matter.

**The pin lagged a publish, twice in one day.** At 2026-08-24T02:06:47Z, Worker
`c9e6c8b9-75c8-46be-b200-76884f40efc7` went live from `main` `06b818f` (Noema #524, RFC-0126);
`spec-compat.json` still read `cbb1b87e`. `/version` closed the gap in one read rather than a
source diff, which is what #509/#512 bought, but the lag itself keeps recurring: **the pin
does not update itself, and a publish does not update it.** Two publishes, two lags, both
caught by reading rather than inferring. That is the improvement — not that the pin stopped
being wrong.

A later `GET https://noema.guru/version` on 2026-08-24 reported Worker
`2bb3a8b4-4252-4160-b91e-80d334e471d4` (`deployed_at` 2026-08-24T03:33:02Z). Do not treat
`c9e6c8b9`, `cbb1b87e`, or `1f974f76` as current.

**A status went stale inside an hour.** The RFC runtime audit's RFC-0126 row said
`PENDING PUBLISH`, which was true when #524 wrote it at 01:49:22Z and false seventeen minutes
later. Nothing was careless; the row was simply written on one side of an event that happened
on the other. Dated rows need a re-read after any publish, not only after a merge.

**A machine contract nobody read.** RFC-0126 ships
[`specs/watch-entity-update-exposure.rfc-0126.json`](../specs/watch-entity-update-exposure.rfc-0126.json)
so a runtime can be checked against it. The census held its own copy of the silent list. A
copy of a contract drifts from it silently. The census must read the RFC-0126 JSON, not a
local copy. Noema #525 is the binding (same `skipIf` as the GC4-S8 fixtures) and was
verified to fail when the JSON and the runtime disagree.

**Cross-repo path hygiene is good.** 110 runtime paths are referenced across these docs; two
do not exist, both in plan documents rather than contracts — `src/play.ts` in
[PLAYER-BRAND-IMPLEMENTATION.md](PLAYER-BRAND-IMPLEMENTATION.md), which is the PLAY HTML file
RFC-0120 retired when humans stopped being Players, and one path in a `superpowers/plans/`
file. Plans describing files that were never built are not defects; they are what a plan is.

**`chamber_suite` is accurate.** `pass: 23 / skip: 3 / skip_ids C14 C16 C17` matches
`hosted-matrix.json` exactly.

### Resolved — `specs.commit` tracks `main`

`spec-compat.json` carried two Specs pins thirteen days apart. `hosted_live.specs_git` was
`26d840b` (2026-08-24). `specs.commit` was `d69be87` (2026-08-11, Specs #18). `pin_label` is
`v0.1-v0.7-core-loop-freeze` and `"ref": "main"` sat in the same block, so it was unclear
whether the pin was a fixed freeze or meant to track.

[Noema #526](https://github.com/Zero-State-LLC/Noema/pull/526) answered it: the pin tracks
`main`, so `d69be87` was stale, not a freeze point. #526 moved `specs.commit` to `26d840b`.
That value is the resolution, not a claim that Specs `main` still sits there. For the
current pins, read `spec-compat.json` and `GET https://noema.guru/version`.

**2026-08-24T01:08:29Z publish.** Worker `cbb1b87e-8341-45a1-a94d-40e10ac6a343`, read from
`GET /version` and pinned in Noema #522. It carries Noema #517 (RFC-0032 Postmark standby)
and #520 (a hidden-room harvest was reaching the public feed); #521 merged six minutes after
the publish and is not in it.

Two things this publish is worth remembering for. It is the first where the pin did not lag —
`/version` existed, so the pin was a reading rather than a reconstruction. And what the build
*contains* still had to be derived from merge order, because `/version` reports the version id
and the deploy time and not a source commit, and neither shipped fix has a public probe:
the Postmark standby is inert until configured and admin-only, and the harvest fix needs a
harvest, with `players_present` `0`. Derived is not observed, and the runtime audit says so
in the row rather than rounding it up.

**2026-08-23T07:16:28Z: `/version` publish.** Worker `591a5fe4-7858-4721-9024-58da9f761e41`,
carrying Noema #509 and #512. `GET /version` now reports the running build directly, and
`/health` is back to the liveness check `OPERATIONS.md` specifies. This is the first pin in this
document that was **read from the live surface rather than inferred**.

**Earlier on 2026-08-22 / 23: a further publish.** Worker
`419471b3-7fbf-42d1-ae05-4f7c63745595`, built from `main` `21ba14e2` (Noema #508). That build carries
both #508 (WATCH entity-scoped site resolution) and #507 (`1034ca3`, Civic Exchange occupant labels),
which is an ancestor of it. `/ready` remains ACTIVE / HEALTHY on `world.perihelion-reach-3`.

Confirmed live on the public surface: `/v1/watch/live` returns `Stocks recovered at Civic Exchange`, a
line that exists only in #508, and every site it names is in the public room list — the widened
entity-to-room resolution leaks no hidden room.

At the time of that publish `spec-compat.json` still pinned the previous `1f974f76`, so the
hand-maintained pin had lagged a real publish three times in one day.

The fix landed in two steps. Noema #509 bound Cloudflare's `version_metadata` and echoed it from
`/health`; Noema #512 then moved those pins to `/version`, where `OPERATIONS.md` puts them, and
restored `/health` to the liveness check it specifies. **Read `/version`, not `/health`** — see the
procedure below.

Note what that surface is and is not: it is **the check, not the source of the id**. The id is always
known to whoever ran the publish; what had been missing is a way for anyone else to read it without
inferring from source diffs.

### How to find out what is live (2026-08-23 onward)

```
curl -s https://noema.guru/version
```

That is the whole procedure. It reports `worker_version_id` and `deployed_at` straight from
Cloudflare's `version_metadata` binding, alongside `protocol_version` and `world_id`. Live
since the 2026-08-23T07:16:28Z publish (Noema #509 + #512).

**Do not reason from `spec-compat.json` alone.** Its pin is hand-updated and lagged a real
publish three times on 2026-08-22 — once by about nine hours. A tracker revision written from
it recorded the wrong live/not-live split for five PRs, and a deploy request was nearly filed
for work already shipped. The pin is a record of what someone wrote down; `/version` is a
reading of what is running. When they disagree, `/version` wins and the pin needs fixing.

If `/version` 404s, the running build predates #512 and you are back to inference — in which
case compare `https://noema.guru/robots.txt` against `workers/noema/src/seo.ts`, and note that
Cloudflare prepends its own managed content-signals block, so a bare 200 proves nothing and the
served body must be diffed against source. Both a false positive and a false negative are
available on that endpoint.

Some changes have no external probe at all. Slice A's GC9-S2 marks surface only once a site
actually has an inherited or schismed tradition, and `public_pulses` is currently `[]` because
the world holds no tradition. Absence of a pulse says nothing about whether the code is
deployed. Where no probe exists, ask the publisher rather than inferring — and record what was
not determined instead of writing "unknown" over a fact someone else holds.

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

**Resolved 2026-08-23** in [noema-client #20](https://github.com/scrimshawlife-ctrl/noema-client/pull/20),
version 0.1.15, open for review. `render_observation` gained two lines in the existing
one-line style, omitted entirely when the field is absent or empty:

```text
Reputation: image 4, second-order 2
Norms: ORG_CREATE influence 7, harvest pressure 0.25, last ratchet norm_ratchet
```

The load-bearing one is `Norms:`. `active_norms.org_create_influence` is the live ORG_CREATE
cost with the ratchet included — server-side `5 + orgCreateExtraInfluence(w)`, not the flat 5
— so an agent deciding whether to found an organization was paying a price it could not read.
Display path only; `to_observation`, `prepare_context` and the JSON serialization are unchanged.

Do **not** move `hosted_live.official_client` when that PR merges. PyPI is at 0.1.14 and that
repository publishes on a GitHub Release, not on merge. The pin moves when 0.1.15 is on PyPI.

## Which assimilated rows a Worker build actually carried (2026-08-23)

The Assimilated table above attributes work to Worker versions. Checked every row against the
files each PR touched:

| Rows | Attribution |
|---|---|
| `#486` `#488` `#489` `#491` `#493` `#494` `#495` `#497` `#498` `#499` `#501` `#503` | Correct. Each touches `workers/`, so a Worker build carries it |
| `#487` | Already correct — the row itself says "Worker SHA unchanged" |
| `#502` | Already correct — the row itself says CI-only |
| `#479` | **Was wrong.** Python harness only; corrected above |

One row in fifteen. The failure shape is worth naming because it is not the same as the pin
lagging a publish: here a real Worker version id was attached to a change that contains no
Worker code, so the row read as hosted when nothing about it was. `Zero-State-LLC/Noema`
`docs/RFC-RUNTIME-AUDIT-2026-08-23.md` now carries the per-RFC version of this distinction
for all 125 contracts.
