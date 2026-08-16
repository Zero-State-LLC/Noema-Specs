# RFC-0037 — GC3-S5 Published Trade Caution

## Status

**Accepted**

Specification-only. No auto-refuse. No hidden price lists. No inventory leak. Closes RFC-0022's deferred "auto trade friction / refuse" by **rejecting** automation and accepting a published surcharge.

## Problem

[SOCIAL-MEMORY.md](../docs/SOCIAL-MEMORY.md) allows memory to raise trade friction. RFC-0022 deferred auto-refuse. An implementer would hide the TRADE affordance, invent a secret markup, or auto-reject against `dangerous` counterparties.

## Proposed change

Accept GC3-S5:

- `TRADE` propose against a counterparty the acting subject has a **live** (GC3-S4 weight > 0) danger or deceptive edge toward costs **+1 compute** (`TRADE_CAUTION`)
- Institution `TRADE` (`acting_for=org`): +1 compute when that org has a live S3 danger/deceptive edge toward the counterparty
- Base v0.1 offer/want amounts unchanged. Affordance **shows** the extra compute. GUI MUST NOT hide TRADE
- Cannot pay → `BUDGET_EXCEEDED` with observable reason `TRADE_CAUTION` (not a hidden method)
- Auto-reject / auto-refuse: **REJECT**. Player or office still chooses accept/reject

Catalog: [`social-memory-catalog.gc3-s5.json`](../specs/social-memory-catalog.gc3-s5.json).  
Slice: [GC3-S5-TRADE-FRICTION.md](../docs/GC3-S5-TRADE-FRICTION.md).

## Alternatives rejected

| Alternative | Why |
|-------------|-----|
| Auto-reject dangerous counterparties | RFC-0022 DEFER → this RFC REJECT |
| Hidden markup / inventory-based price | Leak + price engine |
| Hide TRADE affordance | Partial-observability leak |
| Change base TRADE lots | Frozen v0.1 offer/want |

## Compatibility

Additive published compute on propose only. Existing TRADE accept path unchanged.

## Data / security

No new events. Reason code is `TRADE_CAUTION` only. Must not name contest form, crime method, or stock.

## Validation

`check_gc3_s5`: live danger → extra_compute 1 and no auto_reject; no live edge → extra 0; decayed edge → extra 0.

## Rollback

Charge only the v0.1 TRADE compute. Caution lines remain as S1/S6 projection.

## Unresolved

None. Preferred-counterparty discounts stay out (minigame).
