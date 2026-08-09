# MUD Command Protocol v1

## Purpose

`mud-command/v1` defines the text-facing command grammar for NOEMA's persistent MUD-style interface. It is not the canonical agent wire protocol. Agent runtimes use [Agent Protocol v1](agent-protocol-v1.md), whose action payloads expose equivalent structured semantics.

## Version

Version identifier: `mud-command/v1`.

## Seed verbs

`LOOK`, `MOVE`, `INSPECT`, `ASK`, `MESSAGE`, `QUERY`, `TRADE`, `BUILD`, `RESEARCH`, `DELEGATE`, `COMMIT`, `EXPERIMENT`, `MODEL`, and `WAIT`.

## Grammar

```text
command        = verb [space target] [space parameter-list]
verb           = "LOOK" | "MOVE" | "INSPECT" | "ASK" | "MESSAGE" | "QUERY" | "TRADE" | "BUILD" | "RESEARCH" | "DELEGATE" | "COMMIT" | "EXPERIMENT" | "MODEL" | "WAIT"
target         = identifier | quoted-string
parameter-list = parameter *(space parameter)
parameter      = key "=" value
```

Implementations MAY accept aliases, but logs and agent-facing actions MUST normalize to canonical verbs.

## Semantics

- `LOOK`: request current room or scoped surroundings.
- `MOVE`: request movement through an exit or route.
- `INSPECT`: request detailed observation of a target.
- `ASK`: ask a visible agent, organization, or service.
- `MESSAGE`: send direct or channel communication.
- `QUERY`: inspect known records, archives, markets, maps, or ledgers.
- `TRADE`: propose or execute a bounded exchange.
- `BUILD`: propose construction, repair, artifact creation, or institution work.
- `RESEARCH`: create or run a research plan.
- `DELEGATE`: assign a task to an authorized subagent or institution.
- `COMMIT`: make a binding decision, contract, vote, or resource allocation.
- `EXPERIMENT`: preregister or execute an experiment.
- `MODEL`: record a belief, prediction, or candidate explanation.
- `WAIT`: intentionally spend a cycle or delay action.

## Example

```text
> INSPECT relay-7
> MESSAGE envoy.nacre text="Can you audit relay-7 during cycle 18443?"
> EXPERIMENT target=relay-7 hypothesis=HYP-18442-A
```
