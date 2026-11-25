# RFC-0133 — Quartermaster treasury hold and SUPPLY

## Status

**Accepted**

Owner approval: Danny, in chat, 2026-11-25 ("quartermaster should have its own rules since is system agent. needs to be able to provide services for agents in game", then "ok continue" on options A + C).

Intent: [2026-11-25-quartermaster-services](../intent/2026-11-25-quartermaster-services.md). Spec: [quartermaster-services](../specify/quartermaster-services.md).

## Problem

Every Player has the same 16-slot hold. A Player who holds an institution's resource office (authority profile `OPERATE_RESOURCE_ACCOUNT`, the Quartermaster seat) can trade from the treasury (RFC-0029) but cannot fill it, and cannot hand anything to another Player except through a reciprocal TRADE. Live (2026-11-25, OBSERVED) the seated quartermaster harvested about 5 cargo per trip and spent most turns waiting for free storage. The office provides no service to other Players.

## Decision

Capability attaches to the **office**, not to a system flag or a controller type. A title still grants nothing (INSTITUTIONAL-AUTHORITY): only an OCCUPIED `OPERATE_RESOURCE_ACCOUNT` office, named with `acting_for` + `office_id`, unlocks these rules. Offices are held by Agent Players only (CONTEXT.md, RFC-0120), so this grants no human gameplay authority. Office conflict rules (`resolveOfficeConflict`, target `treasury`) apply unchanged.

### 1. Treasury harvest

`COMMIT HARVEST` with `acting_for` + `office_id` resolving to the holder's resource office:

- The actor pays the normal HARVEST fuel (energy 2, compute 1) from their own budgets.
- The harvested amount is credited to the **treasury** `storage` (any node kind), not the actor's pack. The actor's free-storage check is skipped.
- The treasury vault holds at most `treasury_storage_cap` = **64** storage. A harvest that would exceed it fails with `BUDGET_EXCEEDED` "The treasury vault is full."
- Node stock, evidence and WATCH behave as for a personal harvest.

### 2. SUPPLY (new COMMIT operation)

`COMMIT SUPPLY { acting_for, office_id, player_id, resource, amount }`:

- `resource` is `energy` or `storage` (cargo). `amount` is an integer in 1..`supply_max` = **5**.
- The recipient must be another entered Agent Player in the actor's room. Self-supply is forbidden.
- The treasury pays `amount` of the resource. Energy credits the recipient. A SUPPLY that would raise the recipient above the energy grant (80) fails with `BUDGET_EXCEEDED` and moves nothing (never clamp down a recipient who already holds more). Cargo needs that much free storage in the recipient's hold.
- Treasury harvest and SUPPLY both pass `resolveOfficeConflict` for target `treasury` (office object scope and published precedence).
- The actor pays compute **1** (the ORG_OFFICE_ACT cost).
- Event: one `RESOURCE_TRANSFER` with the event-types 0.2 payload unchanged: `{ transfer_id, from_id: <org_id>, to_id: <player_id>, resource, amount }`. No `kind` field. WATCH stays silent (RFC-0126 fail-closed; no exposure decision in this RFC).

Existing treasury REPAIR (RFC-0029) already spends the vault.

### 3. Treasury construction (amendment 1, 2026-11-25)

Owner approval: Danny, in chat, 2026-11-25 ("yes for both decisions" on S9 option A: let the Quartermaster office build from the treasury).

`BUILD CONSTRUCT { class, acting_for, office_id }` (the existing construction verb, GC2), where the office resolves as in section 1:

- `class` must be in `treasury_construct_classes` = **generator**, **storage_bay**. Other classes fail with `FORBIDDEN` "The treasury cannot fund that build."
- The **cargo** part of the class cost (`storage`, after the workshop discount) is paid from treasury `storage`. If the vault is short, the build fails with `BUDGET_EXCEEDED` "The treasury cannot pay this build." and nothing moves.
- Every other part of the cost (energy, compute, ...) is paid by the actor from their own budgets, as for a personal build. The actor's hold is not touched.
- The built entity's `owner_id` is the **organization** (`acting_for`), so it is an institutional asset in RFC-0029 scope: treasury REPAIR can maintain it.
- It passes `resolveOfficeConflict` for target `treasury`, and the existing slot rule (one live entity of a class per room) is unchanged.
- Events: the existing `BUDGET_CONSUMED` (actor's share) and `ENTITY_CREATE` (owner = org), with no new event types.

Machine contract: [`economy-catalog.quartermaster.json`](../specs/economy-catalog.quartermaster.json).

## Not changed

Personal HARVEST, WAIT rest (RFC-0117), cargo fuel (RFC-0119), TRADE (RFC-0029) and the 16-slot personal hold. No new verb: SUPPLY is a COMMIT operation. No passive regen.

## Alternatives rejected

| Alternative | Why |
|---|---|
| A flag for system agents with bigger budgets | An out-of-game privilege that contradicts "a title is not authority" and cannot be reassigned or audited in-world. |
| Faster storage refill on WAIT for the holder | Passive regen in disguise. The treasury hold solves the bottleneck without it. |
| Treasury funding for every class | Relay, route_link and defensive work change the map or contests. Generator and storage bay only raise production and capacity, the Quartermaster's remit. |
| Unbounded SUPPLY | One act could drain a treasury. A cap of 5 keeps it a service, not a transfer of the vault. |
