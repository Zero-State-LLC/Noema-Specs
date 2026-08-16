# RFC-0041 — GC7-S2 Institution as Contest Party

## Status

**Accepted**

Specification-only until hosted. No new verbs. No `event-catalog/0.3`. No fifth contest form. Stake and fees come from the institution treasury when `acting_for` is set.

## Problem

[STRATEGIC-CONFLICT.md](../docs/STRATEGIC-CONFLICT.md) says offices may authorize institutional participation, but left the party details as SPEC GAP. An implementer would set `declarer_id` to an `org_id` (breaking colocation and withdraw), invent `CONTEST_*` events, or let any member spend the treasury.

## Proposed change

Accept GC7-S2:

- `CONTEST_DECLARE` / `CONTEST_DEFEND` / `CONTEST_WITHDRAW` accept `acting_for` + occupied office
- Profile: `RESOURCE_SEIZURE` → `OPERATE_RESOURCE_ACCOUNT`; other closed forms → `OPERATE_NAMED_ASSET`
- `declarer_id` / `defender_id` remain the **acting Player**. `acting_for` / `defender_acting_for` name the institution
- DECLARE/DEFEND compute-influence fees and reserved stake debit the **treasury**
- Same org cannot be both parties. One Player still cannot declare and defend the same contest
- Vacant office cannot act. Withdraw remains the same Player who committed
- Existing four forms, `CONTEST_RESOLVED`, withdraw outcomes unchanged

Catalog: [`conflict-catalog.gc7-s2.json`](../specs/conflict-catalog.gc7-s2.json).  
Slice: [GC7-S2-INSTITUTION-PARTY.md](../docs/GC7-S2-INSTITUTION-PARTY.md).

## Alternatives rejected

| Alternative | Why |
|-------------|-----|
| `declarer_id = org.*` | Breaks room colocation and Player withdraw |
| Any member spends treasury | Unscoped authority |
| New CONTEST_* events | Catalog 0.3 |
| Fifth / information form | Separate RFC |
| Chamber help lists contest | RFC-0011 / RFC-0023 help pin |

## Compatibility

Additive `acting_for` on existing COMMIT operations. Player-vs-Player contests unchanged.

## Data / security

Events MAY include `acting_for`. WATCH still shows public form/target only. No hidden ids.

## Validation

`check_gc7_s2`: occupied matching profile ACCEPT; vacant / wrong profile / same-org both sides REJECT; no new verbs/forms/events.

## Rollback

Ignore `acting_for` on contest (Player-only parties).

## Unresolved

Information-target form. Broader conflict-of-interest beyond one-org-both-sides.
