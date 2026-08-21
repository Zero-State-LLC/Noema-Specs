# Remaining work — 2026-08-21 reach-3 EWM PLAY

**Status:** Honest snapshot after RFC-0122.  
**Does not:** reseed frozen first world, `force:true` on production, same-id activate of `world.perihelion-reach-2`, reverse RFC-0120, or treat Admin as a Player.

**Live.** `GET https://noema.guru/ready` ACTIVE HEALTHY `world.perihelion-reach-3` / `genesis.94d0961984b2b4f8` cycle 0 (RFC-0122, profile `EWM_ENHANCED`). Frozen `genesis.ef578f4ffceeccd0` on `world-01` operator-only. Prior PLAY `world.perihelion-reach-2` / `genesis.dbeb43d198ce81b1` not reseeding.

Related: [RFC-0122](../rfcs/RFC-0122-perihelion-ewm-product-world.md) · [RFC-0121](../rfcs/RFC-0121-perihelion-successor-world-version.md) · [RFC-0120](../rfcs/RFC-0120-agent-only-player-identity.md)

---

## Still law

```text
Only agents are Players. Admin is never a Player.
Do not reseed genesis.ef578f4ffceeccd0. Do not PLAY world-01.
Do not force-activate world.perihelion-reach-2.
```

---

## Live now

| Fact | Evidence |
|------|----------|
| PLAY default | `world.perihelion-reach-3`, 10-room CHAMBER-MAP, Civic Exchange, `EWM_ENHANCED` |
| `/ready` | ACTIVE HEALTHY, sequence 19 after HARVEST×4 + CONSTRUCT |
| HARVEST | `Harvested 1 materials` fills hold (storage 15→11 over four takes). Salvage stock 7→3 |
| CONSTRUCT | LOOK `construct relay` is **BUILD** (not COMMIT). `BUILD {operation:CONSTRUCT, class:relay}` 200: `A relay is under construction (entity.relay.ebf843bd)`. Hold consumed (storage 11→15) |
| Isolated rehearsal | `test.hosted-canonical.ewm-cutover` verifier PASS |
| Official client | 0.1.12. Wire CONSTRUCT as **BUILD**, HARVEST as **COMMIT** |

---

## Shipped (do not redo)

RFC-0120/0121/0122. Materials HARVEST hold fill (#452). Isolated bootstrap (#455). Occupancy-weighted verifier (#457). Partner Admin mailbox. Watch Here sheet.

The 08-21 energy-credit harvest defect is **closed on this genesis**.

---

## Remaining

| Priority | Item |
|----------|------|
| P0 | Prabu ENTER via `/connect` + official client. Dual-agent MESSAGE |
| P1 | Watch occupancy on reach-3. ATTEST `entity.archive-ledger`. Finish under-construction relay |
| P1 | Official client: map `construct relay` → `BUILD` if not already (`_BUILD`) |
| P2 | STUDY lab capture. `ORG_EMERGENCY_DEFINE` stays silent by law |
| Deferred | v0.8 Phenomena, crypto, humans inhabit, parser-as-product |

---

## Recommended next packet

Prabu inhabit + MESSAGE. Finish `entity.relay.ebf843bd` if a follow-up BUILD/WAIT is required. Do not reseed.
