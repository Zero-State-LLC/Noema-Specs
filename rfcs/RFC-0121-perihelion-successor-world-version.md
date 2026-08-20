# RFC-0121 — Perihelion successor world_version

## Status

**Accepted**

Ops / geography identity. No new Player verbs. No reseed of `genesis.ef578f4ffceeccd0`. No production `DEFAULT_WORLD_ID` flip in the landing PR. RFC-0120 unchanged.

## Problem

Live Perihelion Reach is ACTIVE at `genesis.ef578f4ffceeccd0` with a frozen 5-room map. ADR-006's exactly-10 bound applies to chamber-world fixtures and to any **new** hosted `world_version`. Thaw permits a successor; it does not pick the identity. Ad-hoc room injection, production reseed, and force-supersede remain illegal.

## Context

- [ADR-006](../adr/ADR-006-world-bound-exit-visibility-and-location-discovery.md)
- [CHAMBER-MAP.md](../docs/CHAMBER-MAP.md)
- [GENESIS.md](../docs/GENESIS.md)
- [WORLD-OPERATIONS.md](../docs/WORLD-OPERATIONS.md)
- [RFC-0120](RFC-0120-agent-only-player-identity.md)
- Design: [docs/superpowers/specs/2026-08-20-perihelion-successor-world-version-design.md](../docs/superpowers/specs/2026-08-20-perihelion-successor-world-version-design.md)

## Proposed change

### 1. Live world stays

`world.perihelion-reach` / `genesis.ef578f4ffceeccd0` is not edited. After a later human-gated cutover it is operator-only (Admin / Recover / evidence). Public WATCH, CONNECT, STUDY, and PLAY never select it.

### 2. Successor identity

| Field | Value |
|---|---|
| Public name / theme | Perihelion Reach / `perihelion-reach` |
| Profile / story seeds | `FRACTURED_OLD_WORLD` · `OLD_TRADE_NETWORK` + `LOST_ARCHIVE` |
| `world_id` (future `DEFAULT_WORLD_ID`) | `world.perihelion-reach-2` |
| Isolated rehearsal `world_seed` | `perihelion-successor-rehearsal-01` |
| Production `world_seed` | chosen at the later human gate; MUST NOT be `17011984` |
| Cycle 0 graph | exactly the 10 CHAMBER-MAP rooms |

`genesis_id` hashes `world_name`, `world_seed`, `profile_id`, `story_seed_ids`, `theme_id`, `rules_versions`. It does not hash rooms or `world_id`. Reusing `17011984` with the live claim fields is `genesis.ef578f4ffceeccd0` and is refused on the product path.

### 3. Dual-path Cycle 0

1. Frozen first-world claim set (`Perihelion Reach` + `17011984` + `FRACTURED_OLD_WORLD` + those two story seeds + perihelion-reach theme) → legacy 5-room builder.
2. `world_id` omitted → slug from public name. `Perihelion Reach` → `world.perihelion-reach` → legacy.
3. `world_id` is `world.perihelion-reach` or `world-01` → legacy.
4. This campaign's product path: explicit `world_id` MUST be `world.perihelion-reach-2` plus a new `world_seed` → embed CHAMBER-MAP graph, entry `room.civic-exchange`, overlays retargeted (`entity.relay-7` → relay-quarter; `OLD_TRADE_NETWORK` → civic-exchange; `LOST_ARCHIVE` → `room.archive`; infra scar → `room.infrastructure-vault`). Seed entity_id wins on collision. Public room names stay CHAMBER-MAP names.

Refuse: activate `genesis.ef578f4ffceeccd0` on any DO except `world.perihelion-reach`. Refuse product-path hash collision with that genesis_id.

### 4. Admin routing this campaign

`POST /v1/admin/genesis/preview` and `/activate` take optional `world_id`.

- local / test / dev: omitted → `DEFAULT_WORLD_ID`; `world.perihelion-reach-2` → that DO. Store preview and activate on that DO. Pass `x-noema-world-id` so the DO does not bootstrap as the default world. Default DO sequence unchanged.
- production: any `world_id` in the body → `POLICY_DENIED`. Live DO stays `ALREADY_ACTIVATED`. `force` and reseed stay `POLICY_DENIED`.

Activate still requires `confirm: true`. Activate `world_id` MUST equal the stored preview's `world_id`.

Isolated PLAY does not admit `world.perihelion-reach-2`.

### 5. Later cutover (not this landing)

1. Allow production preview of the successor.
2. Record new `genesis_id`, Cycle 0 digest, `room_count: 10`.
3. Human `confirm: true` activate on `world.perihelion-reach-2`. No `force`.
4. Set production `DEFAULT_WORLD_ID=world.perihelion-reach-2` and deploy.
5. `resolvePlayWorld` already maps `world.perihelion*` to the default DO — after the flip that is the successor. Do not add PLAY to the old DO.
6. Admin later gains an exact allowlist `world.perihelion-reach` for overview / lifecycle / Recover.
7. Controllers rebind: same JWTs; first `ENTER_WORLD` on the successor is a new Cycle 0 body at `room.civic-exchange`. No ledger copy.

### 6. Errors

| Code | When |
|---|---|
| `POLICY_DENIED` | production `world_id` override; production `force`; production reseed |
| `ALREADY_ACTIVATED` | activate on frozen `world.perihelion-reach` |
| `INVALID_SEED` | product-path hashes to `genesis.ef578f4ffceeccd0`; that genesis_id on any other DO |
| `CONFIRMATION_REQUIRED` | activate without `confirm: true` |
| `VALIDATION_FAILED` | product path not exactly 10 CHAMBER-MAP rooms |
| `WORLD_FORBIDDEN` | isolated PLAY of `world.perihelion*` |
| `INVALID_REQUEST` | activate `world_id` ≠ preview `world_id`; explicit `world_id` other than `world.perihelion-reach-2` this campaign |

## Alternatives

Grow the rng builder to 10 rooms for every non-frozen seed — rejected (drift from CHAMBER-MAP; omitted `world_id` slugs to the live DO). RFC without a successor genesis path — rejected (cutover would be unproven). Reseed / force-supersede live genesis — rejected. Reuse `world.perihelion-reach` as the successor DO — rejected (`idFromName` is the live world).

## Compatibility

Live `/ready` identity unchanged. Isolated 10-room ADR-006 fixtures unchanged. Agent protocol unchanged. RFC-0120 unchanged.

## Data impact

No production writes. Local successor DO may hold a rehearsal activation. Enrollment rows are not rewritten. Player rows are not copied.

## Research impact

None this landing. A later cutover is a new `world_version` / genesis; trajectories are not comparable across the two worlds.

## Security impact

Production Admin cannot target a second DO this campaign. Isolated PLAY cannot punch `world.perihelion*`. Humans still cannot PLAY.

## Migration

None for the live world. Later cutover is a new section in the runtime Genesis runbook, not a silent env change.

## Validation

- Frozen candidate preview: `genesis.ef578f4ffceeccd0`, 5 rooms.
- Successor preview: `world.perihelion-reach-2`, new genesis_id, 10 CHAMBER-MAP ids, entry `room.civic-exchange`.
- Production-shaped env denies `world_id` override / force / reseed.
- `admitTestWorldId("world.perihelion-reach-2")` denied.
- Specs `validate_all` includes `check_rfc_0121`.

## Rollback

Delete the RFC PR / Worker PR. Live Perihelion is untouched. A local `world.perihelion-reach-2` DO can be abandoned.
