# RFC-0039 — GC3-S7 Preferred-Counterparty Discount

## Status

**Accepted**

No auto-accept. No hidden prices. No change to v0.1 offer/want lots. Opens the discount RFC-0037 left out of S5.

## Problem

[SOCIAL-MEMORY.md](../docs/SOCIAL-MEMORY.md) allows memory to prefer counterparties. RFC-0037 charged `TRADE_CAUTION` for live hostility and left discounts as a minigame. An implementer would auto-accept reliable traders, hide others, or invent a secret rebate.

## Proposed change

Accept GC3-S7:

- A **live preferred** counterparty is one the acting subject has a live (GC3-S4 weight > 0) S0 `RELIABLE` edge toward (distinct accepted trades ≥ 3). Institution `TRADE` uses the org’s live S3 reliable edge
- Discount: waive the S5 `TRADE_CAUTION` +1 compute when the counterparty is live preferred, even if a live danger/deceptive edge also exists (`CONTESTED`)
- Base v0.1 TRADE compute (1) and offer/want lots unchanged
- Auto-accept / auto-prefer as the only shown TRADE: **REJECT**. Every visible counterparty stays listed
- Affordance MAY label preferred counterparties. It MUST NOT hide others

Catalog: [`social-memory-catalog.gc3-s7.json`](../specs/social-memory-catalog.gc3-s7.json).  
Slice: [GC3-S7-PREFERRED.md](../docs/GC3-S7-PREFERRED.md).

## Alternatives rejected

| Alternative | Why |
|-------------|-----|
| Auto-accept reliable trades | Automation / minigame |
| Hide non-preferred TRADE | Partial-observability leak |
| Secret rebate / inventory price | Leak + price engine |
| Free propose (compute 0) | Changes frozen v0.1 base cost |
| Subtract from offer lots | Frozen amounts |

## Compatibility

Overlay on S5 only. S0/S1/S3/S4/S6 projections unchanged.

## Data / security

No new events. Lines must not include amounts, stock, or hidden ids.

## Validation

`check_gc3_s7`: live reliable + live hostile → extra_compute 0 and auto_accept false; live hostile only → extra 1; no edges → extra 0.

## Rollback

Apply S5 caution without the waiver.

## Unresolved

None for this discount. Institution-as-party contests remain GC7.
