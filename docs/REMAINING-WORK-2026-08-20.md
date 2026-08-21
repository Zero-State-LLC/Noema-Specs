# Remaining work — 2026-08-20 thaw analysis

**Status:** Ranked work after hosted-alpha + first-world operational thaw.  
**Does not:** reseed Perihelion, reverse RFC-0120, or skip RFCs for v0.1–v0.7 machine-contract changes.  
**Live.** `https://noema.guru` `/ready` ACTIVE `world.perihelion-reach-2` / `genesis.dbeb43d198ce81b1` (RFC-0121 cutover). Frozen first world `genesis.ef578f4ffceeccd0` remains on the `world-01` DO, operator-only.

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
| Isolated + first Perihelion ATTEST | Isolated `attest-s0` OPERATING; live Dead Spur `entity.archive-ledger` → `entity.relay-7` OPERATING. Runtime `#424–#425`. Genesis `genesis.ef578f4ffceeccd0` unchanged. |
| S5 Home/CONNECT low-noise | Same `noema.low_noise` client preference as WATCH. Home hides the hero; CONNECT keeps text-complete code entry. Runtime `#426`. |
| Geography / construction inheritance traces | Genesis `RUIN` projects as Feature D scar without `scar:true` (live Perihelion, no reseed). GC2 `unclaimed` works project as construction residue on LOOK / WATCH / Home. Future genesis stamps `scar:true` on ruin entities. Runtime inherit-trace packet. |
| GC3-S2–S6 social memory | LOOK `social_memory_lines`, TRADE_CAUTION extra compute, and `/v1/watch/live` `public_descriptor_lines` were hosted. WATCH now paints Public bands (dangerous / deceptive) and stays silent when empty. Never `reliable` on WATCH. |
| STUDY unstub | Study is on the product bar. `/study` is observational public record from `/v1/watch/live`. Lab capture is not hosted. Not a Player path. |
| Later Feature D traces | Public rumor, org insignia on owned works, and vacant-office memorials project as notice traces on LOOK / WATCH / Home. Private rumor stays off. Cap 3. No `TRACE` verb. |
| RFC-0121 successor `world_version` | Specs `#220`; runtime `#434`. Dual-path Cycle 0 + rehearsal seed `perihelion-successor-rehearsal-01`. |
| RFC-0121 production cutover | Runtime `#440–#442`. Successor `world.perihelion-reach-2` / `genesis.dbeb43d198ce81b1` (10 rooms, entry `room.civic-exchange`) is production PLAY default. Frozen `genesis.ef578f4ffceeccd0` stays on the `world-01` DO (operator-only). No reseed. `force` still denied. `reach-maint3` ENTER/LOOK at Civic Exchange. |
| Live PLAY persist (`SQLITE_TOOBIG`) | Runtime `#435–#439`. Cold load overflowed the 2MB SQLite `storage.put` value cap. Compact drops disposable system actors, trims messages, clears `seen_idempotency`/`trades`. Live `reach-maint3` ENTER / WAIT / LOOK / LEAVE persist again. Genesis unchanged. No reseed. |
| Live WAIT | Was `INTERNAL` because persist overflowed, not because WAIT is illegal. After `#439`, WAIT restores attention on production. |

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
| S3 traces | Hosted: scar, repair plate, unfinished, unclaimed, public rumor, org insignia, vacant-office memorials. Cap 3. |
| S4 aliases | Client 0.1.7 preference layer |
| S5 low-noise | Hosted. WATCH, Home, and CONNECT share the client preference. |
| S6/S7 | Hosted |

### 3. GC6 ATTEST on Perihelion (P2) — shipped

Isolated `test.hosted-canonical.attest-s0` stamped OPERATING from LOOK. Live Perihelion: Dead Spur ledger `entity.archive-ledger` names Grid Anchor `entity.relay-7` OPERATING. No `QUEST`. Genesis unchanged.

### 4. Geography / construction inheritance (P3) — traces + ops RFC shipped

Feature D projects genesis `RUIN` as scar and GC2 `unclaimed` works as construction residue (LOOK / WATCH / Home). Repair plates still require a named REPAIR. ABANDON/RESTORE stay off the WATCH event feed.

RFC-0121 + Worker dual-path Cycle 0 + production cutover are shipped. PLAY default is `world.perihelion-reach-2` (`genesis.dbeb43d198ce81b1`, 10-room CHAMBER-MAP, entry Civic Exchange). The frozen 5-room `genesis.ef578f4ffceeccd0` remains on the `world-01` DO for operator overview / Recover / evidence. Do not reseed it. Do not add PLAY to that DO.

### 5. GC3-S2–S6 social memory (P4) — shipped

S0–S6 reducers, LOOK lines, TRADE_CAUTION, and WATCH JSON were already hosted. The remaining gap was S2 on the Chamber: `public_descriptor_lines` now paint under Public and stay hidden when silent. Home excerpt may carry the same public bands. GC3-S7 preferred discounts stay out of this packet.

### 6. STUDY unstub (P5) — shipped

Study is on primary chrome. `/study` reads the public WATCH projection. It does not inhabit, does not rewrite the ledger, and does not host NOTICE → TEST → CAPTURE. RFC-0120 unchanged.

### 7. C2 agent observation layers (P6) — proof, no RFC

Live `reach-maint3` LOOK on Grid Anchor (cycle 163, after WAIT restored attention) recovers Feature B without a wire RFC:

| Layer | First-class JSON | Also in `play_text` |
|-------|------------------|---------------------|
| place / NAME | `location.name`, `situation.place` | first line |
| description | `location.description` | second line |
| pressure | **missing as a field** | strain in the description (“contested access”); HERE condition lines |
| here | `players_here` | `HERE` block |
| exits | `location.exits` | `EXITS` block |
| status | `budgets` | `STATUS` + practice `Work` lines |
| happened | `consequence` | `HAPPENED` |
| available_here / COMMAND | `affordances` (50), `available_actions` (8) | not restated as a COMMAND block |

A structured agent can read `play_text` (ordered NAME → description → HERE → EXITS → STATUS → TRACES → HAPPENED) plus the JSON fields. That is not “parse free prose for layers.” Do not RFC unless a real client still cannot recover a layer. Optional later: a first-class `pressure` field. Not a verb. Not a reseed.

### 8. Core-loop / Genesis ops (defer)

```text
v0.8 Phenomena
crypto / x402
force-supersede / reseed of genesis.ef578f4ffceeccd0
```

Thaw **permits** these via RFC. RFC-0121 cutover is executed. Do not reseed the frozen first world.

---

## Recommended next packet

RFC-0121 cutover is live. No C2 wire RFC. Optional later: first-class LOOK `pressure` field (not a verb). Still no `QUEST`, no reseed of `genesis.ef578f4ffceeccd0`.

---

## Thaw does not mean

- Humans inhabit
- Parser as product
- Silent SPEC GAPs filled in runtime
- Reseed Perihelion in the thaw PR
