# RFC-0118 — Work consumes cargo

## Status

**Accepted**

No new Player verbs. AUTH-INFRA-CLASS amounts unchanged. Do not invert live `storage` numbers.

## Problem

`storage` is free capacity. HARVEST fills hold. REPAIR/CONSTRUCT still `canPay` storage, which demands empty pack. TRADE `storage` uses energy-sign. Cargo has no job.

## Proposed change

Work verbs consume cargo (free storage up). TRADE `storage: N` is cargo (giver free storage +N, receiver −N). HARVEST unchanged. WATCH silent on pack.

Catalog: `specs/economy-catalog.gc8-s6.json`. Slice: `docs/GC8-S6-WORK-CARGO.md`.

## Alternatives rejected

DROP verb. Flip storage to material stock. TRADE-only dump. Harvest debit-vs-check migrate. Currency/crypto.

## Compatibility

Additive sign flip. Worlds ignoring S6 keep today's lockout-to-work.

## Validation

`check_gc8_s6`: empty-hold work reject; cargo work storage +1; TRADE cargo 15→16 / 16→15; no new verbs.

## Rollback

`canPay`/`debit` storage on work and TRADE again.
