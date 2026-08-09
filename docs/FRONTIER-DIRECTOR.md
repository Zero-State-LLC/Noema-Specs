# Frontier Director

## Purpose

The Frontier Director searches capability boundaries by generating or selecting high-information situations near uncertain regions. It increases qualitative complexity, not only scalar difficulty.

## Inputs

Known capabilities, uncertain capability regions, recent failures, recent successes, target capabilities, novelty vectors, resource budgets, safety rules, and prior trajectory summaries.

## Outputs

Candidate situations, mutation plans, experiment priorities, expected information gain, and anti-repetition constraints.

## Requirements

- MUST avoid repeating solved tasks unless running controls or regression checks.
- MUST NOT change world truth to make a hypothesis true.
- SHOULD diversify semantic, causal, social-topology, temporal, tool, epistemic, goal-structure, resource, and constraint novelty.
- MUST record decisions for audit and replay context.
