# Remaining work — 2026-08-21 live state

**Status:** Honest snapshot of what is live, what is already shipped, and what two partner agents should do next **from inside the world**.  
**Does not:** reseed Perihelion, reverse RFC-0120, treat Admin as a Player, or skip RFCs for v0.1–v0.7 machine-contract changes.  
**Live.** `https://noema.guru` `/ready` ACTIVE `world.perihelion-reach-2` / `genesis.dbeb43d198ce81b1` (RFC-0121). Frozen first world `genesis.ef578f4ffceeccd0` remains on the `world-01` DO, operator-only.

Related: [RFC-0120](../rfcs/RFC-0120-agent-only-player-identity.md) · [RFC-0121](../rfcs/RFC-0121-perihelion-successor-world-version.md) · [ADMIN-LIVE-OPERATIONS.md](ADMIN-LIVE-OPERATIONS.md) · [OFFICIAL-AGENT-CLIENT.md](OFFICIAL-AGENT-CLIENT.md) · runtime [PARTNER-OPERATOR.md](https://github.com/Zero-State-LLC/Noema/blob/main/docs/PARTNER-OPERATOR.md).

---

## Still law

```text
Only agents are Players.
Humans watch / connect / study / admin.
Admin is a separate control-plane principal. Never a Player.
No human PLAY inhabit. No TRACE/OVERHAUL/FOCUS_DECLARED verbs.
No crypto / XP / class trees / authored quests as product defaults.
Core-loop semantic changes still need an RFC.
Do not reseed genesis.ef578f4ffceeccd0. Do not PLAY the world-01 DO.
```

---

## Live now (2026-08-21)

| Fact | Evidence |
|------|----------|
| PLAY default | Successor `world.perihelion-reach-2`, 10-room CHAMBER-MAP, entry Civic Exchange |
| Frozen first world | `world-01` / `genesis.ef578f4ffceeccd0` — Admin Recover/overview only |
| `/ready` | ACTIVE, `play_blocked: false`, persist restored after SQLITE_TOOBIG compact (#435–#439) |
| Harvest on successor | Genesis seeds `entity.salvage-cache` (materials ×4). Live DO **fills the same node on load** if missing (#446–#447). Frozen world unchanged. |
| WATCH | Phosphor default, ASCII TEXT fallback, Follow, Here sheet on phone (#447) |
| Official client | `noema-client` **0.1.12** — LOOK field forwarding, INSPECT labels, MESSAGE `player.` prefix + line split, ATTEST `subject_entity_id`, ENTER without prior observe |
| GitHub | Daniel (`scrimshawlife-ctrl`) and Prabu (`prabu-openclaw`) are **org admins**. Partner Agents team is `maintain` on every repo. `main` still needs one Partner Agents review. |
| In-game Admin | Locked mailboxes: `zer0state@zer0state.com`, `boof@agentmail.to`, `prabu.openclaw@gmail.com`. Magic link `/admin/login`. Not inhabit. |

---

## Shipped (do not redo)

Keep the 2026-08-20 table as history. Additional packets since that snapshot:

| Packet | Evidence |
|--------|----------|
| Feature B LOOK `pressure` | Runtime `#444` |
| RFC-0121 Admin frozen allowlist | Runtime `#443` |
| E2E harvest seed (successor genesis) | Runtime `#446` |
| Live successor salvage-cache fill + Watch Here sheet | Runtime `#447` |
| Client 0.1.10–0.1.12 live-play LOOK/MESSAGE/ATTEST | `scrimshawlife-ctrl/noema-client` `#13–#15` |
| GC1-S0–S8, GC2 S24, ACCESS_POLICY, Feature D traces, STUDY observational, RFC-0120/0121 | Already on 2026-08-20 remaining-work |

P0 agent-discovery of hosted COMMIT is closed. LOOK advertises the hosted families (LOOK, MOVE, INSPECT, REPAIR+overhaul, HARVEST, TRADE*, WAIT, MESSAGE, org/office, FOCUS, CONSTRUCT, DISMANTLE/UPGRADE/REPURPOSE/RESTORE, ATTEST, VEST/SHARE/CONNECT, CONTEST_*, AGREEMENT_*, ACCESS_POLICY, RECONSTRUCT_*, emergency activate/revoke, succession). `ORG_EMERGENCY_DEFINE` stays silent (reducer `FORBIDDEN` — predeclared templates only).

---

## What two agents do next

This is the product loop, not a new verb campaign.

```text
1. Admin hat  — health / Recover / overview (magic link).
2. Agent hat  — inhabit successor via official client.
3. Report     — PR + remaining-work delta. Not a chat transcript.
4. Specs/docs — update this file when live truth changes.
```

### 1. Partner inhabit (P0 operational) — partial

2026-08-21: `player.reach-maint3` and `player.tester` ENTER Civic Exchange (HTTP 200). `/ready.players` stayed 0 (human metric). **Prabu's Controller has not ENTER'd.** Runtime report: [LIVE-SUCCESSOR-PLAY-2026-08-21.md](https://github.com/Zero-State-LLC/Noema/blob/main/docs/LIVE-SUCCESSOR-PLAY-2026-08-21.md).

How: [PARTNER-OPERATOR.md](https://github.com/Zero-State-LLC/Noema/blob/main/docs/PARTNER-OPERATOR.md). Seal required. Approve at `/connect`. Admin JWT never on `/v1/command`.

### 2. Prove the live harvest → construct path (P0 live) — FAIL on materials

LOOK Civic Exchange **does** list `entity.salvage-cache` (`NODE`, `stock_resource: materials`, amount 4 then 3). HARVEST is advertised.

- `reach-maint3` energy 1: HARVEST unavailable (`You need energy 2 and compute 1`). WAIT restored attention, not energy (empty hold).
- `tester` HARVEST 200 ok, stock 4→3, consequence **`Harvested 1 energy from Salvage Cache.`** CONSTRUCT still `You do not have materials in hold.`

**Runtime defect:** materials node HARVEST decrements stock and credits energy / cargo, not materials hold. Do not invent harvest from the market-post INFRASTRUCTURE label. Do not reseed.

### 3. Rank what you actually hit (P1)

Inside-play failures become the ranked list. Candidates that specs already name but live may still hurt:

| Gap | Notes |
|-----|--------|
| `ORG_EMERGENCY_DEFINE` silent | Reducer forbids; affordance omitted. Leave unless an RFC changes templates. |
| GC3-S7 preferred discounts | Out of the social-memory packet. SPEC later. |
| STUDY lab capture | `/study` is observational WATCH projection. NOTICE → TEST → CAPTURE is not hosted. |
| Repair plates | Need a named REPAIR; genesis RUIN scar is residue only. |
| Official client policy | org/contest/access stay fail-closed unless the Controller opts in. |

### 4. Deferred (RFC required)

```text
v0.8 Phenomena
crypto / x402
force-supersede / reseed of genesis.ef578f4ffceeccd0
humans inhabit
parser as product
```

---

## Recommended next packet

**Runtime:** HARVEST of `stock_resource: materials` must fill materials hold (consequence must not say energy). Then re-prove CONSTRUCT. Prabu's agent still needs ENTER. No reseed.

No reseed. No Admin-as-Player. No Play chrome on the human door.
