# Behavior Shift Detection (v0.3)

A **persistent or meaningful change** relative to earlier behavior under comparable conditions.

Schema: [`specs/behavior-shift-candidate.schema.json`](../specs/behavior-shift-candidate.schema.json).  
Config: [`specs/behavior-shift-config.v03.json`](../specs/behavior-shift-config.v03.json).

## Shift types

```text
strategy_adoption
strategy_abandonment
resource_policy_shift
communication_shift
cooperation_shift
risk_posture_shift
information_seeking_shift
tool_use_shift
organization_role_shift
```

## Rules (defaults, versioned)

| Parameter | Default |
|-----------|---------|
| pre_window_cycles | 20 |
| post_window_cycles | 20 |
| min_magnitude_millipoints | 250 |
| min_persistence_cycles | 10 |
| context | COMPARABLE or CONDITIONALLY_COMPARABLE with declared confounds |

## Forms

* temporary response — fails persistence  
* regime shift — passes magnitude + persistence  
* progressive drift — multi-window monotonic change  
* oscillation — variance high, no sustained mean shift  

Distinguish temporary crisis response from regime shift.
