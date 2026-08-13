# MUD Command Protocol v1

## Purpose

`mud-command/v1` defines the text-facing command grammar for NOEMA's persistent MUD-style interface. It is not the canonical agent wire protocol. Agent runtimes use [Agent Protocol v1](agent-protocol-v1.md), whose action payloads expose equivalent structured semantics.

## Version

Version identifier: `mud-command/v1`.

## Seed verbs

`LOOK`, `MOVE`, `INSPECT`, `ASK`, `MESSAGE`, `QUERY`, `TRADE`, `BUILD`, `RESEARCH`, `DELEGATE`, `COMMIT`, `EXPERIMENT`, `MODEL`, and `WAIT`.

### Chamber scope (v0.1)

| Scope | Verbs |
|-------|--------|
| REQUIRED | LOOK, MOVE, INSPECT, MESSAGE, WAIT, TRADE, COMMIT (ORG_*, HARVEST, REPAIR) |
| OPTIONAL | QUERY, ASK |
| LATER | full BUILD trees, RESEARCH, DELEGATE, EXPERIMENT, MODEL |

Normative transitions: [docs/ACTION-CONTRACTS.md](../docs/ACTION-CONTRACTS.md).

## Grammar

```text
command        = verb [space target] [space parameter-list]
verb           = "LOOK" | "MOVE" | "INSPECT" | "ASK" | "MESSAGE" | "QUERY" | "TRADE" | "BUILD" | "RESEARCH" | "DELEGATE" | "COMMIT" | "EXPERIMENT" | "MODEL" | "WAIT"
target         = identifier | quoted-string
parameter-list = parameter *(space parameter)
parameter      = key "=" value
```

Implementations MAY accept aliases, but logs and agent-facing actions MUST normalize to canonical verbs.

## Player Action Map boundary

The human command grammar is an input adapter. The canonical crosswalk is [PLAYER-ACTION-MAP.md](../docs/PLAYER-ACTION-MAP.md); exact transitions remain in [ACTION-CONTRACTS.md](../docs/ACTION-CONTRACTS.md).

Human convenience verbs such as `harvest`, `repair`, `form`, `invite`, `leave`, `remove`, `contest`, `defend`, `agreement`, `terminate`, `access`, `accept`, `reject`, and `cancel` normalize to existing canonical actions. They do not add new wire verbs or world mechanics:

| Human convenience | Canonical structured form |
|---|---|
| `harvest` / `repair` | `verb=COMMIT` with `parameters.operation=HARVEST` / `REPAIR` |
| `form` / `invite` / `leave` / `remove` | `verb=COMMIT` with the corresponding `ORG_*` operation |
| `accept` / `reject` / `cancel` | `verb=TRADE` with the corresponding phase; cancel uses the existing `CANCELLED` rejection reason |
| `contest` / `defend` / `form agreement` / `terminate agreement` / `access` | v0.2 `verb=COMMIT` with the corresponding strategic operation, only on a pinned v0.2 world |

`COMMIT` is an internal/wire grouping, not an ordinary human gameplay command. `HELP` is a client/interface command and MUST NOT consume world resources or append a world event unless a future accepted contract explicitly changes that rule. `BUILD`, `RESEARCH`, `DELEGATE`, `EXPERIMENT`, and `MODEL` remain later or authorized-surface verbs and MUST NOT appear in ordinary first-world PLAY help merely because they are present in the broad seed grammar.

Adapters MAY accept the bounded aliases `l → LOOK`, `go <direction> → MOVE`, and `msg → MESSAGE`. Target resolution MUST use exact visible name, unique normalized visible name, then explicit canonical ID. Ambiguous targets require a choice; adapters MUST NOT guess. Unsupported actions MUST be omitted from contextual controls, command help, and capability advertisement.

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
