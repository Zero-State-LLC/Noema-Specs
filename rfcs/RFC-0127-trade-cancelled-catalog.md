# RFC-0127 — Catalog `TRADE_CANCELLED` on `event-catalog/0.2`

## Status

**Accepted**

Closes the closed-catalog omission recorded in
[EVENT-CATALOG-AUDIT.md](../docs/EVENT-CATALOG-AUDIT.md).
Authorizes one already-emitted type. Does not open `event-catalog/0.3`.
Does not change Chamber `event-catalog/0.1` (24 types).
Does not add verbs, Genesis, a `CRIME_DETECTED` producer, a WATCH RFC, or v0.8.

## Problem

The hosted Worker emits `TRADE_CANCELLED` when the proposer cancels an open
trade. WATCH already projects `<who> withdrew a trade`. The type is in neither
`event-types.json` (24) nor `event-types.0.2.json` (31), has no payload `$def`,
and never existed in the offline Python runtime.

[GC4-S2-INSTITUTION-ACTIONS.md](../docs/GC4-S2-INSTITUTION-ACTIONS.md) §Events
already lists `TRADE_CANCELLED` among existing trade types. The specification
has been treating the type as present. The machine catalogs have not.

[SPEC-FREEZE-CORE-LOOP.md](../docs/SPEC-FREEZE-CORE-LOOP.md) §5.8 requires an
RFC before a closed catalog grows. The runtime pins the type as
`KNOWN_UNCATALOGUED` until this RFC lands. That exception is a follow-up in
the Noema runtime repository, not this one.

## Catalog choice

**Amend `event-catalog/0.2`.** Do not open `event-catalog/0.3`. Do not add the
type to Chamber `event-catalog/0.1`.

| Option | Verdict |
|--------|---------|
| Amend `event-catalog/0.2` | **Accept.** §5.8 requires an RFC, not a new catalog pin. The type is already named as existing in GC4-S2. Hosted worlds that emit it already pin 0.2. One additive type does not need a new catalog identity. |
| Open `event-catalog/0.3` | **Reject.** A new pin for one trade-lifecycle type. Deep Time and dozens of accepted RFCs keep `No event-catalog/0.3` as a non-goal because 0.3 is a later catalog, not a one-type patch. |
| Add the type to `event-catalog/0.1` | **Reject.** Chamber acceptance stays 24 types. [EVENT-CATALOG.md](../docs/EVENT-CATALOG.md) and [RFC-0002](RFC-0002-strategic-contestation-and-crime-events.md) leave that catalog closed. Worlds on 0.1 MAY still record proposer withdrawal as `TRADE_REJECTED` reason `CANCELLED`. |

Freeze text checked: §5.8 is “expand event types only via RFC.” Slice H’s
`no event-catalog/0.3` is a Deep Time / Genesis non-goal, not a ban on amending
0.2. RFC-0002 remains the source of the seven strategic types. This RFC adds
one later type to the same pin.

After this RFC:

| Catalog | Types |
|---------|-------|
| `event-catalog/0.1` | **24** (unchanged) |
| `event-catalog/0.2` | **32** = 24 + 7 (RFC-0002) + `TRADE_CANCELLED` |

## Proposed change

Add `TRADE_CANCELLED` to [`specs/event-types.0.2.json`](../specs/event-types.0.2.json):
one `oneOf` binding, one payload `$def`, one `x-noema-event-types` row.

### Payload

Match the fields the hosted Worker already emits. Do not add fields.

| Field | Required | Meaning |
|-------|----------|---------|
| `trade_id` | yes | The open proposal being withdrawn |
| `by` | yes | The cancelling Player. MUST be the proposer |
| `reason` | yes | `CANCELLED` |

`acting_for` and `office_id` are GC4-S2 additive metadata on institutional
TRADE. The Worker does not emit them on `TRADE_CANCELLED`. This RFC does not
add them.

`TRADE_REJECTED` keeps `rejected_by`. This type uses `by` because that is the
field the Worker writes.

### Reducer

Require an `OPEN` proposal. Require `by` to be that proposal’s proposer. Set
status `CANCELLED`. Release the proposer’s offered reservation. Do not move
holdings. Reject a missing, closed, or unauthorized cancel. The reducer does
not send a notification.

WATCH already projects `<who> withdrew a trade` from this type. This RFC does
not change that projection and does not add a WATCH surface.

### Isolation

Worlds pinned to `event-catalog/0.1` MUST reject `TRADE_CANCELLED`. Existing
0.1 and 0.2 type meanings do not change. `TRADE_REJECTED` reason `CANCELLED`
remains valid on both catalogs.

## Alternatives rejected

| Alternative | Why |
|-------------|-----|
| Keep the type uncatalogued | Violates §5.8; the Worker already emits and publicly projects it |
| Overload `TRADE_REJECTED` reason `CANCELLED` as the only cancel record | The Worker already emits a distinct type; GC4-S2 already names that type |
| Invent `cancelled_by`, `acting_for`, or extra reason values | The Worker does not emit those fields on this type |
| Open `event-catalog/0.3` | New catalog for one type; see Catalog choice |
| Add the type to Chamber 0.1 | Expands the closed 24-type Chamber catalog |
| Change WATCH copy, add verbs, add a crime producer, or touch Genesis | Out of scope |

## Compatibility

Additive on `event-catalog/0.2` only. Historical 0.1 ledgers stay immutable.
Worlds already pinned to 0.2 MAY now admit this type. Worlds on 0.1 MUST
continue to reject it. RFC-0002 strategic types and payloads are unchanged.

Command docs that still say cancel emits only `TRADE_REJECTED` describe the
0.1 recording. On 0.2, proposer cancel emits `TRADE_CANCELLED`.

## Data / research / security

No rewrite of stored events. Replay of a 0.2 ledger that already contains
`TRADE_CANCELLED` becomes catalog-admissible. Claim labels are unchanged. No
new credential, containment, or public/private partition. Reservation release
is the same release `TRADE_REJECTED` already performs.

## Migration

No world pin change. No 0.3 pin. No Genesis reseed.

After this RFC is on Specs `main`, a Noema runtime PR drops
`TRADE_CANCELLED` from `KNOWN_UNCATALOGUED` in
`workers/noema/test/closed-catalog.test.ts`. That follow-up MUST emit
`reason: "CANCELLED"` so the payload matches this `$def`. This repository
does not change the runtime.

## Validation

- `event-types.json` stays 24 types and has no `TRADE_CANCELLED` `$def`
- `event-types.0.2.json` has 32 types and a `TRADE_CANCELLED_payload` `$def`
- Positive fixture admits on `event-catalog/0.2`
- `event-catalog/0.1` rejects `TRADE_CANCELLED`
- Negative payload fixture (missing `by`) rejects
- `python3 validation/validate_all.py` PASS

## Rollback

Supersede this RFC. Remove the type from `event-types.0.2.json`. Restore the
31-type 0.2 pin. The Worker would again treat the type as uncatalogued.

## Unresolved

None for this catalog entry. Optional GC4-S2 `acting_for` / `office_id` on
this type, if the Worker later emits them, needs a later RFC.
