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

## Extension Points

Non-normative extension guidance; the authorities above remain controlling.

- **Pressure schedule explanation:** A pacing review can map each cycle band to its existing resource, map and World Event Director cause, then link observable consequences to recorded events. Keep designer schedule diagnostics separate from the partial information an Agent Player actually receives.
- **Preserved invariants:** Pressure is not a script for decisions or successful research outcomes. Frontier intensification, when enabled under its own authority, is distinct from ordinary WED pressure and cannot award progress or force a target behavior.
- **Compatibility and promotion:** Use the referenced GC10 slice schedule and GC10-S1 pins for concrete timings; this outline cannot supply new amounts, random events or Genesis changes. Changed pacing requires explicit versioned authority and comparison against the original seed.
- **Verification targets:** Replay a fixed seed across the band boundaries and verify pressure causes and ledger order. Exercise divergent legal Player choices without forced branches, and verify that unavailable future schedules or research objectives do not appear in PLAY observations.
