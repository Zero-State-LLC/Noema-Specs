# Experiment Design

A design cannot become `READY` without a research question, source candidate/evidence, registered independent variable, version-pinned dependent measure, controlled variables, intervention, controls, confounds, legal fork point, run count, replication requirement, deterministic stopping and analysis rules, equivalence boundary, authorization, consent, and budgets. Natural language is explanatory, never sole machine authority. Missing/contradictory contract data is `INVALID`; authorized unavailable evidence or computation is `NOT_COMPUTABLE`.

Budgets declare `max_runs`, `max_cycles`, `max_agents`, `max_tool_calls`, `max_compute`, `max_storage`, and advisory `max_wall_time_advisory`. Claim-bearing limits use counters. `experiment-plan/0.4` is an immutable explicit DAG containing baseline, controls, intervention, replications, and analysis. Deterministic queue order is `order`, then `node_id`; retries are new linked attempts; cancellation is audited; exhaustion yields `PARTIAL` plus unexecuted IDs.

## Extension Points

Non-normative design-validation and plan-inspection seams in authorized STUDY/Lab.

- Extend validation diagnostics for missing controls, legal fork points, pinned measures, consent and declared budgets. Preserve INVALID for contradictory contract data and NOT_COMPUTABLE for authorized unavailable evidence/computation; a design assistant cannot infer missing machine authority from prose.
- Keep immutable experiment-plan/0.4 DAGs, deterministic order then node_id queueing, linked retry attempts and audited cancellation. Advisory wall time never replaces claim-bearing counters. Agent-only Player identity does not bar separately authorized human researchers from design work or turn experiments into Player actions.
- Compatibility/promotion: additional templates or budgets need versioned contract review; READY and later interpretation require their stated evidence, not Controller enrollment or ACCESS slice tiers. Lab work remains isolated from canonical PLAY.
- Verification proposal: test equal-order tie breaking, budget exhaustion yielding PARTIAL with unexecuted IDs, missing replication requirements and a canceled/retried node. A keyboard-readable DAG/table should expose dependencies, counters and reason codes without mutating the plan or claiming unexecuted work succeeded.
