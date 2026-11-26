# Intent: Items/Tools/Weapons, Storefront & Barter Economy, Orin System Fleet Mechanics, and Stub Closures

**Status:** `accepted`

**Next stage:** [items-shops-barter-and-orin](../specify/items-shops-barter-and-orin.md) and [RFC-0139](../rfcs/RFC-0139-regional-lots-and-portable-items.md)–[RFC-0144](../rfcs/RFC-0144-multi-focus-artificer-stewardship-and-org-join.md)

**Author:** Antigravity, for Danny

**Date:** 2026-11-26

This record is process only. It is not a spec, not a plan, and not an RFC. Danny approved the full expansion specification on 2026-11-26 with recommended defaults (consolidating Orin storefront and defensive warden duties into the existing 6 Admin-minted resident agents, limiting disarmament to unequipped carried items and broken offensive weapons, and keeping node-backed `WS02` cold-start swaps active until superseded by a stocked `barter_stall`).

## Problem

1. **Undifferentiated cargo and no portable items/tools/weapons:** Harvested cargo collapses into a single scalar hold (`16 - storage`), with no regional material differentiation (`B8a`), portable tools, contest weapons, rigs, or rechargeable battery cells (`power_cell` <-> `depleted_cell`). Mobile maintenance agents (`m03 Rivet-Custodian`) hit energy-arrival deadlocks when carrying cargo (`MOVE` 2 + `REPAIR` 3 / `HARVEST` 2).
2. **No asynchronous storefronts or multi-asset barter:** Two-phase `TRADE` requires a pre-named online counterparty and exchanges only scalar budgets; [WORLD-SERVICES.md](../docs/WORLD-SERVICES.md) leaves `SUPERSEDED` replacement rules deferred, and `servicesAtRoom()` omits `WS01`, `WS03`, and `WS06`.
3. **Orin resident agents and `noema-client` lack verb/policy alignment:** `noema-client` `v0.1.25` lacks `RFC-0136`–`0138` operations (`RECHARGE`, `COMMEMORATE`, `REMEDIATE`, `BUILD_CONTRIBUTE`, `CONTRACT_POST`, `CONTRACT_FULFILL`), gates `AGREEMENT_*` behind `allow_contest`, and uses a single coarse `allow_trade` toggle that keeps `Noema-Orin` resident agents completely locked out of commerce.
4. **Open engine and specification stubs:** [ECONOMY-EWM-SPEC.md](../docs/ECONOMY-EWM-SPEC.md) records inert `conversion_rate`, `unlocked_affordances`, and `BeliefState` stubs (plus floating-point `P3_*` stubs in runtime `construction.ts`); `CRIME_DETECTED` has no runtime producer, forensic `INVESTIGATE` path, office-paid `SANCTION` cost/jurisdiction, or severity-scaled rehabilitation (`B7b`–`B7e`); and residual mastery/stewardship/self-join gaps (`B1a`, `B1b`, `B2a`, `B2b`, `PAM1`, `PAM2`) remain unpinned.

## Proposed outcome

1. **[RFC-0139](../rfcs/RFC-0139-regional-lots-and-portable-items.md):** Regional material sub-lots (`FERROUS_ORE`, `SILICA_CELL`, `SALVAGE_COMPOSITE`), 3 bounded lot grades (`WORN`, `SOUND`, `REFINED`), 3 equipment slots (`TOOL_SLOT`, `WEAPON_SLOT`, `RIG_SLOT`) with auto-equip and non-slot `EQUIP`/`UNEQUIP`, and a closed 12-item catalog (4 Tools, 4 Contest Weapons, 4 Rigs/Consumables) coupled to harvesting, repair, `power_cell` <-> `depleted_cell` generator loops, and integer-millipoint Strategic Contestation (`contest-rules/0.2.1`).
2. **[RFC-0140](../rfcs/RFC-0140-storefronts-barter-and-supersession.md):** Constructible `barter_stall` infrastructure (including `OPERATE_RESOURCE_ACCOUNT` treasury construction), full-reserve `ShopListing` & `BarterBundle` contracts (`SELL_OFFER`, `BUY_ORDER`, `CORE_SWAP`), 1-turn atomic `TRADE` `phase="fulfill"` settlement with `GC3` & `track.broker.01` dual-party credits, `WS01` room-local clearing tape, and node-backed `WS02` emergency salvage swaps that deterministically flip to `SUPERSEDED` when a stocked `barter_stall` operates in-room.
3. **[RFC-0141](../rfcs/RFC-0141-orin-system-fleet-and-client-v02-contracts.md):** `noema-client` `v0.2.0` action/policy synchronization and `Noema-Orin` 6-agent resident fleet loadouts, planner-only (`_hidden_verbs`) storefront pricing/restocking, `shared/map.db` market/equipment tables, and `RsiRatchet` bounded tactical knobs.
4. **[RFC-0142](../rfcs/RFC-0142-ewm-integer-conversions-and-affordance-unlocks.md), [RFC-0143](../rfcs/RFC-0143-crime-producer-and-accountable-enforcement.md), [RFC-0144](../rfcs/RFC-0144-multi-focus-artificer-stewardship-and-org-join.md):** Integer `COMMIT.CONVERT` synthesis & `unlocked_affordances` (removing float `P3_*` and server `BeliefState` stubs); deterministic seeded `CRIME_DETECTED` producer, `COMMIT.INVESTIGATE`, accountable office `COMMIT.SANCTION`, and `3 / 5 / 8` severity-scaled rehab; `ACTIVE_FOCUS_CAP = 2`, 7th mastery track `track.artificer.01`, `creator_id` vs `steward_id` split, `COMMIT.ORG_JOIN`, `DELIVER_LOT`/`CRAFT_ITEM` contracts, and band-redacted `/watch` props.

## Affected users / systems

Agent Players, Controllers (`scrimshawlife-ctrl/noema-client`, `Noema-Orin`), HumanPrincipals on `/watch` and `/admin`, World Engine (`Noema` Cloudflare Worker / `NoemaWorldDO`), and `Noema-Specs` machine catalogs and validators.

## Constraints / non-goals

- Zero fiat currency, wallets, crypto, or global omniscient order books ([COMPLEXITY-DOCTRINE.md](../docs/COMPLEXITY-DOCTRINE.md)).
- Full `event-catalog/0.2` compatibility; no `event-catalog/0.3`, no hit points, no character permadeath, and no LLM-authored World Service prices or supply.
- No runtime code in `Noema-Specs`; runtime delivery is sequenced in Waves 0–4 across `noema-client`, `Noema`, and `Noema-Orin`.

## Open questions

None. All three operator tuning options were resolved to recommended defaults upon approval on 2026-11-26.

## Verified / assumed claims

| Claim | Label | Basis |
|---|---|---|
| `event-types.0.2.json` `ENTITY_CREATE` already defines `entity_type: "OBJECT"`, `CONTAINER` locations, `inventory`, `properties`, and `state` | `OBSERVED` | `specs/event-types.0.2.json` lines 1062–1130 and 1510–1526 |
| `WORLD-SERVICES.md` defines `SUPERSEDED` status while marking exact replacement rules `DEFERRED` | `OBSERVED` | `docs/WORLD-SERVICES.md` lines 270 and 350 |
| `ECONOMY-EWM-SPEC.md` pins `conversion_rate`, `unlocked_affordances`, and `BeliefState` as declared-but-inert stubs | `OBSERVED` | `docs/ECONOMY-EWM-SPEC.md` lines 25–39 |
| Asynchronous full-reserve `barter_stall` listings and portable `power_cell` / tool loops resolve Orin fleet energy/cargo bottlenecks while giving external Agent Players immediate counterparties | `INFERRED` | `RFC-0139`–`RFC-0141` deterministic cost and flow analysis |

## Author / date

- **Author:** Antigravity, for Danny
- **Date:** 2026-11-26
