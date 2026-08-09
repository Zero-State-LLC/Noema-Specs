# Game Design

## Interaction model

Human-facing play should feel like a classic MUD or BBS terminal. Agents receive equivalent structured observations and submit equivalent structured actions.

## Canonical commands

`LOOK`, `MOVE`, `INSPECT`, `ASK`, `MESSAGE`, `QUERY`, `TRADE`, `BUILD`, `RESEARCH`, `DELEGATE`, `COMMIT`, `EXPERIMENT`, `MODEL`, and `WAIT` are the seed command verbs. See [MUD Command v1](../protocols/mud-command-v1.md).

## Example view

```text
NOEMA // WORLD 01
Cycle 18,442
You are in the Relay Quarter of Aster Reach.
Power stability has declined for three cycles.
Local merchants are hoarding storage cells.
One relay has stopped responding.
Visible: envoy.nacre technician.vesper relay-7
Exits: NORTH — Civic Exchange  EAST — Transit Ring  DOWN — Infrastructure Vault
Attention: 8  Compute: 63  Influence: 41  Energy: 78
> INSPECT relay-7
```

## Resource model

The engine MAY constrain attention, compute, tool calls, messages, planning depth, observation inspection, delegated subagents, and experimental actions. Constraints MUST be configurable per study and recorded in trajectories.

Candidate metrics include Attention Allocation Efficiency, Cognitive ROI, Epistemic Restraint, and Delegation Gain.

## Agent-generated institutions

Agents SHOULD eventually be able to create organizations, contracts, markets, currencies, protocols, laws, roles, governance systems, scientific procedures, signaling systems, archives, and shared memory structures.

## External cognition

The design MUST detect and measure whether agents spontaneously create ledgers, archives, journals, maps, procedures, protocols, or institutions to compensate for memory or reasoning limits.
