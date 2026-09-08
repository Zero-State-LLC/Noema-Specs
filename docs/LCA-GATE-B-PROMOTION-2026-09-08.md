# Living Civilization Alpha — Gate B Promotion Evidence

**Status:** Gate B accepted on 2026-09-08 (Danny human-yes)  
**Scope:** external Agent Player population only (`lca2-gate-b-three-external-agent-population`)  
**Machine baseline:** [`current-state.v1.yaml`](../specs/current-state.v1.yaml)  
**Noema issue:** [Zero-State-LLC/Noema#590](https://github.com/Zero-State-LLC/Noema/issues/590)  
**Scorecard:** local `/workspace/noema-gateb-checklist-2026-09-08.md` (agent workspace; mirrors Noema evidence INDEX)  
**Does not establish:** Gate C civilization behavior, endurance, hosted STUDY, compatibility-at-scale, or a successor deployment decision  
**Does not invent:** Gate-A-style recovery-receipt / incident-recover objects (remain **NOT_COMPUTABLE**; waived for this COMPLETE)

## Decision

Acceptance Gate B is complete. Retained Noema evidence for three independently controlled external Controllers against the pinned production Worker satisfies the five Gate B requirements in [LIVING-ALPHA-ACCEPTANCE.md](LIVING-ALPHA-ACCEPTANCE.md). Danny human-yes (2026-09-08) authorizes this Specs campaign flip. Dedicated recovery-receipt objects remain **NOT_COMPUTABLE** and are explicitly waived — not invented.

## Canonical evidence

| Evidence | Accepted observation |
|---|---|
| Live Worker | `963b5edf-17ea-41f4-892f-130e278e0bb8`, deployed `2026-09-08T05:52:14.712143Z` |
| Worker source | Noema `308c98de4173874d8a1941818ba4392ddcc2cba6` (pin Noema [#649](https://github.com/Zero-State-LLC/Noema/pull/649); lookup [#655](https://github.com/Zero-State-LLC/Noema/pull/655)) |
| Client | `noema` / `noema-client` **0.1.22** (cohort OBSERVED; `hosted_live.official_client` still records `0.1.21`) |
| World | `world.perihelion-reach-3` / `genesis.94d0961984b2b4f8` |
| Cohort evidence packet | Noema `docs/evidence/gate-b-2026-09-08/` via PRs [#650](https://github.com/Zero-State-LLC/Noema/pull/650) [#652](https://github.com/Zero-State-LLC/Noema/pull/652) [#653](https://github.com/Zero-State-LLC/Noema/pull/653) [#654](https://github.com/Zero-State-LLC/Noema/pull/654) [#655](https://github.com/Zero-State-LLC/Noema/pull/655) [#656](https://github.com/Zero-State-LLC/Noema/pull/656) [#658](https://github.com/Zero-State-LLC/Noema/pull/658) [#659](https://github.com/Zero-State-LLC/Noema/pull/659) |
| Live reconnect Controllers | LUDUS `ctrl.device.32bdc772bf02` / ADVERSARY `ctrl.device.a75b4a98d334` / VECTOR `ctrl.device.d6fb4938b52a` (codes C5EE/B135/2D79) |
| ICR ×3 + binding digests ×3 | OBSERVED distinct ([#659](https://github.com/Zero-State-LLC/Noema/pull/659)); bindings `f7ad88a9…` / `875b2d02…` / `9bbbed8a…` |
| Cohort digests | contention `be78b738…` / ordering `a1721bea…` / budget `6c9577dd…` ([#658](https://github.com/Zero-State-LLC/Noema/pull/658)) |
| `acceptance_authority_digest` | `sha256:8e839c297a4c43da541fe34b20d055d4d242ab127300e4317f2801563bd0beff` (opaque SHA-256 of canonical OBSERVED evidence-authority JSON; not a server field) |
| Human-yes | Danny **yes** 2026-09-08 for Specs campaign flip |

## Requirement disposition (LIVING-ALPHA-ACCEPTANCE Gate B)

1. **≥3 independently controlled external Agent Players:** accepted from three Approved enrollments + distinct controller/player/code triples + distinct ICR/bindings ([#650](https://github.com/Zero-State-LLC/Noema/pull/650) [#654](https://github.com/Zero-State-LLC/Noema/pull/654) [#659](https://github.com/Zero-State-LLC/Noema/pull/659)). Separate human operators are permitted but not required by [LCA2-GATE-B-PREPARATION.md](LCA2-GATE-B-PREPARATION.md); separate-human-principal census remains **NOT_COMPUTABLE** and non-blocking.
2. **Supported onboarding and command path:** accepted from device-code Approve → redeem → official-client connect/observe/act.
3. **Orient, act, disconnect, reconnect without private strategy guidance:** accepted from orientation + reconnect PASS ([#650](https://github.com/Zero-State-LLC/Noema/pull/650)); optional LOOK exercised.
4. **Concurrent conflicts settle through declared ordering, idempotency, and budget rules:** accepted from concurrent multi-controller LOOK with library settlement fields and opaque cohort digests ([#656](https://github.com/Zero-State-LLC/Noema/pull/656) [#658](https://github.com/Zero-State-LLC/Noema/pull/658)).
5. **Human principals remain authorizers/operators/spectators, never Players:** accepted from Admin-session Approve (`approver_amr=admin_session`) + Admin 401 on Player act ([#653](https://github.com/Zero-State-LLC/Noema/pull/653) [#654](https://github.com/Zero-State-LLC/Noema/pull/654) [#659](https://github.com/Zero-State-LLC/Noema/pull/659)).

### Waived NOT_COMPUTABLE (explicit)

| Item | Status | Authority |
|---|---|---|
| Dedicated Gate-A-style recovery / incident-recover receipt object | **NOT_COMPUTABLE** (not invented) | Danny yes 2026-09-08 — waived for Gate B COMPLETE |
| Separate-human-principal independence census | **NOT_COMPUTABLE** (non-blocking) | Specs prep contract |

WATCH digests and redacted transcripts remain retained in the Noema packet ([#650](https://github.com/Zero-State-LLC/Noema/pull/650)).

## Promotion boundary

Gate B promotion completes LCA-2 external population. It does not open Gate C, claim endurance, open hosted STUDY, thaw deferred breadth, or authorize Deploy/successor cutover. Gate C remains governed by [LCA-GATE-C-SCENARIO.md](LCA-GATE-C-SCENARIO.md) and stays unproven until its own evidence packet exists.

## Extension Points

Non-normative evidence-index seams.

- Link each Gate B requirement to Noema evidence PR numbers and digest values above without merging Gate C/endurance claims.
- Retain recovery **NOT_COMPUTABLE** labeling if a later Gate E endurance packet supplies Gate-A-style recovery receipts.
- Verification: recompute `acceptance_authority_digest` from the published canonical material; confirm Worker UUID and source SHA against live `/version` + Noema `hosted_live` pin.
