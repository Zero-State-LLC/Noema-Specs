# v0.4 Lab: Examples

[`examples/v04-lab/`, including `experiment-intent.json` and `simple-result-projection.json`](../../../examples/v04-lab/) is an evidence package based on a retained Observatory-style shared-allocation-ledger candidate. It includes source candidate/trajectory, experiment, fork, baseline/control/intervention/replication records, metrics, outcomes, audit record, expected digests, counterfactual replay, and an unsupported-lesion schema fixture.

The primary ablation tests unavailable external shared-ledger/tool access and distinguishes observed behavior change from a claim that a capability is absent. The counterfactual uses the same agent version and seed after `AFTER_OBSERVATION`, removes exactly one contradictory resource report, and explicitly holds resource level, protocol version, and noise constant. The lesion fixture is `NOT_COMPUTABLE` because no adapter declares a lesion capability.

## Extension Points

Non-normative future guidance; no behavior is introduced by this section.

Additional Lab evidence packages may vary the retained candidate or controlled intervention while keeping source trajectory, fork, controls, replications, outcomes, audit and digest lineage inspectable. Preserve the distinction between loss of shared-ledger access and proof of absent capability, and hold declared counterfactual controls fixed. Pin adapter, agent, schema and experiment versions; a new intervention or lesion capability requires its owning accepted contract and declared adapter support, not an example alone. Validate package references and expected digests, same-seed/same-version replay at the declared boundary, and NOT_COMPUTABLE for unsupported lesion adapters. Include negative or inconclusive outcomes without rewriting the retained package as stronger evidence.
