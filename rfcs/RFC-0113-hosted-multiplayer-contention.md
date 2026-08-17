# RFC-0113 — Hosted multiplayer contention

## Status

**Accepted**

Specification-only until hosted tests. No new verbs. No live chat. No cycle freeze.

## Problem

Two Players can harvest the same node. Hosted already serializes on one Durable Object, but nothing pins that as the multiplayer rule. Implementers invent split-yield, chat sockets, or a full scheduler.

## Proposed change

Accept [HOSTED-MP-CONTENTION.md](../docs/HOSTED-MP-CONTENTION.md). Hosted colliding `HARVEST`/`REPAIR` is first-accepted. Empty stock is `FORBIDDEN` “Not enough stock available.” Coordination is existing `MESSAGE` and shout.

Catalog: [`hosted-mp-catalog.s0.json`](../specs/hosted-mp-catalog.s0.json).

## Alternatives rejected

| Alternative | Why |
|-------------|-----|
| Cycle-freeze sort | Separate RFC; changes PLAY/WAIT |
| Soft split | Kills the coordination game |
| Live chat | Fights relay economy |

## Compatibility

Additive documentation of current hosted writer. Worlds that already fail empty harvest stay compatible.

## Data / security

No new events. WATCH must not gain amounts or mail text.

## Validation

`check_hosted_mp_s0`: first-ok ACCEPT; second-empty REJECT NOT_ENOUGH_STOCK; split/live-chat/new-verb REJECT.

## Rollback

Ignore the slice. Existing HARVEST miss still applies.

## Unresolved

Frozen-cycle hosted scheduler (later RFC).
