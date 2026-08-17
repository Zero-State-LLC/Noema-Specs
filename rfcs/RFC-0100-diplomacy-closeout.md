# RFC-0100 — Diplomacy S2 remaining types, effects, and help

## Status

**Accepted**

Specification-only until hosted. No new events. No `event-catalog/0.3`. WED / ATTEST stay omitted. ACCESS_POLICY stays a separate verb.

## Problem

[DIPLOMACY-S1.md](../docs/DIPLOMACY-S1.md) forms and ends TRADE only. The other four Accepted types, their machine effects, and Chamber help remain dark. An implementer would invent types, skip breach, or hide the verb.

## Proposed change

Accept Diplomacy S2. Close the AGREEMENT family on existing `COMMIT.AGREEMENT_FORM` / `AGREEMENT_TERMINATE` and `event-catalog/0.2`:

| Type | Default machine terms | Live effect |
|------|----------------------|-------------|
| `TRADE` | `preferential_trade=true` | Unchanged (S0). Transfers still use TRADE. |
| `NON_AGGRESSION` | four v0.2 contest forms forbidden | Declaring a listed form emits `AGREEMENT_BROKEN` (`CONTEST_VIOLATION`). Contest still opens. |
| `ACCESS` | `access_room_ids` = formation room | Parties may MOVE through a matching DENY restriction. |
| `RESOURCE_COMMITMENT` | offerer energy 1 by `cycle+5` | After `by_cycle`, still-ACTIVE → `AGREEMENT_BROKEN` (`COMMITMENT_MISS`). |
| `MUTUAL_DEFENSE` | `defense_support_millipoints=50` | Added to defender score when a party is the defender. |

Also:

- `help` names AGREEMENT. `help agreement` lists form / terminate and the five types
- Offer/accept/terminate stay S0/S1
- WED / ATTEST stay omitted
- No ACCESS_POLICY verb. No new events

Catalog: [`diplomacy-catalog.s2.json`](../specs/diplomacy-catalog.s2.json).  
Slice: [DIPLOMACY-S2.md](../docs/DIPLOMACY-S2.md).

## Alternatives rejected

| Alternative | Why |
|-------------|-----|
| New events | Catalog closed |
| ACCESS_POLICY verb | Separate pin |
| Help WED / ATTEST | Separate pins |
| Sixth type | Catalog closed |
| Forbid contest instead of breach | Spec says breach |

## Compatibility

Additive types and help. Worlds ignoring S2 keep TRADE-only form.

## Data / security

Public pairwise agreements. No private terms on WATCH. Help lists types, not party ids.

## Validation

`check_diplomacy_s2`: five types; help AGREEMENT true; WED/ATTEST false; no new verbs.

## Rollback

Revert to TRADE-only form, no help, no live effects.

## Unresolved

YOUR POSITION. ACCESS_POLICY verb. WED / ATTEST help.
