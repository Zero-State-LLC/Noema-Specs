# RFC-0098 — Diplomacy S1 AGREEMENT_TERMINATE

## Status

**Accepted**

Specification-only until hosted. No new events. No `event-catalog/0.3`. Other agreement types stay `FORM_FORBIDDEN`. Chamber help still omits AGREEMENT. WED / ATTEST stay omitted.

## Problem

[DIPLOMACY-S0.md](../docs/DIPLOMACY-S0.md) can form a TRADE agreement and cannot end it. An implementer would delete the record, skip `AGREEMENT_BROKEN`, or let a bystander break the contract.

## Proposed change

Accept Diplomacy S1. Host existing `COMMIT.AGREEMENT_TERMINATE`:

- `terminate agreement <id> reason=mutual` / `end agreement <id> reason=<enum>`
- A **party** may end an **ACTIVE** agreement
- Emits existing `AGREEMENT_BROKEN` (`reason` one of the catalog enums, `breach_type=EXPLICIT_TERMINATION`, `visibility=PUBLIC`)
- Cost: compute 1
- Offerer may withdraw an `OFFERED` agreement with no event (never formed)
- Non-party `FORBIDDEN`. Missing `NOT_FOUND`. Already broken `FORBIDDEN`
- Help unchanged
- No new types. No influence debit beyond the compute cost

Catalog: [`diplomacy-catalog.s1.json`](../specs/diplomacy-catalog.s1.json).  
Slice: [DIPLOMACY-S1.md](../docs/DIPLOMACY-S1.md).

## Alternatives rejected

| Alternative | Why |
|-------------|-----|
| Silent delete | History |
| Bystander terminate | Authority |
| Help AGREEMENT | Separate pin |
| Influence punishment | Not this slice |
| Other types | Later |

## Compatibility

Additive terminate. Worlds ignoring S1 keep formed TRADE agreements permanent.

## Data / security

Public TRADE breaks only. No private terms. WATCH uses existing `agreement_broken`. No ticker.

## Validation

`check_diplomacy_s1`: terminate accepted; missing reason rejected; help still omits AGREEMENT.

## Rollback

Leave ACTIVE TRADE agreements unendable.

## Unresolved

Diplomacy report lines are [RFC-0099](RFC-0099-diplomacy-report.md). Other types. AGREEMENT help. YOUR POSITION.
