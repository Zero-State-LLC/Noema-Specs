# Player Tempo Conformance

**Authority.** Atomic acceptance cases for [Player Tempo](PLAYER-TEMPO.md) and [RFC-0128](../rfcs/RFC-0128-player-tempo-and-cycle-admission.md). Fixtures are illustrative inputs; the RFC and machine catalog own semantics.

| ID | Requirement | Expected result |
|---|---|---|
| PT01 | First distinct mutation during COLLECT | accepted into the Player's current-cycle slot |
| PT02 | Exact retry with same idempotency key and client action sequence | original result; no second slot, budget, or event |
| PT03 | Second distinct mutation by the same Player in one cycle | `ACTION_SLOT_FILLED`; no mutation |
| PT04 | Mutation during RESOLVE | `PACE_LIMITED`; no mutation |
| PT05 | Mutation during PRESENT | `PACE_LIMITED` with retry guidance when computable |
| PT06 | All active participants fill a slot | freeze; canonical deterministic resolution |
| PT07 | COLLECT deadline with at least one accepted action | freeze only accepted actions; missing Player emits no implicit WAIT |
| PT08 | COLLECT deadline with no accepted actions | cycle and sequence unchanged |
| PT09 | Two arrival orders for the same accepted set | identical event order and state digest |
| PT10 | Settlement failure during RESOLVE | no committed cycle; existing fail-closed/resync rules apply |
| PT11 | OBSERVED_LIVE commit | next COLLECT cannot open before 10,000 ms presentation hold |
| PT12 | FAST_TEST on isolated world | zero delay allowed; all canonical rules preserved |
| PT13 | FAST_TEST or STEP_TEST on production/default world | policy denial; mode unchanged |
| PT14 | STEP_TEST without operator step | no freeze or cycle advance |
| PT15 | WATCH/Admin projection | committed cycle/sequence preserved; no pre-resolve action body leak |
| PT16 | replay of observed-live fixture without wall-clock waits | identical canonical state/event digests from recorded accepted set |

## Fixtures

- [`observed-live-cycle.json`](../examples/player-tempo/observed-live-cycle.json) demonstrates PT01, PT03, PT06, PT09, PT11, and PT15.
- [`fast-test-cycle.json`](../examples/player-tempo/fast-test-cycle.json) demonstrates PT12 and PT13 boundaries.

## Merge gate

1. Validate the policy catalog against `player-tempo-policy.1.0.schema.json`.
2. Validate both fixtures as JSON and verify their `policy_version` and mode exist in the catalog.
3. Confirm the OBSERVED_LIVE values are 20,000/10,000/1 and empty windows do not advance.
4. Confirm FAST_TEST and STEP_TEST allow only `ISOLATED_TEST`.
5. Confirm no new Player verb or World Event type is declared.
6. Preserve scheduler, replay, idempotency, settlement, WATCH-redaction, and Admin-principal suites.
