# Remaining work — 2026-08-21 Worker pin

**Status:** Honest snapshot after production deploy of Semantic Evolution v0.1.  
**Does not:** reseed frozen first world, `force:true` on production, same-id activate of `world.perihelion-reach-2`, reverse RFC-0120, or treat Admin as a Player.

**Live.** `GET https://noema.guru/ready` ACTIVE HEALTHY `world.perihelion-reach-3` / `genesis.94d0961984b2b4f8` cycle 91 sequence 260. Worker `5c796d6e` (`main` `#474`, Deep Time persist fix); official client `noema-client==0.1.14` (`#77a08ca`/`0.1.14` NOT_IN_WORLD recovery). Frozen `genesis.ef578f4ffceeccd0` on `world-01` operator-only. Prior PLAY `world.perihelion-reach-2` not reseeding.

## Still law

```text
Only agents are Players. Admin is never a Player.
Do not reseed genesis.ef578f4ffceeccd0. Do not PLAY world-01.
Do not force-activate world.perihelion-reach-2.
```

## Live now

| Fact | Evidence |
|------|----------|
| PLAY default | `world.perihelion-reach-3` / `EWM_ENHANCED` / Civic Exchange |
| Worker | `5c796d6e` — p5-01–p5-04 + Deep Time (#469/#470/#473) + watch-map (#471) on PLAY |
| `/ready` | world_id and genesis_id unchanged across that deploy |
| WATCH | no `image_score` / `reputation_summary`. **Correction:** `/v1/watch/map` (#471) exposed per-room raw `protocol_strength` / `harvest_pressure`; redaction to §7 bands is Noema#488 (open) |

## Remaining

| Priority | Item |
|----------|------|
| P0 | ~~Prabu ENTER via `/connect` + official client. Dual-agent MESSAGE~~ **Done 2026-08-21.** Entered as Player `player.devicedda6be5c9f55`, ran a traced E2E session, sent a real `MESSAGE` to `player.reach-maint3` in Civic Exchange (`Message delivered to reach-maint3.`). Kept Admin (locked `prabu.openclaw@gmail.com` mailbox) and Player strictly separate per RFC-0120. |
| P1 | Official-client chrome for LOOK `hint` / `reputation_summary` / `active_norms` |
| ~~P1~~ | ~~`noema-client` `cmd_act` NOT_IN_WORLD swallow~~ **Done** — closed by `noema-client` `0.1.14` (`ensure_in_world()` auto-recovery; fail-loud on other pre-act observe errors). `noema-client#17` closed; fork PR #18 superseded. |
| ~~P1~~ | ~~policy-gate visibility~~ **Done** (harness side) — `HarnessPolicy.blocked()` tags advertised-but-gated affordances in context + tester report (`Noema#479`, merged). Client-side `doctor` signal remains open in `noema-client`. |
| P2 | Default `noema play` adapter (`FirstValidAffordanceAdapter`) always fires the first-listed affordance — in Civic Exchange that's `WAIT` every turn, so headless `play` does nothing useful out of the box without a real adapter. |
| Deferred | Wasserstein Ollivier, live cultural-generation |

## Recommended next packet

P0 done. `noema-client#17` and `Noema#476` resolved (see above). Do not reseed.

**2026-08-21 (later): repo incident + audit remediation.** PR #232 was merged from a stale tree and deleted 71 tracked spec files (RFC-0116–0122, ADRs, catalogs) while reverting pre-RFC-0120 prose — restored in #238. Audit remediation in flight: specs #239 (maint-evolve supervisor pin, stacked), #240 (RFC-0123 ratchet bounds + costly TRADE-reject, stacked); runtime Noema#488 (/watch/map §7 redaction), #489 (active_norms honesty, Deep Time checkpoint restore, fail-closed prod bootstrap), #490 (RFC-0123 runtime + genesis EWM seeds reach live state), #491 (manifesto honesty pass post-RFC-0120).
