# Living Civilization Alpha — Gate C Promotion Evidence

**Status:** Gate C accepted on 2026-09-08 (Danny human-yes)  
**Scope:** existing-system civilization only (`lca3-gate-c-existing-system-civilization`)  
**Machine baseline:** [`current-state.v1.yaml`](../specs/current-state.v1.yaml)  
**Noema tracking issue:** [Zero-State-LLC/Noema#661](https://github.com/Zero-State-LLC/Noema/issues/661) — close only after this Specs merge lands; this packet does not instruct an auto-close  
**Does not establish:** Gate D WATCH legibility, Gate E endurance, Gate F successor decision, hosted STUDY, compatibility-at-scale, or a successor deployment decision  
**Does not invent:** a dedicated recovery-receipt schema or fields beyond the OBSERVED Admin recover JSON

## Decision

Acceptance Gate C is complete. Retained Noema evidence for candidate `lca3-gate-c-existing-system-civilization` on the pinned production Worker satisfies the eight coupled paths in [LIVING-ALPHA-ACCEPTANCE.md](LIVING-ALPHA-ACCEPTANCE.md) and [LCA-GATE-C-SCENARIO.md](LCA-GATE-C-SCENARIO.md). Danny human-yes (2026-09-08 PT) authorizes this Specs campaign flip.

Paths 1–7 are accepted from Noema [#664](https://github.com/Zero-State-LLC/Noema/pull/664). Path 8 is accepted from the existing Admin lifecycle recover JSON (Danny-accepted as the Path 8 restart/recovery receipt; no new schema). Dedicated Gate-A-style recovery-receipt objects remain **NOT_COMPUTABLE** and are not invented.

## Canonical evidence

| Evidence | Accepted observation |
|---|---|
| Live Worker | `2c48d671-620a-43df-bb56-87438671e734`, deployed `2026-09-08T09:03:17.074Z` |
| Worker source | Noema `4aedef79259262df411d28cf49d139788939a125` (pin Noema [#660](https://github.com/Zero-State-LLC/Noema/pull/660)) |
| World | `world.perihelion-reach-3` / `genesis.94d0961984b2b4f8` |
| Candidate stub | Noema [#662](https://github.com/Zero-State-LLC/Noema/pull/662) (`docs/evidence/gate-c-2026-09-08/`) |
| Remint Admin ICR | Noema [#663](https://github.com/Zero-State-LLC/Noema/pull/663) — codes `ED58-A179` / `D9D6-9463` / `CB1F-E6BA` (LUDUS / ADVERSARY / VECTOR) |
| Remint Controllers | LUDUS `ctrl.device.f2d32e6656db` / ADVERSARY `ctrl.device.567685259784` / VECTOR `ctrl.device.23d75b3e1b86` |
| Paths 1–7 | PASS — Noema [#664](https://github.com/Zero-State-LLC/Noema/pull/664) (`docs/evidence/gate-c-2026-09-08/civilization-run.md`) |
| Path 8 recover JSON | Danny-accepted existing Admin recover response (no new schema): `recover_mode=restore` `revision=20257` `head_present=true` `reason=gate-c-path8-declared-restart` `operator_session=asess.824cfb77e446` |
| Heads after restore | cycle `17415` / sequence `40949` / `ACTIVE` / `HEALTHY` |
| Client | `noema` / `noema-client` **0.1.22** (cohort OBSERVED; `hosted_live.official_client` still records `0.1.21`) |
| Human-yes | Danny **yes** 2026-09-08 PT for Specs campaign flip |
| Tracking | Noema [#661](https://github.com/Zero-State-LLC/Noema/issues/661) stays open until this Specs merge lands |

Historical Gate B COMPLETE evidence remains Worker `963b5edf-17ea-41f4-892f-130e278e0bb8` / source `308c98de4173874d8a1941818ba4392ddcc2cba6` in [LCA-GATE-B-PROMOTION-2026-09-08.md](LCA-GATE-B-PROMOTION-2026-09-08.md). That packet is not rewritten.

### Path 8 recover JSON (OBSERVED; Danny-accepted receipt)

```json
{"ok":true,"status":"ACTIVE","settlement_health":"HEALTHY","revision":20257,"recover_mode":"restore","head_present":true,"reason":"gate-c-path8-declared-restart","operator_session":"asess.824cfb77e446"}
```

Declared restart used existing Admin lifecycle `INCIDENT` → recover. POST `/ready` held the same heads (`cycle=17415`, `sequence=40949`, `ACTIVE`, `HEALTHY`). This packet records those OBSERVED keys only.

## Requirement disposition (LIVING-ALPHA-ACCEPTANCE Gate C)

1. **Resource or transport pressure changes a decision:** accepted from harvest/lot-cost MOVE and revised TRADE_NOTICE under pressure ([#664](https://github.com/Zero-State-LLC/Noema/pull/664)).
2. **Mastery or specialization creates a meaningful difference:** accepted from FOCUS broker versus engineer and the later construct/office versus exchange paths ([#664](https://github.com/Zero-State-LLC/Noema/pull/664)).
3. **Coordination beats isolation:** accepted from two settled trades plus org membership and office NOTICE ([#664](https://github.com/Zero-State-LLC/Noema/pull/664)).
4. **Social memory affects a later decision:** accepted from post-trade counterpart continuity (later NON_AGGRESSION and a second settled trade) without a universal score ([#664](https://github.com/Zero-State-LLC/Noema/pull/664)).
5. **An organization uses bounded authority:** accepted from Reach Works Co-op `org.reach-works-co-op.4dd0afd6`, Works Steward office, and `ORG_OFFICE_ACT` NOTICE ([#664](https://github.com/Zero-State-LLC/Noema/pull/664)).
6. **Communication constraints affect coordination:** accepted from TRADE_NOTICE / BOARD / CHANNEL / MESSAGE surfaces and `NOT_COLOCATED` AGREEMENT_FORM failure then later success ([#664](https://github.com/Zero-State-LLC/Noema/pull/664)).
7. **Conflict or disruption has a recovery path:** accepted from `CONTEST_DECLARE` ACCESS_CONTEST then `CONTEST_WITHDRAW` with stake forfeit ([#664](https://github.com/Zero-State-LLC/Noema/pull/664)).
8. **State and consequences survive restart:** accepted from declared INCIDENT → lifecycle recover; Danny accepted the existing recover JSON above as the Path 8 receipt (no new schema). Heads held `cycle=17415` / `sequence=40949` `ACTIVE` `HEALTHY` after restore.

### Strategy plurality

At least two viable strategies were observed under the same pins: Strategy A (LUDUS/VECTOR broker, harvest/trade, TRADE_NOTICE/BOARD) and Strategy B (ADVERSARY engineer, construct workshop/route_link, org office + CHANNEL). They differ on specialization, resource/route, construction allocation, organization/access, and communication surface ([#664](https://github.com/Zero-State-LLC/Noema/pull/664)).

### Explicit non-invention (Path 8)

| Item | Status | Authority |
|---|---|---|
| Dedicated Gate-A-style recovery / incident-recover receipt object | **NOT_COMPUTABLE** (not invented) | Path 8 uses the existing Admin recover JSON; Danny yes 2026-09-08 PT |
| New recover schema fields | **Not invented** | Only OBSERVED keys: `ok`, `status`, `settlement_health`, `revision`, `recover_mode`, `head_present`, `reason`, `operator_session` |

## Promotion boundary

Gate C promotion completes LCA-3 existing-system civilization. Campaign machine state advances to **LCA-4** / active **Gate D**. It does not pass Gate D, Gate E, or Gate F. It does not claim endurance (four-hour or 24-hour), open hosted STUDY, thaw deferred breadth, or authorize Deploy / successor cutover.

Noema [#661](https://github.com/Zero-State-LLC/Noema/issues/661) is the runtime tracking issue. Close it only after this Specs merge lands. Do not treat this packet as a Noema auto-close instruction.

## Extension Points

Non-normative evidence-index seams.

- Link each Gate C coupled path to Noema #662 / #663 / #664 and the Path 8 recover JSON without merging Gate D/E/F, endurance, or hosted STUDY claims.
- Keep historical Gate B Worker `963b5edf` notes intact in the Gate B packet and current-state pin notes.
- Verification: confirm Worker UUID and source SHA against live `/version` + Noema `hosted_live` pin; confirm recover JSON keys match the OBSERVED Admin response.
