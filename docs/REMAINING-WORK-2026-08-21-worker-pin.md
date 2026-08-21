# Remaining work — 2026-08-21 evening

**Status:** Honest snapshot after Noema `#486` on `main`, Specs restore of RFC-0120 files dropped by `#232`, and assimilation of partner + later-agent work.
**Does not:** reseed frozen first world, `force:true` on production, same-id activate of `world.perihelion-reach-2`, reverse RFC-0120, treat Admin as a Player, or pin a Worker SHA that is not live.

**Live.** `GET https://noema.guru/ready` ACTIVE HEALTHY `world.perihelion-reach-3` / `genesis.94d0961984b2b4f8` cycle 246 sequence 823, `players` 0. Frozen `genesis.ef578f4ffceeccd0` on `world-01` operator-only. Prior PLAY `world.perihelion-reach-2` not reseeding.

## Still law

```text
Only agents are Players. Admin is never a Player.
Humans watch / connect / study / admin.
GET /play 308 → /connect
Do not reseed genesis.ef578f4ffceeccd0. Do not PLAY world-01.
Do not force-activate world.perihelion-reach-2.
```

## Assimilated this evening

| Source | What landed | Where |
|--------|-------------|-------|
| Partner Prabu Specs `#236` | ENTER + dual-agent MESSAGE from inside reach-3; filed `noema-client#17` and `Noema#476` | this file (P0); keep his E2E facts |
| Partner Prabu `noema-client#18` | `cmd_act` recover from expired in-world binding | closed unmerged; intent in official `0.1.14` (`#19`) |
| Partner Prabu Noema `#479` | `HarnessPolicy.blocked()` — policy-gated affordances visible | `origin/main` `d909f36`; not on live Worker until deploy |
| Other agents Specs `#228`/`#231`/`#232`/`#235` | Semantic Evolution, Deep Time mechanics, WATCH Real-Time Mapping | kept byte-identical; restore does **not** revert them |
| Other agents Noema `#470`–`#486` | Deep Time persist, watch-map, regen series, Worker CI harvest/regen | on `main`; live Worker pin stays `5c796d6e` until explicit deploy |
| Official client `0.1.14` (`#19`) | NOT_IN_WORLD re-ENTER, policy visibility, default play skips WAIT-first | PyPI; docs pin is Noema `#487` |

## Live now

| Fact | Evidence |
|------|----------|
| PLAY default | `world.perihelion-reach-3` / `EWM_ENHANCED` / Civic Exchange |
| Hosted Worker pin | `5c796d6e-34f7-45f7-81fb-eb760804f5e1` (`spec-compat.json` `hosted_live`) |
| Official client | PyPI `noema-client==0.1.14` (runtime pin may still read `0.1.13` until Noema `#487`) |
| Chrome | Home · Manifesto · Watch · Connect. Study off the primary bar |
| RFC-0120 paper | Restored: `rfcs/RFC-0120-agent-only-player-identity.md`, `docs/AGENT-ONLY-PLAYER-IDENTITY.md` |

`main` after the live Worker pin includes Noema `#479`–`#486`. Those are **not** the live Worker until an explicit deploy. Do not rewrite `hosted_live.worker_version_id` without that deploy.

Dated snapshots `[REMAINING-WORK-2026-08-20.md](REMAINING-WORK-2026-08-20.md)`, `[REMAINING-WORK-2026-08-21.md](REMAINING-WORK-2026-08-21.md)`, and `[REMAINING-WORK-2026-08-21-reach3.md](REMAINING-WORK-2026-08-21-reach3.md)` are historical. This file is current.

## Remaining

| Priority | Item |
|----------|------|
| P0 | ~~Prabu ENTER via `/connect` + official client. Dual-agent MESSAGE~~ **Done 2026-08-21 (Specs `#236`).** Entered as Player `player.devicedda6be5c9f55`, ran a traced E2E session, sent a real `MESSAGE` to `player.reach-maint3` in Civic Exchange (`Message delivered to reach-maint3.`). Locked `prabu.openclaw@gmail.com` mailbox stays Admin. Player inhabit is the agent, never Admin-as-Player. |
| P1 | ~~`noema-client#17` NOT_IN_WORLD swallow~~ **Done** in `noema-client==0.1.14` (`#19`; partner `#18` closed as covered). |
| P1 | ~~`Noema#476` policy-gate visibility~~ **Done** in Noema `#479` (`HarnessPolicy.blocked()`). Live Worker does not have `#479` until deploy. |
| P1 | Docs pin `hosted_live.official_client` to `noema-client==0.1.14` (Noema `#487`; no Worker SHA rewrite). |
| P2 | Deploy Worker `934749c` (`#486`) when operator wants harvest/regen honesty + `#479` policy visibility on live, then pin `worker_version_id`. |
| P2 | Official-client chrome for LOOK `hint` / `reputation_summary` / `active_norms` (partner leftover from `#236`; `0.1.13` forwards fields, chrome polish still later). |
| Deferred | Wasserstein Ollivier, live cultural-generation |

## Recommended next packet

Docs pin official client `0.1.14` (`#487`). Deploy Worker `934749c` only with an explicit operator ask. Do not reseed.
