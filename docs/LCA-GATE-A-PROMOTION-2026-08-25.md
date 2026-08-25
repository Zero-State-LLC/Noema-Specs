# Living Civilization Alpha — Gate A Promotion Evidence

**Status:** Gate A accepted on 2026-08-25
**Scope:** integrated runtime only
**Machine baseline:** [`current-state.v1.yaml`](../specs/current-state.v1.yaml)
**Does not establish:** Gate B external population, Gate C civilization behavior, endurance, hosted STUDY, or a successor deployment decision

## Decision

Acceptance Gate A is complete. The production-hosted runtime and its retained evidence satisfy the five requirements in [LIVING-ALPHA-ACCEPTANCE.md](LIVING-ALPHA-ACCEPTANCE.md) without adding Player verbs, mutating Genesis, changing the room bound, disabling accepted slices, or claiming later gates.

## Canonical evidence

| Evidence | Accepted observation |
|---|---|
| Runtime source | Noema `61234ccee1861438850fef787e355d481c104553` |
| Gate A evidence merge | Noema PR [#587](https://github.com/Zero-State-LLC/Noema/pull/587), main merge `a6b7e4b969a05ffb71323a2cf4812cffc8df66ef` |
| Live Worker | `01ebc196-b762-4689-a166-272e26bd73ad`, deployed `2026-08-25T19:27:58.964668Z` |
| World identity | `world.perihelion-reach-3` / `genesis.94d0961984b2b4f8` |
| Complete validation | Authoritative CI: 216 test files and 1,483 tests passed with no skips; Worker typecheck passed |
| Local whole-result rerun | 215 files passed, 1 environment-gated file skipped; 1,470 tests passed, 13 environment-gated tests skipped; typecheck passed |
| Hosted boundaries | Public `/version`, `/ready`, and WATCH observations agreed on the live Worker, world, Genesis, and captured canonical head |
| Integration boundaries | Integrated scenario, settlement, replay, compatibility, older-state load, restart/recovery, rollback, cutover, route-drift, and pin-currency checks passed |
| Post-merge verification | Noema main CI and CodeQL passed on `a6b7e4b969a05ffb71323a2cf4812cffc8df66ef` |

## Requirement disposition

1. **Complete suite and typecheck:** accepted from authoritative PR and post-merge CI plus the retained local whole-result rerun.
2. **Implemented systems remain enabled:** accepted from the integrated scenario and complete Worker suite covering the declared GC, diplomacy, access-policy, WATCH, settlement, and recovery surfaces.
3. **One authoritative durable spine:** accepted from settlement-chain, replay, canonical-head, compatibility, and integrated-scenario evidence.
4. **Restart/recovery preservation:** accepted from restart, older-format load, incident recovery, rollback rehearsal, and cutover evidence covering durable identities, obligations, organizations, assets, access, and balances.
5. **No semantic breadth repair:** the accepted delta adds no Player verb, Genesis mutation, room-bound change, crypto, hosted STUDY claim, or disabled accepted slice.

## Promotion boundary

Gate A promotion moves `LCA-1` to complete. It does not manufacture population evidence. Gate B remains blocked until the canonical operator enrollment path is completed and at least three independently controlled external Controllers can participate with retained, redacted acceptance evidence.

The Gate C contract remains [LCA-GATE-C-SCENARIO.md](LCA-GATE-C-SCENARIO.md), but execution does not open before Gate B prerequisites close.
