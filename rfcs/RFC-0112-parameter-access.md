# RFC-0112 — GC1-S8 Engineer overhaul parameter

## Status

**Accepted**

**Hosted.** Agent Players discover `extent=overhaul` on structured REPAIR affordances. No new verbs. No `event-catalog/0.3`. No class discount.

## Problem

[MASTERY-SPECIALIZATION.md](../docs/MASTERY-SPECIALIZATION.md) says mastery enriches **parameters** under the same verbs. S2–S7 add quality, decay, prior-work, offices, titles, and focus. An implementer would still add `OVERHAUL` as a verb or cheapen ordinary `REPAIR` for Engineers.

## Proposed change

Accept GC1-S8. `REPAIR` gains an optional `extent` parameter.

- Default `standard` is today's REPAIR for every Player
- `overhaul` is legal only for a recognized, **MAINTAINED** Engineer
- Extra energy +1; extra condition +5 on top of S2; cap 100
- Human `repair <target> overhaul`
- Chamber `help repair` names the parameter. WED / ATTEST stay omitted
- LATENT, unrecognized, or other tracks: reject the overhaul, leave standard REPAIR available

Catalog: [`mastery-catalog.gc1-s8.json`](../specs/mastery-catalog.gc1-s8.json).  
Slice: [GC1-S8-PARAMETER-ACCESS.md](../docs/GC1-S8-PARAMETER-ACCESS.md).

## Alternatives rejected

| Alternative | Why |
|-------------|-----|
| New `OVERHAUL` verb | Explodes the taxonomy |
| Cheaper default REPAIR | Forbidden class discount |
| BUILD.UPGRADE-only | Perihelion first play is REPAIR |
| LATENT still overhauls | S3 says practiced hands go slack |
| Multi-focus / decay credit | Later leftovers |
| WED / ATTEST help | Parked |

## Compatibility

Additive argument on existing `COMMIT.REPAIR`. Worlds ignoring S8 treat unknown `extent` as standard or reject the extra field; they MUST NOT invent a new verb.

## Data / security

No new events. Hidden practice counts stay off WATCH. Rejection MUST NOT leak the exact recognition tally.

## Validation

`check_gc1_s8`: standard ACCEPT; overhaul Engineer MAINTAINED ACCEPT; unrecognized / LATENT / wrong track REJECT; extra energy enforced; no new verbs or events.

## Rollback

Ignore `extent=overhaul`. Ordinary REPAIR unchanged.

## Unresolved

Multi-focus cap 1–3. Decay-window credit for focus. Further parameters on BUILD / TRADE / INSPECT.
