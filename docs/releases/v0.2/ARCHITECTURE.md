# v0.2 Frontier — Architecture Delta

## Module addition

Add module `frontier_director` to the modular monolith ([MODULE-CONTRACTS.md](../../MODULE-CONTRACTS.md)):

| Field | Contract |
|-------|----------|
| purpose | Enumerate/rank informative situations near capability uncertainty |
| owns_state | request audits, candidate ledgers, plans (research partition) |
| reads | capability primitives, trajectory summaries, genomes, world public digests |
| writes | research-side plans/audits only |
| forbidden | direct WorldState mutation; rewriting evidence/history |
| outputs | frontier-plan, candidate-ledger, audit, replay-context, **proposals** for injection |

## Frontier → World boundary (normative)

```text
Frontier Director
    ↓ proposes (research layer)
Frontier Plan (selected candidates)
    ↓ policy admission
SITUATION_INJECTED  (+ follow-on ENTITY_UPDATE / noise events as needed)
    ↓
World Engine reducers
    ↓
canonical WorldState + Event Ledger
```

| Rule | MUST |
|------|------|
| Selection alone | no world effect |
| Direct WorldState write by Frontier | **forbidden** |
| Only canonical catalog events | mutate world truth |
| Claim-bearing ranker | deterministic; no opaque model |

## Dataflow with existing modules

```text
agent_registry / research_capture → trajectory digests
capability primitives (research) → targets / uncertainty
frontier_director → plan + audit
action_router / operator_api → admit plan as external input
world_engine → SITUATION_INJECTED
observation_engine → partial/noisy/contradictory projections
spectator_projection → public pressure + redacted research overlay
```

## Scheduler interaction

Frontier decisions become eligible at `decision_cycle` ([SCHEDULER.md](../../SCHEDULER.md) phase 6 / external inputs). Admitted injections are ordered with other external inputs before reduce.

## Gamification constraint

Situations appear as natural pressures. Research targets (`target_capabilities`, novelty, control_role) are **research overlay only**, not player UI.

## Extension Points

Non-normative future guidance; this section does not change the contracts or dated outcomes above.

**Seam.** Frontier plan adapters and admission traceability can extend the proposal-to-external-input boundary of the modular monolith.

**Preserved invariants.** Selection alone has no world effect; plans and audits stay research-side, claim-bearing ranking is deterministic, and only admitted canonical events change WorldState. Research target labels stay off Player surfaces.

**Compatibility and promotion.** Version director/ranking and catalog semantics when they change; module wiring does not authorize production injection or bypass existing policy admission and scheduler order.

**Validation expectations.** Trace a selected-but-denied plan, an admitted injection, and repeated replay through decision_cycle ordering; confirm no direct Frontier state writes and redaction of novelty/control-role fields from Player projections.
