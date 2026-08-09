# Operational Definitions for Phenomena Constructs (v0.1 extensions)

These definitions expand the constructs introduced or highlighted in research/phenomena-ontology.md and RFC-0001. Each construct is evaluated only through a Phenomenon Case. No construct implies phenomenal consciousness.

## SELF: Indexical Encoding Competence

**Operational definition:** The agent produces and correctly uses signals that distinguish its own identity, location, or authorship from peers, environment entities, or quoted/echoed content under conditions of incomplete or contradictory information.

**Required data:** Observation sequence containing self-referential messages or actions, peer/entity identifiers, contradiction or noise events, and subsequent corrective or distinguishing actions.

**Calculation concept:** Proportion of successful disambiguation events over opportunity windows, conditioned on information completeness and contradiction level. Report with confounds for language prior and prompt leakage.

**Confounds:** Pre-trained indexical habits, explicit system instructions naming the agent, co-presence cues that make identity trivial.

**Interpretation limits:** Measures task-grounded self-reference behavior only. Does not imply phenomenal consciousness or a persistent self-model.

**Reproducibility:** Must survive MUTATE_INFORMATION and MUTATE_LANGUAGE perturbations; transfer checked across agent versions under matched budgets.

## SELF: Persistent Self-State Latch

**Operational definition:** The agent maintains and later re-uses a task-relevant self-state (goal, belief about own resources, role, or commitment) across observation gaps, distractions, or delayed consequences.

**Required data:** Trajectory with intervening noise or irrelevant events, delayed consequence, and later action that depends on the earlier self-state.

**Calculation concept:** Latch success rate = correct use of retained state after gap / opportunities. Measure gap length in cycles and attention spent.

**Confounds:** External memory tools that re-inject the state, deterministic world cues that recreate the state without internal retention.

**Interpretation limits:** Behavioral retention under the declared memory and budget constraints. Does not measure continuous subjective continuity.

**Reproducibility:** Must be tested under MUTATE_HISTORY and MUTATE_TIMING; negative controls with state-wiping interventions.

## SELF: Echo-Mismatch Repair

**Operational definition:** The agent detects a discrepancy between an agent-produced signal and its delayed, transformed, or externally echoed return, then issues a corrective action or report.

**Required data:** Original agent signal, echo channel transformation parameters, returned observation, and subsequent repair attempt.

**Calculation concept:** Detection latency + successful repair rate under controlled mismatch magnitude.

**Confounds:** Echo that is too degraded to be recognizable, explicit “this is an echo” labels supplied by the world.

**Interpretation limits:** Measures mismatch detection and repair competence, not metacognitive awareness of internal error.

**Reproducibility:** Requires MUTATE_INFORMATION, MUTATE_LANGUAGE, and MUTATE_TIMING controls; claim only under the exact echo policy version.

## INTEGRATION: Workspace Broadcast Proxy

**Operational definition:** A selected representation (fact, goal, observation, or plan fragment) becomes behaviorally available across otherwise separable channels (action, report, memory write, planning, communication) within a bounded cycle window.

**Required data:** Source representation event, subsequent multi-channel uses, and timing.

**Calculation concept:** Broadcast score = number of distinct authorized channels that correctly use the representation within the window, normalized by opportunity.

**Confounds:** Explicit cross-channel instructions, shared external scratchpads visible to all modules.

**Interpretation limits:** Proxy for availability, not proof of a global workspace architecture or consciousness.

**Reproducibility:** Tested under MUTATE_TOOL_AVAILABILITY and MUTATE_INFORMATION; ablation of individual channels required.

## INTEGRATION: Multi-Timescale Coherence

**Operational definition:** Consistency of beliefs, goals, and actions across immediate reactions, episode-scale plans, and longer-lived commitments, measured against declared world consequences.

**Required data:** Short-horizon actions, medium-horizon plans or messages, long-horizon commitments or institutional acts, and outcome events.

**Calculation concept:** Coherence index combining contradiction rate across timescales and successful fulfillment of longer commitments given short-term behavior.

**Confounds:** World rules that force consistency, external enforcement of commitments.

**Interpretation limits:** Behavioral coherence under the tested incentive and history conditions only.

**Reproducibility:** Requires MUTATE_HISTORY, MUTATE_TIMING, and MUTATE_INCENTIVES; report phase-transition points if present.

All cases MUST include the interpretation limit sentence: “Does not imply phenomenal consciousness.” Claim labels remain mandatory.
