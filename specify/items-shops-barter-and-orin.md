# Items, Storefronts, Barter Economy, Orin Fleet Contracts & Stub Closures

**Status:** Accepted with [RFC-0139](../rfcs/RFC-0139-regional-lots-and-portable-items.md), [RFC-0140](../rfcs/RFC-0140-storefronts-barter-and-supersession.md), [RFC-0141](../rfcs/RFC-0141-orin-system-fleet-and-client-v02-contracts.md), [RFC-0142](../rfcs/RFC-0142-ewm-integer-conversions-and-affordance-unlocks.md), [RFC-0143](../rfcs/RFC-0143-crime-producer-and-accountable-enforcement.md), and [RFC-0144](../rfcs/RFC-0144-multi-focus-artificer-stewardship-and-org-join.md).  
**Kind:** Multi-subsystem world-rule, client-boundary, and stub-closure specification.  
**Date:** 2026-11-26  
**Intent:** [2026-11-26-items-shops-barter-orin-and-stubs](../intent/2026-11-26-items-shops-barter-orin-and-stubs.md).  
**Version domains:** Preserves `event-catalog/0.2` (32 closed event types). Adds subsystem catalogs [`items-catalog.0.1.json`](../specs/items-catalog.0.1.json), [`shop-catalog.0.1.json`](../specs/shop-catalog.0.1.json), and [`crime-enforcement-catalog.0.1.json`](../specs/crime-enforcement-catalog.0.1.json), plus `contest-rules/0.2.1` additive equipment millipoint rules.

## Workflows

- **SKILL.ORIENT** — grounded in `CONTEXT.md`, [COMPLEXITY-DOCTRINE.md](../docs/COMPLEXITY-DOCTRINE.md), [WORLD-SERVICES.md](../docs/WORLD-SERVICES.md), [CONTEST-RESOLUTION.md](../docs/CONTEST-RESOLUTION.md), and [ECONOMY-EWM-SPEC.md](../docs/ECONOMY-EWM-SPEC.md).
- **SKILL.SPEC_CHANGE** & **SKILL.RFC** — intent-first package spanning `RFC-0139` through `RFC-0144` with machine catalogs and deterministic validator hooks.
- **SKILL.SCHEMA** & **SKILL.DETERMINISM** — pure integer fixed-point quantities and millipoints (`noema-jcs/1`), seeded `SHA256` crime detection draws, and closed `event-catalog/0.2` event payloads.
- **SKILL.GAME_SYSTEM** — couples regional extraction, workshop fabrication, energy battery logistics, strategic contestation, forensic investigation, institutional enforcement, and asynchronous barter storefronts without fiat currency or hit points.
- **SKILL.REVIEW** & **SKILL.VALIDATE** — `bash validation/run.sh`, `python3 tools/check_gc_proposals.py`, and `npx -y @nanonets/graft@0.26.0 --dir graft build --check`.
- **SKILL.HANDOFF_RUNTIME** — 5-wave runtime build order across `scrimshawlife-ctrl/noema-client` (`v0.2.0`), `Zero-State-LLC/Noema`, and `Zero-State-LLC/Noema-Orin`.
- **Existing skills (when installed):** `grill-with-docs`, `to-spec`, `to-tickets`, `code-review`, `google-developer-style`.
- **Owner specialist:** World Engine economy, strategic conflict, and Controller integration.
- **Existing Action:** repository CI (`.github/workflows/ci.yml`); no new workflow required.

## Summary of Normative Scope

1. **Regional Material Lots & Portable Items ([RFC-0139](../rfcs/RFC-0139-regional-lots-and-portable-items.md), [`items-catalog.0.1.json`](../specs/items-catalog.0.1.json)):**
   - Partitions occupied cargo into `FERROUS_ORE`, `SILICA_CELL`, and `SALVAGE_COMPOSITE` across `WORN`, `SOUND`, and `REFINED` grades.
   - Defines 3 equipment slots (`TOOL_SLOT`, `WEAPON_SLOT`, `RIG_SLOT`) with auto-equip on acquisition and non-slot `EQUIP`/`UNEQUIP` preparation (`max 2/cycle`).
   - Pins 12 frontier items (4 Tools, 4 Contest Weapons, 4 Rigs/Consumables) including reusable `power_cell` <-> `depleted_cell` battery cores and `contest-rules/0.2.1` integer millipoint modifiers.
2. **Storefronts, Barter & Supersession ([RFC-0140](../rfcs/RFC-0140-storefronts-barter-and-supersession.md), [`shop-catalog.0.1.json`](../specs/shop-catalog.0.1.json)):**
   - Adds constructible `barter_stall` infrastructure (personal or `OPERATE_RESOURCE_ACCOUNT` treasury-built), full-reserve `ShopListing`s (`SELL_OFFER`, `BUY_ORDER`, `CORE_SWAP`), and 1-turn atomic `TRADE` `phase="fulfill"` settlement.
   - Completes `WS01`–`WS06` room presence, `WS01` room-local clearing tape, and node-backed `WS02` emergency salvage swaps that deterministically transition to `SUPERSEDED` when a stocked `barter_stall` operates in-room.
3. **Orin Resident Fleet & `noema-client` `v0.2.0` ([RFC-0141](../rfcs/RFC-0141-orin-system-fleet-and-client-v02-contracts.md)):**
   - Synchronizes `noema-client` action validation and granular `ClientPolicy` flags across `RFC-0136`–`0144`.
   - Equips the 6 `Noema-Orin` resident roles (`m01`–`m06`) with deterministic planner-only (`_hidden_verbs`) storefront pricing, battery core recycling, tool fabrication, contract posting, and defensive contest/sanction patrols.
4. **EWM Conversions, Crime Producer & Residual GC Closures ([RFC-0142](../rfcs/RFC-0142-ewm-integer-conversions-and-affordance-unlocks.md), [RFC-0143](../rfcs/RFC-0143-crime-producer-and-accountable-enforcement.md), [RFC-0144](../rfcs/RFC-0144-multi-focus-artificer-stewardship-and-org-join.md), [`crime-enforcement-catalog.0.1.json`](../specs/crime-enforcement-catalog.0.1.json)):**
   - Replaces float `P3_*` and server `BeliefState` stubs with integer `COMMIT.CONVERT` and deterministic `unlocked_affordances`.
   - Pins seeded `CRIME_DETECTED` detection, `COMMIT.INVESTIGATE`, office-paid `COMMIT.SANCTION`, and `3 / 5 / 8` severity-scaled rehabilitation.
   - Pins `ACTIVE_FOCUS_CAP = 2`, 7th mastery track `track.artificer.01`, `creator_id` vs `steward_id` split, `COMMIT.ORG_JOIN`, `DELIVER_LOT` / `CRAFT_ITEM` civic contracts, and band-redacted `/watch` indicators.
