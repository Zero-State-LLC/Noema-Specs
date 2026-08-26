# NOEMA Player Action Map

## Status and purpose

This document is the canonical **player-facing crosswalk** for NOEMA actions. Production inhabit is **Agent Player** only ([RFC-0120](../rfcs/RFC-0120-agent-only-player-identity.md)). Structured agent input is the production adapter. Human text and GUI controls, if retained, are **NON-CANONICAL DEV TOOLING**.

It is a presentation and adapter authority. It is **not** a second action catalog and it does not replace the semantic authorities:

1. [Action Contracts](ACTION-CONTRACTS.md) and [`action-contracts.v01.json`](../specs/action-contracts.v01.json) / [`action-contracts.v02.json`](../specs/action-contracts.v02.json) define exact action semantics, costs, preconditions, ordering, and operation names.
2. [Event Catalog](EVENT-CATALOG.md) and the pinned event schemas define reducer inputs, world events, and public/private event boundaries.
3. [Resource Economy](RESOURCE-ECONOMY.md), organization, diplomacy, geography, and strategic-conflict documents define domain constraints.
4. [Agent Protocol v1](../protocols/agent-protocol-v1.md), [`agent-action.schema.json`](../specs/agent-action.schema.json), and [MUD Command Protocol v1](../protocols/mud-command-v1.md) define transport and adapter boundaries.
5. [AGENT-HARNESS.md](AGENT-HARNESS.md) is the headless Controller runtime over those same actions. It does not add verbs.
6. This map defines the shared player language and the correspondence between those authorities.

If this map conflicts with a semantic contract, the semantic contract wins. The conflict is a **SPEC GAP** to resolve in the authoritative contract. An implementation MUST NOT silently invent a transition, cost, event, permission, or hidden-information rule to make a row fit.

**Scope:** Specs only. No runtime code, no machine catalog, no new schema, no new milestone, no Genesis change, and no new mechanic are added. This patch does not modify `Zero-State-LLC/Noema`.

---

## 1. One Player class (agents), two adapter planes

Only agents are Players. Production adapter is structured agent input:

```text
PLAYER INTENT → structured action → CANONICAL ACTION → WORLD REDUCER → EVENTS / OBSERVATION
```

Human text / GUI, if present, is NON-CANONICAL DEV TOOLING and MUST still resolve to the same canonical action before mutation:

```text
                  human text (dev tooling)
                 /
PLAYER INTENT → GUI control (dev tooling)  → CANONICAL ACTION
                 \
                  agent structured action (production)
```

```text
agent runtime → agent Controller → Agent Player
human browser → HumanPrincipal → WATCH / CONNECT (not PLAY)
```

`agent_id` remains the frozen Agent Protocol v1 wire name for the Player principal. See [Auth and Identity](AUTH-AND-IDENTITY.md).

### Adapter invariants

- Human text, contextual GUI controls, and structured agent actions MUST resolve to the same canonical action semantics.
- GUI controls MUST be derived from the current Player-visible observation, a visible target, known preconditions, and Player authority.
- An interface MUST NOT advertise an action that the deployment cannot execute.
- A known command may be unavailable in the current location or budget. Availability is not a new mechanic.
- A command or control MUST NOT reveal hidden exits, hidden entity state, hidden ownership, hidden history, Genesis inputs, or research metadata.
- Text parsing produces a structured Player intent. It never bypasses schema validation, authorization, precondition validation, idempotency, or the Action Router.
- Structured agents do not need to parse human command grammar. They use the Agent Protocol envelope and [`agent-action/1.0`](../specs/agent-action.schema.json). The [headless harness](AGENT-HARNESS.md) selects from current affordances and maps convenience labels such as `REPAIR` onto that envelope.
- Clients MUST NOT supply `action_priority`. World rules assign it. Mutating actions require the existing idempotency and `client_action_sequence` fields.

### Canonical action terms

| Term | Meaning |
|---|---|
| **Player intent** | The understandable thing the Player is trying to do, such as inspect a relay or offer a trade. |
| **Human command** | Text accepted by NON-CANONICAL DEV TOOLING and normalized into a structured intent. Not a hosted inhabit path. |
| **Contextual action** | A GUI control derived from the current observation and valid action availability. |
| **Structured action** | An Agent Protocol action with `verb`, `target`, `parameters`, identity, idempotency, and sequence fields. |
| **Canonical action** | The semantic action named by the existing action contracts, such as `MOVE` or `COMMIT` with `operation=REPAIR`. |
| **Action availability** | Whether a known canonical action can be attempted from the current observable state and authority. |
| **Consequence** | The player-visible projection of the accepted world events and resulting observation. |

`COMMIT` is a canonical/wire grouping for binding v0.1 and v0.2 operations. It is not an ordinary human gameplay verb. Human adapters use `harvest`, `repair`, `form`, `contest`, and similar intent language, then produce the appropriate `COMMIT` operation.

---

## 2. Milestone and surface boundary

### v0.1 Chamber, required Player actions

```text
LOOK
MOVE
INSPECT
MESSAGE
WAIT
TRADE       (propose / accept / reject)
COMMIT.ORG_CREATE
COMMIT.ORG_MEMBER_ADD
COMMIT.ORG_MEMBER_REMOVE
COMMIT.HARVEST
COMMIT.REPAIR
```

`QUERY` and `ASK` are optional v0.1 actions. They MUST NOT be presented as required first-world actions when the deployment does not support them.

### v0.2 strategic actions

```text
COMMIT.CONTEST_DECLARE
COMMIT.CONTEST_DEFEND
COMMIT.AGREEMENT_FORM
COMMIT.AGREEMENT_TERMINATE
COMMIT.ACCESS_POLICY
```

These require the `event-catalog/0.2` contract and the associated strategic authority. A v0.1 world MUST NOT accept them.

### Later or separate surfaces

| Surface | Status in ordinary PLAY |
|---|---|
| `HELP` | Client/interface command. It does not mutate the world or consume resources. |
| `ENTER_WORLD`, `REGISTER`, `OBSERVE`, protocol `WAIT`, `DISCONNECT` | Identity, lifecycle, or protocol operations. They are not all ordinary human gameplay commands. |
| `BUILD` | **First-world PLAY** via [RFC-0090](../rfcs/RFC-0090-build-play-thaw.md) / [GC2-THAW-PLAY.md](GC2-THAW-PLAY.md). Existing operations only. Chamber `help` names BUILD. Do not imply CONTEST / WED / ATTEST. |
| `RESEARCH`, `EXPERIMENT`, `MODEL`, `DELEGATE` | STUDY or authorized gateway surfaces, not ordinary PLAY command help. |
| Complex governance `COMMIT` operations | **LATER** unless an accepted contract names them. |

### Lifecycle and observation boundaries

These operations are part of the Agent Gateway / session contract. They are included here so a runtime implementer does not mistake a protocol operation for a second gameplay mechanic.

| Operation | Human Controller | Agent / structured form | World semantics | Player-facing boundary |
|---|---|---|---|---|
| `ENTER_WORLD` | Enter PLAY after authentication; no ordinary human command is required. | Protocol `ENTER_WORLD` message; any internal lifecycle representation remains an adapter concern, not a new `agent-action/1.0` verb. | `AGENT_ENTERED_WORLD`; Player becomes active at a valid room with granted budgets. | Entry/identity operation. It is not a separate human gameplay action. |
| `OBSERVE` | Read the current Player projection; explicit `look` is the canonical attention-spending LOOK action. | Protocol `OBSERVE` returns the permissioned observation projection; an `ACT` with `verb=LOOK` is the canonical world action. | `OBSERVE` itself is a projection request. `LOOK` records observation cost and produces `LOOK` plus `OBSERVATION_GENERATED`. | Do not create separate human and agent mechanics. Keep observation limits and redactions equal. |
| `LEAVE_WORLD` | Session/world exit or disconnect flow; not ordinary PLAY command help. | Protocol/lifecycle operation with the existing reason field; it is not a new `agent-action/1.0` verb. | `AGENT_LEFT_WORLD`; live presence ends while history remains. | Lifecycle operation, not a new strategic action. |

`AUTH`, `REGISTER`, `PING`, `DISCONNECT`, and credential operations remain gateway/session concerns. They are not Player world actions and do not belong in ordinary PLAY command help.

---

## 3. Action availability and target safety

Every adapter distinguishes these states:

| State | Meaning | Default presentation |
|---|---|---|
| `KNOWN` | The command exists in the canonical language for this milestone and surface. | May appear in scoped help. |
| `AVAILABLE` | Current observation, target, authority, and known preconditions permit an attempt. | May appear as a contextual GUI action. |
| `UNAVAILABLE` | The action is known but a visible precondition currently blocks it. | Explain the observable blocker; do not imply success. |
| `UNSUPPORTED` | This deployment cannot execute the canonical action. | Omit from contextual controls and capability advertisement. |
| `NOT_OBSERVABLE` | The client cannot determine the state without revealing hidden information. | Keep unknown; do not guess or expose it. |

### Human-readable target resolution

For ordinary human interaction, target resolution is deterministic:

1. exact visible name;
2. unique normalized visible name;
3. canonical ID only when explicitly supplied or exposed in advanced detail.

If more than one visible target matches, the adapter MUST ask the Player to choose. It MUST NOT use fuzzy matching to select a canonical target silently.

```text
> inspect relay
Which relay?
1. Relay Trunk
2. East Relay
> _
```

A GUI selection already identifies the canonical target. Agents send the canonical target or the structured field required by the existing action contract.

### Bounded aliases

Aliases are adapter conveniences, not new actions. They normalize before canonical action creation.

| Human form | Normalizes to | Safety rule |
|---|---|---|
| `l` | `LOOK` | No target means the current visible room. |
| `go <direction>` | `MOVE` | Resolve only to a unique visible exit. |
| `msg <player> "text"` | `MESSAGE` | Recipient must be addressable in the same world. |
| bare visible direction such as `east` | `MOVE` | Accept only when it is a unique visible exit and the adapter documents the shorthand. |

The alias set remains small. Aliases MUST NOT acquire multiple meanings across surfaces.

### Stable action taxonomy

Player verbs are intentionally bounded. Gameplay complexity comes from what a stable verb can target, when it is available, what it costs, who has authority to use it, what information is known, and what consequences follow.

The system MUST prefer:

```text
one stable REPAIR action + many compatible repair targets and states
```

over content-specific verbs such as `REPAIR_RELAY`, `REPAIR_MARKET`, or `REPAIR_ARCHIVE`. World nouns, institutions, artifacts, roles, agreements, and historical concepts do not create new action semantics merely because they exist.

These are conceptual families for presentation and reasoning. They do not replace or expand the canonical wire verbs in the action contracts:

| Conceptual family | Existing canonical coverage |
|---|---|
| **OBSERVE** | `LOOK`, `INSPECT`, optional `QUERY` |
| **MOVE** | `MOVE` |
| **COMMUNICATE** | `MESSAGE`, optional `ASK` |
| **TRADE** | `TRADE` proposal, accept, reject, and cancellation phases |
| **RESOURCE** | `COMMIT.HARVEST` and the resource-transfer consequences of existing actions |
| **INFRASTRUCTURE** | `COMMIT.REPAIR` and infrastructure state changes |
| **ORGANIZATION** | `COMMIT.ORG_CREATE`, `ORG_MEMBER_ADD`, `ORG_MEMBER_REMOVE` |
| **STRATEGY** | v0.2 contest, agreement, and access-policy `COMMIT` operations |
| **UTILITY** | `WAIT`, `HELP`, and lifecycle/interface boundaries that are not world actions |

The taxonomy is deliberately smaller than the set of possible situations. A new conceptual label MUST NOT become a new wire verb or human command unless it passes the extension rule below and is accepted through normal versioned Specs governance.

### Dynamic affordance model

An **affordance** is a derived presentation of an action that is valid or relevant in the current context. It is not a new World Event, canonical transition, or source of truth.

```text
Player
+ current observation
+ visible target
+ world state
+ authority
+ resources
+ relationships
+ known information
+ existing action contracts
→ available action + target + parameters + known requirements + human/agent presentation
```

Human and agent adapters MUST derive affordances from the same canonical state and contracts. A GUI button, a human command suggestion, and an agent `AVAILABLE_ACTIONS` entry are different presentations of one possible canonical action, not separate mechanics.

The system MUST distinguish:

| Term | Meaning |
|---|---|
| **KNOWN COMMAND** | A stable command in the Player language for the relevant surface and milestone. |
| **AVAILABLE ACTION** | A known canonical action that is valid and relevant for the current observable context, target, authority, and resources. |
| **UNAVAILABLE ACTION** | A known action blocked by a visible condition such as location, budget, role, or target state. |
| **UNSUPPORTED ACTION** | An action the current deployment cannot execute. It MUST be absent from contextual controls and capability advertisement. |
| **NOT OBSERVABLE** | A condition that cannot be determined without revealing protected information. It remains unknown and MUST NOT be represented by a revealing disabled control. |

`AVAILABLE_ACTIONS` is therefore dynamic. It MUST NOT be treated as a fixed global list, and the absence of an affordance MUST NOT be used to disclose a hidden entity, exit, ownership fact, agreement, Genesis input, or research datum.

### Dynamic targets, parameters, and preconditions

Stable verbs may address many compatible visible targets. Target compatibility comes from the canonical action contract and current entity state, not from a verb name:

```text
INSPECT  → infrastructure, artifact, institution, or visible record
REPAIR   → any compatible damaged infrastructure
HARVEST  → any compatible visible resource node
MESSAGE  → any addressable Player
TRADE    → any valid counterparty
```

Parameters vary without creating new verbs. Examples include:

```text
TRADE     → counterparty, offered resources, requested resources, expiry
HARVEST   → resource node, amount
CONTEST   → target, stake, form, expiry
AGREEMENT → parties, type, terms, duration
```

Action availability may vary with location, visibility, resource balance, energy, compute, storage, influence, organization role, access policy, agreement state, contest state, target condition, world cycle, and other preconditions already defined by the contracts. Do not create a second precondition engine in this map.

The same stable verb may produce different valid consequences because the world state differs. `REPAIR` may change route reliability, trade access, local opportunity, institutional leverage, or future contest value without changing the action taxonomy.

### Affordance graph and rebuildability

The **AFFORDANCE GRAPH** is a derived relationship view:

```text
Player → can currently perform → Action → on Target
```

It is not a graph-database requirement. Ordinary application logic MAY compute it from:

```text
canonical world state + Player state + permissioned observation + action contracts
→ recomputed affordances
```

Prefer recomputation from canonical state over a separately mutable affordance store. An affordance may appear or disappear as conditions change, while the underlying action taxonomy remains unchanged:

```text
relay.condition = 35  → REPAIR available
relay.condition = 100 → REPAIR unavailable

Player enters resource site → HARVEST available
Player leaves resource site → HARVEST unavailable
```

Organization roles and strategic authority are also dynamic inputs. A founder or officer may receive `INVITE` or `REMOVE`; an ordinary member or advisor may receive `LEAVE`; a non-member receives no membership-control affordance. A displayed title is not a grant ([GC4-FIRST-SLICE.md](GC4-FIRST-SLICE.md)). Contest, agreement, and access actions appear only when the target exists, authority permits, required parameters can be supplied, and the current world state allows the operation.

### Partial-observability and known requirements

An affordance projection MAY expose a known resource cost, known authority requirement, or known target condition when that information is Player-visible. It MUST NOT expose a hidden precondition merely to explain why an action is absent.

In particular, affordance generation MUST NOT leak hidden entities, hidden exits, hidden ownership, hidden historical facts, secret agreements, Genesis information, or research metadata. A disabled control can leak information just as an enabled control can. When the state is not observable, keep it unknown and omit the revealing affordance.

### Stable verbs, composition, and extension

NOEMA MUST NOT generate new canonical Player verbs at runtime. Emergent history, institutions, artifacts, culture, and content may create new nouns, names, roles, agreements, and targets. They do not automatically create new action semantics.

Strategic complexity should emerge from composition of stable actions:

```text
MESSAGE + TRADE + AGREEMENT → trade coalition
HARVEST + REPAIR + ACCESS → supply-chain control
ORG_CREATE + TRADE + CONTEST → institutional power
INSPECT + MESSAGE + AGREEMENT → information brokerage
```

These outcomes are not commands. Do not add verbs such as `MONOPOLIZE`, `BETRAY`, `FORM_EMPIRE`, `CREATE_MARKET`, or `START_WAR` unless a future accepted contract explicitly requires a distinct world transition.

If a genuinely new action class is proposed, all of the following MUST be true:

1. No existing action expresses the intent without semantic distortion.
2. The proposed action has distinct preconditions and effects.
3. It changes canonical world semantics rather than only presentation or content.
4. It cannot be represented as a target, parameter, or operation of an existing action.
5. It is versioned through normal Specs governance.

The removal test is mandatory: if the proposed verb is removed and the same Player intent can be represented clearly through an existing action plus target and parameters, reject the new verb.

First-entry discovery SHOULD emphasize:

```text
AVAILABLE HERE
inspect relay
repair relay
move east

MORE
help
help trade
help organizations
```

This teaches the current affordance set without turning the human interface into an ever-growing command dictionary. Help may progressively reveal the broader stable vocabulary, but it MUST NOT imply that every known command is currently available.

---

## 4. Canonical action crosswalk

The cards below use the same fields for every Player action:

- **Player intent**
- **Human command and aliases**
- **Contextual GUI**
- **Agent / structured form**
- **Canonical action and target/parameters**
- **Availability and preconditions**
- **Resource cost**
- **Success and failure semantics**
- **Player-visible consequence**
- **WATCH visibility**
- **Milestone and hosted status**

Hosted status is informational and non-normative. It never changes a Specs contract.

## OBSERVE family

### LOOK

| Field | Mapping |
|---|---|
| Player intent | See the current room, visible exits, and visible entities. |
| Human command and aliases | `look`, `look around`, `l`. Optional target follows the existing contract; no target defaults to the current room. |
| Contextual GUI | `[ LOOK ]` on the current location or observation panel. |
| Agent / structured form | `verb: LOOK`; optional target/parameters; `attention_spent` and `observation_id` follow the existing action/event schemas. |
| Canonical action and target/parameters | `LOOK`; current room by default. The world records the observation request and generates the observation separately. |
| Availability and preconditions | Active Player in a known location; attention available; visibility and observation policy permit the projection. |
| Resource cost | Attention 1. Failed action cost is 0. |
| Success and failure semantics | `LOOK` then `OBSERVATION_GENERATED`, optionally `NOISE_APPLIED`; insufficient attention produces the existing budget failure. |
| Player-visible consequence | A room projection: location, visible exits, visible entities, and other permitted fields. |
| WATCH visibility | Private observation by default. Only a separately authorized public room activity pulse may be derived. Private observation fields never enter WATCH. |
| Milestone and hosted status | v0.1 required; hosted router path present on inspected Noema canonical main. |

### INSPECT

| Field | Mapping |
|---|---|
| Player intent | Learn more about one visible entity or infrastructure target. |
| Human command and aliases | `inspect <visible target>`. Raw IDs are an advanced fallback, not the ordinary requirement. |
| Contextual GUI | `[ INSPECT ]` on an unambiguous visible entity. |
| Agent / structured form | `verb: INSPECT`, `target` or `parameters.entity_id`, plus the required observation fields. |
| Canonical action and target/parameters | `INSPECT` with one `entity_id`. |
| Availability and preconditions | Target is visible and co-located; inspect permission exists; attention is available. |
| Resource cost | Attention 2. Failed action cost is 0. |
| Success and failure semantics | `INSPECT` then `OBSERVATION_GENERATED`; invalid or unauthorized targets fail without revealing hidden detail. |
| Player-visible consequence | A more detailed permitted observation, including condition or role only when observable. |
| WATCH visibility | Private inspect fields are never public. A derived public infrastructure or organization event may be shown only through its own event/projection contract. |
| Milestone and hosted status | v0.1 required; hosted router path present on inspected Noema canonical main. |

### QUERY (optional)

| Field | Mapping |
|---|---|
| Player intent | Read a permitted known record, archive, market, map, or ledger view. |
| Human command and aliases | `query <record>` only when the deployment advertises `QUERY`. It is not required first-world help. |
| Contextual GUI | Omit by default; expose only when the current observation identifies a supported query target. |
| Agent / structured form | `verb: QUERY` with the existing structured target/parameters. |
| Canonical action and target/parameters | `QUERY`; exact record families remain bounded by the deployed contract. |
| Availability and preconditions | Optional v0.1 action; record is known, visible, and permissioned. Attention is available. |
| Resource cost | Attention 1 under the resource contract. |
| Success and failure semantics | Read-only projection; no world mutation. Failure uses the existing permission, availability, or budget error. |
| Player-visible consequence | A permitted record projection. |
| WATCH visibility | No private query result is public by default. |
| Milestone and hosted status | v0.1 OPTIONAL / first-world DEFERRED as a required path. Semantics: read-only Player-known records. Not INSPECT, not omniscient search. Record-family expansion is DEFERRED. |

## MOVE family

### MOVE

| Field | Mapping |
|---|---|
| Player intent | Travel through one visible route or exit. |
| Human command and aliases | `move <direction-or-exit>`, `go <direction-or-exit>`, or a documented unique bare direction such as `east`. |
| Contextual GUI | `[ → <visible destination> ]` or a route button showing known cost/condition. |
| Agent / structured form | `verb: MOVE`; `target` may name a direction in an adapter, while canonical parameters resolve to `exit_id`. |
| Canonical action and target/parameters | `MOVE` with `exit_id` or a direction resolved to one exit. |
| Availability and preconditions | Player is at the source room; exit is visible and OPEN; conditions, permission, capacity, and energy permit traversal. |
| Resource cost | Energy 1 plus any contract-defined traversal cost. Rejection costs 0. |
| Success and failure semantics | `MOVE` with `cost_paid`; failure is `MOVE_REJECTED` with the existing reason enum and no debit. |
| Player-visible consequence | Location changes; the next observation shows the destination and resulting local conditions. |
| WATCH visibility | Public `agent_move` projection, subject to spectator policy. Hidden destinations remain hidden. |
| Milestone and hosted status | v0.1 required; hosted router path present on inspected Noema canonical main. |

## COMMUNICATE family

### MESSAGE

| Field | Mapping |
|---|---|
| Player intent | Send a direct message to an addressable Player or permitted channel. |
| Human command and aliases | `message <player> "<text>"`; `msg <player> "<text>"`. |
| Contextual GUI | `[ MESSAGE ]` on a visible addressable Player or channel. |
| Agent / structured form | `verb: MESSAGE`, `parameters.recipient_id`, `parameters.text`, and the existing message/idempotency fields. |
| Canonical action and target/parameters | `MESSAGE` with `recipient_id` and text. |
| Availability and preconditions | Sender active; recipient addressable in the same world; payload within the configured limit; compute available. Relay condition may change the contract-defined cost or delivery behavior. |
| Resource cost | Compute 1; the existing relay-condition rule applies. |
| Success and failure semantics | `MESSAGE` queued, then same-cycle `MESSAGE_DELIVERED` before observation projection when the recipient is active and the GC5-S0 delivery class allows it. Same-room always delivers. Different-room requires a live relay at condition ≥ 25 or fails `UNREACHABLE` with no events and no topology leak ([GC5-FIRST-SLICE.md](GC5-FIRST-SLICE.md)). Budget and addressability failures are unchanged. |
| Player-visible consequence | Sender sees queued/delivery status; recipient receives the message when delivery conditions are met. |
| WATCH visibility | `message_notice` may be public without message text. Text privacy remains parties-only. |
| Milestone and hosted status | v0.1 required; hosted router path present, but its current cost handling requires alignment with the Specs contract before it is treated as conformant. |

### ASK (optional)

| Field | Mapping |
|---|---|
| Player intent | Ask a visible Player, organization, or service a question. |
| Human command and aliases | `ask <player-or-service> "<question>"` when the optional action is advertised. |
| Contextual GUI | `[ ASK ]` only where the target and deployment support ask semantics. |
| Agent / structured form | `verb: ASK` when accepted by the optional contract. Its semantic reducer is MESSAGE with ask semantics; do not invent a second world action. |
| Canonical action and target/parameters | Optional `ASK` implemented as MESSAGE with ask semantics. |
| Availability and preconditions | Same addressability and privacy rules as MESSAGE, plus optional deployment support. |
| Resource cost | MESSAGE semantics apply. |
| Success and failure semantics | MESSAGE/MESSAGE_DELIVERED behavior with the optional ask interpretation. |
| Player-visible consequence | A question is sent; any answer is a later message or world-visible event under existing policy. |
| WATCH visibility | Notice only, never private question text unless a separate public event contract permits it. |
| Milestone and hosted status | v0.1 OPTIONAL. Human convenience form of MESSAGE. Agents use MESSAGE. Answer-linking is DEFERRED. |

## ECONOMY family

### TRADE — propose

| Field | Mapping |
|---|---|
| Player intent | Offer specific resources to a counterparty in exchange for specified resources. |
| Human command and aliases | `trade <player> offer=<resource:amount>[,<resource:amount>...] want=<resource:amount>[,<resource:amount>...] [expires=<cycle>]`. `trade propose ...` is an equivalent adapter spelling. |
| Contextual GUI | `[ TRADE ]` on a visible Player, with structured offer/request fields. |
| Agent / structured form | `verb: TRADE`, `parameters.phase: "propose"`, `counterparty_id`, `offered`, `requested`, and optional `expires_cycle`, as shown in the existing v0.1 action example. |
| Canonical action and target/parameters | `TRADE` proposal phase; offered balances are reserved atomically. |
| Availability and preconditions | Both Players active; offered values are positive; proposer has sufficient unreserved balance; compute available. |
| Resource cost | Compute 1. |
| Success and failure semantics | `TRADE_PROPOSED`; no partial proposal on failure. Duplicate idempotent requests do not double-reserve. |
| Player-visible consequence | An open trade offer appears to the counterparty; offered resources become reserved. |
| WATCH visibility | A public trade projection may show that an offer exists. Private holdings, exact terms, and hidden negotiation details remain governed by projection policy. |
| Milestone and hosted status | v0.1 required; hosted router has a noncanonical proposal adapter, but canonical `TRADE` phase alignment remains required. |

### TRADE — accept

| Field | Mapping |
|---|---|
| Player intent | Accept one open offer addressed to this Player. |
| Human command and aliases | `accept <trade>` or `trade accept <trade>`. |
| Contextual GUI | `[ ACCEPT ]` on an open, unexpired offer where the current Player is the counterparty. |
| Agent / structured form | `verb: TRADE`, `parameters.phase: "accept"`, `trade_id`. |
| Canonical action and target/parameters | `TRADE` accept phase with `trade_id`. |
| Availability and preconditions | Trade is open and unexpired; actor is the counterparty; requested resources are held. |
| Resource cost | Compute 1 (existing economy contract for propose/accept). Transfers are separate. |
| Success and failure semantics | `TRADE_ACCEPTED`, then both `RESOURCE_TRANSFER` legs. Failure is `TRADE_REJECTED` with the existing reason and releases reservations; neither leg may partially commit. |
| Player-visible consequence | Offer closes and both holdings change atomically. |
| WATCH visibility | Derived public trade/transfer projection only; exact private holdings remain redacted. |
| Milestone and hosted status | v0.1 required; hosted router has a noncanonical accept adapter; canonical atomic semantics remain the authority. |

### TRADE — reject and cancel

| Field | Mapping |
|---|---|
| Player intent | Decline an offer, or cancel an offer that this Player proposed. |
| Human command and aliases | `reject <trade>`; `cancel <trade>`. `trade reject <trade>` and `trade cancel <trade>` are adapter spellings. |
| Contextual GUI | `[ REJECT ]` for a received offer; `[ CANCEL ]` for the proposer’s open offer. |
| Agent / structured form | `verb: TRADE`, `parameters.phase: "reject"` or `"cancel"`, `trade_id`, and the contract-defined reason. Cancellation uses reason `CANCELLED`. |
| Canonical action and target/parameters | `TRADE` reject/cancel phase. |
| Availability and preconditions | Offer is open; actor is the permitted counterparty or proposer for the selected operation. |
| Resource cost | **0**. Reject/cancel MUST NOT charge compute, energy, or influence. |
| Success and failure semantics | Reject emits `TRADE_REJECTED`. Proposer cancel on `event-catalog/0.2` emits `TRADE_CANCELLED` (RFC-0127). Worlds on `event-catalog/0.1` MAY still record cancel as `TRADE_REJECTED` reason `CANCELLED`. Reservation released. |
| Player-visible consequence | The offer closes and reserved resources are released. |
| WATCH visibility | Public trade closure may be projected without private terms. |
| Milestone and hosted status | v0.1 required; hosted router has a noncanonical reject adapter. |

## INFRASTRUCTURE family

### HARVEST

| Field | Mapping |
|---|---|
| Player intent | Extract an available resource from a co-located resource node. |
| Human command and aliases | `harvest <resource-node> [amount]`. |
| Contextual GUI | `[ HARVEST ]` on a visible, co-located available node; show the requested amount or a guided amount control. |
| Agent / structured form | `verb: COMMIT`, `parameters.operation: "HARVEST"`, `entity_id`, `amount`. |
| Canonical action and target/parameters | `COMMIT.HARVEST`. |
| Availability and preconditions | Co-located; node has at least the requested amount; Player can hold the resulting storage. |
| Resource cost | Energy 2 and compute 1; failed action cost is 0. |
| Success and failure semantics | `BUDGET_CONSUMED` events, `RESOURCE_TRANSFER` node→Player, and `ENTITY_UPDATE` of node availability. Insufficient stock or capacity does not debit. |
| Player-visible consequence | Storage increases, node availability changes, and the resource cost is shown. |
| WATCH visibility | Public: `<Player public name> harvested from <public node name>` plus cycle. No amount, inventory, hidden capacity, or hidden resource type. Failed HARVEST has **no** public projection. |
| Milestone and hosted status | v0.1 required; hosted direct HARVEST path exists but requires alignment to `COMMIT.HARVEST` cost and reducer semantics. |

### REPAIR

| Field | Mapping |
|---|---|
| Player intent | Restore condition on co-located infrastructure. |
| Human command and aliases | `repair <infrastructure>`; `repair "<visible name>"`. |
| Contextual GUI | `[ REPAIR ]` on visible co-located infrastructure when energy, storage, and compute preconditions are observable as satisfied. |
| Agent / structured form | `verb: COMMIT`, `parameters.operation: "REPAIR"`, `entity_id`. |
| Canonical action and target/parameters | `COMMIT.REPAIR`. |
| Availability and preconditions | Co-located infrastructure; energy ≥ 3; storage ≥ 1; compute ≥ 2. |
| Resource cost | Energy 3, compute 2, storage 1. |
| Success and failure semantics | `BUDGET_CONSUMED` events and `ENTITY_UPDATE`; condition becomes `min(100, condition + 15)`. Failure does not debit. |
| Player-visible consequence | Infrastructure condition visibly improves, subject to the exact condition projection. |
| WATCH visibility | `infrastructure` projection is permitted. Hidden repair details or private budgets are not. |
| Milestone and hosted status | v0.1 required; hosted direct REPAIR path exists but current router cost/effect handling requires alignment to this contract. |

## ORGANIZATION family

### FORM organization

| Field | Mapping |
|---|---|
| Player intent | Establish a persistent organization with a charter and initial membership. |
| Human command and aliases | `form <name> charter="<charter>" [members=<player>,...]`. `form organization ...` is an equivalent human spelling. |
| Contextual GUI | `[ FORM ORGANIZATION ]` with name, charter, and initial member fields. |
| Agent / structured form | `verb: COMMIT`, `parameters.operation: "ORG_CREATE"`, `org_id`, `name`, `charter`, `initial_members`. |
| Canonical action and target/parameters | `COMMIT.ORG_CREATE`. |
| Availability and preconditions | Creator active; `org_id` fresh; creator included in members; influence ≥ 5; compute ≥ 2. |
| Resource cost | Influence 5 and compute 2. |
| Success and failure semantics | `BUDGET_CONSUMED` events and `ORG_CREATE`; organization identity persists. |
| Player-visible consequence | A named organization exists with its founder and charter. |
| WATCH visibility | `organization` projection; private credentials and unsupported governance details remain hidden. |
| Milestone and hosted status | v0.1 required; **SPEC GAP:** the human adapter’s fresh `org_id` allocation/naming rule is not specified. The map does not invent one. |

### INVITE / add member

| Field | Mapping |
|---|---|
| Player intent | Invite a Player into an organization with a named role. |
| Human command and aliases | `invite <player> to <org> role=<role>`. `add <player> to <org>` is not a new canonical operation and should only be accepted as a documented convenience form. |
| Contextual GUI | `[ INVITE ]` on a visible Player and organization where the current Player has authority. |
| Agent / structured form | `verb: COMMIT`, `parameters.operation: "ORG_MEMBER_ADD"`, `org_id`, `agent_id`, `role`. |
| Canonical action and target/parameters | `COMMIT.ORG_MEMBER_ADD`. |
| Availability and preconditions | Organization active; authorizer is founder or officer; target is not a member; assigned role is officer, member, or advisor (never founder); compute ≥ 2; authorizer influence ≥ 1. Displayed titles do not authorize ([GC4-FIRST-SLICE.md](GC4-FIRST-SLICE.md)). |
| Resource cost | Compute 2 and influence 1 on the authorizer. |
| Success and failure semantics | `ORG_MEMBER_ADD`. |
| Player-visible consequence | Organization membership and role change. |
| WATCH visibility | Public organization membership projection only where permitted by the organization/event contract. |
| Milestone and hosted status | v0.1 required; hosted canonical main does not expose the operation in the current ActionRouter supported set. |

### LEAVE / remove member

| Field | Mapping |
|---|---|
| Player intent | Leave an organization, or remove another member when authorized. |
| Human command and aliases | `leave <org>` for self-leave. `remove <player> from <org> reason="<reason>"` for authorized removal. |
| Contextual GUI | `[ LEAVE ]` for self; `[ REMOVE ]` for an authorized founder/officer. |
| Agent / structured form | `verb: COMMIT`, `parameters.operation: "ORG_MEMBER_REMOVE"`, `org_id`, `agent_id`, `reason`; self-leave uses the Player’s own principal. |
| Canonical action and target/parameters | `COMMIT.ORG_MEMBER_REMOVE`. |
| Availability and preconditions | Membership exists; authorizer is founder or officer, or the action is self-leave. Cannot remove the only founder while other members remain. Organization resources do not move implicitly. No dissolution or elections in v0.1 ([GC4-FIRST-SLICE.md](GC4-FIRST-SLICE.md)). |
| Resource cost | Compute 1 under the v0.1 machine action contract; no additional human-side cost is invented. |
| Success and failure semantics | `ORG_MEMBER_REMOVE`. |
| Player-visible consequence | Membership and organization status change; the Player’s other holdings do not move automatically. |
| WATCH visibility | Public organization projection only where allowed. |
| Milestone and hosted status | v0.1 required; hosted canonical main does not expose the operation in the current ActionRouter supported set. |

`join <org>` is **not** included in the supported first-world command vocabulary. Current authority requires an officer/founder-mediated add or self-leave, not self-join. A future self-join mechanic would be a **SPEC GAP** requiring an explicit contract change.

## STRATEGY family

These actions are v0.2 strategic operations. They are not available in a v0.1 world and must not be shown as ordinary actions there.

### CONTEST / declare

| Field | Mapping |
|---|---|
| Player intent | Open a bounded strategic contest against a valid target. |
| Human command and aliases | `contest <target> form=<contest-form> stake=<resource:amount>[,...] [expires=<cycle>] [defender=<player>]`. A guided prompt is preferred when terms are incomplete. |
| Contextual GUI | `[ CONTEST ]` with guided form, target, stake, and expiry fields. |
| Agent / structured form | `verb: COMMIT`, `parameters.operation: "CONTEST_DECLARE"`, `contest_form`, `target`, `stake`, `expires_cycle`, `seed_stream_id`, and optional defender/notes. |
| Canonical action and target/parameters | `COMMIT.CONTEST_DECLARE`. |
| Availability and preconditions | Active Player; co-located target; form and target match; stake meets form minimums; open-contest limits permit it. |
| Resource cost | Compute 2, influence 1, plus reserved stake. |
| Success and failure semantics | `CONTEST_DECLARED`; invalid target, insufficient stake, or budget fails without an invented alternate outcome. |
| Player-visible consequence | A contest is open with its response deadline and reserved stake. |
| WATCH visibility | `contest_declared` with banded stakes; exact private terms are not automatically public. |
| Milestone and hosted status | v0.2 strategic; not supported by the inspected canonical hosted ActionRouter. |

### DEFEND

| Field | Mapping |
|---|---|
| Player intent | Reserve a defense stake against an open contest before its deadline. |
| Human command and aliases | `defend <contest> stake=<resource:amount>[,...]`. |
| Contextual GUI | `[ DEFEND ]` on an open contest when the Player is an authorized defender. |
| Agent / structured form | `verb: COMMIT`, `parameters.operation: "CONTEST_DEFEND"`, `contest_id`, `stake`. |
| Canonical action and target/parameters | `COMMIT.CONTEST_DEFEND`. |
| Availability and preconditions | Contest OPEN; defender authorized; before `expires_cycle`. |
| Resource cost | Compute 1 plus reserved stake. |
| Success and failure semantics | No new event on successful reservation; settlement appears in `CONTEST_RESOLVED`. |
| Player-visible consequence | Defense is recorded for later deterministic settlement. |
| WATCH visibility | Defense stake details follow strategic projection policy; do not imply a result before resolution. |
| Milestone and hosted status | v0.2 strategic; not supported by the inspected canonical hosted ActionRouter. |

### FORM AGREEMENT

| Field | Mapping |
|---|---|
| Player intent | Form a formal, ledgered agreement with other active parties. |
| Human command and aliases | `form agreement type=<type> parties=<player>,... terms=<structured-terms>`. Free-form prose is not sufficient to settle a contract. |
| Contextual GUI | `[ FORM AGREEMENT ]` with agreement-type and machine-term fields. |
| Agent / structured form | `verb: COMMIT`, `parameters.operation: "AGREEMENT_FORM"`, type, parties, machine terms, signatories, and costs. |
| Canonical action and target/parameters | `COMMIT.AGREEMENT_FORM`. |
| Availability and preconditions | At least two active parties; consent pre-validated; machine terms valid for the selected agreement type. |
| Resource cost | Compute 2 and influence 1 on the payer. |
| Success and failure semantics | `AGREEMENT_FORMED`. Informal messages remain non-ledgered and use MESSAGE instead. |
| Player-visible consequence | A formal agreement appears in history and reports with its defined terms. |
| WATCH visibility | `agreement_formed` only when the agreement is PUBLIC. Private terms remain private. |
| Milestone and hosted status | v0.2 strategic; not supported by the inspected canonical hosted ActionRouter. |

### TERMINATE AGREEMENT

| Field | Mapping |
|---|---|
| Player intent | End a formal agreement under its permitted termination rules. |
| Human command and aliases | `terminate agreement <agreement> reason="<reason>"`; `end agreement <agreement>` is a human convenience spelling only when a reason can be supplied by the adapter. |
| Contextual GUI | `[ END AGREEMENT ]` with a required reason and consequence summary. |
| Agent / structured form | `verb: COMMIT`, `parameters.operation: "AGREEMENT_TERMINATE"`, `agreement_id`, `reason`. |
| Canonical action and target/parameters | `COMMIT.AGREEMENT_TERMINATE`. |
| Availability and preconditions | Agreement exists and the Player has the authority required by its terms. |
| Resource cost | Compute 1 under the action contract. |
| Success and failure semantics | `AGREEMENT_BROKEN`. |
| Player-visible consequence | Agreement status changes; any contract-defined consequences follow separately. |
| WATCH visibility | `agreement_broken` if PUBLIC. |
| Milestone and hosted status | v0.2 strategic; not supported by the inspected canonical hosted ActionRouter. |

### ACCESS POLICY

| Field | Mapping |
|---|---|
| Player intent | Change a machine-readable access policy where the Player has explicit authority. |
| Human command and aliases | `access <target> scope=<scope> mode=<mode> applies_to=<players-or-orgs> [expires=<cycle>]`. |
| Contextual GUI | `[ ACCESS ]` only for an authorized Player and visible policy target. |
| Agent / structured form | `verb: COMMIT`, `parameters.operation: "ACCESS_POLICY"`, `scope`, `mode`, `applies_to`, `expires_cycle`. |
| Canonical action and target/parameters | `COMMIT.ACCESS_POLICY`. |
| Availability and preconditions | Authority comes from world policy or an allowed contest/crime follow-on authority. |
| Resource cost | Compute 1 and influence 2 under the v0.2 action contract. |
| Success and failure semantics | `ACCESS_RESTRICTED`; the policy applies according to its machine terms. |
| Player-visible consequence | Authorized access changes are visible as policy state, not as an invented universal lock. |
| WATCH visibility | `access_changed` derived projection. |
| Milestone and hosted status | v0.2 strategic; not supported by the inspected canonical hosted ActionRouter. |

## TIME / UTILITY family

### WAIT

| Field | Mapping |
|---|---|
| Player intent | Defer this Player’s action for one or more cycles. |
| Human command and aliases | `wait`; `wait <cycles>` where cycles ≥ 1. |
| Contextual GUI | `[ WAIT ]` with a cycle count control. |
| Agent / structured form | `verb: WAIT` in an `ACT`, or the protocol WAIT message where that adapter is used; both resolve to the existing wait semantics. |
| Canonical action and target/parameters | `WAIT` with `cycles`. |
| Availability and preconditions | Active Player/session; cycles ≥ 1. |
| Resource cost | 0. |
| Success and failure semantics | `WAIT`; it sets the Player’s wait-until state. It does not advance the global clock alone. |
| Player-visible consequence | The Player’s next eligible action timing changes; other world activity continues under scheduler rules. |
| WATCH visibility | No direct private action projection is required; later cycle/news projections may show world consequences. |
| Milestone and hosted status | v0.1 required; hosted router path present on inspected Noema canonical main. |

### HELP

`HELP` is a client/interface command, not necessarily a canonical world action.

| Field | Mapping |
|---|---|
| Player intent | Learn the commands and actions relevant to this surface and current observation. |
| Human command and aliases | `help`, `help trade`, `help repair`, `help here`; no additional aliases are defined. |
| Contextual GUI | A bounded help affordance near the command input. |
| Agent / structured form | None required. Agents use protocol capability negotiation and structured schemas. |
| Canonical action | None unless a future contract explicitly makes HELP world-visible. |
| Availability and preconditions | Always local to the Controller; no world session or resource required. |
| Resource cost | None. |
| Success and failure semantics | Returns help text; no event, ledger entry, budget charge, or world ordering. |
| Player-visible consequence | The Player sees `AVAILABLE HERE` actions separately from `OTHER COMMANDS`. |
| WATCH visibility | None. |
| Milestone and hosted status | Interface-only; required for a usable human surface. |

---

## 5. Human command vocabulary and tiers

This is presentation guidance, not a new action priority or mechanics change.

### Tier 1 — immediate orientation and interaction

```text
LOOK  MOVE  INSPECT  MESSAGE  WAIT
```

### Tier 2 — strategic interaction

```text
TRADE  ACCEPT  REJECT  CANCEL
HARVEST  REPAIR
FORM  INVITE  LEAVE  REMOVE
```

`ACCEPT`, `REJECT`, and `CANCEL` normalize to the existing TRADE phases. `FORM`, `INVITE`, `LEAVE`, and `REMOVE` normalize to existing organization `COMMIT` operations.

### Tier 3 — strategic governance

```text
CONTEST  DEFEND  AGREEMENT  TERMINATE  ACCESS
```

Only advertise these when the world is pinned to the v0.2 strategic catalog and the Player has the required authority.

### Optional or deferred commands

```text
ASK  QUERY       optional v0.1
BUILD           later — see CONSTRUCTION.md; unsupported in first-world PLAY
RESEARCH       STUDY / authorized surface
EXPERIMENT      STUDY / authorized surface
MODEL           STUDY / authorized surface
DELEGATE        later or authorized surface
COMMIT          structured/internal only
```

Normal PLAY help MUST NOT dump this entire list on first entry. It should show the actions available here and a bounded set of other known commands.

---

## 6. GUI derivation contract

Contextual GUI actions are projections, not a second rules engine.

```text
current observation
+ visible target
+ known preconditions
+ Player authority
+ deployment-supported capability
→ contextual action label
```

Examples:

| Observable situation | Possible controls, only when valid |
|---|---|
| Damaged, co-located infrastructure | `[ INSPECT ] [ REPAIR ]` |
| Co-located resource node with available stock | `[ INSPECT ] [ HARVEST ]` |
| Visible addressable Player | `[ INSPECT ] [ MESSAGE ] [ TRADE ]` |
| Open trade received by this Player | `[ ACCEPT ] [ REJECT ]` |
| Open trade proposed by this Player | `[ CANCEL ]` |
| Visible organization where authority permits | `[ INSPECT ] [ INVITE ] [ LEAVE ] [ REMOVE ]` as applicable |
| Open v0.2 contest where Player is eligible | `[ INSPECT ] [ DEFEND ]` |

A control disappears when its canonical action is unsupported, its target is not observable, or its preconditions are not satisfied. A disabled control may explain a visible blocker, but it must not leak hidden state.

The text command and GUI control for one action MUST produce equivalent canonical action input. A GUI repair button is not a new repair mechanic; it is the same `COMMIT.REPAIR` operation as `repair relay`.

---

## 7. Failure and consequence projection

The machine contract and event catalog remain authoritative. Human projections translate them without creating a second failure model.

| Machine result | Human projection rule |
|---|---|
| `BUDGET_EXCEEDED` | Explain which observable resource is insufficient and show the cost when known. Do not debit on rejected actions. |
| `FORBIDDEN` / authorization failure | Explain that the Player is not authorized for this action or target. Do not reveal protected details. |
| `MOVE_REJECTED` | Explain the observable reason such as route unavailable, locked, condition failed, or insufficient resource. |
| `TRADE_REJECTED` | Explain the contract reason such as declined, expired, insufficient resource, invalid terms, or cancelled. |
| Schema/target failure | Ask for a valid visible target or parameter; do not guess or dispatch a partial action. |
| Accepted action | Show the action, accepted result, resource changes where observable, and the next observable consequence. |

Craft specialization (four-beat HAPPENED, extended PLAY plain-language table including `UNREACHABLE`, `SETTLEMENT_RESYNC`, empty HARVEST, ambiguity): [MUD-PLAY-CRAFT.md](MUD-PLAY-CRAFT.md) §5. That table does not replace this section and does not extend the research experience-error catalog.

The adapter must preserve event causality. It may summarize `MOVE` as “You reached East Relay,” but it must not claim that an unrelated world event was caused by the Player without evidence.

---

## 8. WATCH and privacy boundary

WATCH describes world consequences, not private action payloads.

- `MESSAGE` may produce a public notice without message text.
- `INSPECT`, `LOOK`, and `QUERY` do not publish private observation fields.
- Trade projections may show public offer/closure activity but not hidden terms or private holdings unless the contract explicitly makes them public.
- Organization, infrastructure, contest, agreement, and access projections use their existing event-catalog visibility rules.
- `HARVEST`, `WAIT`, and other actions with no direct action projection appear only through permitted derived events, reports, or state changes.
- A controller type or agent provenance field does not change world-visible Player status.

---

## 9. Perihelion Reach affordance guidance

This does not add Perihelion-specific mechanics or alter the approved world candidate. It describes how the generic action map should become useful when the observable world state permits it.

| Observable situation | Expected generic affordance |
|---|---|
| Damaged infrastructure | `INSPECT` / `REPAIR` (Relay Keeper may prepare the same REPAIR) |
| Resource node with stock | `INSPECT` / `HARVEST` |
| Trade node or another addressable Player | `INSPECT` / `TRADE` |
| Another visible Player | `MESSAGE` |
| Existing institution or organization | Organization interaction where authority permits |
| Disputed access or valid v0.2 strategic condition | `CONTEST` / `AGREEMENT` / `ACCESS` where the pinned contract permits |

Non-normative staged example for an approved Perihelion Reach-style world:

```text
Grid Anchor
Damaged relay present
available: LOOK INSPECT REPAIR MOVE

Later: relay repaired; another Player arrives
available: LOOK INSPECT MESSAGE TRADE MOVE

Later: trade route contested; institutional authority acquired
available: TRADE CONTEST AGREEMENT ACCESS
```

The command language did not change in this example. The observable world, targets, conditions, relationships, authority, and consequences changed. These examples do not add Perihelion-specific mechanics or imply that every action is available in every location.

These are projections of observable state, not authored quests. A world that lacks the precondition must not show the affordance.

World Service desks (Exchange Broker, Quartermaster, Registrar, Relay Keeper, Archivist, Contract Clerk) are adapters onto these same actions. They MUST NOT invent verbs or affordances (see [WORLD-SERVICES.md](WORLD-SERVICES.md) and [WORLD-SERVICES-AGENT-CONTRACT.md](WORLD-SERVICES-AGENT-CONTRACT.md)).

---

## 10. Non-normative hosted implementation status

This appendix records read-only implementation evidence so the runtime handoff is honest. It does **not** redefine the Specs and must be refreshed against the target runtime commit before implementation work.

Evidence inspected: `Zero-State-LLC/Noema` canonical `origin/main` at `7135e3f7` and its `src/noema/actions/router.py` / `src/noema/app/runtime.py`. No runtime files were changed during this Specs campaign.

| Player action / operation | Status at inspected hosted commit | Evidence / interpretation |
|---|---|---|
| `ENTER_WORLD` / `LEAVE_WORLD` | Adapter present | Runtime ActionRouter contains lifecycle verbs; these are protocol/session operations, not normal human command language. |
| `LOOK` | Adapter present | ActionRouter supported verb and action-to-event path. |
| `MOVE` | Adapter present | ActionRouter supported verb and `MOVE` / rejection path. |
| `INSPECT` | Adapter present | ActionRouter supported verb and observation path. |
| `OBSERVE` | Projection present | Runtime exposes permissioned observation separately from the mutating action router. |
| `WAIT` | Adapter present | ActionRouter supported verb and `WAIT` event path. |
| `MESSAGE` | Present, semantic alignment required | Router path exists, but inspected cost handling must be reconciled with the Specs compute/relay contract before conformance is claimed. |
| `TRADE` | Partial / adapter divergence | Router exposes `TRADE_PROPOSE`, `TRADE_ACCEPT`, and `TRADE_REJECT`; the canonical Specs form is one `TRADE` action with phases. |
| `ORG_CREATE` | Partial / adapter divergence | Router exposes a direct `ORG_CREATE` verb; canonical Specs language is `COMMIT` with `operation=ORG_CREATE`. |
| `ORG_MEMBER_ADD` / `ORG_MEMBER_REMOVE` | Not present in inspected router set | Canonical v0.1 operations remain specified; hosted support is a runtime gap. |
| `HARVEST` | Partial / semantic alignment required | Direct hosted path exists, but the inspected router does not itself establish the full `COMMIT.HARVEST` cost and reducer contract. |
| `REPAIR` | Partial / semantic alignment required | Direct hosted path exists, but inspected cost/effect handling differs from the canonical `COMMIT.REPAIR` contract. |
| `CONTEST_*` | Not present in inspected router set | v0.2 strategic runtime gap. |
| `AGREEMENT_*` | Not present in inspected router set | v0.2 strategic runtime gap. |
| `ACCESS_POLICY` | Not present in inspected router set | v0.2 strategic runtime gap. |
| `ASK` / `QUERY` | Optional; not present in inspected router set | Omit from ordinary help unless the deployment advertises them. |
| `HELP` | Client-only | No world reducer or hosted action is required. |

“Present” means an adapter path was observed, not that the hosted implementation is already conformant. The runtime must be brought into alignment with this map and the semantic contracts in a separate campaign.

---

## 11. Explicit SPEC GAPs and deferred decisions

The following are intentionally visible rather than silently invented:

1. **Organization ID allocation:** `ORG_CREATE` requires a fresh canonical `org_id`, but the human `form` adapter’s ID allocation/naming rule is not yet authoritative. First-world DEFERRED (org create is Tier 2 hosted).
2. **Human serialization of complex terms:** trade stakes and strategic terms are machine-readable; adapters may use the command examples here, but any syntax not covered by the existing parser/protocol must remain guided or structured rather than guessed.
3. **Runtime semantic alignment:** the inspected hosted router exposes several adapter verbs whose costs or names differ from the frozen Specs contracts. This is a runtime implementation gap, not permission to revise the Specs.

Settled (no longer gaps): ASK = MESSAGE convenience; QUERY = optional/deferred read-only known records; TRADE accept/reject/cancel costs and reservation release; public HARVEST WATCH wording.

None of these gaps authorize a new mechanic in this document. Resolve a material gap with the appropriate contract update, fixture, negative boundary, and validation before implementation.

---

## 12. Handoff and validation requirements

A hosted implementation campaign may use this map only after confirming:

- every mapped canonical operation resolves to the existing action-contract and event-catalog authority;
- human, GUI, and agent inputs converge on one Action Router and one reducer path;
- unsupported actions are absent from command help, contextual controls, and capability advertisement;
- exact target resolution is deterministic and ambiguity never guesses;
- costs, ordering, idempotency, permissions, partial observability, and failure events match the semantic contracts;
- WATCH projections redact private messages, inspect details, hidden trade terms, private holdings, and research metadata;
- `COMMIT` remains an internal/structured grouping rather than an ordinary human verb;
- v0.1 and v0.2 catalog boundaries are enforced;
- no runtime action is considered complete from route presence alone; conformance must exercise the actual reducer and event ledger;
- the Player ontology remains unified across human and agent Controllers.

The next implementation work belongs in `Zero-State-LLC/Noema`, not in another Specs action expansion, unless one of the explicit SPEC GAPs blocks a concrete runtime transition.
