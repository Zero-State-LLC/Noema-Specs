# RFC-0141: `Noema-Orin` Resident System Fleet Mechanics and Official Client `v0.2.0` Alignment

## Status

**Accepted**

Owner approval: Danny, 2026-11-26.  
Intent: [2026-11-26-items-shops-barter-orin-and-stubs](../intent/2026-11-26-items-shops-barter-orin-and-stubs.md). Spec: [items-shops-barter-and-orin](../specify/items-shops-barter-and-orin.md).

## Problem

1. Official client `scrimshawlife-ctrl/noema-client` (`v0.1.25`) omits [RFC-0136](RFC-0136-generator-recharge-and-deeptime-watch-projection.md)–[RFC-0138](RFC-0138-ws06-civic-contracts-and-mastery-tracks.md) operations (`RECHARGE`, `COMMEMORATE`, `REMEDIATE`, `BUILD_CONTRIBUTE`, `CONTRACT_POST`, `CONTRACT_FULFILL`), couples `AGREEMENT_*` to `allow_contest`, and collapses all commerce behind one `allow_trade` boolean.
2. On `Noema-Orin`, `DENY_ALWAYS` blocks all `TRADE`, `AGREEMENT_*`, and `CONTEST_DEFEND` actions across the 6 resident system roles (`m01`–`m06`), leaving external Agent Players with no live shopkeeper, civic contract issuer, or warden in `world.perihelion-reach-3`.

## Decisions

### 1. Official Client `v0.2.0` Action Validation & Decoupled `ClientPolicy`

1. **Action Routing (`noema_client/actions.py`):**
   - Direct commands (`_DIRECT`): add `RECHARGE` (`mutating=True`, resolving visible generator `entity_id` or carried `depleted_cell`).
   - Build operations (`_BUILD`): add `BUILD_CONTRIBUTE`.
   - Commit operations (`_COMMIT`): add `COMMEMORATE`, `REMEDIATE`, `CONTRACT_POST`, `CONTRACT_FULFILL`, `CRAFT`, `REFINE`, `EQUIP`, `UNEQUIP`, `USE_ITEM`, `SCRAP_ITEM`, `CONVERT`, `INVESTIGATE`, `SANCTION`, `ASSIGN_STEWARD`, and `ORG_JOIN`.
   - Carried-item target resolution: `EQUIP`, `UNEQUIP`, `USE_ITEM`, `SCRAP_ITEM`, and item `REPAIR` resolve targets against `obs.inventory` / `obs.equipment` in addition to room entities.
   - `TRADE` phases: validate `propose`, `accept`, `reject`, `cancel`, `stock`, `withdraw`, `list`, `unlist`, and `fulfill`.
2. **Granular `ClientPolicy` Flags (`noema_client/policy.py`):**
   - Introduce `allow_trade_p2p`, `allow_shop_fulfill`, `allow_shop_manage`, `allow_agreement` (`AGREEMENT_*`, `CONTRACT_*`), `allow_contest_defend`, `allow_contest_declare`, and `allow_items`, preserving legacy `allow_trade` and `allow_contest` kwargs as backward-compatible defaults.

### 2. Consolidated 6-Unit `Noema-Orin` Resident Fleet Architecture

All capabilities attach to in-world offices, items, and budgets — **zero out-of-game system privileges** ([RFC-0120](RFC-0120-agent-only-player-identity.md), [RFC-0133](RFC-0133-quartermaster-treasury-services.md)). Storefront and warden duties consolidate into the **existing 6 Admin-minted handles** (`m01`–`m06`):

1. **Planner-Only Economic & Enforcement Guards (`_hidden_verbs`):**
   - `TRADE` (`stock`, `withdraw`, `list`, `unlist`), `CONTRACT_POST`, `SUPPLY`, and `SANCTION` MUST remain in `_hidden_verbs()` (hidden from LLM index selection and generic fallbacks), executed solely by deterministic planner functions with bounded scarcity formulas so small models cannot hallucinate giveaway trades or unprovoked sanctions.
2. **Role Loadouts & Deterministic Playbooks:**
   - `m01 Aphelia-Founder` (`signal_transceiver` + `aegis_baffle`): publishes `OPEN_CHARTER` governance rule ([RFC-0144](RFC-0144-multi-focus-artificer-stewardship-and-org-join.md)), maintains `1..2` escrowed `WS06` contracts (`REPAIR_TARGET`, `DELIVER_LOT`, `ATTEST_ROOM`) at `room.civic-exchange`, `COMMEMORATE`s crystallized lore, and forms `NON_AGGRESSION`/`MUTUAL_DEFENSE` agreements.
   - `m02 Tallow-Quartermaster` (`plasma_cutter` + `cargo_rig`, `OPERATE_RESOURCE_ACCOUNT`): constructs and operates the Reach Compact `barter_stall` at `room.civic-exchange`; maintains deterministic `CORE_SWAP` (`1 power_cell <- 1 depleted_cell + 1..2 SILICA_CELL`), `SELL_OFFER` (tools & fresh `power_cell`s), and `BUY_ORDER` (`6 energy <- 3 FERROUS_ORE | SALVAGE_COMPOSITE`) listings; recycles `depleted_cell` cores at `room.generator-hall`; `SUPPLY`s needy cohort peers.
   - `m03 Rivet-Custodian` (`arc_welder` + `cargo_rig`, `OPERATE_NAMED_ASSET`, `focus: ["engineer", "artificer"]`): fabricates tools, rigs, and `power_cell`s at `workshop` whenever cohort loadouts or `barter_stall` reserves drop below floor; performs `REPAIR`/`overhaul`, `BUILD_CONTRIBUTE`, and pre-fossilization `REMEDIATE`.
   - `m04 Vellum-Archivist` (`chrono_lens` + defensive `cipher_spike`, `ACCESS_RESTRICTED_ARCHIVE`, `focus: ["archivist", "surveyor"]`): executes `INVESTIGATE` on crime scenes ([RFC-0143](RFC-0143-crime-producer-and-accountable-enforcement.md)), defends public `ARTIFACT`s via `CONTEST_DEFEND`, publishes multi-controller reconstructions, and `COMMEMORATE`s fossilized scars.
   - `m05 Cantor-Speaker` (`signal_transceiver`, `PUBLISH_NOTICE`, `focus: ["herald"]`): broadcasts grounded `(observed at seq N)` `TRADE_NOTICE` and `BOARD` digests of active `barter_stall` stock and open `WS06` contracts across hub/gate rooms.
   - `m06 Perigee-Surveyor` (`plasma_cutter` + `arc_lance` + `aegis_baffle`, `focus: ["explorer", "surveyor"]`): maps room lots, stall listings, and open contests into `shared/map.db`; harvests edge `SALVAGE_COMPOSITE`; acts as defensive warden via `CONTEST_DEFEND` and evidence-backed `SANCTION` when Compact assets are attacked (`allow_contest_declare=False`, `allow_contest_defend=True`).
   - Operator tier `reach-maint3` remains strictly restricted to `ENTER/LOOK/INSPECT/WAIT/HARVEST` (`MOVE` and `TRADE` denied).

### 3. Controller-Local Memory & RSI Ratchet Bounds

- `shared/map.db` adds controller-local tables `shop_stalls`, `shop_listings`, and `equipment_state` populated strictly from agent observations (`AGENT-HARNESS` §21).
- `RsiRatchet` adds bounded knobs `tool_repair_floor` (`10..50`, default `25`), `battery_reserve_target` (`0..3`, default `1`), and `shop_margin_bias` (`-1..2`, default `0`), plus automatic canary rollback if `unequipped_broken_tool_turns >= 12`.

## Security & Privacy Invariants

- System-actor tokens (`issued_by=admin`) remain excluded from external live-agent censuses and never count toward Gate `PSR-1` independent-operator cohorts.
- Private `persona.json`, `policy_knobs.json`, and `mind/memory.db` remain strictly off-wire (`ADR-0002`).
