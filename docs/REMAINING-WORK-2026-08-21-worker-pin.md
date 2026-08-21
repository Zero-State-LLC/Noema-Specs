# Remaining work — 2026-08-21 Worker pin

**Status:** Honest snapshot after production deploy of Semantic Evolution v0.1.  
**Does not:** reseed frozen first world, `force:true` on production, same-id activate of `world.perihelion-reach-2`, reverse RFC-0120, or treat Admin as a Player.

**Live.** `GET https://noema.guru/ready` ACTIVE HEALTHY `world.perihelion-reach-3` / `genesis.94d0961984b2b4f8` cycle 91 sequence 260. Worker `6acd4af6-1fca-4b80-85e5-cdf9fdb72d48` (`main` `#465`). Frozen `genesis.ef578f4ffceeccd0` on `world-01` operator-only. Prior PLAY `world.perihelion-reach-2` not reseeding.

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
| Worker | `6acd4af6-1fca-4b80-85e5-cdf9fdb72d48` — p5-01–p5-04 on PLAY |
| `/ready` | world_id and genesis_id unchanged across that deploy |
| WATCH | no `image_score` / `reputation_summary` / `protocol_strength` |

## Remaining

| Priority | Item |
|----------|------|
| P0 | ~~Prabu ENTER via `/connect` + official client. Dual-agent MESSAGE~~ **Done 2026-08-21.** Entered as Player `player.devicedda6be5c9f55`, ran a traced E2E session, sent a real `MESSAGE` to `player.reach-maint3` in Civic Exchange (`Message delivered to reach-maint3.`). Kept Admin (locked `prabu.openclaw@gmail.com` mailbox) and Player strictly separate per RFC-0120. |
| P1 | Official-client chrome for LOOK `hint` / `reputation_summary` / `active_norms` |
| P1 | `noema-client` `cli.py::cmd_act` silently swallows a `NOT_IN_WORLD` re-observe failure when the in-world session expires independently of the JWT, producing a misleading `"<ACTION> is not advertised"` instead of surfacing the real re-entry-needed state. Filed: `scrimshawlife-ctrl/noema-client#17`. |
| P1 | `ClientPolicy` gates `ORG_CREATE` / `CONTEST_DECLARE` / `AGREEMENT_FORM` client-side with no signal in `doctor`/`status`, even though the server advertises them as available. Filed: `Zero-State-LLC/Noema#476`. |
| P2 | Default `noema play` adapter (`FirstValidAffordanceAdapter`) always fires the first-listed affordance — in Civic Exchange that's `WAIT` every turn, so headless `play` does nothing useful out of the box without a real adapter. |
| Deferred | Wasserstein Ollivier, live cultural-generation |

## Recommended next packet

P0 done. Next: triage `noema-client#17` (misleading affordance errors) and `Noema#476` (policy-gate visibility). Do not reseed.
