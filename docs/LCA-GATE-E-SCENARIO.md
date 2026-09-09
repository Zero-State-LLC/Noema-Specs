# Living Civilization Alpha — Gate E Scenario Contract

**Status:** campaign acceptance companion. Gate E remains unproven. This companion does not COMPLETE Gate E.
**Authority:** [Living Civilization Alpha Acceptance](LIVING-ALPHA-ACCEPTANCE.md)
**Campaign:** [Perihelion Reach — Living Civilization Alpha](LIVING-CIVILIZATION-ALPHA.md)
**Machine baseline:** [`current-state.v1.yaml`](../specs/current-state.v1.yaml)
**Suggested candidate:** `lca5-gate-e-endurance`
**Tracking:** [Zero-State-LLC/Noema#682](https://github.com/Zero-State-LLC/Noema/issues/682)

This document is not an executable release package, a new Game Completeness slice, or authority to deploy. It defines the evidence contract for Acceptance Gate E using systems that are already specified and implemented. Document existence is not a Gate E COMPLETE claim.

Default candidate id is `lca5-gate-e-endurance`. The naming ladder is Gate B `lca2`, Gate C `lca3`, Gate D `lca4`, Gate E `lca5`. Danny may later lock `lca4` as the Gate E id; until that lock, use `lca5`.

## Purpose

Gate E proves endurance. It does not add mechanics, verbs, or a new civilization scenario to make a long run easier.

A candidate must show that the already integrated live world stays honest under a four-hour run that passes before a 24-hour run opens, and then under a final span of at least 24 continuous hours that includes at least one planned restart or recovery drill **inside** that 24-hour window. Continuous means settlement and identity survive the drill. It does not mean "no restart." Incidents, settlement lag, and stale projections are marked as they occur. Operator interventions stay bounded and logged. They are not used to script the desired outcome.

A missing executable recovery or Controller surface is an integration or runtime defect unless [the residual register](SPEC-GAP-REGISTER-2026-08-25.md) identifies a true open contract. The run must not silently fill a SPEC GAP.

## Prerequisites

A Gate E candidate may begin only when all of the following are recorded:

- Gate D is COMPLETE. Specs [#334](https://github.com/Zero-State-LLC/Noema-Specs/pull/334) (`23987586`) records candidate `lca4-gate-d-watch-legibility` and [LCA-GATE-D-PROMOTION-2026-09-09.md](LCA-GATE-D-PROMOTION-2026-09-09.md). Gate D completion is a prerequisite, not a Gate E pass;
- Gate A, Gate B, and Gate C promotion packets remain recorded and are not rewritten;
- at least three independently controlled external Controllers are connected **before the four-hour clock starts**. Live `/ready` `players: 0` is a **weak** census, not a population proof. Reconnect the Gate B / Gate C trio (or an equivalent independently controlled set) during Prep. A zero-Controller full window that is not labeled `NOT_COMPUTABLE` fails honesty;
- Path 8 style recovery remains available through the existing Admin recover JSON. Do not invent a dedicated recovery-receipt schema. Dedicated Gate-A-style recovery-receipt objects stay **NOT_COMPUTABLE** (not invented);
- the world id, Genesis id, seal constraints, room bound, start and end canonical heads, Worker source and deployed version, Specs pin, Controller/client pins, enabled systems, intervention budget, planned recovery drill, WATCH capture, and evidence digest method are pinned;
- planned operator actions and external inputs are declared during Prep, before Phase A.

Live pins below are **OBSERVED at authoring**. The candidate must re-pin them at run start. Authoring pins are not the run pins.

| Surface | OBSERVED at authoring (2026-09-09) |
|---|---|
| Live Worker | `592c06a4-fa8c-40f6-bec7-21cbc45689f9` |
| Production Deploy | [workflow run 34317120696](https://github.com/Zero-State-LLC/Noema/actions/runs/34317120696) |
| Pin PR | Noema [#681](https://github.com/Zero-State-LLC/Noema/pull/681) `0ff8aaad` |
| Unify source | Noema [#680](https://github.com/Zero-State-LLC/Noema/pull/680) `39d4856a` |
| World / genesis | `world.perihelion-reach-3` / `genesis.94d0961984b2b4f8` |
| Gate D COMPLETE | Specs [#334](https://github.com/Zero-State-LLC/Noema-Specs/pull/334) `23987586` / [LCA-GATE-D-PROMOTION-2026-09-09.md](LCA-GATE-D-PROMOTION-2026-09-09.md) |
| Tracking | [Noema #682](https://github.com/Zero-State-LLC/Noema/issues/682) |

Gate E does not promote `IMPLEMENTED_RUNTIME` to `LIVE_HOSTED` by document existence. Promotion follows observed four-hour, in-window recovery, and 24-hour evidence.

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
- treating `/ready` `players: 0` as a sufficient population census;
- treating a serial recovery **between** the four-hour and 24-hour windows as a substitute for the in-24h drill;
- a Gate E COMPLETE claim from this companion's existence.

A successor decision remains [Gate F](LIVING-ALPHA-ACCEPTANCE.md#gate-f--successor-decision-packet).

## Candidate declaration

During Prep, before the four-hour clock starts, record:

```text
candidate_id                    # default: lca5-gate-e-endurance
                                # naming: Gate B=lca2, C=lca3, D=lca4 → E=lca5
                                # Danny may later lock lca4; until then use lca5
world_id / genesis_id / seal constraints / room bound
specs_git / worker_git / deployed_worker_version
live pins at run start          # re-pin; do not reuse authoring pins as the run pins
start/end canonical heads       # per phase, including across the in-24h drill
recovery receipts               # Path 8 Admin recover JSON; dedicated schema NOT_COMPUTABLE
WATCH capture + evidence digest
Controller/client pins          # ≥3 independently controlled external Controllers
enabled implemented systems
planned operator interventions and intervention budget
intervention log                # class, bound, reason, heads; updated through every phase
planned in-24h recovery drill   # required inside Phase B; Path 8 style
optional inter-window rehearsal # between 4h and 24h; does not substitute
Gate D prerequisite packet      # LCA-GATE-D-PROMOTION-2026-09-09.md / Specs #334
tracking                        # Noema #682
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

### Prep — no clock

Prep does not count toward four-hour or 24-hour duration.

1. Publish stubs for the candidate declaration, evidence-pack index, and intervention log.
2. Record Danny human-yes to start the candidate (not a COMPLETE).
3. Reconnect at least three independently controlled external Controllers. Bind Controller/client pins.
4. Re-pin Worker, Deploy, Specs, world, genesis, and start heads at run start.
5. Freeze the intervention budget. Declare the planned in-24h recovery drill.
6. Confirm WATCH capture method and evidence-digest method.

Do not start the Phase A clock until those items are recorded. `/ready` `players: 0` after Prep is a defect or a `NOT_COMPUTABLE` mark, not a silent start.

### Phase A — four-hour candidate

1. Freeze the Phase A window and starting head.
2. Confirm ≥3 independently controlled external Controllers remain connected.
3. Run at least four continuous hours on the pinned world.
4. Mark incidents, settlement lag, and stale projections as they occur. Do not backfill a clean log.
5. Log every operator intervention with class, bound, and reason ([OPERATOR-INTERVENTIONS.md](OPERATOR-INTERVENTIONS.md)).
6. Record Phase A start/end canonical heads, WATCH capture, and evidence digest.
7. Record Phase A `PASS`, `FAIL`, or `NOT_COMPUTABLE`.

Phase B does not open unless Phase A is `PASS`.

### Phase B — 24-hour candidate with in-window drill

1. Open Phase B only after Phase A `PASS`.
2. Pin the Phase B start head and wall-clock start.
3. Keep the final candidate on the same pinned world for at least 24 continuous hours.
4. Execute **at least one planned restart or recovery drill inside the 24-hour window**. A drill that occurs only between Phase A and Phase B does not satisfy criterion 3.
5. Use the existing Admin recover JSON (Path 8 style). Record the OBSERVED keys as recovery receipts. Do not invent a dedicated recovery-receipt schema. Dedicated recovery-receipt objects remain **NOT_COMPUTABLE**.
6. **Continuous** means settlement and identity survive the drill: identities, holdings, obligations, organizations, access state, settled balances, and relevant notices reconstruct consistently with the declared heads. Continuous does **not** mean "no restart."
7. Keep ≥3 independently controlled external Controllers. If the census drops to zero Controllers for a full window and the packet is not labeled `NOT_COMPUTABLE`, the packet fails honesty.
8. Continue honest incident, lag, and stale marks. Continue the intervention log inside the budget.
9. Record Phase B start/end canonical heads, in-window recover JSON, WATCH capture, and evidence digest.
10. Record Phase B `PASS`, `FAIL`, or `NOT_COMPUTABLE`, then a conjunctive candidate verdict.

A serial recovery between the four-hour and 24-hour windows may be noted as optional extra rehearsal. It does **not** substitute for the in-24h drill unless this companion later says otherwise.

A four-hour pass alone is not Gate E. A 24-hour clock without a prior four-hour pass is not Gate E. A 24-hour clock whose only recovery sits between windows is not Gate E. Calendar elapsed without the evidence pack is not Gate E.

## Honest marking

Criterion 4 is conjunctive with the phases. The packet must mark:

- **Incidents** using existing `World.status` / health overlay language (`ACTIVE` / `PAUSED` / `INCIDENT`; `DEGRADED` / `PLAY_BLOCKED` / `RECOVERY_REQUIRED`). Cite [INCIDENT-RECOVERY.md](INCIDENT-RECOVERY.md). Do not relabel an incident as healthy.
- **Settlement lag** using existing settlement labels (`HEALTHY` / `DEGRADED` / `BLOCKING`). A lag that exceeds the declared bound is marked, not smoothed.
- **Stale projections** on WATCH, Admin Live, or world-report surfaces (`live` / `recent` / `stale` / `unavailable`). A stale public projection is marked stale. It is not rewritten as current.
- **Zero-Controller windows.** `/ready` `players: 0` is a weak census. A full Phase A or Phase B window with fewer than three independently controlled external Controllers must be labeled `NOT_COMPUTABLE` or fail. Leaving it unlabeled fails honesty.

Silence where an incident, lag, stale, or zero-Controller mark was required is a fail. Inventing a cleaner timeline than the receipts show is a fail.

## Operator interventions

Criterion 5 is conjunctive with the phases. Interventions stay inside the closed classes `CONTROL_PLANE` / `WORLD_OPERATION` / `EXTERNAL_INPUT` / `RECOVERY` and inside the Prep intervention budget. Each intervention is:

- declared in the candidate or justified as an incident response;
- bounded in scope and duration;
- logged with operator identity class, time, heads, and reason;
- not used to grant resources, script strategy, hide defects, or force a `PASS`.

An undeclared intervention that changes the desired outcome fails the candidate.

## Evidence pack

A complete Gate E evidence pack contains:

- candidate declaration and immutable version pins at run start (not only authoring pins);
- Gate D COMPLETE prerequisite citation (Specs #334 / `23987586` / [LCA-GATE-D-PROMOTION-2026-09-09.md](LCA-GATE-D-PROMOTION-2026-09-09.md));
- tracking citation [Noema #682](https://github.com/Zero-State-LLC/Noema/issues/682);
- Controller/client pins, reconnect status, and redacted enrollment or binding identity for ≥3 independently controlled external Controllers;
- start and end canonical heads for Prep bind, Phase A, Phase B, and the in-24h drill;
- recovery receipts: existing Admin recover JSON (Path 8 style) for the in-window drill. Dedicated recovery-receipt objects stay `NOT_COMPUTABLE` (not invented);
- WATCH capture and evidence digest for Phase A and Phase B;
- enabled implemented systems and known production-alpha deltas;
- Phase A four-hour continuity evidence and verdict;
- Phase B 24-continuous-hour evidence, including the in-window drill and settlement/identity survival across that drill;
- optional inter-window rehearsal note, if any, marked as non-substituting;
- incident, settlement-lag, stale-projection, and zero-Controller marks for every phase;
- intervention log with budget, bounds, and reasons;
- a final `PASS`, `FAIL`, or `NOT_COMPUTABLE` verdict with reasons.

Missing evidence is not a pass. If a required surface is not deployed, mark the item `NOT_COMPUTABLE` or fail the candidate rather than substituting a unit test.

## Gate E verdict

| Verdict | When to record |
|---|---|
| `PASS` | Prep binds pins and ≥3 Controllers. Phase A four-hour run passes before Phase B opens. Phase B spans at least 24 continuous hours and includes ≥1 planned restart or recovery drill **inside** that window. Settlement and identity survive the drill. Incidents, lag, stale projections, and zero-Controller windows are marked honestly. Interventions stay inside the budget and are not used to script the outcome. Declaration fields are complete. No STUDY claim, Gate F `GO`, Deploy-as-success, new verb, Genesis mutation, invented recovery schema, or undeclared script is required. |
| `FAIL` | Phase A fails; Phase B opens without Phase A `PASS`; the 24-hour span does not show settlement/identity survival; the planned drill is omitted, only between windows, or scripted; marks are dishonest; a zero-Controller full window is unlabeled; or an intervention scripts the desired outcome. |
| `NOT_COMPUTABLE` | Required pins, ≥3 External Controllers, recover JSON, heads, WATCH capture, evidence digest, or continuity evidence cannot be established. Dedicated recovery-receipt objects remain `NOT_COMPUTABLE` and are not invented. Absence of the four-hour pass, the in-24h drill, or the 24-hour span is not a pass. |

A Gate E pass does not by itself pass Gate F and does not authorize production cutover. **Gate E remains unproven.** This companion does not COMPLETE Gate E.

## Extension Points

Non-normative guidance; no runtime, i18n, accessibility, or gate completion is claimed.

### Downstream evidence reuse

Extend a later Gate F successor packet by referencing the same immutable Gate E evidence and the Gate D prerequisite packet. Do not replace either record.

### Preserved invariants

Keep the five acceptance criteria conjunctive. Phase B opens only after Phase A `PASS`. The planned drill is inside the 24-hour window. Continuous means settlement/identity survival across the drill, not "no restart." Path 8 continues to use the existing Admin recover JSON. Dedicated recovery-receipt objects stay `NOT_COMPUTABLE` unless a later packet supplies them without invention. Only agents are Players. Default candidate id stays `lca5` unless Danny locks `lca4`.

### Compatibility and promotion

Later gates may impose stricter evidence but cannot rewrite historical Gate A, Gate B, Gate C, or Gate D verdicts, authorize production cutover, or grant new mechanics. This document does not accept RFC-0130. Document existence is not a Gate E or Gate F COMPLETE claim. Gate E remains unproven.

### Validation fixtures before adoption

Propose a complete pinned four-hour pack plus a 24-hour clock that opened without Phase A `PASS`: the latter cannot pass. A packet whose only recovery sits between the four-hour and 24-hour windows cannot pass. A packet that treats "continuous" as "no restart" cannot pass. A packet that invents a dedicated recovery-receipt schema cannot pass. A packet that hides settlement lag or an unlabeled zero-Controller full window cannot pass. These local completeness cases grant no Gate E–F acceptance.
