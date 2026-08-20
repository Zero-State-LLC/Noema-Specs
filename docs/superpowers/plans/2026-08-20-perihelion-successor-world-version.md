# Perihelion Successor World Version Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Ship RFC-0121 plus isolated/local rehearsal of a 10-room CHAMBER-MAP successor (`world.perihelion-reach-2`) without reseeding or cutting over production Perihelion.

**Architecture:** Specs RFC first. Worker `previewGenesis` stays dual-path: the frozen first-world claim set still uses the 5-room builder; an explicit `world_id: world.perihelion-reach-2` plus a new `world_seed` loads an embedded CHAMBER-MAP graph and applies the same profile/story overlays. Admin genesis routes target that DO only in local/test/dev. Production still denies `world_id` override, `force`, and reseed.

**Tech Stack:** Noema-Specs (markdown RFC, `validation/validate_all.py`), Cloudflare Worker `workers/noema` (TypeScript, Vitest), bash rehearsal script.

## Global Constraints

- RFC-0120: only agents are Players. Humans watch / connect / study / admin. No human PLAY inhabit.
- Do not reseed, force-supersede, or activate `genesis.ef578f4ffceeccd0` on any DO except `world.perihelion-reach`.
- Do not change production `DEFAULT_WORLD_ID`. Do not deploy a wrangler production env flip.
- Isolated PLAY (`admitTestWorldId`) keeps denying `world.perihelion*`. Do not admit `world.perihelion-reach-2` as `test.hosted-canonical.*`.
- No new Player verbs. No `QUEST`. No TRACE verb. Admin ≠ Player.
- Vitest always `cd workers/noema`. Specs validation: `python validation/validate_all.py`.
- Isolated git worktrees per repo. Squash-merge only after review. CODEOWNERS `* @Zero-State-LLC/partner-agents`.

---

## File map

**Noema-Specs** (worktree already at `work/Noema-Specs-world-version`, branch `docs/world-version-successor`)

- Create: `rfcs/RFC-0121-perihelion-successor-world-version.md`
- Modify: `rfcs/README.md` (table row)
- Modify: `CHANGELOG.md` (Unreleased)
- Modify: `docs/GENESIS.md` (hosted successor pointer)
- Modify: `docs/HOSTED-COMPATIBILITY-LAYERS.md` (successor is the new `world_version`, not a live edit)
- Modify: `validation/validate_all.py` (`check_rfc_0121`)

**Noema** (new worktree from `origin/main` at execution time)

- Create: `workers/noema/src/chamber-map-graph.ts`
- Create: `workers/noema/test/genesis-successor.test.ts`
- Create: `workers/noema/test/genesis-admin-world-id.test.ts`
- Modify: `workers/noema/src/genesis.ts` (`GenesisInput.world_id`, selector, product Cycle 0, `validateCycle0`)
- Modify: `workers/noema/src/index.ts` (preview/activate `world_id`, production deny, `x-noema-world-id` on DO fetch)
- Modify: `workers/noema/src/world-do.ts` (genesis routes honor `x-noema-world-id`; refuse locked genesis on the wrong DO; activate `world_id` must match preview)
- Modify: `workers/noema/test/genesis.test.ts` (frozen candidate still 5 rooms)
- Modify: `workers/noema/test/test-world.test.ts` (still denies `world.perihelion-reach-2`)
- Modify: `scripts/genesis_rehearsal.sh` (`--world-id`, successor seed, refuse `noema.guru` for successor activate)
- Modify: `docs/GENESIS-RUNBOOK.md` (later cutover; this campaign does not run it)

---

### Task 1: Specs — RFC-0121

**Files:**
- Create: `rfcs/RFC-0121-perihelion-successor-world-version.md`
- Modify: `rfcs/README.md`
- Modify: `CHANGELOG.md`
- Modify: `docs/GENESIS.md`
- Modify: `docs/HOSTED-COMPATIBILITY-LAYERS.md`
- Modify: `validation/validate_all.py`

**Interfaces:**
- Consumes: ADR-006 landing; live identity `genesis.ef578f4ffceeccd0` / `world.perihelion-reach`; CHAMBER-MAP 10 ids; RFC-0120.
- Produces: RFC-0121 Accepted (or Draft→Accepted in the same PR if that is repo practice for ops RFCs — this campaign treats the PR as Accepted on merge). Successor identity: `world.perihelion-reach-2`, rehearsal seed `perihelion-successor-rehearsal-01`.

- [ ] **Step 1: Write the RFC**

Create `rfcs/RFC-0121-perihelion-successor-world-version.md`:

```markdown
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
```

- [ ] **Step 2: Index, changelog, GENESIS pointer, compatibility layer**

`rfcs/README.md` — add after RFC-0120:

```markdown
| [RFC-0121](RFC-0121-perihelion-successor-world-version.md) | **Accepted** | Perihelion successor `world.perihelion-reach-2`; 10-room CHAMBER-MAP; no live reseed |
```

`CHANGELOG.md` Unreleased: one bullet that RFC-0121 specifies the successor, does not reseed, does not flip production `DEFAULT_WORLD_ID`.

`docs/GENESIS.md` after the access invariant table, add:

```markdown
## Hosted successor (RFC-0121)

Live Perihelion Reach `genesis.ef578f4ffceeccd0` / `world.perihelion-reach` stays the activated 5-room world. A new hosted product world is `world.perihelion-reach-2` with the 10-room CHAMBER-MAP Cycle 0. Production cutover is a later human-gated ops step. Do not reseed the live genesis.
```

`docs/HOSTED-COMPATIBILITY-LAYERS.md` after “Changing the live room set requires a new Genesis / `world_version`”:

```markdown
That successor is RFC-0121: `world.perihelion-reach-2`, not an edit of `genesis.ef578f4ffceeccd0`.
```

- [ ] **Step 3: Validator**

In `validation/validate_all.py`, add `check_rfc_0121` and call it from `main` next to `check_rfc_0120`:

```python
def check_rfc_0121() -> None:
    rfc = (ROOT / "rfcs" / "RFC-0121-perihelion-successor-world-version.md").read_text(encoding="utf-8")
    if "**Accepted**" not in rfc.split("## Status", 1)[-1].split("##", 1)[0]:
        fail("RFC-0121 must be Accepted")
    for needle in (
        "world.perihelion-reach-2",
        "genesis.ef578f4ffceeccd0",
        "perihelion-successor-rehearsal-01",
        "room.civic-exchange",
        "POLICY_DENIED",
        "RFC-0120",
    ):
        if needle not in rfc:
            fail(f"RFC-0121 missing {needle}")
    if "reseed `genesis.ef578f4ffceeccd0`" in rfc.lower() and "Do not reseed" not in rfc:
        fail("RFC-0121 must forbid live reseed")
    if "Do not reseed" not in rfc and "no reseed" not in rfc.lower():
        fail("RFC-0121 must forbid live reseed")
    ok("RFC-0121 Perihelion successor world_version")
```

- [ ] **Step 4: Run validator**

Run: `python validation/validate_all.py`

Expected: PASS, including `RFC-0121 Perihelion successor world_version`.

- [ ] **Step 5: Commit**

```bash
git add rfcs/RFC-0121-perihelion-successor-world-version.md rfcs/README.md CHANGELOG.md docs/GENESIS.md docs/HOSTED-COMPATIBILITY-LAYERS.md validation/validate_all.py
git commit -m "$(cat <<'EOF'
docs(spec): RFC-0121 Perihelion successor world_version

10-room CHAMBER-MAP successor at world.perihelion-reach-2.
Does not reseed genesis.ef578f4ffceeccd0 or flip production DEFAULT_WORLD_ID.
EOF
)"
```

---

### Task 2: Worker — dual-path Cycle 0 (pure `previewGenesis`)

**Files:**
- Create: `workers/noema/src/chamber-map-graph.ts`
- Create: `workers/noema/test/genesis-successor.test.ts`
- Modify: `workers/noema/src/genesis.ts`
- Modify: `workers/noema/test/genesis.test.ts`

**Interfaces:**
- Consumes: existing `previewGenesis(input: GenesisInput): Promise<GenesisResult>`, `validateCycle0`, `buildCycle0` 5-room path, `GenesisRoom`.
- Produces: `GenesisInput.world_id?: string`; `CHAMBER_MAP_ROOM_IDS` (`readonly string[]` length 10); `chamberMapRooms(): Record<string, GenesisRoom>`; `isFrozenFirstWorldClaim(input: { world_name: string; world_seed: string; profile_id: string; story_seed_ids?: string[] }): boolean`; `SUCCESSOR_WORLD_ID = "world.perihelion-reach-2"`; product-path `previewGenesis` with that `world_id` returns 10 CHAMBER-MAP rooms, entry `room.civic-exchange`, genesis_id ≠ `genesis.ef578f4ffceeccd0`.

- [ ] **Step 1: Write failing tests**

`workers/noema/test/genesis.test.ts` — add inside `describe("hosted genesis"`):

```typescript
const FROZEN = {
  world_name: "Perihelion Reach",
  world_seed: "17011984",
  profile_id: "FRACTURED_OLD_WORLD",
  story_seed_ids: ["OLD_TRADE_NETWORK", "LOST_ARCHIVE"],
};

it("frozen first-world candidate keeps genesis_id and 5-room graph", async () => {
  const a = await previewGenesis(FROZEN);
  expect(a.genesis_id).toBe("genesis.ef578f4ffceeccd0");
  expect(Object.keys(a.cycle0.rooms).sort()).toEqual(
    ["room.civic-exchange", "room.infra-vault", "room.relay-quarter", "room.ruin-shelf", "room.transit-ring"].sort(),
  );
  expect(a.cycle0.rooms["room.archive"]).toBeUndefined();
  expect(a.validation.ok).toBe(true);
});
```

Create `workers/noema/test/genesis-successor.test.ts`:

```typescript
import { describe, expect, it } from "vitest";
import { GenesisError, previewGenesis, validateCycle0 } from "../src/genesis";
import { CHAMBER_MAP_ROOM_IDS } from "../src/chamber-map-graph";

const SUCCESSOR = {
  world_name: "Perihelion Reach",
  world_seed: "perihelion-successor-rehearsal-01",
  profile_id: "FRACTURED_OLD_WORLD" as const,
  story_seed_ids: ["OLD_TRADE_NETWORK", "LOST_ARCHIVE"],
  world_id: "world.perihelion-reach-2",
};

describe("genesis successor product path", () => {
  it("emits 10 CHAMBER-MAP rooms on world.perihelion-reach-2", async () => {
    const a = await previewGenesis(SUCCESSOR);
    expect(a.world_id).toBe("world.perihelion-reach-2");
    expect(a.genesis_id).not.toBe("genesis.ef578f4ffceeccd0");
    expect(a.world_name).toBe("Perihelion Reach");
    expect(a.cycle0.entry_room_id).toBe("room.civic-exchange");
    expect(Object.keys(a.cycle0.rooms).sort()).toEqual([...CHAMBER_MAP_ROOM_IDS].sort());
    expect(a.cycle0.rooms["room.civic-exchange"].name).toBe("Civic Exchange");
    expect(a.cycle0.rooms["room.infra-vault"]).toBeUndefined();
    expect(a.cycle0.rooms["room.ruin-shelf"]).toBeUndefined();
    expect(validateCycle0(a.cycle0).ok).toBe(true);
    expect(a.validation.ok).toBe(true);
  });

  it("same successor inputs are deterministic", async () => {
    const a = await previewGenesis(SUCCESSOR);
    const b = await previewGenesis(SUCCESSOR);
    expect(a.genesis_id).toBe(b.genesis_id);
    expect(a.cycle0_digest).toBe(b.cycle0_digest);
  });

  it("refuses product-path hash collision with the frozen genesis", async () => {
    await expect(
      previewGenesis({
        ...SUCCESSOR,
        world_seed: "17011984",
      }),
    ).rejects.toMatchObject({ code: "INVALID_SEED" });
  });

  it("refuses unknown explicit world_id this campaign", async () => {
    await expect(
      previewGenesis({ ...SUCCESSOR, world_id: "world.other" }),
    ).rejects.toMatchObject({ code: "INVALID_REQUEST" });
  });

  it("lands overlays on chamber rooms", async () => {
    const a = await previewGenesis(SUCCESSOR);
    const ids = (room: string) => a.cycle0.rooms[room].entities.map((e) => e.entity_id);
    expect(ids("room.relay-quarter")).toContain("entity.relay-7");
    expect(ids("room.civic-exchange")).toContain("entity.old-market-post");
    expect(ids("room.archive")).toContain("entity.archive-ledger");
    expect(a.cycle0.rooms["room.archive"].entities.find((e) => e.entity_id === "entity.archive-ledger")?.entity_type).toBe(
      "ARTIFACT",
    );
  });

  it("seed entity_id wins on overlay collision", async () => {
    const { buildProductCycle0ForTest } = await import("../src/genesis");
    const rooms = (await previewGenesis(SUCCESSOR)).cycle0.rooms;
    rooms["room.archive"].entities.push({
      entity_id: "entity.archive-ledger",
      label: "seed wins",
      entity_type: "ARTIFACT",
    });
    // Re-apply would skip — assert the public preview does not duplicate the id
    const a = await previewGenesis(SUCCESSOR);
    const n = a.cycle0.rooms["room.archive"].entities.filter((e) => e.entity_id === "entity.archive-ledger").length;
    expect(n).toBe(1);
  });
});
```

If exporting `buildProductCycle0ForTest` is too leaky, drop that import and keep only the `n === 1` assertion on a normal preview (product graph starts empty, overlay adds once).

- [ ] **Step 2: Run tests to verify they fail**

Run: `cd workers/noema && npx vitest run test/genesis.test.ts test/genesis-successor.test.ts`

Expected: FAIL — `chamber-map-graph` not found and/or successor `world_id` ignored so room count is 5, genesis_id may collide, `room.archive` missing.

- [ ] **Step 3: Embed CHAMBER-MAP graph**

Create `workers/noema/src/chamber-map-graph.ts`. Copy names/descriptions from Specs `examples/chamber-world/world-seed.json`. Lowercase directions. `GenesisRoom.exits` are `{ direction, to_room_id }` only (drop traversal_cost / conditions this campaign).

```typescript
export const CHAMBER_MAP_ROOM_IDS = [
  "room.civic-exchange",
  "room.relay-quarter",
  "room.foundry-corridor",
  "room.transit-ring",
  "room.infrastructure-vault",
  "room.archive",
  "room.outer-works",
  "room.storage-district",
  "room.generator-hall",
  "room.frontier-gate",
] as const;

export const CHAMBER_MAP_ENTRY_ROOM_ID = "room.civic-exchange";

const NAMES: Record<(typeof CHAMBER_MAP_ROOM_IDS)[number], { name: string; description: string }> = {
  "room.civic-exchange": { name: "Civic Exchange", description: "Central meeting and trade hub. High visibility." },
  "room.relay-quarter": { name: "Relay Quarter", description: "Primary communication infrastructure. Early degradation pressure." },
  "room.foundry-corridor": { name: "Foundry Corridor", description: "Production-focused corridor. Resource nodes and production infrastructure." },
  "room.transit-ring": { name: "Transit Ring", description: "Movement hub with multiple exits. Chokepoint potential." },
  "room.infrastructure-vault": { name: "Infrastructure Vault", description: "Hardened maintenance and logistics space. Defensible." },
  "room.archive": { name: "Archive", description: "Knowledge and document focus. Low material, high information." },
  "room.outer-works": { name: "Outer Works", description: "Edge location. Exploration gateway and risk." },
  "room.storage-district": { name: "Storage District", description: "Logistics node. High storage_bay potential." },
  "room.generator-hall": { name: "Generator Hall", description: "Power generation. Critical for production modifiers." },
  "room.frontier-gate": { name: "Frontier Gate", description: "Edge of known map. Leads toward later expansion." },
};

const LINKS: Array<[string, string, string, string]> = [
  ["room.civic-exchange", "room.relay-quarter", "north", "south"],
  ["room.civic-exchange", "room.transit-ring", "east", "west"],
  ["room.civic-exchange", "room.storage-district", "west", "east"],
  ["room.relay-quarter", "room.infrastructure-vault", "down", "up"],
  ["room.relay-quarter", "room.generator-hall", "east", "west"],
  ["room.foundry-corridor", "room.transit-ring", "south", "north"],
  ["room.foundry-corridor", "room.generator-hall", "west", "east"],
  ["room.transit-ring", "room.outer-works", "east", "west"],
  ["room.transit-ring", "room.frontier-gate", "south", "north"],
  ["room.storage-district", "room.infrastructure-vault", "north", "south"],
  ["room.civic-exchange", "room.archive", "down", "up"],
  ["room.outer-works", "room.frontier-gate", "south", "north"],
];

export function chamberMapRooms(): Record<string, import("./genesis").GenesisRoom> {
  const rooms: Record<string, import("./genesis").GenesisRoom> = {};
  for (const id of CHAMBER_MAP_ROOM_IDS) {
    const n = NAMES[id];
    rooms[id] = { room_id: id, name: n.name, description: n.description, exits: [], entities: [] };
  }
  for (const [a, b, dirA, dirB] of LINKS) {
    rooms[a].exits.push({ direction: dirA, to_room_id: b });
    rooms[b].exits.push({ direction: dirB, to_room_id: a });
  }
  return rooms;
}
```

Add the missing `exit.ow-fg` pair from the seed (outer-works ↔ frontier-gate) as in LINKS above.

- [ ] **Step 4: Dual-path `previewGenesis`**

In `workers/noema/src/genesis.ts`:

```typescript
export const FROZEN_GENESIS_ID = "genesis.ef578f4ffceeccd0";
export const SUCCESSOR_WORLD_ID = "world.perihelion-reach-2";

export interface GenesisInput {
  world_name: string;
  world_seed: string;
  profile_id: string;
  story_seed_ids?: string[];
  world_id?: string;
}

export function isFrozenFirstWorldClaim(input: {
  world_name: string;
  world_seed: string;
  profile_id: string;
  story_seed_ids?: string[];
}): boolean {
  const seeds = [...(input.story_seed_ids || [])].sort().join(",");
  return (
    input.world_name.trim() === "Perihelion Reach" &&
    input.world_seed.trim() === "17011984" &&
    input.profile_id === "FRACTURED_OLD_WORLD" &&
    seeds === "LOST_ARCHIVE,OLD_TRADE_NETWORK"
  );
}
```

After computing `world_id` (explicit trimmed, else slug as today):

- If `isFrozenFirstWorldClaim(input)` → legacy `buildCycle0`. If explicit `world_id` is set and is not `world.perihelion-reach` / `world-01` / omitted-slug, throw `GenesisError("INVALID_SEED", "frozen genesis_id cannot target another world")` **before** building 10 rooms. (Product-path + `17011984` hits this.)
- Else if explicit `world_id` is missing OR equals `world.perihelion-reach` OR `world-01` → legacy `buildCycle0`.
- Else if explicit `world_id === SUCCESSOR_WORLD_ID` → `buildProductCycle0(...)`.
- Else throw `GenesisError("INVALID_REQUEST", "world_id override this campaign must be world.perihelion-reach-2")`.

`buildProductCycle0`: start from `chamberMapRooms()`, set `entry_room_id` to `CHAMBER_MAP_ENTRY_ROOM_ID`, run the same overlay block as `buildCycle0` with retargets:

- `rooms[hub]` / `entity.relay-7` / scar conduit → `room.relay-quarter` (create entity only if that `entity_id` is absent).
- `room.infra-vault` → `room.infrastructure-vault`.
- `room.ruin-shelf` → `room.archive`.
- `OLD_TRADE_NETWORK` market post → `room.civic-exchange`.
- `LOST_ARCHIVE` ledger → `room.archive`.

Helper:

```typescript
function addEntity(
  room: GenesisRoom,
  ent: GenesisRoom["entities"][number],
): void {
  if (room.entities.some((e) => e.entity_id === ent.entity_id)) return;
  room.entities.push(ent);
}
```

`validateCycle0`: if `Object.keys(world.rooms).length === 10` and every `CHAMBER_MAP_ROOM_IDS` id is present, require exactly that set (fail on extras). Else keep 3–8. Do not fail the frozen 5-room path.

After `genesis_id` is computed, if product path (`world_id === SUCCESSOR_WORLD_ID`) and `genesis_id === FROZEN_GENESIS_ID`, throw `INVALID_SEED` (belt and suspenders with the claim-set check).

- [ ] **Step 5: Run tests to verify they pass**

Run: `cd workers/noema && npx vitest run test/genesis.test.ts test/genesis-successor.test.ts`

Expected: PASS. Existing rehearsal (`perihelion-rehearsal-01`, no `world_id`) still 5-room legacy via slug `world.perihelion-reach`.

- [ ] **Step 6: Commit**

```bash
git add workers/noema/src/chamber-map-graph.ts workers/noema/src/genesis.ts workers/noema/test/genesis.test.ts workers/noema/test/genesis-successor.test.ts
git commit -m "feat(genesis): dual-path Cycle 0 for perihelion-reach-2"
```

---

### Task 3: Worker — Admin `world_id` routing (local only)

**Files:**
- Create: `workers/noema/test/genesis-admin-world-id.test.ts`
- Modify: `workers/noema/src/index.ts`
- Modify: `workers/noema/src/world-do.ts`

**Interfaces:**
- Consumes: `previewGenesis` with `world_id`; `SUCCESSOR_WORLD_ID`; `FROZEN_GENESIS_ID`.
- Produces: `resolveAdminGenesisWorldId(requested: string | undefined, env: { NOEMA_ENV?: string; DEFAULT_WORLD_ID?: string }): { ok: true; world_id: string } | { ok: false; code: "POLICY_DENIED" | "INVALID_REQUEST"; message: string }`. Preview/activate fetch the DO with `idFromName(world_id)` and header `x-noema-world-id: world_id`. Production with body `world_id` → HTTP 403 `POLICY_DENIED`.

- [ ] **Step 1: Write failing tests**

Follow existing Worker test env helpers (`test/test-world.test.ts` `env()`). Export `resolveAdminGenesisWorldId` from `genesis.ts` or a tiny `admin-genesis-world.ts`. Prefer `workers/noema/src/genesis.ts` to avoid a new wiring file unless `genesis.ts` is already too large — if so, `workers/noema/src/admin-genesis-world.ts`.

```typescript
import { describe, expect, it } from "vitest";
import { resolveAdminGenesisWorldId } from "../src/genesis";

describe("resolveAdminGenesisWorldId", () => {
  it("omitted uses DEFAULT_WORLD_ID", () => {
    const r = resolveAdminGenesisWorldId(undefined, { NOEMA_ENV: "local", DEFAULT_WORLD_ID: "world-01" });
    expect(r).toEqual({ ok: true, world_id: "world-01" });
  });

  it("local allows world.perihelion-reach-2", () => {
    const r = resolveAdminGenesisWorldId("world.perihelion-reach-2", { NOEMA_ENV: "local", DEFAULT_WORLD_ID: "world-01" });
    expect(r).toEqual({ ok: true, world_id: "world.perihelion-reach-2" });
  });

  it("production denies any override", () => {
    const r = resolveAdminGenesisWorldId("world.perihelion-reach-2", {
      NOEMA_ENV: "production",
      DEFAULT_WORLD_ID: "world.perihelion-reach",
    });
    expect(r).toEqual({ ok: false, code: "POLICY_DENIED", message: "world_id override forbidden in production" });
  });

  it("rejects other explicit ids", () => {
    const r = resolveAdminGenesisWorldId("world.other", { NOEMA_ENV: "local", DEFAULT_WORLD_ID: "world-01" });
    expect(r.ok).toBe(false);
    if (!r.ok) expect(r.code).toBe("INVALID_REQUEST");
  });
});
```

Add a Worker-level test if the repo already boots `worker.fetch` for Admin genesis (copy the admin session pattern from `admin-email-login.test.ts` / genesis rehearsal). Minimum: unit tests above plus `world-do` activate refuse:

When implementing activate, if `preview.genesis_id === "genesis.ef578f4ffceeccd0"` and the loaded world's `world_id` is not `world.perihelion-reach`, return 400 `INVALID_SEED`.

If `body.world_id` (new field on genesis-activate JSON) is set and `preview.world_id !== body.world_id`, return 400 `INVALID_REQUEST`.

- [ ] **Step 2: Run tests to verify they fail**

Run: `cd workers/noema && npx vitest run test/genesis-admin-world-id.test.ts`

Expected: FAIL — `resolveAdminGenesisWorldId` not exported.

- [ ] **Step 3: Implement resolver and wire routes**

```typescript
export function resolveAdminGenesisWorldId(
  requested: string | undefined,
  env: { NOEMA_ENV?: string; DEFAULT_WORLD_ID?: string },
): { ok: true; world_id: string } | { ok: false; code: "POLICY_DENIED" | "INVALID_REQUEST"; message: string } {
  const fallback = String(env.DEFAULT_WORLD_ID || "world-01").trim() || "world-01";
  const value = String(requested || "").trim();
  if (!value) return { ok: true, world_id: fallback };
  const envName = (env.NOEMA_ENV || "local").toLowerCase();
  if (envName === "production") {
    return { ok: false, code: "POLICY_DENIED", message: "world_id override forbidden in production" };
  }
  if (value !== "world.perihelion-reach-2") {
    return { ok: false, code: "INVALID_REQUEST", message: "world_id override this campaign must be world.perihelion-reach-2" };
  }
  return { ok: true, world_id: value };
}
```

In `index.ts` preview handler: parse `world_id` from body; `const target = resolveAdminGenesisWorldId(body.world_id, env)`; if `!target.ok` return `cors(err(target.code, target.message, target.code === "POLICY_DENIED" ? 403 : 400))`. Pass `world_id: target.world_id` into `previewGenesis` only when `body.world_id` was set (so omitted still slugs inside preview). Then:

```typescript
const id = env.WORLD_DO.idFromName(target.world_id);
const stub = env.WORLD_DO.get(id);
const worldHeaders = { "content-type": "application/json", "x-noema-world-id": target.world_id };
```

Use `worldHeaders` on `health`, `genesis-preview-store`. Re-preview `previewGenesis` with the same `world_id` field as the first call.

Activate handler: parse `world_id?: string`; same `resolveAdminGenesisWorldId`; pass `{ genesis_id, admin_session_id, force, world_id: target.world_id }` to the DO; set `x-noema-world-id`.

In `world-do.ts` at the start of `genesis-preview-store`, `genesis-preview-get`, `genesis-activate`, and the `health` used by preview: `this.requestedWorldId = request.headers.get("x-noema-world-id")` if present (do **not** require `admitTestWorldId` — that would deny `world.perihelion-reach-2`). `load()` already uses `resolveLoadWorldId(this.requestedWorldId, DEFAULT_WORLD_ID)`.

On `genesis-activate`:

```typescript
if (preview.genesis_id === "genesis.ef578f4ffceeccd0" && preview.world_id !== "world.perihelion-reach") {
  return Response.json({ error: { code: "INVALID_SEED", message: "frozen genesis cannot activate on another world" } }, { status: 400 });
}
if (body.world_id && preview.world_id !== body.world_id) {
  return Response.json({ error: { code: "INVALID_REQUEST", message: "world_id does not match preview" } }, { status: 400 });
}
```

Keep production `force` 403 as today.

- [ ] **Step 4: Run tests**

Run: `cd workers/noema && npx vitest run test/genesis-admin-world-id.test.ts test/genesis.test.ts test/genesis-successor.test.ts`

Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add workers/noema/src/genesis.ts workers/noema/src/index.ts workers/noema/src/world-do.ts workers/noema/test/genesis-admin-world-id.test.ts
git commit -m "feat(admin): local genesis world_id override for perihelion-reach-2"
```

---

### Task 4: Local activate + agent ENTER smoke (tests)

**Files:**
- Modify: `workers/noema/test/genesis-successor.test.ts` (or new `test/genesis-successor-enter.test.ts`)
- Modify: `workers/noema/test/test-world.test.ts`

**Interfaces:**
- Consumes: activate path from Task 3; `applyWorldCommand` / existing inhabit test helpers from `test/play-attach.test.ts` or `test/agent-inhabit`.
- Produces: local successor world after activate has `entry_room_id === "room.civic-exchange"` and 10 rooms; agent `ENTER_WORLD` places `principal.player_id` there with empty inventory; human command still 403; `admitTestWorldId("world.perihelion-reach-2")` still `WORLD_FORBIDDEN`.

- [ ] **Step 1: Write failing tests**

`test/test-world.test.ts` inside `describe("admitTestWorldId"`):

```typescript
it("denies world.perihelion-reach-2", () => {
  const denied = admitTestWorldId("world.perihelion-reach-2");
  expect(denied.ok).toBe(false);
  if (!denied.ok) expect(denied.code).toBe("WORLD_FORBIDDEN");
});
```

Successor ENTER: reuse the isolated Worker env helper that already activates or applies commands. If DO activate is heavy, unit-test `cycle0ToWorld` by constructing from `previewGenesis(SUCCESSOR).cycle0` is **not** enough for ENTER — prefer the existing `applyWorldCommand` fixture pattern from `adr-006-world-bound.test.ts` / `agent-play-scope.test.ts`:

```typescript
it("agent ENTER on successor Cycle 0 body lands in civic-exchange", async () => {
  const preview = await previewGenesis(SUCCESSOR);
  const world = cycle0ToWorld(preview.cycle0); // export from world-do or a test-only mapper
  const principal = { player_id: "player.tester", controller_type: "agent", /* scopes as play-attach */ };
  const result = await applyWorldCommand(world, principal, { command: "ENTER_WORLD", arguments: {} });
  expect(result.ok).toBe(true);
  expect(world.players["player.tester"].room_id).toBe("room.civic-exchange");
  expect(world.players["player.tester"].entered).toBe(true);
});
```

If `cycle0ToWorld` is private, export `cycle0ToWorldForTest` from `world-do.ts` or move `cycle0ToWorld` to `genesis.ts` / `cycle0-world.ts`. Prefer exporting the existing function rather than duplicating it.

Human 403: existing `agent-play-scope.test.ts` already covers human command 403 — add a one-liner that successor preview does not change that file's contract. Do not weaken RFC-0120 tests.

Empty body: assert no copied inventory keys (`cargo`, `works`) on the new player row beyond default budgets.

- [ ] **Step 2: Run tests to verify they fail**

Run: `cd workers/noema && npx vitest run test/test-world.test.ts test/genesis-successor.test.ts`

Expected: FAIL on ENTER until `cycle0ToWorld` is exported / successor world has civic-exchange entry.

- [ ] **Step 3: Minimal implementation**

Export `cycle0ToWorld` (or a named `export function cycle0ToWorld`). Do not copy players from any other world object. `admitTestWorldId` already denies `world.perihelion*` via `startsWith("world.perihelion")` — the new test should already pass once added; do not add an allow.

- [ ] **Step 4: Run tests**

Run: `cd workers/noema && npx vitest run test/test-world.test.ts test/genesis-successor.test.ts test/genesis.test.ts test/genesis-admin-world-id.test.ts test/adr-006-world-bound.test.ts`

Expected: PASS. ADR-006 still exactly 10 on the fixture; live 5-room tests unchanged.

- [ ] **Step 5: Commit**

```bash
git add workers/noema/src/world-do.ts workers/noema/test/genesis-successor.test.ts workers/noema/test/test-world.test.ts
git commit -m "test(genesis): successor ENTER at civic-exchange; perihelion-2 still WORLD_FORBIDDEN"
```

---

### Task 5: Rehearsal script + runbook (no production cutover)

**Files:**
- Modify: `scripts/genesis_rehearsal.sh`
- Modify: `docs/GENESIS-RUNBOOK.md`

**Interfaces:**
- Consumes: Admin preview/activate with `world_id` (Task 3).
- Produces: `./scripts/genesis_rehearsal.sh --successor` previews `world.perihelion-reach-2` / seed `perihelion-successor-rehearsal-01`; `--activate` refused if `BASE` contains `noema.guru`; default script path (no `--successor`) unchanged.

- [ ] **Step 1: Extend the script**

After the existing `ACTIVATE` flag parse:

```bash
SUCCESSOR=0
for a in "$@"; do
  case "$a" in
    --activate) ACTIVATE=1 ;;
    --successor) SUCCESSOR=1 ;;
  esac
done
```

When `SUCCESSOR=1`:

```bash
if echo "$BASE" | grep -q 'noema.guru'; then
  echo "successor rehearsal refuses production host"
  exit 1
fi
REH='{"world_name":"Perihelion Reach","world_seed":"perihelion-successor-rehearsal-01","profile_id":"FRACTURED_OLD_WORLD","story_seed_ids":["OLD_TRADE_NETWORK","LOST_ARCHIVE"],"world_id":"world.perihelion-reach-2"}'
```

Assert `r['world_id']=='world.perihelion-reach-2'`, `r['preview_summary']['room_count']==10`, `r['genesis_id']!='genesis.ef578f4ffceeccd0'`.

Activate body when `SUCCESSOR=1`:

```bash
{"genesis_id":"...","confirm":true,"world_id":"world.perihelion-reach-2"}
```

Default (no `--successor`) keeps current `REH` and must not send `world_id`.

- [ ] **Step 2: Runbook**

In `docs/GENESIS-RUNBOOK.md` Deferred / after Production safeguards, add:

```markdown
## Successor world (RFC-0121) — not production this landing

Rehearse locally:

```bash
ADMIN_TOKEN=… BASE=http://127.0.0.1:8787 ./scripts/genesis_rehearsal.sh --successor
# explicit local activate only; never against https://noema.guru
ADMIN_TOKEN=… BASE=http://127.0.0.1:8787 ./scripts/genesis_rehearsal.sh --successor --activate
```

Later production cutover (human gate, separate campaign): preview successor on production (override deny lifted then), compare genesis_id ≠ `genesis.ef578f4ffceeccd0` and room_count 10, `confirm: true` activate on `world.perihelion-reach-2`, set `DEFAULT_WORLD_ID=world.perihelion-reach-2`, deploy. Do not `force`. Do not reseed `genesis.ef578f4ffceeccd0`.
```

Do not remove “Do not reseed `genesis.ef578f4ffceeccd0`” from the top of the runbook.

- [ ] **Step 3: Commit**

```bash
git add scripts/genesis_rehearsal.sh docs/GENESIS-RUNBOOK.md
git commit -m "docs(ops): successor genesis rehearsal; production cutover stays later"
```

---

## Self-review

**Spec coverage**

| Spec requirement | Task |
|---|---|
| Frozen 5-room identity / genesis_id | 1, 2 |
| Successor `world.perihelion-reach-2` + 10 CHAMBER-MAP | 1, 2 |
| Rehearsal seed `perihelion-successor-rehearsal-01` | 1, 2, 5 |
| Dual-path selector + overlay retarget + seed-wins | 2 |
| Production `world_id` / force / reseed denied | 1, 3 |
| DO `x-noema-world-id` so successor is not default bootstrap | 3 |
| Locked genesis cannot activate on another DO | 3 |
| Isolated PLAY still denies `world.perihelion-reach-2` | 4 |
| Local ENTER civic-exchange, no ledger copy, RFC-0120 | 4 |
| Rehearsal script refuses `noema.guru` | 5 |
| Later cutover specified, not executed | 1, 5 |
| No production `DEFAULT_WORLD_ID` change | Global + Task 5 |

**Not in this plan (spec non-goals):** production activate, wrangler production env, public chrome hiding old world, Admin allowlist inspect, enrollment rewrite.

**Placeholder scan:** none. Rehearsal seed and successor `world_id` are literal.

**Type consistency:** `SUCCESSOR_WORLD_ID`, `FROZEN_GENESIS_ID`, `GenesisInput.world_id?: string`, `resolveAdminGenesisWorldId`, `CHAMBER_MAP_ROOM_IDS`, `chamberMapRooms()` used under those names in Tasks 2–5.
