# RFC-0105 — GC1-S6 public titles

## Status

**Accepted**

No new verbs. No `event-catalog/0.3`. No focus ledger. No WED / ATTEST help.

## Problem

[MASTERY-SPECIALIZATION.md](../docs/MASTERY-SPECIALIZATION.md) still lists WATCH / public titles as later. GC1-S1 recognition is self-only. An implementer would emit XP on WATCH, title every practicing track, or leak LATENT and hidden-room work.

## Proposed change

Accept GC1-S6. Other Players in a public room, and WATCH, MAY see one world-native title derived from existing GC1-S1 recognition.

- Evidence stays derived (not WorldState). No new events
- Public PLAY attaches `public_practice_lines` on **other** Players here, public rooms only
- Copy is third person: `{handle} is known for survey work.` (explorer: `{handle} knows these rooms.`)
- Cap 1 line per other Player. Prefer catalog display order among live recognized tracks
- LATENT withholds the public line. Recognition remains
- Hidden rooms withhold titles
- WATCH shows the same public line only while the Player is in a public room. No ticker. No private counts
- Self `practice_lines` stay first-person and unchanged
- Chamber help unchanged (WED / ATTEST stay omitted)

Catalog: [`mastery-catalog.gc1-s6.json`](../specs/mastery-catalog.gc1-s6.json).  
Slice: [GC1-S6-PUBLIC-TITLES.md](../docs/GC1-S6-PUBLIC-TITLES.md).

## Alternatives rejected

| Alternative | Why |
|-------------|-----|
| Publish practicing lines | Not recognition |
| Publish LATENT titles | S4 already withholds public benefit |
| Hidden-room titles | Observation leak |
| Multiple public lines | Roster spam |
| `SPECIALIZATION_RECOGNIZED` / event-catalog/0.3 | Extra ledger |
| WATCH ticker or practice counts | Spectator leak |
| Change self `practice_lines` | S1/S3 already pin first person |
| Focus ledger in this slice | Separate RFC |

## Compatibility

Additive projection. Worlds ignoring S6 keep recognition self-only.

## Data / security

Titles are derived. Private practice counts stay off WATCH and off other Players. Hidden rooms stay untitled.

## Validation

`check_gc1_s6`: recognized Surveyor in a public room yields one third-person line; LATENT and hidden rooms withhold; unrecognized withholds; cap 1; WATCH uses the same line; no new verbs or events; self practice unchanged.

## Rollback

Omit `public_practice_lines` and WATCH title fields.

## Unresolved

Focus as ledger. Parameter-access upgrades.
