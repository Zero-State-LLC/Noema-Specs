# Geography

## Hierarchy (minimal)

```text
World
  └── Region          (optional grouping for reports and navigation)
       └── Room / Site
            └── Exit / Route
```

No further hierarchy is required for Chamber or early Frontier. A room is one graph node. Distinct spatial places are new rooms plus exits, never interiors that require a second `MOVE` in the same `room_id` ([ADR-007](../adr/ADR-007-atomic-rooms-intra-room-depth-and-seed-ownership.md)).

## Strategic purposes of geography

Geography must support:

- Movement cost and chokepoints
- Resource distribution
- Infrastructure placement
- Information asymmetry
- Exploration
- Territorial presence
- Trade routes
- Isolation and contested zones

## Key status terms

| Term | Meaning |
|------|---------|
| **known** | Agent has observed the room or has received reliable second-hand information |
| **unknown** | No observation record exists for this agent |
| **accessible** | An OPEN exit path exists from current location under current conditions |
| **blocked** | Exit state is CLOSED, BLOCKED, or condition-failed |
| **controlled** | Sustained presence + infrastructure + organizational authority (see [TERRITORY-CONTROL.md](TERRITORY-CONTROL.md)) |
| **contested** | Multiple actors actively competing for presence or infrastructure control |
| **neutral** | No dominant controller; open access under normal rules |
| **hazardous** | World-event or infrastructure condition that raises costs or risk |

## Design constraints

- Rooms are not decorative. Every room in the Chamber map must declare at least one `strategic_roles` value from `resource | infrastructure | chokepoint | information | trade | starting_position` ([ADR-007](../adr/ADR-007-atomic-rooms-intra-room-depth-and-seed-ownership.md)).
- Exits can carry traversal cost and conditions ([WORLD-ENGINE.md](WORLD-ENGINE.md), [ACTION-CONTRACTS.md](ACTION-CONTRACTS.md) MOVE).
- Hidden or blocked exits create exploration value. Routes, initial visibility, and starting hazards are defined in the seed ([ADR-006](../adr/ADR-006-world-bound-exit-visibility-and-location-discovery.md)).

## Relation to existing seeds

Chamber maps in [`examples/v01-seed/`](../examples/v01-seed/) and [`examples/v01-strategic/`](../examples/v01-strategic/) instantiate this hierarchy with rooms, exits, infrastructure, and resource nodes.
