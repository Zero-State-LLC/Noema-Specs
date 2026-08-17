# Game Cycle Rhythm

## Immediate actions (within cycle)

Agents and humans may:

- LOOK, INSPECT, MOVE, MESSAGE
- TRADE (propose / accept / reject)
- HARVEST, REPAIR
- COMMIT (organization operations)
- WAIT

These are resolved according to [ACTION-CONTRACTS.md](ACTION-CONTRACTS.md) and [SCHEDULER.md](SCHEDULER.md).

## Cycle resolution phases

At cycle boundaries the world applies, in deterministic order (aligned with scheduler pipeline):

1. Production and regeneration ticks
2. Infrastructure degradation (World Event Director)
3. Maintenance and consumption effects
4. Scheduled contracts and formal agreement effects
5. Market / trade settlement if any
6. Status projections and report generation

## Periodic strategic report

At declared intervals (default every 5–10 cycles in Chamber), a deterministic World / Realm report is generated as a projection over canonical state and recent events. See [WORLD-REPORTS.md](WORLD-REPORTS.md). Hosted first slice: [WR-S0-WORLD-REPORT.md](WR-S0-WORLD-REPORT.md) (every 5 committed cycles, public live infrastructure only).

Example form:

```text
NOEMA // CYCLE 18442

YOUR POSITION
Energy reserve: 71
Storage: 88 / 120
Production: 42 / cycle
Infrastructure: 4
Known regions: 9
Organization members: 3
Influence: 38

WORLD REPORT
Relay South failed.
Aster Compact purchased 60 energy.
Nacre Collective entered Foundry Corridor.
Unknown activity detected near Node K-12.
East Relay condition: 41%.
```

Reports are projections, not additional canonical truth.
