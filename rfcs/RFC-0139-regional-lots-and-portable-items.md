# RFC-0139: Regional Material Sub-Lots, Portable Items, Tools, Rigs, and Strategic Contest Weapons

## Status

**Accepted**

Owner approval: Danny, 2026-11-26.  
Intent: [2026-11-26-items-shops-barter-orin-and-stubs](../intent/2026-11-26-items-shops-barter-orin-and-stubs.md). Spec: [items-shops-barter-and-orin](../specify/items-shops-barter-and-orin.md).  
Machine contract: [`items-catalog.0.1.json`](../specs/items-catalog.0.1.json).

## Problem

1. Harvested cargo in [RESOURCE-ECONOMY.md](../docs/RESOURCE-ECONOMY.md) and [RFC-0045](RFC-0045-lot-quality.md) collapses into a single undifferentiated hold count (`16 - storage`), leaving `B8a` lot-grade residuals open and giving Perihelion Reach's 10 rooms no material supply-chain interdependence.
2. Agent Players have no portable tools, rigs, battery packs, or strategic contest arms: [RFC-0050](RFC-0050-workshop.md) `workshop` entities grant only a `-1` storage discount rather than fabricating durable equipment, and mobile maintenance agents suffer chronic energy/cargo deadlocks (`MOVE` 2 + `REPAIR` 3 or `HARVEST` 2).

## Decisions

### 1. Regional Material Archetypes & 3-Tier Lot Grades (`economy-catalog/gc8-s5`)

1. Personal pack capacity remains governed by integer `budgets.storage` (default free capacity `16`, occupied hold `effective_cap - budgets.storage`).
2. Occupied cargo is partitioned into **three regional material archetypes** derived deterministically from the harvested node's `room_id` (with untyped legacy cargo defaulting to `SALVAGE_COMPOSITE`):
   - `FERROUS_ORE`: `room.foundry-corridor`, `room.infrastructure-vault`.
   - `SILICA_CELL`: `room.generator-hall`, `room.relay-quarter`, `room.archive`.
   - `SALVAGE_COMPOSITE`: `room.outer-works`, `room.storage-district`, `room.frontier-gate`, `room.civic-exchange`, plus any `DISMANTLE` or `SCRAP_ITEM` salvage. `SALVAGE_COMPOSITE` may substitute for missing `FERROUS_ORE` or `SILICA_CELL` in generic `REPAIR`/`CONSTRUCT` at `+1` extra unit, never in specialized `CRAFT` recipes.
3. **Closed Lot Grades (`WORN` | `SOUND` | `REFINED`):**
   - `WORN`: harvested when node `condition < 50`; spoils `1` unit/cycle in personal pack (`0` spoilage while stored inside an operational `storage_bay` or `barter_stall` with `condition >= 50`); crafted items start at `condition = 70`.
   - `SOUND`: harvested when `50 <= condition < 85`, or upgraded from `WORN` via `stabilizer_kit`; never spoils; crafted items start at `condition = 100`.
   - `REFINED`: produced via `COMMIT` `operation: "REFINE"` (`2 SOUND -> 1 REFINED` of same archetype at a ready `workshop`, cost `{ energy: 2, compute: 1 }`), or harvested at `condition >= 85` while equipping `plasma_cutter`; reduces `CONSTRUCT`/`UPGRADE` cargo cost by `1` (min `1`); items crafted solely from `REFINED` lots receive `quality: "TEMPERED"` (`condition = 120`, `max_condition = 120`).

### 2. Portable Item Entities & Equipment Slots (`event-catalog/0.2` Compatible)

1. Portable items are canonical `OBJECT` entities emitted via existing `ENTITY_CREATE`, `ENTITY_UPDATE`, and `ENTITY_DESTROY` payloads in [`event-types.0.2.json`](../specs/event-types.0.2.json):
   - Carried by an Agent Player: `location: { kind: "CONTAINER", container_entity_id: player_id }`, `owner_id: player_id`.
   - Escrowed in a `barter_stall` or `storage_bay`: `location: { kind: "CONTAINER", container_entity_id: entity_id }`.
   - Dropped in a room: `location: { kind: "ROOM", room_id }`.
2. **Bulk & Three Equipment Slots (`TOOL_SLOT`, `WEAPON_SLOT`, `RIG_SLOT`):**
   - Unequipped carried items occupy `bulk` (`1..3`) hold units; equipping reduces hold occupancy to `equipped_bulk = max(1, bulk - 1)`.
   - **Auto-Equip:** Acquiring an item via `CRAFT`, `TRADE` `accept`, or `TRADE` `fulfill` automatically equips it if the corresponding `equip_slot` is empty (unless `auto_equip: false`).
   - **Non-Slot Prep (`COMMIT.EQUIP` / `COMMIT.UNEQUIP`):** Costs `{}` (`0` energy, `0` compute) and does **not** consume the cycle's mutating tempo slot (`max 2` swaps per Player per cycle).
3. **Durability, Breakage & Deep Time Provenance:**
   - Item `condition` is an integer in `0..120`. At `condition == 0`, the item becomes `BROKEN` (bonuses inactive) and is **never silently deleted**.
   - A `BROKEN` or worn item may be repaired at a ready `workshop` via `COMMIT.REPAIR` (`target: item_id`, cost `1` matching material lot + `{ energy: 2, compute: 1 }`, restoring `+35` condition up to `max_condition`) or recycled via `COMMIT.SCRAP_ITEM` (`cost: { energy: 1 }`, emitting `ENTITY_DESTROY` and crediting `1 SALVAGE_COMPOSITE`).
   - Items retain `maker_id`, public `origin_room_id` (withheld if hidden), `forged_cycle`, and `contest_veterancy`; surviving `>= 5` contests or `>= 15` repairs sets `notable_history: true` for archival `INSPECT`/`ATTEST`.

### 3. Closed 12-Item Catalog (`items-catalog/0.1`)

Fabricated via `COMMIT` `operation: "CRAFT"` (`cmd: "craft <archetype>"`) at a ready (`!in_progress`, `condition >= 25`) `workshop` (`cipher_spike` additionally requires `archive_annex`; `power_cell` may also be crafted at a ready `generator`). Exact parameters are pinned in [`items-catalog.0.1.json`](../specs/items-catalog.0.1.json):

1. **Tools (`TOOL_SLOT`):**
   - `arc_welder`: `2 FERROUS_ORE + 1 SILICA_CELL`, `{ energy: 4, compute: 2 }`. `REPAIR`/`RESTORE` energy `-1` (`3 -> 2`), condition delta `+10`, enables repairing `condition == 0` non-scarred infrastructure; wear `-4`.
   - `plasma_cutter`: `2 FERROUS_ORE + 2 SALVAGE_COMPOSITE`, `{ energy: 5, compute: 2 }`. `HARVEST` energy `-1` (`2 -> 1`), `+2` bonus stock yield without extra `harvest_pressure`, `REFINED` harvest on `condition >= 85` nodes, `DISMANTLE` energy `-2` & `+1` salvage; wear `-3`.
   - `chrono_lens`: `2 SILICA_CELL + 1 SALVAGE_COMPOSITE`, `{ energy: 3, compute: 3 }`. `INSPECT`/`ATTEST`/`RECONSTRUCT` attention `-1` (min `0` known, min `1` new), `+0.15` `reconstructionFidelity` (integer `150` millipoints), unlocks `COMMIT.INVESTIGATE`; wear `-2`.
   - `signal_transceiver`: `2 SILICA_CELL + 1 FERROUS_ORE`, `{ energy: 3, compute: 3 }`. Waives `GC5-S1` 1-cycle long-range `MESSAGE` delay when relay is `25..49`, permits emergency long-range send at relay `10..24` (`+1` energy), extends `BOARD`/`TRADE_NOTICE` expiry `+4` cycles; wear `-2`.
2. **Weapons (`WEAPON_SLOT` — Coupled to [CONTEST-RESOLUTION.md](../docs/CONTEST-RESOLUTION.md), Zero HP):**
   - `breach_charge`: `2 FERROUS_ORE + 2 SILICA_CELL`, `{ energy: 5, compute: 2, influence: 1 }`. `+140` declarer millipoints on `INFRASTRUCTURE_DISRUPTION` / `ACCESS_CONTEST`, `+10` `max_condition_delta` or `+2` restriction cycles on `SUCCESS`, `+250` crime `detection_mp`, `-50` wear on resolve.
   - `grapnel_array`: `2 FERROUS_ORE + 2 SALVAGE_COMPOSITE`, `{ energy: 4, compute: 2 }`. `+110` declarer millipoints on `RESOURCE_SEIZURE`, `max_seizure_amount` `5 -> 8`; on `SUCCESS` with margin `>= 100` mp (and target lacks `aegis_baffle`), seizes `1` **unequipped** carried item when target holds `0` liquid cargo; `+150` `detection_mp`, `-15` wear.
   - `arc_lance`: `2 FERROUS_ORE + 2 SILICA_CELL`, `{ energy: 5, compute: 3 }`. `+90` declarer millipoints on `PRESENCE_PRESSURE` (displacement + `2`-cycle action lock on `SUCCESS`), `+120` defender millipoints on `CONTEST_DEFEND` (any form), `-1` influence cost on `COMMIT.SANCTION`; `+100` `detection_mp` if unauthorized, `-10` wear.
   - `cipher_spike`: `3 SILICA_CELL` (requires `archive_annex`), `{ energy: 3, compute: 4 }`. `+125` declarer millipoints (`+4` seal cycles) or `+110` defender millipoints on `INFORMATION_CONTEST`; `+120` `detection_mp`, `-15` wear.
3. **Rigs & Consumables (`RIG_SLOT` / `COMMIT.USE_ITEM`):**
   - `cargo_rig` (`RIG_SLOT`): `2 FERROUS_ORE + 2 SALVAGE_COMPOSITE`, `{ energy: 4, compute: 2 }`. Personal storage capacity `+6` (`16 -> 22`) and waives `+1` cargo `MOVE` energy surcharge; wear `-1` per cargo `MOVE`.
   - `aegis_baffle` (`RIG_SLOT`): `2 FERROUS_ORE + 2 SILICA_CELL`, `{ energy: 5, compute: 3 }`. Passive `+100` defense millipoints when wearer or co-located stewarded entity is contested; halves `RESOURCE_SEIZURE` loss (`ceil(amt / 2)`) and blocks item seizure/disarm; wear `-12` when triggered.
   - `power_cell` (`CONSUMABLE`): `1 SILICA_CELL + 1 SALVAGE_COMPOSITE`, `{ energy: 4, compute: 1 }`. `COMMIT.USE_ITEM` grants `+12` `energy` (clamped at `80`, `0` cooldown) and updates item in-place to `depleted_cell` (`condition: 0`). Extending [RFC-0136](RFC-0136-generator-recharge-and-deeptime-watch-projection.md), `RECHARGE` at an operational `generator` may target a carried `depleted_cell` to restore it to `power_cell` (`condition: 100`, generator wear `-3`).
   - `stabilizer_kit` (`CONSUMABLE`): `2 SALVAGE_COMPOSITE + 1 SILICA_CELL`, `{ energy: 3, compute: 2 }`. `COMMIT.USE_ITEM` upgrades carried `WORN` lots to `SOUND` or reduces un-fossilized room economic scar strength by `0.50` (`harvest_pressure` `-4`, preserving [RFC-0051](RFC-0051-irreversible-scar.md) dismantle ruins untouched); consumed via `ENTITY_DESTROY`.

### 4. Contest Resolution Equipment Extension (`contest-rules/0.2.1`)

1. Net contest score adds `declarer_weapon_mp` and subtracts `(defender_weapon_mp + defender_rig_mp)` using pure integer millipoints (`+15` mp bonus while `TEMPERED` `condition > 100`; `floor(mp * 7 / 10)` for `MAKESHIFT`). When neither party equips items, `0.2.1` reduces identically to `contest-rules/0.2.0`.
2. **Bounded Disarm Scope:** Equipped work tools (`TOOL_SLOT`) are **never** stripped by contests. Only unequipped carried items (under `grapnel_array` margin `>= 100` mp without `aegis_baffle`) may be seized, and an offensive declarer whose equipped weapon reaches `condition == 0` during a failed contest (`score <= -150` against active `CONTEST_DEFEND`, double wear) drops that broken weapon to `{ kind: "ROOM", room_id }`.

## Security, Determinism & Rollback

- All IDs (`item.<slug>.<hash>`) use deterministic committed-fact hashing; no floating-point balances or unseeded RNG.
- Rollback: disable `CRAFT`/`REFINE`/`EQUIP`/`USE_ITEM`/`SCRAP_ITEM` affordances; existing `OBJECT` entities remain benign inspectable props and `contest-rules/0.2.0` arithmetic applies when equipment modifiers are zeroed.
