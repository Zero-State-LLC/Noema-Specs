# Intent: Quartermaster office services (treasury hold and SUPPLY)

**Status:** `accepted`

**Next stage:** `specify/quartermaster-services.md` and [RFC-0133](../rfcs/RFC-0133-quartermaster-treasury-services.md)

**Author:** Jcode, for Danny

**Date:** 2026-11-25

This record is process only. It is not a spec, not a plan, and not an RFC. It does not authorize implementation. Danny approved options A + C in chat on 2026-11-25 ("quartermaster should have its own rules since is system agent. needs to be able to provide services for agents in game", then "ok continue").

## Problem

Every Agent Player has the same 16-slot hold ([RESOURCE-ECONOMY.md](../docs/RESOURCE-ECONOMY.md)). The holder of an institution's `OPERATE_RESOURCE_ACCOUNT` office can trade from the treasury ([RFC-0029](../rfcs/RFC-0029-institution-trade-repair.md)) but cannot fill it, and has no way to serve another Agent Player except a reciprocal TRADE. A seated quartermaster spends most turns waiting for free storage.

## Proposed outcome

The resource office carries two services: harvesting straight into the treasury vault, and handing small amounts of treasury energy or cargo to an Agent Player in the same room. The capability belongs to the office and moves with it.

## Affected users / systems

Agent Players holding or receiving from a resource office; the World Engine; Controllers that read LOOK affordances. WATCH is unaffected (silent).

## Constraints / non-goals

- No new verb. SUPPLY is a COMMIT operation and needs an RFC (RFC-0133).
- No passive regeneration, no change to the personal hold, HARVEST costs, or TRADE.
- No grant keyed to controller type or a system flag.
- The event uses the existing `RESOURCE_TRANSFER` payload (event-types 0.2) unchanged.
- No WATCH exposure decision.

## Open questions

- Treasury-funded CONSTRUCT is deferred.
- Whether SUPPLY ever reaches WATCH needs a separate RFC-0126 exposure decision.

## Verified / assumed claims

| Claim | Label | Basis |
|---|---|---|
| A seated quartermaster stalls on free storage | `OBSERVED` | Live fleet log 2026-11-25: 5 role actions in 40 turns, WAIT/MOVE between harvests |
| `RESOURCE_TRANSFER` payload has no `kind` and requires `transfer_id` | `OBSERVED` | `specs/event-types.0.2.json` |
| Office capability does not reintroduce human gameplay authority | `INFERRED` | Offices are held by Agent Players only (CONTEXT.md, RFC-0120) |

## Author / date

- **Author:** Jcode, for Danny
- **Date:** 2026-11-25
