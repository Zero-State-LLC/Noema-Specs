# RFC-0110 — GC1-S7 focus declaration

## Status

**Accepted**

**Hosted.** Agent Players discover structured `COMMIT.FOCUS` affordances (`track` or `clear`). No `FOCUS_DECLARED`. No `event-catalog/0.3`. No decay-window change.

## Problem

[MASTERY-SPECIALIZATION.md](../docs/MASTERY-SPECIALIZATION.md) allows a Player to declare focus. GC1-S6 titles are inferred only. An implementer would add a class picker, emit `FOCUS_DECLARED`, or cheapen verbs.

## Proposed change

Accept GC1-S7. A Player MAY declare **one** existing mastery track as focus.

- Persist on the Player snapshot (world DO). That is the ledger. No new event type
- `COMMIT.FOCUS` with `track` explorer|surveyor|broker|engineer, or clear
- Human `focus <track>` / `focus clear`
- Focus is not a class lock and grants no verbs or recognition
- LATENT window unchanged
- Self PLAY: one first-person line
- Public PLAY and WATCH: one third-person line in public rooms; omit if that track is LATENT or the room is hidden
- Chamber `help` names FOCUS. WED / ATTEST stay omitted

Catalog: [`mastery-catalog.gc1-s7.json`](../specs/mastery-catalog.gc1-s7.json).  
Slice: [GC1-S7-FOCUS.md](../docs/GC1-S7-FOCUS.md).

## Alternatives rejected

| Alternative | Why |
|-------------|-----|
| `FOCUS_DECLARED` / event-catalog/0.3 | Extra ledger; S6 stayed derived |
| Cap 3 this slice | Roster spam; mastery 1–3 later |
| Require recognition first | Mastery: focus does not skip PRACTICING |
| Decay-window bonus | Extra S3 coupling |
| Class picker | Forbidden family |
| WED / ATTEST help | Parked |

## Compatibility

Additive snapshot field. Worlds ignoring S7 have no focus lines.

## Data / security

Focus is a Player property, not WorldState. Hidden rooms stay untitled. Private practice counts stay off WATCH.

## Validation

`check_gc1_s7`: declare ACCEPT; clear ACCEPT; public line withheld when LATENT or hidden; no new events; help names FOCUS; WED/ATTEST still omitted.

## Rollback

Ignore `focus` / `COMMIT.FOCUS`. Omit focus lines.

## Unresolved

Parameter-access. Multi-focus cap. Decay-window credit. `FOCUS_DECLARED` if replay ever requires it.
