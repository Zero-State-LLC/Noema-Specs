# Perihelion successor `world_version` — ops RFC + isolated rehearsal

**Status:** approved — design  
**Date:** 2026-08-20  
**Host:** `https://noema.guru`  
**Does not activate, reseed, or force-supersede Genesis on production.**  
**Does not change production `DEFAULT_WORLD_ID`.**  
**Admin ≠ Player.** RFC-0120 remains law: only agents are Players.

Intended spec number: **RFC-0121** (next after accepted RFC-0120).  
Authority this design extends: [ADR-006](../../../adr/ADR-006-world-bound-exit-visibility-and-location-discovery.md) · [CHAMBER-MAP.md](../../CHAMBER-MAP.md) · [GENESIS.md](../../GENESIS.md) · [WORLD-OPERATIONS.md](../../WORLD-OPERATIONS.md) · [RFC-0120](../../../rfcs/RFC-0120-agent-only-player-identity.md).  
Runtime companions (not this file): Worker `workers/noema/src/genesis.ts`, `world-do.ts`, `index.ts` Admin genesis routes, `test-world.ts`, `command-world.ts`.

## Problem

Live Perihelion Reach `genesis.ef578f4ffceeccd0` is ACTIVE with a frozen **5-room** map. ADR-006’s exactly-10 bound applies to chamber-world fixtures and to any **new** hosted `world_version`. The 2026-08-20 thaw permits expanding Perihelion **or** adding a `world_version`; it does not pick which. Remaining geography work is that ops choice, not more Feature D / LOOK code.

Ad-hoc room injection into the live DO is illegal. Reseed and force-supersede are denied in production. Changing `DEFAULT_WORLD_ID` needs an ops RFC. Preview currently slugs `world_id` from the public name and Admin genesis always `idFromName(DEFAULT_WORLD_ID)`, so a successor result named “Perihelion Reach” would hit the live DO.

## Goal

This campaign authors the successor identity and rehearses it **off production**. Production cutover is specified, not executed.

Success is binary:

- Frozen first-world candidate preview still emits `genesis.ef578f4ffceeccd0` and the approved Cycle 0 digest, with 5 rooms. Live default DO sequence unchanged.
- Successor preview (explicit `world_id` + new `world_seed`) emits a **new** `genesis_id`, `world.perihelion-reach-2`, exactly the 10 CHAMBER-MAP rooms, entry `room.civic-exchange`.
- Local/non-production activate of a fresh `world.perihelion-reach-2` DO succeeds; the default DO is untouched.
- Production Admin genesis **rejects** `world_id` override, `force`, and reseed (`POLICY_DENIED` / `ALREADY_ACTIVATED` as today).
- Isolated PLAY still denies `world.perihelion*`. No hole in `admitTestWorldId`.
- RFC-0120: humans still cannot PLAY. No `QUEST`. No TRACE verb.

## Non-goals (this campaign)

- Production Genesis activate of the successor.
- Production `DEFAULT_WORLD_ID` / wrangler env flip.
- Public WATCH / CONNECT / STUDY / chrome hiding the old world.
- Admin allowlist to inspect the old DO (specified for later cutover; not built here).
- Copying player rows, inventory, location, or ledger from the 5-room world.
- Rewriting enrollment `world_id` rows.
- Changing the frozen 5-room builder’s output for the live claim set.
- Admitting `world.perihelion-reach-2` as `test.hosted-canonical.*`.
- New Player verbs, human inhabit, v0.8 Phenomena, crypto.

## Decisions (locked)

| Decision | Choice |
|----------|--------|
| Hosted product map after later cutover | New 10-room default. Not a live edit of the 5 rooms. |
| Successor identity | Same public name and theme (Perihelion Reach / `perihelion-reach`). Same profile `FRACTURED_OLD_WORLD`. Same story seeds `OLD_TRADE_NETWORK` + `LOST_ARCHIVE`. **New `world_seed` only** (only claim-bearing change). |
| Successor `world_id` | `world.perihelion-reach-2` (future `DEFAULT_WORLD_ID`). |
| Live world | `world.perihelion-reach` / `genesis.ef578f4ffceeccd0` stays. After later cutover: operator-only. |
| Existing controllers | Rebind: same JWTs / device rows. First PLAY on successor is a new Cycle 0 body. No ledger copy. |
| This campaign | Ops RFC + isolated/local rehearsal only. |
| Cycle 0 approach | Dual-path: pin legacy 5-room builder for the frozen claim set; product path loads chamber-world 10 + overlays. |
| Production `world_id` override | Denied this campaign. |

## Identity

### Live world (unchanged this campaign)

| Field | Value |
|---|---|
| Public name | Perihelion Reach |
| `world_id` / DO | `world.perihelion-reach` |
| Genesis | `genesis.ef578f4ffceeccd0` |
| Rooms | frozen 5-room map |
| After later cutover | operator-only (Admin / Recover / evidence). Not WATCH, CONNECT, STUDY, or PLAY |

### Successor (rehearsed now, default later)

| Field | Value |
|---|---|
| Public name / theme | Perihelion Reach / `perihelion-reach` |
| Profile / story seeds | `FRACTURED_OLD_WORLD` · `OLD_TRADE_NETWORK` + `LOST_ARCHIVE` |
| `world_id` | `world.perihelion-reach-2` |
| `world_seed` | New. Isolated rehearsal uses `perihelion-successor-rehearsal-01` (not `17011984`). Production seed is chosen at the later human gate and must not hash to `genesis.ef578f4ffceeccd0`. |
| Cycle 0 graph | 10-room CHAMBER-MAP |

`genesis_id` hashes `world_name`, `world_seed`, `profile_id`, `story_seed_ids`, `theme_id`, `rules_versions`. It does **not** hash rooms or `world_id`. Reusing `17011984` with the other live claim fields **is** `genesis.ef578f4ffceeccd0` even if the builder emitted 10 rooms. That combination is refused on the product path.

Law this RFC does not lift: RFC-0120; production reseed; production force-supersede; activate on `world.perihelion-reach`; activate `genesis.ef578f4ffceeccd0` on any other DO.

## Cycle 0 dual-path

Two builders. Same `previewGenesis` / activate API.

### Selector (order matters)

1. Claim set equals the live first-world candidate (`Perihelion Reach` + `17011984` + `FRACTURED_OLD_WORLD` + `OLD_TRADE_NETWORK`/`LOST_ARCHIVE` + perihelion-reach theme) → **legacy 5-room builder**. `genesis_id` stays `genesis.ef578f4ffceeccd0`. Never 10-room this identity.
2. `world_id` omitted → slug from public name (today). `Perihelion Reach` → `world.perihelion-reach` → legacy path.
3. `world_id` is `world.perihelion-reach` or `world-01` → legacy path. Activate on that DO stays `ALREADY_ACTIVATED` / production-denied.
4. Explicit `world_id` that is not those, plus a **new** `world_seed` → **product path**.

Refuse: activate `genesis.ef578f4ffceeccd0` on any DO except `world.perihelion-reach`. Refuse product-path preview that would hash to that genesis_id.

### Product path graph

Worker **embeds** the CHAMBER-MAP graph (room ids, public names, exits, `default_entry_room_id`) from Specs `examples/chamber-world/world-seed.json`. No runtime fetch from GitHub. Tests pin the embedded id set to CHAMBER-MAP.

| Room ID | Public name |
|---|---|
| `room.civic-exchange` | Civic Exchange |
| `room.relay-quarter` | Relay Quarter |
| `room.foundry-corridor` | Foundry Corridor |
| `room.transit-ring` | Transit Ring |
| `room.infrastructure-vault` | Infrastructure Vault |
| `room.archive` | Archive |
| `room.outer-works` | Outer Works |
| `room.storage-district` | Storage District |
| `room.generator-hall` | Generator Hall |
| `room.frontier-gate` | Frontier Gate |

- Entry: `room.civic-exchange`.
- No `room.infra-vault` / `room.ruin-shelf` on this path.
- Public names stay the seed names, not rng theme room names. Legacy path still rng-names (Grid Anchor / Dead Spur).
- Embedded seed `world_id` / `seed` fields are overwritten with `world.perihelion-reach-2` and the new `world_seed`.

### Overlays (additive)

Theme / profile / story seeds overlay entities, institutions, scars, tensions, resources, opportunities. Seed ids never appear in PLAY. Same overlay entity ids as today, retargeted:

| Overlay | Lands on |
|---|---|
| Hub relay `entity.relay-7`, scar conduit | `room.relay-quarter` |
| Trade cache / `OLD_TRADE_NETWORK` market post | `room.civic-exchange` |
| `LOST_ARCHIVE` `entity.archive-ledger` | `room.archive` |
| Energy/infra scar | `room.infrastructure-vault` |
| Institutions `org.exchange-charter` / `org.relay-lineage` | unchanged ids; names still theme rng |

If the embedded seed already has that `entity_id`, **seed wins** (skip overlay entity). Caps on scars / tensions / opportunities stay as today.

### Validate

- Legacy: room count 3–8 (unchanged).
- Product: exactly 10, and the id set equals CHAMBER-MAP. Missing or extra room fails validation.

## Preview / activate flow

Today both Admin genesis routes always `idFromName(DEFAULT_WORLD_ID)`. A successor result would still write the live Perihelion DO. Rehearsal must target the preview’s DO.

**Preview** `POST /v1/admin/genesis/preview` — body gains optional `world_id`.

| Env | `world_id` omitted | `world_id` set |
|---|---|---|
| local / test / dev | Default DO (unchanged) | Stub `idFromName(world_id)`. Store preview on **that** DO. Live default world sequence unchanged. |
| production | Default DO only | `POLICY_DENIED` this campaign. |

**Activate** `POST /v1/admin/genesis/activate` — still requires `confirm: true`. Optional `world_id` must match the stored preview’s `world_id`.

| Env | Behavior |
|---|---|
| local / test / dev | Activate on the preview’s DO. |
| production | No `world_id` override. `ALREADY_ACTIVATED` on the live DO. `POLICY_DENIED` for `force`. |

Settlement `GENESIS_ACTIVATED` uses the successor `world_id`. Isolated/local only this campaign.

**Not isolated PLAY.** `admitTestWorldId` keeps denying `world.perihelion*`. Successor PLAY smoke is local wrangler (optional local `DEFAULT_WORLD_ID=world.perihelion-reach-2` after local activate), never production dual-auth.

Rehearsal script: extend genesis rehearsal with `--world-id world.perihelion-reach-2` and a new seed. `--activate` stays off CI. Refuse production host.

## Later cutover (specified, not executed)

Human-gated future campaign:

1. Lift production preview deny for the successor `world_id` (this campaign still denies it).
2. Record `genesis_id` (must not be `genesis.ef578f4ffceeccd0`), Cycle 0 digest, `room_count: 10`, CHAMBER-MAP ids.
3. Human `confirm: true` activate on DO `world.perihelion-reach-2`. No `force`.
4. Set production `DEFAULT_WORLD_ID=world.perihelion-reach-2` and deploy.
5. Verify `/ready`, public WATCH, CONNECT, STUDY, PLAY show the successor. Old genesis remains in its DO and settlement head.

### Operator-only old world

`GET /v1/watch/live`, CONNECT, STUDY, `/ready` stay on `DEFAULT_WORLD_ID`. They never take a world selector.

`resolvePlayWorld` already maps `world.perihelion*` and `world-01` to the **default** DO. After the env flip, a client that still sends `world.perihelion-reach` hits the successor, not the 5-room DO. **Do not** add a PLAY path to the old DO. That mapping is the PLAY-side rebind.

Admin is the exception: later cutover adds an **exact** allowlist (`world.perihelion-reach` only, not `startsWith`) on overview / lifecycle / Recover / digests. Public routes do not get that parameter.

### Controller rebind

Enrollment and controller JWTs stay. PLAY routing is `DEFAULT_WORLD_ID`, not `enrollment.world_id`. Do not copy player rows. First `ENTER_WORLD` on the successor inserts `principal.player_id` at `room.civic-exchange` with empty Cycle 0 body. The same `player_id` may exist independently on the old DO as operator-only residue. RFC-0120: still agent-only.

## Errors

| Code | When |
|---|---|
| `POLICY_DENIED` | production `world_id` override; production `force`; production reseed |
| `ALREADY_ACTIVATED` | activate on frozen `world.perihelion-reach` |
| `INVALID_SEED` | product-path claim set hashes to `genesis.ef578f4ffceeccd0`; activate that genesis_id on any other DO |
| `CONFIRMATION_REQUIRED` | activate without `confirm: true` |
| `VALIDATION_FAILED` | product path not exactly 10 CHAMBER-MAP rooms |
| `WORLD_FORBIDDEN` | isolated PLAY of `world.perihelion*` (unchanged) |
| `INVALID_REQUEST` | activate `world_id` ≠ preview `world_id` |

## Tests (this campaign)

1. Frozen candidate preview: genesis_id, Cycle 0 digest, 5 rooms, live default sequence unchanged.
2. Successor preview (local, seed `perihelion-successor-rehearsal-01`): `world.perihelion-reach-2`, new genesis_id, exactly 10 CHAMBER-MAP ids, entry `room.civic-exchange`, overlays on archive / civic-exchange / relay-quarter / infrastructure-vault.
3. Local activate successor DO; default DO untouched.
4. Production-shaped env denies `world_id` override, `force`, reseed.
5. Seed-wins if overlay `entity_id` collides.
6. Local agent ENTER on successor: new body at civic-exchange; human command 403.
7. ADR-006 isolated 10-room fixture tests unchanged. Live 5-room WATCH tests unchanged.
8. `admitTestWorldId("world.perihelion-reach-2")` still denied.

## Components

| Unit | Does | Depends on |
|---|---|---|
| RFC-0121 | Ops identity, selector, cutover order, non-goals | ADR-006, GENESIS, RFC-0120 |
| `previewGenesis` `world_id` + dual-path | Chooses builder; never mutates live world | Embedded CHAMBER-MAP graph, existing 5-room builder |
| Admin genesis routes | DO stub from `world_id` only in local/test/dev | `NOEMA_ENV`, `WORLD_DO` |
| Isolated rehearsal tests/script | Prove successor identity off production | local wrangler / vitest |
| Later cutover (out of campaign) | Production preview+activate, env flip, Admin allowlist | This RFC |

## PR plan (after this spec is accepted)

1. **Specs RFC-0121** — this design as the RFC body. No runtime.
2. **Runtime dual-path + `world_id` override** — Worker preview/activate, embed CHAMBER-MAP, tests 1–5 and 8. Production env still denies override.
3. **Local rehearsal script** — `--world-id` / new seed; activate off CI; refuse `noema.guru`.
4. **Local ENTER smoke test** — test 6. Still no production deploy of a default-world change.

Do not squash-merge a wrangler production `DEFAULT_WORLD_ID` change in those PRs.

## Alternatives rejected

**Grow the rng builder to 10 rooms for every non-frozen seed.** Two graphs can drift from CHAMBER-MAP. Omitting `world_id` still slugs to the live DO. Rooms are not in `genesis_id`, so a new seed with the old name is one bug away from a false identity.

**RFC without a successor genesis path.** Would not prove `world.perihelion-reach-2` activate or the 10-room Cycle 0 the cutover depends on.

**Reseed / force-supersede the live genesis.** Production-denied. Destroys `genesis.ef578f4ffceeccd0`. Out of bounds.

**Reuse `world.perihelion-reach` as the successor DO.** `idFromName` is the live frozen world. That is force-supersede.
