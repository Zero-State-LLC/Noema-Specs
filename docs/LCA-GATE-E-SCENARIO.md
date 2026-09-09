# Living Civilization Alpha — Gate E Scenario Contract

**Status:** campaign acceptance companion. Gate E remains unproven. This companion does not COMPLETE Gate E.
**Authority:** [Living Civilization Alpha Acceptance](LIVING-ALPHA-ACCEPTANCE.md)
**Campaign:** [Perihelion Reach — Living Civilization Alpha](LIVING-CIVILIZATION-ALPHA.md)
**Machine baseline:** [`current-state.v1.yaml`](../specs/current-state.v1.yaml)
**Suggested candidate:** `lca4-gate-e-endurance`

This document is not an executable release package, a new Game Completeness slice, or authority to deploy. It defines the evidence contract for Acceptance Gate E using systems that are already specified and implemented. Document existence is not a Gate E COMPLETE claim.

## Purpose

Gate E proves endurance. It does not add mechanics, verbs, or a new civilization scenario to make a long run easier.

A candidate must show that the already integrated live world stays honest under a four-hour run, a planned restart or recovery drill, and then a final span of at least 24 continuous hours. Incidents, settlement lag, and stale projections are marked as they occur. Operator interventions stay bounded and logged. They are not used to script the desired outcome.

A missing executable recovery or Controller surface is an integration or runtime defect unless [the residual register](SPEC-GAP-REGISTER-2026-08-25.md) identifies a true open contract. The run must not silently fill a SPEC GAP.

## Prerequisites

A Gate E candidate may begin only when all of the following are recorded:

- Gate D is COMPLETE. Specs [#334](https://github.com/Zero-State-LLC/Noema-Specs/pull/334) (`23987586`) records candidate `lca4-gate-d-watch-legibility` and [LCA-GATE-D-PROMOTION-2026-09-09.md](LCA-GATE-D-PROMOTION-2026-09-09.md). Gate D completion is a prerequisite, not a Gate E pass;
- Gate A, Gate B, and Gate C promotion packets remain recorded and are not rewritten;
- External Controllers from the Gate B / Gate C trio remain required. If live `/ready` reports `players=0`, reconnect those Controllers before Phase A starts. A zero-player clock is not endurance evidence;
- Path 8 style recovery remains available through the existing Admin recover JSON. Do not invent a dedicated recovery-receipt schema. Dedicated Gate-A-style recovery-receipt objects stay **NOT_COMPUTABLE** (not invented);
- the world id, Genesis id, seal constraints, room bound, canonical head range, Worker source and deployed version, Specs pin, Controller set, planned interventions, and planned recovery drill are pinned;
- planned operator actions and external inputs are declared before Phase A.

Live pins below are **OBSERVED at authoring**. The candidate must re-pin them at run start. Authoring pins are not the run pins.

| Surface | OBSERVED at authoring (2026-09-09) |
|---|---|
| Live Worker | `592c06a4-fa8c-40f6-bec7-21cbc45689f9` |
| Production Deploy | [workflow run 34317120696](https://github.com/Zero-State-LLC/Noema/actions/runs/34317120696) |
| Pin PR | Noema [#681](https://github.com/Zero-State-LLC/Noema/pull/681) `0ff8aaad` |
| Unify source | Noema [#680](https://github.com/Zero-State-LLC/Noema/pull/680) `39d4856a` |
| World / genesis | `world.perihelion-reach-3` / `genesis.94d0961984b2b4f8` |
| Gate D COMPLETE | Specs [#334](https://github.com/Zero-State-LLC/Noema-Specs/pull/334) `23987586` / [LCA-GATE-D-PROMOTION-2026-09-09.md](LCA-GATE-D-PROMOTION-2026-09-09.md) |

Gate E does not promote `IMPLEMENTED_RUNTIME` to `LIVE_HOSTED` by document existence. Promotion follows observed four-hour, recovery, and 24-hour evidence.

## Non-goals

The candidate must not depend on:

- hosted STUDY, research scores as Player rewards, or private cognition claims;
- a Gate F `GO`, successor cutover, or production publication;
- Deploy-as-success: a successful Deploy, calendar elapsed, or this companion's existence is not a Gate E pass;
- new canonical Player verbs, action aliases that change semantics, or a second interaction campaign;
- operator-authored strategy, outcome scripting, privileged resource grants, hidden topology disclosure, or target-specific WED pressure added to force endurance;
- RFC-0130, or any other unaccepted RFC, as a Gate E dependency;
- Genesis mutation, reseeding, force-supersession, new rooms, or room-bound expansion;
- crypto, wallets, x402, external settlement, XP, quests, class trees, or v0.8 Phenomena;
- inventing a dedicated recovery-receipt schema; Path 8 uses the existing Admin recover JSON;
- a Gate E COMPLETE claim from this companion's existence.

A successor decision remains [Gate F](LIVING-ALPHA-ACCEPTANCE.md#gate-f--successor-decision-packet).

## Candidate declaration

Before Phase A starts, record:

```text
candidate_id                    # suggested: lca4-gate-e-endurance
world_id / genesis_id / seal constraints / room bound
specs_git / worker_git / deployed_worker_version
live pins at run start          # re-pin; do not reuse authoring pins as the run pins
canonical_head_range            # start and end heads for each phase
Controller set                  # Gate B/C trio; package, version, configuration class
Controller reconnect status     # required if players=0 at run start
Gate D prerequisite packet      # LCA-GATE-D-PROMOTION-2026-09-09.md / Specs #334
planned operator interventions and external inputs
planned recovery drill          # Path 8 style; existing Admin recover JSON
enabled implemented systems
WATCH capture method
known production-alpha deltas
```

Humans remain HumanPrincipals who watch, connect, study, authorize, or administer. They are not Players.

## Phase protocol

Use already implemented live, Admin recover, and Controller surfaces. Do not add a new endurance mechanic.

This contract is the detailed companion to [Living Alpha Acceptance — Gate E](LIVING-ALPHA-ACCEPTANCE.md#gate-e--endurance). The five acceptance criteria are quoted here without amendment:

1. A four-hour candidate run passes before the 24-hour run opens.
2. The final candidate spans at least 24 continuous hours.
3. At least one planned restart or recovery drill occurs.
4. Incidents, settlement lag, or stale projections are marked honestly.
5. Operator interventions are bounded, logged, and not used to script the desired outcome.

### Phase A — four-hour candidate

1. Pin the candidate declaration. Freeze the Phase A window and starting head.
2. Confirm the Gate B / Gate C External Controller trio is connected. Reconnect if `players=0`.
3. Run at least four continuous hours on the pinned world.
4. Mark incidents, settlement lag, and stale projections as they occur. Do not backfill a clean log.
5. Log every operator intervention with class, bound, and reason ([OPERATOR-INTERVENTIONS.md](OPERATOR-INTERVENTIONS.md)).
6. Record Phase A `PASS`, `FAIL`, or `NOT_COMPUTABLE`.

Phase C does not open unless Phase A is `PASS`.

### Phase B — planned recovery

1. Execute the declared restart or recovery drill after Phase A `PASS`.
2. Use the existing Admin recover JSON (Path 8 style). Record the OBSERVED keys only. Do not invent a dedicated recovery-receipt schema. Dedicated recovery-receipt objects remain **NOT_COMPUTABLE**.
3. Confirm strategically durable identities, holdings, obligations, organizations, access state, settled balances, and relevant notices reconstruct consistently with the declared heads.
4. Mark any incident, lag, or stale projection the drill exposes.
5. Record Phase B `PASS`, `FAIL`, or `NOT_COMPUTABLE`.

An unplanned incident during Phase A or Phase C does not replace the planned drill. Additional recoveries are logged honestly; they do not waive Phase B.

### Phase C — 24-hour candidate

1. Open Phase C only after Phase A `PASS`. Phase B `FAIL` or `NOT_COMPUTABLE` prevents a conjunctive Gate E pass.
2. Pin the Phase C start head and wall-clock start.
3. Keep the final candidate on the same pinned world for at least 24 continuous hours.
4. Keep External Controllers independently controlled. Reconnect and mark any drop to `players=0`.
5. Continue honest incident, lag, and stale marks. Continue bounded intervention logs.
6. Record Phase C `PASS`, `FAIL`, or `NOT_COMPUTABLE`, then a conjunctive candidate verdict.

A four-hour pass alone is not Gate E. A 24-hour clock without a prior four-hour pass is not Gate E. Calendar elapsed without the evidence pack is not Gate E.

## Honest marking

Criterion 4 is conjunctive with the phases. The packet must mark:

- **Incidents** using existing `World.status` / health overlay language (`ACTIVE` / `PAUSED` / `INCIDENT`; `DEGRADED` / `PLAY_BLOCKED` / `RECOVERY_REQUIRED`). Cite [INCIDENT-RECOVERY.md](INCIDENT-RECOVERY.md). Do not relabel an incident as healthy.
- **Settlement lag** using existing settlement labels (`HEALTHY` / `DEGRADED` / `BLOCKING`). A lag that exceeds the declared bound is marked, not smoothed.
- **Stale projections** on WATCH, Admin Live, or world-report surfaces (`live` / `recent` / `stale` / `unavailable`). A stale public projection is marked stale. It is not rewritten as current.

Silence where an incident, lag, or stale mark was required is a fail. Inventing a cleaner timeline than the receipts show is a fail.

## Operator interventions

Criterion 5 is conjunctive with the phases. Interventions stay inside the closed classes `CONTROL_PLANE` / `WORLD_OPERATION` / `EXTERNAL_INPUT` / `RECOVERY`. Each intervention is:

- declared in the candidate or justified as an incident response;
- bounded in scope and duration;
- logged with operator identity class, time, heads, and reason;
- not used to grant resources, script strategy, hide defects, or force a `PASS`.

An undeclared intervention that changes the desired outcome fails the candidate.

## Evidence pack

A complete Gate E evidence pack contains:

- candidate declaration and immutable version pins at run start (not only authoring pins);
- Gate D COMPLETE prerequisite citation (Specs #334 / `23987586` / [LCA-GATE-D-PROMOTION-2026-09-09.md](LCA-GATE-D-PROMOTION-2026-09-09.md));
- Controller set, reconnect status, and redacted enrollment or binding identity;
- Phase A window, start/end heads, and four-hour continuity evidence;
- Phase B planned-recovery evidence: existing Admin recover JSON (Path 8 style) plus reconstructed-state check. Dedicated recovery-receipt objects stay `NOT_COMPUTABLE` (not invented);
- Phase C window, start/end heads, and 24-continuous-hour evidence;
- incident, settlement-lag, and stale-projection marks for every phase;
- operator intervention log with bounds and reasons;
- WATCH or public-head captures sufficient to show the world remained the declared candidate;
- a final `PASS`, `FAIL`, or `NOT_COMPUTABLE` verdict with reasons.

Missing evidence is not a pass. If a required surface is not deployed, mark the item `NOT_COMPUTABLE` or fail the candidate rather than substituting a unit test.

## Gate E verdict

| Verdict | When to record |
|---|---|
| `PASS` | Phase A four-hour run passes, the planned recovery drill occurs, and the final candidate spans at least 24 continuous hours. Incidents, lag, and stale projections are marked honestly. Interventions are bounded, logged, and not used to script the outcome. Pins are complete. No STUDY claim, Gate F `GO`, Deploy-as-success, new verb, Genesis mutation, invented recovery schema, or undeclared script is required. |
| `FAIL` | Phase A fails, Phase C opens without Phase A `PASS`, the 24-hour span is not continuous, the planned drill is omitted or scripted, marks are dishonest, or an intervention scripts the desired outcome. |
| `NOT_COMPUTABLE` | Required pins, External Controllers, recover JSON, or continuity evidence cannot be established. Dedicated recovery-receipt objects remain `NOT_COMPUTABLE` and are not invented. Absence of the four-hour pass, the planned drill, or the 24-hour span is not a pass. |

A Gate E pass does not by itself pass Gate F and does not authorize production cutover. **Gate E remains unproven.** This companion does not COMPLETE Gate E.

## Extension Points

Non-normative guidance; no runtime, i18n, accessibility, or gate completion is claimed.

### Downstream evidence reuse

Extend a later Gate F successor packet by referencing the same immutable Gate E evidence and the Gate D prerequisite packet. Do not replace either record.

### Preserved invariants

Keep the five acceptance criteria conjunctive. Phase C opens only after Phase A `PASS`. Path 8 continues to use the existing Admin recover JSON. Dedicated recovery-receipt objects stay `NOT_COMPUTABLE` unless a later packet supplies them without invention. Only agents are Players.

### Compatibility and promotion

Later gates may impose stricter evidence but cannot rewrite historical Gate A, Gate B, Gate C, or Gate D verdicts, authorize production cutover, or grant new mechanics. This document does not accept RFC-0130. Document existence is not a Gate E or Gate F COMPLETE claim. Gate E remains unproven.

### Validation fixtures before adoption

Propose a complete pinned four-hour pack plus a 24-hour clock that opened without Phase A `PASS`: the latter cannot pass. A packet that omits the planned recovery drill cannot pass. A packet that invents a dedicated recovery-receipt schema cannot pass. A packet that hides settlement lag cannot pass. These local completeness cases grant no Gate E–F acceptance.
