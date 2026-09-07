# Game Balance Principles

## Structural principles (not numerical perfection)

- Multiple viable strategies exist.
- No single resource or action is universally dominant.
- Expansion creates complexity, maintenance, and exposure.
- Hoarding has opportunity cost.
- Cooperation can outperform isolation in some situations; isolation remains viable in others.
- Information can substitute for raw resources.
- Setbacks create adaptation opportunities ([LOSS-RECOVERY.md](LOSS-RECOVERY.md)).
- No irreversible early-game snowball from one lucky event.
- Strategic choices create real tradeoffs.
- Large Realms become harder to manage, not secretly debuffed.

## Coupling requirement

Isolated mechanics that do not affect other strategic systems are defects ([CORE-GAME-LOOP.md](CORE-GAME-LOOP.md), [GAME-SYSTEM-MAP.md](GAME-SYSTEM-MAP.md)).

**Decision density** and **coupling density** are qualitative gates in [COMPLEXITY-DOCTRINE.md](COMPLEXITY-DOCTRINE.md). Prefer friction that creates decisions over repetitive labor. Prefer one infrastructure concept with many consequences over a private progression tree.

## Extension Points (additive, i18n AX R3 Gate B handoff + MUD/PLAY craft per noema-specs-mud-craft)

- **i18n centralization (STRINGS + t() in ui.py/8765 Chamber)**: Keys for "game_balance", "coupling_requirement", "decision_density", "coupling_density". Use t() for balance tables, coupling notes in Chamber game/strategic surfaces, PLAY.

- **R3 Chamber (RFC-0120 agent-only Player identity + human S0 withhold)**: Agent game balance and coupling in strategic systems. Human S0 separate.

- **Gate B S0-S3 + version comparisons**: Coupling to core loop/system map, decision/coupling density gates. Versioned with COMPLEXITY-DOCTRINE.

- **AX (semantic/ARIA/keyboard/contrast/live regions per omh patterns + CDP)**: Notes/lists for coupling/density with aria-labels, keyboard, live for gates.

- **Plugin atoms / graft / ops / maint-evolve (noema-specs-mud-craft)**: Atoms for balance packs. Graft for coupling traceability.

- **MUD native interaction / PLAY craft / LCA2 handoff (per noema-specs-mud-craft + MUD-PLAY-CRAFT)**: Native i18n for game balance in MUD/PLAY. Handoff to MUD-NATIVE-*, CORE-GAME-LOOP.md, GAME-SYSTEM-MAP.md, COMPLEXITY-DOCTRINE.md, PLAYER-*, AGENT-PLAY, LCA2.

- Cross-refs: CORE-GAME-LOOP.md, GAME-SYSTEM-MAP.md, COMPLEXITY-DOCTRINE.md, MUD-PLAY-CRAFT.md, noema-specs-mud-craft, ui.py, elevation plan, graft, 8765, R3/Gate B, prior EPs, full list.
