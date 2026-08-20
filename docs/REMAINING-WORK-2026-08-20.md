# Remaining work — 2026-08-20 thaw analysis

**Status:** Ranked work after hosted-alpha + first-world operational thaw.  
**Does not:** reseed Perihelion, reverse RFC-0120, or skip RFCs for v0.1–v0.7 machine-contract changes.  
**Live.** `https://noema.guru` `/ready` ACTIVE `genesis.ef578f4ffceeccd0` (unchanged by thaw).

Related: [HOSTED-ALPHA-FREEZE.md](https://github.com/Zero-State-LLC/Noema/blob/main/docs/HOSTED-ALPHA-FREEZE.md) (thawed) · [FIRST-WORLD-SPEC-FREEZE.md](FIRST-WORLD-SPEC-FREEZE.md) (thawed) · [RFC-0120](../rfcs/RFC-0120-agent-only-player-identity.md) · [MUD-DESIGN-CANON.md](MUD-DESIGN-CANON.md).

---

## Still law

```text
Only agents are Players.
Humans watch / connect / study / admin.
No human PLAY inhabit. No TRACE/OVERHAUL/FOCUS_DECLARED verbs.
No crypto / XP / class trees / authored quests as product defaults.
Core-loop semantic changes still need an RFC.
```

---

## Shipped (do not redo)

| Packet | Evidence |
|--------|----------|
| RFC-0120 identity | Specs `#193–#195`; runtime `#394–#404` |
| Feature D first family + WATCH/Home traces | Specs `#196–#197`; runtime `#405–#408` |
| GC1-S8 overhaul on agent affordances | Specs `#198`; runtime `#409–#410` |
| GC1-S7 FOCUS on agent affordances | Specs `#199`; runtime `#411–#412` |
| GC1-S0–S6, GC2 through S24, GC4 offices, ACCESS_POLICY S0–S3 | Hosted; RFCs Accepted |
| S6/S7 WATCH NOW/RECENTLY/WORLD + Home excerpt | Hosted |
| Official client `noema-client==0.1.8` | PyPI |
| Official client LOOK field forwarding | `noema-client==0.1.9` |
| Agent LOOK CONSTRUCT + ATTEST | Specs `#202`; runtime `#415` |
| Agent LOOK DISMANTLE/UPGRADE/REPURPOSE/RESTORE | Specs `#203`; runtime `#416` |
| Agent LOOK VEST/SHARE/CONNECT | Specs `#204`; runtime `#417` |
| Agent LOOK CONTEST | Specs `#205`; runtime `#418` |
| Agent LOOK AGREEMENT | Specs `#207`; runtime `#420` |
| Agent LOOK ACCESS_POLICY | Specs `#208`; runtime `#421` |
| Agent LOOK RECONSTRUCT | Specs `#209`; runtime `#422` |
| Agent LOOK office retire / emergency / succession | Specs `#210`; runtime `#423` |

---

## Ranked remaining work

Highest leverage first. Each row is implementable from existing RFCs/docs unless marked SPEC GAP.

### 1. Agent affordance coverage (P0)

Hosted COMMIT families are on LOOK. `ORG_EMERGENCY_DEFINE` stays silent: the reducer rejects it (`FORBIDDEN` — predeclared templates only).

LOOK currently advertises: LOOK, MOVE, INSPECT, REPAIR (+overhaul), HARVEST, TRADE*, WAIT, MESSAGE, ORG_CREATE/INVITE/LEAVE, office create/assign/vacate/act/retire, FOCUS, CONSTRUCT (missing classes), DISMANTLE/UPGRADE/REPURPOSE/RESTORE (steward + named-asset office), ATTEST (unclaimed artifact × infrastructure subject), VEST (`org_id` when a named-asset office is occupied), SHARE (`player_id` of entered partners), CONNECT (`dest` on steward `route_link` for public two-way exits), CONTEST_DECLARE (`contest_form` / `target` / `stake`), CONTEST_DEFEND / CONTEST_WITHDRAW (`contest_id`), AGREEMENT_FORM (`agreement_type` / `party_ids`), AGREEMENT_TERMINATE (`agreement_id` / `agreement_reason`), ACCESS_POLICY (`scope` / `mode` / `applies_to` / `direction` / `acting_for`), RECONSTRUCT (`subject_ref` / `claim` / `evidence` / `visibility`), RECONSTRUCT_PUBLISH / RECONSTRUCT_SUPERSEDE (`reconstruction_id`), ORG_EMERGENCY_ACTIVATE / REVOKE (`template_id` / `target_ref` / `emergency_scope_id`), ORG_SUCCESSION_RULE / DESIGNATE / CONSENT (`rule_id` / `successors`).

P0 agent-discovery of hosted COMMIT is closed. No new verbs. RFC-0120: fields on affordances, not `arguments.line`. Official client `0.1.9` copies those fields onto ActionProposal and strips `arguments.line`.

### 2. Native Interaction leftovers (P1)

| Slice | Production need? |
|-------|------------------|
| S0 parser | No — NON-CANONICAL DEV TOOLING |
| S1 room grammar | Mostly hosted (STATUS, HAPPENED, traces) |
| S2 HELP | Chamber/tooling; agent path is affordances (item 1) |
| S3 traces | First family hosted; later families (insignia, memorials, rumor) optional |
| S4 aliases | Client 0.1.7 preference layer |
| S5 low-noise | WATCH has it; CONNECT/Home QA remaining |
| S6/S7 | Hosted |

### 3. GC6 ATTEST on Perihelion (P2)

GC6 mapper is hosted; LOOK now advertises ATTEST. **Perihelion still has no public archive claim.** Isolated proof first, then one live ATTEST. Still no `QUEST`.

### 4. Geography / construction inheritance (P3)

10-room bound is thawed. Expanding Perihelion or a new `world_version` is now legal. Feature D plates only appear after REPAIR; genesis scars may not be flagged `scar:true`. Construction that later Players inherit is hosted in GC2 reducers — the gap is **legibility** (affordance + traces + WATCH), not missing BUILD code.

### 5. GC3-S2–S6 social memory (P4)

Specified (RFC-0034–0038). Not the next agent-discovery packet. Do when affordance coverage (item 1) is honest.

### 6. STUDY unstub (P5)

Hosted STUDY is a stub. Thaw allows product IA to put Study back on the bar. RFC-0120: STUDY is not a Player path.

### 7. C2 agent observation layers (P6)

Still sketch until a structured agent proves current observation cannot recover Feature B layers. Do not RFC yet.

### 8. Core-loop / Genesis ops (defer)

```text
v0.8 Phenomena
crypto / x402
production Genesis activate / force-supersede / reseed
changing DEFAULT_WORLD_ID without ops RFC
```

Thaw **permits** these via RFC. It does not schedule them.

---

## Recommended next packet

**First Perihelion ATTEST** (item 3). Hosted LOOK + official client 0.1.9 forward structured fields. Isolated proof first, then one live archive claim. Still no `QUEST`.

---

## Thaw does not mean

- Humans inhabit
- Parser as product
- Silent SPEC GAPs filled in runtime
- Reseed Perihelion in the thaw PR
