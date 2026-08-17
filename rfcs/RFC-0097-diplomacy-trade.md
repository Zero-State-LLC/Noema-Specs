# RFC-0097 — Diplomacy S0 TRADE agreement form

## Status

**Accepted**

Specification-only until hosted. No new events. No `event-catalog/0.3`. AGREEMENT_TERMINATE stays out. Other agreement types stay `FORM_FORBIDDEN`. Chamber help still omits AGREEMENT. WED / ATTEST stay omitted.

## Problem

[DIPLOMACY.md](../docs/DIPLOMACY.md) and `COMMIT.AGREEMENT_FORM` are Accepted on `event-catalog/0.2`, but the hosted Chamber returns `NOT_IMPLEMENTED` for `form agreement`. World reports cannot list diplomacy because there is no agreement store. An implementer would invent types, bind a party without consent, or add help.

## Proposed change

Accept Diplomacy S0. Host **TRADE** only:

- `form agreement trade with <player>` / structured `COMMIT.AGREEMENT_FORM`
- Both parties entered and colocated in a **public** room
- First call offers (`OFFERED`). Matching counterparty call accepts
- Accept emits existing `AGREEMENT_FORMED` (`agreement_type=TRADE`, `terms.machine.preferential_trade=true`)
- Cost: compute 2, influence 1 per successful AGREEMENT_FORM (offerer and acceptor)
- Other types `FORM_FORBIDDEN`
- Hidden rooms `NOT_OBSERVABLE`
- Help unchanged (still no AGREEMENT / TERMINATE)
- No AGREEMENT_TERMINATE. No NON_AGGRESSION / ACCESS / RESOURCE_COMMITMENT / MUTUAL_DEFENSE effects

Catalog: [`diplomacy-catalog.s0.json`](../specs/diplomacy-catalog.s0.json).  
Slice: [DIPLOMACY-S0.md](../docs/DIPLOMACY-S0.md).

## Alternatives rejected

| Alternative | Why |
|-------------|-----|
| Bind without accept | Consent |
| All five types | Later slices |
| AGREEMENT_TERMINATE | Separate pin |
| Help AGREEMENT | Separate pin (like CONTEST before RFC-0095) |
| Preferential discount | Already GC3-S7 social |
| New events | Catalog closed |

## Compatibility

Additive TRADE form. Worlds ignoring S0 keep `form agreement` unimplemented.

## Data / security

Public TRADE agreements only after accept. No private terms. WATCH uses existing `agreement_formed` when the event is emitted. No ticker.

## Validation

`check_diplomacy_s0`: TRADE form accepted; unknown type rejected; help still omits AGREEMENT; no terminate.

## Rollback

Return `NOT_IMPLEMENTED` for `form agreement` again.

## Unresolved

TERMINATE. Other types. AGREEMENT help. Diplomacy report lines.
