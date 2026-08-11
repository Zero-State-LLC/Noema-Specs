# v0.4 Lab: Examples

[`examples/v04-lab/`, including `experiment-intent.json` and `simple-result-projection.json`](../../../examples/v04-lab/) is an evidence package based on a retained Observatory-style shared-allocation-ledger candidate. It includes source candidate/trajectory, experiment, fork, baseline/control/intervention/replication records, metrics, outcomes, audit record, expected digests, counterfactual replay, and an unsupported-lesion schema fixture.

The primary ablation tests unavailable external shared-ledger/tool access and distinguishes observed behavior change from a claim that a capability is absent. The counterfactual uses the same agent version and seed after `AFTER_OBSERVATION`, removes exactly one contradictory resource report, and explicitly holds resource level, protocol version, and noise constant. The lesion fixture is `NOT_COMPUTABLE` because no adapter declares a lesion capability.
