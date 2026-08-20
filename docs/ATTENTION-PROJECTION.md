# Attention Projection (v0.2)

Uses v0.1 resource `attention` ([RESOURCE-ECONOMY.md](RESOURCE-ECONOMY.md)). Defaults preserved: grant 8; LOOK costs 1; INSPECT costs 2.

Versioned thresholds in [`specs/attention-projection.v02.json`](../specs/attention-projection.v02.json).

## Deterministic transforms

Let `A` = agent current attention **before** action cost reservation.

| Condition | LOOK result | INSPECT result |
|-----------|-------------|----------------|
| `A ≥ 6` (threshold_full) | full room projection | full allowed entity fields |
| `3 ≤ A < 6` (threshold_reduced) | reduced field set R | reduced inspect set R_i |
| `1 ≤ A < 3` (threshold_minimal) | minimal: room name + exits only | minimal: entity label only |
| `A < cost` | `BUDGET_EXCEEDED`; no observation | same |

### Reduced field set R (LOOK)

Include: `room_id`, `name`, `exits[].direction`, co-located `display_name` list.
Omit: entity state details, infrastructure condition integers, resource node `available`.

### Reduced field set R_i (INSPECT)

Include: `entity_id`, `label`, `entity_type`, condition **band** only.
Omit: exact condition integer, inventory internals, private properties.

### Minimal

Include only identifiers needed to act (room name / entity label). All optional detail omitted.

## Exhaustion

Failed insufficient attention: cost 0 (v0.1 rule). No subjective “quality” language in contracts—only explicit field sets.

## Post-MOVE orientation (craft)

Successful `MOVE` SHOULD carry a destination orientation bundle using the same attention field sets as LOOK **after** MOVE cost reservation, without charging a second LOOK attention debit. Failed MOVE carries no destination bundle. Clients MUST NOT auto-spam LOOK when the current observation already orients this room. Detail: [MUD-PLAY-CRAFT.md](MUD-PLAY-CRAFT.md) §7a. No new verb. If bundling requires ledger/event changes, use the RFC process.
