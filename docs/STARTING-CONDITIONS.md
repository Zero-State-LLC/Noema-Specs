# Starting Conditions (Chamber)

## Design goals

- Support 2, 4, 6, or 10 participants cleanly
- No obvious deterministic starting advantage
- Immediate local scarcity and meaningful first decisions
- Neutral infrastructure that creates early cooperation or contest pressure

## Default genesis elements

- Canonical 10-room map: [`examples/chamber-world/world-seed.json`](../examples/chamber-world/world-seed.json) ([CHAMBER-MAP.md](CHAMBER-MAP.md))
- Shared or nearby resource nodes with limited initial stock (Foundry Corridor, Outer Works)
- Neutral imperfect infrastructure: relay ~70, generator ~60, storage_bay, production_node
- Starting budgets as defined in [RESOURCE-ECONOMY.md](RESOURCE-ECONOMY.md)
- No pre-formed organizations (agents create them)
- Minimal initial knowledge (local room + limited exits)
- Default entry: `room.civic-exchange`
- Deterministic World Event Director schedule that begins mild pressure after a few cycles ([GC10-FIRST-SLICE.md](GC10-FIRST-SLICE.md): cycle 4, relay condition −15)

## Asymmetric starts

Supported only as an explicitly declared mode. Default Chamber is symmetric in opportunity, not in final outcome.

## Pacing handoff

After genesis, pressure progression follows [FIRST-20-CYCLES.md](FIRST-20-CYCLES.md).

## Extension Points

Non-normative future guidance; no new behavioral authority or reopening of accepted/deferred slices.

- **Document-specific seam:** Expand deterministic starting-condition evaluations across the supported participant counts and explicitly declared asymmetric modes.
- **Invariants, compatibility, promotion, and verification:** Preserve limited knowledge, agent-created organizations, opportunity symmetry, and the canonical Chamber seed/pacing pins. New starts require separate versioned Genesis approval, never live reseeding; verify replay, initial observations, scarcity, and early pressure without giving hidden map knowledge.
