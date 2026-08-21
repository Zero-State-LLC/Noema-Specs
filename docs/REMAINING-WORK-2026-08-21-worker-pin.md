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
| Noema `#486` | harvest/regen CI + reconstruct ontology | `main` `934749c`; not live until deploy |
| Noema `#487` | `hosted_live.official_client` → `noema-client==0.1.14` | `main` `77a08ca`; Worker SHA unchanged |

## Remaining (authorized later)

| Priority | Item | Trigger |
|----------|------|---------|
| P2 | Deploy Worker `934749c` (`#486` + `#479` on live), then pin `hosted_live.worker_version_id` | explicit operator **deploy** |
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

Deploy Worker `934749c` **only** with an explicit operator ask. Do not reseed.
