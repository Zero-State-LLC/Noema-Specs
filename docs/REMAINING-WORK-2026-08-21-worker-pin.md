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
| Partner Prabu Noema `#479` | `HarnessPolicy.blocked()` | `main`; not on live Worker until deploy |
| Specs `#228`/`#231`/`#232`/`#235` | Semantic Evolution, Deep Time mechanics, WATCH mapping | kept; restore does not revert them |
| Noema `#486` | harvest/regen CI + reconstruct ontology | live in Worker `fb57910f` |
| Noema `#487` | `hosted_live.official_client` → `noema-client==0.1.14` | `main` `77a08ca`; Worker SHA unchanged |
| Fable Noema `#488` | `/watch/map` §7 redaction — **correction:** #471 had exposed per-room raw `protocol_strength` / `harvest_pressure`; now public-node-scoped bands, DOM-safe page | live in Worker `fb57910f` |
| Fable Noema `#489` | honest `active_norms`, Deep Time checkpoint restore, fail-closed prod bootstrap latch | live in Worker `fb57910f` |
| Fable Noema `#491` | manifesto honesty pass (Players Are Agents, unbacked claims pulled) | live in Worker `fb57910f` |
| Fable Noema `#493` | PR #245 acceptance scenarios observable — inheritance, office precedence folded into `office_lines` | live in Worker `fb57910f` |
| Fable Noema `#494` | EWM honesty — live grounding term, TS/Python parity, unobservable metrics declared not inferred | live in Worker `fb57910f` |
| Fable Noema `#495` | EWM honesty debt tranche — delayed-message grounding, `drift_alerts` subset, attest ratchet. **This is the commit the 2026-08-22 publish was built from** | live in Worker `fb57910f` |
| Fable Noema `#497` | ADR-008 — no implicit random streams in persisted world state. A replay-conformance **correctness** fix, not a feature | `main`; **not** in `fb57910f` — next deploy |
| Partner Noema `#501` | public `sitemap.xml` + `robots.txt` | `main`; **not** in `fb57910f` — next deploy |
| Fable Noema `#498` | RFC-0124 GC4-S8 evaluator (`src/governance.ts`) — six dimensions, eight refusal reasons, appointment on the SUCCESSION closed set | `main`; **not** in `fb57910f` — next deploy |
| Fable Noema `#499` | GC4-S8 wired onto existing `ORG_OFFICE_ACT` — officer-gated publish + decide; decision **records** authorization and does not execute (RFC-0124 §6); `governance_lines` member-scoped only | `main`; **not** in `fb57910f` — next deploy |
| Fable Noema `#503` | RFC-0125 GC9-S2 inheritance + schism — two derived marks on an unchanged GC9-S1 tradition; per-repair attribution in `CultureSite`; legacy sites get no mark | `main`; **not** in `fb57910f` — next deploy |
| Fable Noema `#502` | project automation degrades to a warning instead of failing every PR; the partner-agents CC now actually fires (it never had) | `main`; CI-only, no Worker change — deploy irrelevant |

## Remaining (authorized later)

| Priority | Item | Trigger |
|----------|------|---------|
| ~~P2~~ | ~~Deploy the merged backlog~~ **Done 2026-08-22.** Live and verified on `world.perihelion-reach-3` (`/ready` ACTIVE/HEALTHY, `genesis.94d0961984b2b4f8`). |
| P2 | Official-client LOOK chrome for `hint` / `reputation_summary` / `active_norms` | only if live 0.1.14 still misrenders |

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

**2026-08-22: Slice B runtime complete (RFC-0124 / GC4-S8).** Both halves are on `main` and unreleased: Noema#498 (evaluator) and Noema#499 (wiring). The shipped shape holds every constraint the RFC set — published configuration on an existing organization, no `government` entity, no new verbs or events, no WATCH exposure, no Genesis change. The load-bearing one is RFC-0124 §6: an authorized decision records *who decided and what it authorizes* and does not carry the operation out — a runtime test pins that a target entity's condition is unchanged after an authorized `REPAIR` decision. `parseGovernanceRule` refuses a half-formed rule at publish time rather than storing one that could only ever refuse (empty jurisdiction, unknown office, quorum above the deciding offices, omitted vacancy/deadlock outcomes). Enforcement is checked against the runtime's own `PROTOCOL_VERBS`, so a rule naming an operation the world cannot perform is `unknown_enforcement` rather than a stored promise. Not live until the next deploy.

**2026-08-22: Slice A runtime complete (RFC-0125 / GC9-S2).** Accepted in Specs#252, implemented in Noema#503, on `main` and unreleased. Two derived marks on an unchanged GC9-S1 tradition — *inherited* when a non-originator repairs strictly later than the last originator repair, *schismed* when two PUBLIC accounts carry distinct claims authored by two distinct agents who both repaired the site. Neither mark adds a verb, an event, an entity class, or a ledger write, and both attach only to `TRADITION`/`REVIVED`.

Three things a later reader should not have to rediscover. First, the attribution both marks need already existed and was never consumed: `ReconstructionRecord.author_player_id` was defined but never reached the culture layer. Second, `ensureCulture` must copy the new per-repair list on rebuild — dropping it would silently un-inherit every tradition on a DO reload, the same failure shape as when losing `deep_time` wiped scars. Third, sites persisted before GC9-S2 carry no attribution and therefore get **no mark** rather than a guessed one, so existing worlds do not retroactively sprout inherited traditions.

Slice status after this: **A and B implemented and unreleased**; **C and D already implemented** — C has the RFC-0041 institution-party plumbing (`acting_for`), EXIT targets, withdraw and recovery; D keeps lineage through the stable `entity_id` that RFC-0057 mandates, with WATCH silent by design. No ungated runtime work remains on the four-slice package. Not live until the next deploy.

## Deploy boundary (2026-08-22)

A deploy landed on 2026-08-22, so the phrase "not live until deploy" now means opposite things on either
side of it — four rows above it were carried, three below it were not. The boundary is therefore stated
once here rather than left to be inferred per row.

The publish moved the `hosted_live` pin once, producing Worker `fb57910f-a32b-4dc3-95ff-526188b0984d` (was `5c796d6e`), built
from `main` `333a0e5` — Noema #495, 2026-08-21 22:49 -0700. Pinned in `spec-compat.json` by Noema #500.

**Everything merged after `333a0e5` is not live.** In order: #497, #498, #499, #501, #502, #503, #500.

Two things about that set are worth calling out rather than leaving in a table:

- **Slices A and B are both entirely undeployed.** No agent in Perihelion Reach can publish a governance
  rule or inherit a practice yet, however green the runtime tests are.
- **ADR-008 (#497) is undeployed, and it is a correctness fix rather than a feature.** The live Worker
  still persists world state through the implicit random streams ADR-008 forbids, so replay conformance
  is not yet true of production. This should be weighted above the two feature slices when the next
  deploy is scheduled.

Noema #502 is CI-only and carries no Worker change, so it is unaffected either way.
