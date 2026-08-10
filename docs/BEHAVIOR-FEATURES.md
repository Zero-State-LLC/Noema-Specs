# Behavior Features (v0.3)

Stable intermediate representation between trajectories and detectors.

Catalog: [`specs/behavior-feature-catalog.v03.json`](../specs/behavior-feature-catalog.v03.json).  
Version: `behavior-features/0.3`.

## Families (v0.3)

```text
action_distribution
resource_allocation
movement_exploration
communication
trade_economic
organization_faction
information_seeking
tool_usage
waiting_inaction
repair_infrastructure
cooperation_signal
conflict_rivalry
response_latency_cycles
strategy_persistence
strategy_switching
```

## Per-feature contract

```yaml
feature_id:
version:
input_records: [events, observations, messages, ...]
calculation: deterministic rule
window: { type, cycles }
domain: millipoints_0_1000 | count | rate_milli
normalization: clamp / rank / none
missing_data: NOT_COMPUTABLE | zero_if_empty_window_declared
confounds: []
visibility: research
claim_label: INFERRED
```

No feature is an “intelligence” score. Fixed-point millipoints preferred. Thresholds versioned in catalog.
