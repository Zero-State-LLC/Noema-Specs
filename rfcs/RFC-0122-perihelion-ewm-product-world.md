# RFC-0122 — Perihelion EWM product world_version

## Status

**Accepted**

Ops / geography identity. No new Player verbs. No reseed of `genesis.ef578f4ffceeccd0`. No `force:true` on `world.perihelion-reach-2` or frozen `world-01`. Isolated EWM proof (`test.hosted-canonical.ewm-cutover`) is the gate.

## Problem

`EWM_ENHANCED` is on the Worker. Isolated inhabit PASSed. Same-id activate on `world.perihelion-reach-2` is `409 ALREADY_ACTIVATED`; production `force:true` is `403`. Building the game must not wait on a reseed of live reach-2.

## Decision

| Field | Value |
|---|---|
| Public name | Perihelion Reach |
| Profile / story seeds | `EWM_ENHANCED` · `OLD_TRADE_NETWORK` + `RESOURCE_CRISIS` |
| Product `world_id` (next `DEFAULT_WORLD_ID`) | `world.perihelion-reach-3` |
| Production `world_seed` | new; MUST NOT be `17011984` |
| Cycle 0 | CHAMBER-MAP 10 rooms, entry Civic Exchange, EWM seed (salvage-cache regen 1.15, archetypes, production node) |

`world.perihelion-reach-2` / `genesis.dbeb43d198ce81b1` stays as-is (operator Recover). Frozen first world stays operator-only.

## Governance (relaxed)

Production **may** `preview` + `activate` (`confirm: true`) `world.perihelion-reach-3` without a further RFC. Isolated PASS is sufficient.

Still forbidden:

- `force:true` in production
- activate on `world.perihelion-reach-2` or `world-01` / `world.perihelion-reach`
- product-path hash collision with `genesis.ef578f4ffceeccd0`

## Cutover (two deploys)

1. Land admission + ledger namespace. `DEFAULT_WORLD_ID` stays `world.perihelion-reach-2`. Deploy. Activate `world.perihelion-reach-3`.
2. Set `DEFAULT_WORLD_ID=world.perihelion-reach-3` and deploy. PLAY maps `world.perihelion*` to that default. Controllers `ENTER_WORLD` at Civic Exchange on the new Cycle 0. No ledger copy.

## Errors

| Code | When |
|---|---|
| `POLICY_DENIED` | production `force`; reseed |
| `ALREADY_ACTIVATED` | activate on frozen or already-ACTIVE reach-2 |
| `INVALID_SEED` | product-path hashes to `genesis.ef578f4ffceeccd0` |
| `CONFIRMATION_REQUIRED` | activate without `confirm: true` |
