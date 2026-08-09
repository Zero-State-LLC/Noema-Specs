# ADR-004: World truth isolation from research

## Status
Accepted

## Context
If research interpretation or Frontier Director pressure can rewrite world state, experiments lose internal validity.

## Decision
World Engine is the sole authority for world truth. Research subsystems (Observatory, Experiment Lab, Phenomenon Compiler, Capability Graph, Frontier Director) may select, project, minimize, or label but MUST NOT mutate canonical state. Situation injection occurs only through versioned, ledgered events.

## Consequences
- Clear ownership of reducers.
- Frontier Director becomes a situation selector, not a truth editor.
- Deep Time history remains reliable archaeology.
