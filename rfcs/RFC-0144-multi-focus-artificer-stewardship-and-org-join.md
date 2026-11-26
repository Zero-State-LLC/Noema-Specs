# RFC-0144: Multi-Focus Cap, Artificer Mastery Track, Creator/Steward Split, Charter Self-Join, Extended Civic Contracts, and Band-Redacted Market/Equipment WATCH

## Status

**Accepted**

Owner approval: Danny, 2026-11-26.  
Intent: [2026-11-26-items-shops-barter-orin-and-stubs](../intent/2026-11-26-items-shops-barter-orin-and-stubs.md). Spec: [items-shops-barter-and-orin](../specify/items-shops-barter-and-orin.md).

Supersedes draft proposals `RFC-PROPOSAL-GC1-FULL-MASTERY-EXTENSION`, `RFC-PROPOSAL-GC1-FAILED-ATTEMPTS-WEIGHTS`, `RFC-PROPOSAL-GC2-CONSTRUCTION-QUANTITIES`, and `RFC-PROPOSAL-GC2-OWNER-STEWARD`.

## Decisions

### 1. Multi-Focus (`ACTIVE_FOCUS_CAP = 2`), Focus Decay Credit, Failed-Attempt Rule & `track.artificer.01`

1. **Multi-Focus & Decay Credit (extends [RFC-0110](RFC-0110-focus-declaration.md) & `GC1-S9`/`S10`):**
   - Each Agent Player may hold up to **`2` active focus tracks** (`ACTIVE_FOCUS_CAP = 2`). Declaring a 3rd track replaces the oldest held focus unless `clear: true` is passed.
   - Active focused tracks become `LATENT` after **`18` idle cycles** (`FOCUSED_LATENT_AFTER_CYCLES = 18` vs `12` unfocused).
2. **7th Derived Mastery Track (`track.artificer.01`):**
   - Added alongside the 6 tracks in [RFC-0138](RFC-0138-ws06-civic-contracts-and-mastery-tracks.md) (`PUBLIC_TITLE_CAP = 1` unchanged):
   - Credit events: distinct `entity_id` crafted (`COMMIT.CRAFT`), upgraded (`BUILD.UPGRADE`), or fulfilled as seller on a `barter_stall` (`TRADE` `phase="fulfill"`).
   - Recognition threshold: `3`. Public title: `"{handle} shapes the Reach's tools."`
   - Maintained benefit: crafted items gain `+10` starting and max `condition` (`STANDARD` `110`, `TEMPERED` `120`) and `COMMIT.REFINE` compute cost `-1` (min `0`).
   - `OFFICE_REQUIRED_TRACKS` adds `"artificer"`, `"archivist"`, and `"herald"` alongside `"engineer"` and `"broker"`.
3. **Failed-But-Legal Practice Rule:**
   - Rejected commands (`BUDGET_EXCEEDED`, `FORBIDDEN`, `INVALID_REQUEST`) grant `0` practice and `0` recognition.
   - A legal `CONTEST_DEFEND` on an unfavorable `CONTEST_RESOLVED` or a `PARTIAL_SUCCESS` contest grants `1` maintenance/practice unit (preventing `LATENT` decay) and `0` recognition units.

### 2. Creator Attribution vs. Active Steward Split (`COMMIT.ASSIGN_STEWARD`)

1. Built `INFRASTRUCTURE` and `OBJECT` entities record immutable `creator_id` (set on `ENTITY_CREATE` for Deep Time attribution) separately from mutable `steward_id` (an Agent Player) and optional `steward_office_id` (an Organization `OfficeRecord`). By default at creation, `steward_id = owner_id`.
2. `COMMIT` `operation: "ASSIGN_STEWARD"` (`cost: { compute: 1 }`): personal `owner_id` or seated `OPERATE_NAMED_ASSET` / `OPERATE_RESOURCE_ACCOUNT` officer assigns `steward_id` or `steward_office_id` via `ENTITY_UPDATE` without mutating `creator_id` or `owner_id`. When an office changes holder via `GC4` succession, stewardship of all assets bound to `steward_office_id` follows the new holder automatically.

### 3. Deterministic `org_id` Allocation & Charter Self-Join (`COMMIT.ORG_JOIN`)

1. Pin `allocateOrgId(name, seq, cycle)` (`org.<slug>.<deterministicSuffix>`) as the sole canonical `org_id` rule across structured and text adapters.
2. Define `COMMIT` `operation: "ORG_JOIN"` (`cost: { compute: 1 }`, `cmd: "join <org_id>"`):
   - Permitted only when target `Organization` is `ACTIVE`, actor is not already a member, actor has no live `institution_memory.danger` edge with that organization, AND either (a) the organization has an active [RFC-0124](RFC-0124-governance-rule-contract.md) governance rule with `admission_mode: "OPEN_CHARTER"` or (b) `player_id` appears in `org.invited_player_ids`.
   - Emits standard `ORG_MEMBER_ADD` (`role: "member"`, `authorized_by` = governing office holder or `org.creator_id`). Unconditional self-join without charter/invite fails closed (`FORBIDDEN`).

### 4. Supply & Fabrication `WS06` Civic Contracts

Extend [RFC-0138](RFC-0138-ws06-civic-contracts-and-mastery-tracks.md) `ContractKind` with two closed barter-coupled contract kinds (`MAX_OPEN_CONTRACTS_PER_ORG = 3` unchanged):
- `"DELIVER_LOT"`: Fulfiller co-located in `contract.room_id` transfers `target_count` (`1..6`) of `target_material` (`FERROUS_ORE` | `SILICA_CELL` | `SALVAGE_COMPOSITE`, `SOUND`+) into the posting org's treasury or `barter_stall` and receives escrowed `storage`, `influence` (`1..3`), `energy` (`2..10`), or an escrowed `power_cell`.
- `"CRAFT_ITEM"`: Fulfiller delivers `1` qualifying `SOUND`+ item of `target_item_archetype` (`condition >= 80`) into the posting org's `barter_stall` or `storage_bay` and receives the escrowed reward.

### 5. Band-Redacted Public `/watch` (`watch-live/1.0`) Extensions

Public rooms on `watch-live/1.0` MAY carry strictly optional, band-redacted fields:
- `market_band?: "stocked" | "sparse" | "empty"` (`>= 3` open fills, `1..2` fills, `0` fills on a public room `barter_stall`; omitted if no stall).
- `crime_band?: "trace" | "detected"` (active public forensic residue or recent `PUBLIC` `CRIME_DETECTED`; hidden rooms never project).
- `occupants[].equipped_categories?: Array<"tool" | "weapon" | "rig">` (category silhouettes only for 3D pawns — never `item_id`, `condition`, or unequipped inventory).
- `room_activity[].verb`: allows `"craft"`, `"barter"`, `"investigate"`, and `"sanction"` with internal-ID redaction and resident-privacy rules unchanged.
