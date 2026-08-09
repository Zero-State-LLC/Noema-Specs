# Replay Protocol v1

## Purpose

`replay-protocol/v1` defines replay requests, replay boundaries, divergence reporting, and equivalence criteria.

## Replay inputs

A replay MUST declare world seed, world version, protocol versions, deterministic config, initial state or snapshot, ordered event ledger, and equivalence boundary.

## Replay modes

- Deterministic world replay.
- Deterministic protocol replay.
- Stochastic agent replay.
- Behavioral equivalence replay.

## Request shape

```json
{
  "protocol": "replay-protocol/v1",
  "request_id": "replay-001",
  "world_id": "world-01",
  "from_cycle": 18440,
  "to_cycle": 18444,
  "inputs": {
    "world_seed": "noema-example-seed",
    "world_version": "world/v1",
    "protocol_versions": ["agent-protocol/v1", "mud-command/v1", "event-ledger/v1"],
    "deterministic_config": true,
    "ledger_uri": "bundle://original-trajectory.jsonl"
  },
  "equivalence_boundary": {
    "mode": "world-state-digest",
    "required_fields": ["room_states", "resource_balances", "message_delivery"]
  }
}
```

## Divergence report

A divergence report MUST include cycle, event id if known, expected digest, observed digest, equivalence boundary, replay mode, and whether the divergence invalidates the claim.
