# First 20 Cycles (Chamber Pacing)

Do not script player decisions. Specify pressure progression only.

| Cycles | Pressure |
|--------|----------|
| 1–3 | Orientation + local scarcity |
| 4–7 | Trade and infrastructure pressure become meaningful ([GC10-FIRST-SLICE.md](GC10-FIRST-SLICE.md) schedule) |
| 8–12 | Information asymmetry + organization incentives ([GC10-S1-PRESSURE.md](GC10-S1-PRESSURE.md) resource at 8, access at 12) |
| 13–16 | World event introduces cross-agent pressure |
| 17–20 | Consequences of earlier investment and trade choices become visible |

This gives implementers a clear pacing target without forcing outcomes.

## Implementation note

Pressure is realized through existing resource economy, World Event Director, and seed layout ([RESOURCE-ECONOMY.md](RESOURCE-ECONOMY.md), [CHAMBER-MAP.md](CHAMBER-MAP.md)). Frontier may intensify later cycles when enabled; it MUST NOT force research outcomes.

## Extension Points (additive, i18n AX R3 Gate B handoff + MUD/PLAY craft per noema-specs-mud-craft)

- **i18n centralization (STRINGS + t() in ui.py/8765 Chamber)**: Keys for "first_20_cycles", "pacing_target", "frontier_intensify". Use t() for pacing notes, frontier in Chamber first-cycles/PLAY surfaces.

- **R3 Chamber (RFC-0120 agent-only Player identity + human S0 withhold)**: Agent pacing and frontier in early cycles. Human S0 separate.

- **Gate B S0-S3 + version comparisons**: Pacing target, frontier intensification rules. Versioned with resource/ chamber systems.

- **AX (semantic/ARIA/keyboard/contrast/live regions per omh patterns + CDP)**: Notes/lists for pacing/frontier with aria-labels, keyboard, live for notes.

- **Plugin atoms / graft / ops / maint-evolve (noema-specs-mud-craft)**: Atoms for pacing packs. Graft for implementation traceability.

- **MUD native interaction / PLAY craft / LCA2 handoff (per noema-specs-mud-craft + MUD-PLAY-CRAFT)**: Native i18n for pacing/frontier in MUD/PLAY early cycles. Handoff to MUD-NATIVE-*, RESOURCE-ECONOMY.md, CHAMBER-MAP.md, PLAYER-*, AGENT-PLAY, LCA2.

- Cross-refs: RESOURCE-ECONOMY.md, CHAMBER-MAP.md, MUD-PLAY-CRAFT.md, noema-specs-mud-craft, ui.py, elevation plan, graft, 8765, R3/Gate B, prior EPs, full list.
