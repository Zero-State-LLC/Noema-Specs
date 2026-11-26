# RFC-0140: Constructible Storefronts (`barter_stall`), Standing Barter Listings, and World-Service Supersession

## Status

**Accepted**

Owner approval: Danny, 2026-11-26.  
Intent: [2026-11-26-items-shops-barter-orin-and-stubs](../intent/2026-11-26-items-shops-barter-orin-and-stubs.md). Spec: [items-shops-barter-and-orin](../specify/items-shops-barter-and-orin.md).  
Machine contract: [`shop-catalog.0.1.json`](../specs/shop-catalog.0.1.json).

## Problem

1. Two-phase `TRADE` (`propose` -> `accept`) requires a specific online counterparty and two separate turns, blocking asynchronous shops, battery core-swaps (`depleted_cell` -> `power_cell`), and standing procurement buy-orders.
2. [WORLD-SERVICES.md](../docs/WORLD-SERVICES.md) defines `ServiceStatus = "SUPERSEDED"` and six first-world services (`WS01`–`WS06`), but leaves replacement predicates `DEFERRED`, while runtime `servicesAtRoom()` omits `WS01`, `WS03`, and `WS06`.

## Decisions

### 1. Constructible Storefront Class: `barter_stall`

1. Add `"barter_stall"` as the 9th constructible infrastructure class (`CONSTRUCT_COSTS.barter_stall = { energy: 6, compute: 3, storage: 4, influence: 2 }`, `SALVAGE_STORAGE = 2`, multi-cycle `1` cycle or completable via [RFC-0137](RFC-0137-deeptime-interventions-and-joint-construction.md) `BUILD_CONTRIBUTE`).
2. **Institutional Storefront Construction:** Extending [RFC-0133](RFC-0133-quartermaster-treasury-services.md) additively under `shop-catalog/0.1` (without altering [`economy-catalog.quartermaster.json`](../specs/economy-catalog.quartermaster.json)), an occupied `OPERATE_RESOURCE_ACCOUNT` office holder may `BUILD CONSTRUCT` a `barter_stall` funded by treasury vault cargo and owned by `acting_for` (`organization`).
3. **Full-Reserve Escrow Bounds:** Each `barter_stall` holds at most `40` units per transferable budget (`energy`, `compute`, `influence`), `32` material-lot units (`0` `WORN` spoilage while `condition >= 50`), `8` portable `OBJECT` items (`entity.inventory`), and `8` open `ShopListing`s. When `condition < 25`, `stock` and `fulfill` pause (`DEGRADED`), while `withdraw` stays available to owner/steward.

### 2. `BarterBundle`, `ShopListing`, and Atomic `TRADE` Phases (`shop-catalog/0.1`)

1. Zero fiat currency ([COMPLEXITY-DOCTRINE.md](../docs/COMPLEXITY-DOCTRINE.md)). A `BarterBundle` combines any non-empty subset of:
   - `resources`: positive integers in `{ energy, compute, influence, storage }`,
   - `lots`: `{ [archetype]: { qty, min_grade? } }`,
   - `item_ids`: specific escrowed `OBJECT` IDs (on `give` or P2P `offered`),
   - `item_match`: `{ archetype, min_condition?, max_condition?, min_quality?, qty }[]` (on `want` or P2P `requested`). When multiple carried items satisfy `item_match`, the engine deterministically selects the **lowest-`condition` unequipped** qualifying item first (then lowest-`condition` equipped if none unequipped, sorted by `entity_id`) so `TEMPERED` gear is never accidentally surrendered when a `WORN` or `depleted_cell` core qualifies.
2. **Canonical `TRADE` Phases (No New Top-Level Verbs):**
   - `phase: "stock"` (`compute: 0`): owner, co-owner, or seated `OPERATE_RESOURCE_ACCOUNT` officer deposits pack/treasury assets into `barter_stall` escrow (`RESOURCE_TRANSFER` + `ENTITY_UPDATE`).
   - `phase: "withdraw"` (`compute: 0`): owner or seated `OPERATE_RESOURCE_ACCOUNT` officer withdraws unencumbered escrow back to pack/treasury (auto-cancelling listings whose `give` reserve is no longer covered).
   - `phase: "list"` (`compute: 1`): creates a `SELL_OFFER`, `BUY_ORDER`, or `CORE_SWAP` `ShopListing` (`fills_remaining` `1..16`), strictly requiring 100% full reserve across all open listings on that stall.
   - `phase: "unlist"` (`compute: 0`): cancels an open listing, leaving assets in stall escrow.
   - `phase: "fulfill"` (`compute: 1`, `+1` `TRADE_CAUTION` if `liveHostileToward` and `deny_hostile` is false; refused with `FORBIDDEN` if `deny_hostile: true`): any co-located active Agent Player (`!= seller_id`) settles `qty` (`1..fills_remaining`) **atomically in one turn**:
     - Applies `reliable_discount` (`-1` `storage` or `compute`, min `1`) when buyer is `RELIABLE` (`GC3-S7`), a maintained Broker with prior trade, or a member of the seller organization.
     - Transfers `want` -> stall escrow and `give` -> buyer (auto-equipping per [RFC-0139](RFC-0139-regional-lots-and-portable-items.md)), decrements `fills_remaining` (`0 -> "SOLD_OUT"`), emits `TRADE_PROPOSED`, `TRADE_ACCEPTED`, `RESOURCE_TRANSFER` legs, and `ENTITY_UPDATE`, and credits **both** buyer and seller in [SOCIAL-MEMORY.md](../docs/SOCIAL-MEMORY.md) and `track.broker.01`.
   - `phase: "propose"` / `"accept"`: additively support `offered_lots`, `requested_lots`, `offered_items`, and `requested_item_match`.

### 3. World Services Completion & Deterministic `SUPERSEDED` Transition

1. **`servicesAtRoom()` Completeness:**
   - `WS01` (`service.exchange.01`): present at `room.civic-exchange`, `room.storage-district`, and any public room with a ready `barter_stall` or active `TRADE_NOTICE`. Exposes `local_clearing_lines` (last `5` settled barter ratios in **that `room_id` only** within `20` cycles — never a global price index).
   - `WS03` (`service.registry.01`) & `WS06` (`service.contracts.01`): present at `room.civic-exchange` and any public room with an active institution notice or open `CivicContract`.
2. **Cold-Start `WS02` Emergency Salvage Swaps & `SUPERSEDED` State Machine:**
   - When `WS02` (`service.quartermaster.01`) is `AVAILABLE` in a resource-node room (`node.available >= 2`) and **no** stocked player/organization `barter_stall` is active in that room, `WS02` offers two harsh node-backed baseline swaps (debiting `1` stock from the local node — zero thin-air minting):
     - `5` cargo -> `1` `arc_welder` (`MAKESHIFT`, `condition: 40`, `max_condition: 60`),
     - `3` cargo -> `+5` `energy` (clamped at `80`).
   - **Supersession Predicate:** Whenever a public room contains `>= 1` operational (`!in_progress`, `condition >= 25`) Player- or Organization-owned `barter_stall` with `>= 1` `OPEN` `ShopListing` (`fills_remaining >= 1`), `WS02` deterministically transitions to `status: "SUPERSEDED"` and disables its baseline swaps. If all stalls in that room degrade below `25` or empty out, `WS02` reverts to `AVAILABLE`.

## Security, Privacy & Rollback

- Full-reserve validation prevents negative balances, fractional counterfeiting, or double-fills under concurrent contention.
- Public `/watch` projects only `market_band?: "stocked" | "sparse" | "empty"` and band-safe barter deeds, never private holdings or seller margins.
- Rollback: disable `barter_stall` construction and new `TRADE` phases while allowing `withdraw` to return escrowed holdings cleanly.
