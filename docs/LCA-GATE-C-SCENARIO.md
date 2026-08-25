# Living Civilization Alpha — Gate C Scenario Contract

**Status:** campaign acceptance companion
**Authority:** [Living Civilization Alpha Acceptance](LIVING-ALPHA-ACCEPTANCE.md)
**Campaign:** [Perihelion Reach — Living Civilization Alpha](LIVING-CIVILIZATION-ALPHA.md)
**Machine baseline:** [`current-state.v1.yaml`](../specs/current-state.v1.yaml)

This document is not an executable release package, a new Game Completeness slice, or authority to deploy. It defines the evidence contract for Acceptance Gate C using systems that are already specified and implemented.

## Purpose

Gate C proves that existing systems compose into a small Agent Player civilization. It does not add mechanics to make a demonstration easier. A candidate must show that scarcity, specialization, coordination, memory, authority, communication, disruption, and persistence change one another through the existing action, event, state, and projection spine.

A missing executable surface is an integration or runtime defect unless [the residual register](SPEC-GAP-REGISTER-2026-08-25.md) identifies a true open contract. The run must not silently fill a SPEC GAP.

## Prerequisites

A Gate C candidate may begin only when all of the following are recorded:

- Gate A candidate evidence remains honest about what is integrated, deployed, and still unproven;
- Gate B has at least three independently controlled external Agent Players using supported onboarding and command paths;
- the world id, Genesis id, seal constraints, room bound, canonical start head, Worker source and deployed version, Specs pin, official-client or conforming Controller versions, and enabled implemented systems are pinned;
- credential, reconnect, idempotency, contention, recovery, and redaction prerequisites have acceptance evidence;
- planned operator actions and external inputs are declared before the run.

Gate C does not promote `IMPLEMENTED_RUNTIME` to `LIVE_HOSTED` by document existence. Promotion follows observed evidence.

## Non-goals

The candidate must not depend on:

- new canonical Player verbs, action aliases that change semantics, or a second interaction campaign;
- Genesis mutation, reseeding, force-supersession, new rooms, or room-bound expansion;
- crypto, wallets, x402, external settlement, XP, quests, class trees, or v0.8 Phenomena;
- hosted STUDY claims, research scores as Player rewards, or private cognition claims;
- a scalar reputation or trust score as world truth;
- operator-authored strategy, outcome scripting, privileged resource grants, hidden topology disclosure, or target-specific WED pressure;
- a single golden script that all Controllers are instructed to follow.

## Candidate declaration

Before the first Player action, record:

```text
candidate_id
world_id / genesis_id / seal constraints / room bound
specs_git / worker_git / deployed_worker_version
canonical_start_head
Controller package, version, and configuration class for each Player
credential and admission path (redacted)
enabled implemented systems
planned operator interventions and external inputs
restart / recovery checkpoint
WATCH capture method
known production-alpha deltas
```

Humans remain HumanPrincipals who watch, connect, study, authorize, or administer. They are not Players.

## Coupled path checklist

Each item must be exercised through an already implemented Player or operator surface. Evidence must identify the action or condition, the settled consequence, and the later decision it changed.

- [ ] **Resource or transport pressure changes a decision.** Scarcity, route cost, storage, infrastructure condition, or distance causes a Player to change target, timing, exchange terms, route, or allocation. A scripted statement that scarcity mattered is insufficient.
- [ ] **Mastery or specialization creates a meaningful difference.** Ledger-derived practice, recognition, focus, parameter access, quality, eligibility, or maintained assets change a viable choice. No XP, class menu, global level, or research capability score is introduced.
- [ ] **Coordination beats isolation.** Trade, shared repair, service exchange, agreement, or construction produces a result that is materially cheaper, safer, faster, more durable, or otherwise preferable to each Player acting alone.
- [ ] **Social memory affects a later decision.** Evidence-backed dyadic or institutional memory changes caution, counterpart choice, access, agreement, office, or information sharing. No universal score is used, and hidden facts do not leak.
- [ ] **An organization uses bounded authority.** At least one office, agreement, grant, membership rule, or access policy is exercised within its declared scope. An organization label without an authority-bearing decision does not count.
- [ ] **Communication constraints affect coordination.** Relay condition, deterministic delay or failure, board/channel scope, notice persistence, expiry, or addressability changes who knows what and when. Private message text remains private.
- [ ] **Conflict or disruption has recovery.** A contest, breach, infrastructure failure, access dispute, pressure event, or comparable existing disruption creates loss or constraint, followed by a legal recovery, repair, restoration, renegotiation, or compensating strategy.
- [ ] **State and consequences survive restart.** Identities, holdings, obligations, organizations, access state, settled balances, durable messages/notices, constructed or repaired assets, and relevant memory reconstruct consistently after the declared restart or recovery checkpoint.

The checklist is conjunctive. Isolated slice demonstrations do not satisfy Gate C.

## Strategy plurality

At least two materially different strategies must reach a viable continuation state under the same pinned candidate conditions.

A strategy is materially different when it makes different coupled choices about at least three of:

```text
resource source or route
specialization / maintained practice
coordination partner or agreement
construction / repair allocation
organization office or access policy
communication surface or timing
conflict response and recovery
```

The evidence pack must include:

1. a brief pre-run strategy declaration from each Controller that does not reveal private chain-of-thought;
2. the realized action/consequence path;
3. where the strategies diverged;
4. why each remained viable;
5. any dominant script, dead mechanic, operator dependency, or forced convergence observed.

If one script dominates because alternatives are not executable, cannot recover, or never affect state, record an integration defect. Do not repair it by adding breadth during the run.

## Evidence pack

A complete Gate C evidence pack contains:

- candidate declaration and immutable version pins;
- canonical start and end heads plus event/state commitment digests;
- restart and recovery receipts tied to the candidate heads;
- redacted Player transcripts or Agent Protocol action/receipt sequences;
- Controller identities by package/version/configuration class, not private prompts or credentials;
- WATCH capture covering the important public changes and declared unknowns;
- a checklist trace mapping every coupled-path item to settled event, state, receipt, and later decision evidence;
- strategy-plurality comparison and defect log;
- operator actions, external inputs, incidents, exclusions, and redactions;
- a final `PASS`, `FAIL`, or `NOT_COMPUTABLE` verdict with reasons.

Missing evidence is not a pass. If a surface is not deployed, mark the item `NOT_COMPUTABLE` or fail the candidate rather than substituting a unit test.

## Gate C verdict

This contract is the detailed companion to [Living Alpha Acceptance — Gate C](LIVING-ALPHA-ACCEPTANCE.md#gate-c--existing-system-civilization). Gate C passes only when:

- all eight coupled paths are supported by the evidence pack;
- at least two materially different viable strategies are observed;
- at least one bounded institution participates in a consequential decision;
- restart/recovery preserves strategically durable consequences;
- no forbidden fill, undeclared operator script, new verb, Genesis mutation, or hidden-information leak is required.

A Gate C pass does not by itself pass Gate D, E, or F and does not authorize production cutover.

## Extension points

Later gates attach without rewriting this contract:

- **Gate D — WATCH legibility:** consumes the Gate C WATCH capture, public event/state trace, and declared unknowns. It adds blind-review legibility evidence without changing Gate C world behavior.
- **Gate E — Endurance:** repeats or extends the same scenario contract across four-hour and twenty-four-hour windows, adding planned absence, scheduled world-time, incident, restart, and recovery evidence.
- **Gate F — Successor decision:** consumes Gate C–E evidence plus migration, rollback, compatibility, seal, and operator packets to issue `GO`, `NO-GO`, or `NOT_COMPUTABLE`.

A later gate may add stricter evidence requirements. It must not retroactively treat this scenario as authority for new mechanics.
