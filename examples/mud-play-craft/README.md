# MUD Play Craft — Chamber room projection examples

**Status:** Non-normative presentation fixtures.  
**Authority:** [MUD-PLAY-CRAFT.md](../../docs/MUD-PLAY-CRAFT.md) · Feature B in [MUD-NATIVE-INTERACTION-AND-WORLD-PRESENCE.md](../../docs/MUD-NATIVE-INTERACTION-AND-WORLD-PRESENCE.md)  
**Seed:** [world-seed.json](../chamber-world/world-seed.json) (Chamber 10-room map)  
**Craft item:** C1

## Purpose

Show how Feature B room order + craft STATUS/HAPPENED should *read* for three strategically distinct Chamber rooms, using only seed-backed names, exits, and entities.

These fixtures:

- do **not** change Genesis, verbs, budgets, or settlement;
- do **not** invent entities, exits, or quests;
- are **not** golden reducer trajectories (those remain `examples/v01-seed/`);
- MAY be used as manual QA scripts or future presentation tests.

## Feature B order (reminder)

```text
ROOM NAME
DESCRIPTION
PRESSURE        optional, observable only
HERE
EXITS
STATUS
HAPPENED
COMMAND         / AVAILABLE HERE
```

## Rooms covered

| File | Room | Why |
|------|------|-----|
| [projection-civic-exchange.md](projection-civic-exchange.md) | Civic Exchange | Trade hub, high visibility, no local infra entities |
| [projection-relay-quarter.md](projection-relay-quarter.md) | Relay Quarter | Degrading relay → MESSAGE/repair pressure |
| [projection-foundry-corridor.md](projection-foundry-corridor.md) | Foundry Corridor | Production + resource nodes → HARVEST/REPAIR asymmetry |

## Structured sketch

[agent-observation-layers.sketch.json](agent-observation-layers.sketch.json) maps Feature B layers to conceptual agent fields (**not** a wire schema; RFC required before protocol change).

## Hosted audit

[hosted-play-audit-checklist.md](hosted-play-audit-checklist.md) — advisory C9 checklist for local/isolated/Perihelion inhabit (no reseed).

## QA checklist

For each projection file:

1. Layers appear in Feature B order.
2. DESCRIPTION has no live stock counts or Player lists.
3. PRESSURE is room-local only.
4. EXITS match seed directions + known destination names.
5. STATUS uses only existing budgets (illustrative defaults from seed `budget_defaults`).
6. AVAILABLE HERE ⊆ legal affordances for visible targets (no hidden acts).
7. No research labels, sequence-as-primary-UI, or quest narrator.
