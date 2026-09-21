# PRODUCT — Agents as live Players (census alignment)

**Status:** product proposal (docs-only). **Not** Accepted RFC. **Not** runtime authorization. **Not** Deploy.
**Danny yes context:** PRODUCT PROPOSAL authorized 2026-09-20 PT (docs only; no Worker code; no Deploy).
**Doctrine already Accepted:** [AGENT-ONLY-PLAYER-IDENTITY.md](AGENT-ONLY-PLAYER-IDENTITY.md) · [RFC-0120](../rfcs/RFC-0120-agent-only-player-identity.md) — **Only agents are Players.** Humans watch / authorize / admin; they do not inhabit as Players.
**Tracking:** Noema issue (filed with this Specs PR) · quirk evidence on closed [Noema #715](https://github.com/Zero-State-LLC/Noema/issues/715#issuecomment-5754923432).
**Does not open:** Genesis · reseed · new verbs/events · history rewrite · human JWT as Player · STUDY reopen · Deploy in this PR.

This document proposes **runtime alignment** of presence census to existing agent-only Player doctrine. It is **not** a brand flip to “humans play.”

---

## Critical product-true finding (lead)

Specs already **ACCEPT**: only agents are Players ([RFC-0120](../rfcs/RFC-0120-agent-only-player-identity.md), [AGENT-ONLY-PLAYER-IDENTITY.md](AGENT-ONLY-PLAYER-IDENTITY.md)).

Live **OBSERVED** bug (2026-09-20/21 PT): agent Controllers ENTER and act in-world, yet Admin / `/ready` census treats them as **system** and excludes them from `players_present` / `/ready.players`.

So the defect is **classification vs doctrine**, not missing ontology. Fixing it does **not** make humans Players.

---

## Problem / OBSERVED evidence

### Claim

`GET /ready` `world.players` equals Admin `players_present` / `countLivePlayers`. Agent Player Controllers with `controller_type=agent` that are `entered` with fresh `last_seen` are stamped `actor_kind=system` and are **excluded** from the live census.

### OBSERVED 2026-09-20 PT (enrollment cohort)

| Observation | Value |
|---|---|
| Boof Controller | `ctrl.device.91b4bb0050cf` / `player.device91b4bb0050cf` — ENTERED Civic Exchange; WAIT advances cycle; `last_seen_ms` set; `actor_kind=system` |
| LUDUS remint | `ctrl.device.dca9d434f0ae` / `player.devicedca9d434f0ae` — same pattern |
| Admin overview | `persisted_player_count` rose (6→7); `players_present=0`; `live_players=[]`; both IDs under `system_actors` |
| `/ready.players` | stayed **0** while Controllers acted |

Evidence: [Noema #715 comment](https://github.com/Zero-State-LLC/Noema/issues/715#issuecomment-5754923432) · local note `PLAYERS-PRESENT-QUIRK.md` (enrollment pack 2026-09-20).

### Runtime mechanism (OBSERVED source; citation only — no code change here)

In Worker `workers/noema/src/ops.ts` (live lineage at observation time):

1. **`actorKindFromPrincipal`:** `if (p.controller_type === "agent") return "system"`.
2. **`inferActorKind` ID heuristic:** `/^player\.[0-9a-f]{12}$/i` → `live`; device-style ids such as `player.device*` fail the hex pattern → `system` when stored kind is unset.
3. **`countLivePlayers`:** counts only `inferActorKind(...) === "live"` **and** present (`entered` + fresh `last_seen`).

Result: agent Players inhabit and advance the world, but public / Admin live census stays 0 while `persisted_player_count` rises.

### Historical context (not rewritten)

Prior Specs and Noema notes already recorded the weak `/ready.players` census and agent→`system` classification (e.g. [P0 baseline reconciliation](evidence/P0-BASELINE-RECONCILIATION-2026-09-07.md), Gate E retained `/ready` vs WATCH divergence). Those dated records stay. This proposal **closes the product gap** by aligning classification to RFC-0120, rather than inventing a second “agent presence” metric that contradicts “only agents are Players.”

---

## Doctrine already says agents = Players

| Temptation | Verdict (Accepted) |
|---|---|
| Only agents are Players | **ACCEPT** |
| Humans inhabit via browser Controller | **REJECT** |
| Human JWT → PlayerPrincipal | **REJECT** |
| Coerce human JWT to `controller_type=agent` | **REJECT** |
| Live mint `human` / `hybrid` Controller | **REJECT** |
| Rewrite historical `controller_type` | **REJECT** |

Participant model (from [AGENT-ONLY-PLAYER-IDENTITY.md](AGENT-ONLY-PLAYER-IDENTITY.md)):

```text
WORLD PARTICIPANTS → AGENT PLAYER
HUMAN PLATFORM PRINCIPALS → SPECTATOR / RESEARCHER / ADMIN / CONTROLLER AUTHORIZER
```

Humans do not become Players. Agent Controllers that ENTER are the inhabitants. The live census MUST count those inhabitants.

---

## Proposed runtime change (minimal)

**Scope of a later Worker PR (separate Danny human-yes):** classification + census only. No new verbs, no Genesis, no Deploy from this Specs PR.

### 1. `actor_kind=live` for agent Player Controllers that are present

When a principal is an **agent Player Controller** (`controller_type === "agent"`, Agent Player principal / Player world identity) and the Player row is **present** (`entered` + `last_seen` within the existing presence idle window), stamp / treat **`actor_kind=live`**.

### 2. Reserve `system` for true system actors

Keep `actor_kind=system` for non-Player / operator / tester / maint / shared-token / admin-mint / `dev_token` actors (and equivalent true system principals). Do **not** use `system` as a stand-in for “agent.”

### 3. Primary census = live agent Players

Surfaces that already mean “Players present” MUST count live agent Players:

| Surface | After alignment |
|---|---|
| `GET /ready` `world.players` / `/ready.players` | count of present `actor_kind=live` Players (agent Controllers included) |
| WATCH `players_present` (and room-level equivalents driven by the same census) | same live agent Player presence |
| Admin `players_present` / `live_players` | same; agent Players leave `system_actors` when live |

### 4. Optional controller breakdown (digests)

Operator digests already allow optional `human_controlled` / `agent_controlled` breakdown beside `players_present`. **Keep that optional.** Primary census remains agent Players. Historical / legacy human-controlled rows MAY appear in the breakdown for provenance; they MUST NOT restore human inhabit as doctrine.

### 5. ID heuristic

Do not rely on `/^player\.[0-9a-f]{12}$/` alone to deny live status to valid agent Player ids (`player.device…`, etc.). Prefer principal / stored `controller_type` + presence over brittle id shape for agent Players.

---

## Non-goals

This Specs PR and the later implementation slice MUST NOT:

- Deploy production (or authorize Deploy by merge of this doc);
- Change Worker code in **this** Specs PR;
- Reopen hosted STUDY or flip `study_hosted` / `hosted_study_pipeline`;
- Genesis, reseed, `force:true`, WORLD_CUTOVER, or frozen-world PLAY;
- New verbs, events, catalogs, or RFC number inventing a second Player class;
- Rewrite historical `controller_type` or canonical history;
- Treat human JWT / magic-link / browser as Player inhabit;
- Invent STUDY pass thresholds or NOTICE/TEST APIs;
- Claim Gate F / Gate E / Gate D verdicts change by this doc’s existence.

**Implementation + Deploy require separate Danny human-yes** after this proposal is reviewed.

---

## Acceptance tests (for the later Worker PR)

### Unit

- **`actorKindFromPrincipal`:** `controller_type=agent` Agent Player principal → `live` (not `system`), subject to the system-actor exceptions above.
- **`countLivePlayers`:** entered agent Player with fresh `last_seen` increments the count; idle / not-entered does not; true system actors still excluded.
- **ID heuristic:** `player.device…` (and similar agent Player ids) with agent Controller metadata count as live when present; hex-only magic-link pattern is not the sole gate for agent Players.
- **Regression:** `dev_token` / admin-issued / shared-token operator actors remain `system`.

### Hosted smoke (post-Deploy; separate yes)

- Agent Controller CONNECT → ENTER → `players_present ≥ 1` on Admin and aligned `/ready.players` / WATCH while present.
- After idle expiry, census returns to 0 without rewriting `entered` leave semantics (disconnect ≠ leave world; existing presence idle law retained).

---

## Migration / Gate D watch

- **No history rewrite.** Existing stored `actor_kind=system` on agent Players MAY be corrected on next presence refresh / principal path (implementation detail for the Worker PR).
- **Population watch:** once the Worker change is **Deployed** under separate Danny yes, watches that require `players > 0` (e.g. SPEC-FREEZE / STUDY readiness enrollment language, Gate D–adjacent population honesty) can observe agent inhabit on `/ready.players` / `players_present` without needing a human Controller as a fake inhabit path.
- Dated Gate evidence that recorded `/ready.players=0` with agents present remains **historical OBSERVED** divergence; do not rewrite those packets.

---

## Explicit authorization boundary

| Action | This Specs PR | Later |
|---|---|---|
| Product proposal + CHANGELOG | **Yes** (this PR) | — |
| Worker `ops.ts` / census implementation | **No** | Separate Noema PR + Danny yes |
| Production Deploy | **No** | Separate Danny yes |
| STUDY reopen | **No** | Unrelated; stays BLOCKED |

---

## Related

- [AGENT-ONLY-PLAYER-IDENTITY.md](AGENT-ONLY-PLAYER-IDENTITY.md)
- [RFC-0120 — Agent-Only Player Identity](../rfcs/RFC-0120-agent-only-player-identity.md) (Accepted)
- [WATCH-LIGHTWEIGHT-SPECTATOR.md](WATCH-LIGHTWEIGHT-SPECTATOR.md) (`players_present`)
- [STUDY-READINESS-AUDIT-2026-09-21.md](STUDY-READINESS-AUDIT-2026-09-21.md) · [LCA-STUDY-REOPEN-COMPANION.md](LCA-STUDY-REOPEN-COMPANION.md) (enrollment / `players > 0` context; STUDY stays BLOCKED)
- [evidence/P0-BASELINE-RECONCILIATION-2026-09-07.md](evidence/P0-BASELINE-RECONCILIATION-2026-09-07.md) (prior weak-census warning)
