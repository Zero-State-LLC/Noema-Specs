# GC1-S7 — Focus declaration

**Status:** Executable specification. Runtime authorized with RFC-0110.  
**Depends on:** [GC1-S6-PUBLIC-TITLES.md](GC1-S6-PUBLIC-TITLES.md) · [MASTERY-SPECIALIZATION.md](MASTERY-SPECIALIZATION.md)  
**RFC:** [RFC-0110](../rfcs/RFC-0110-focus-declaration.md)  
**Does not open:** `FOCUS_DECLARED` event · `event-catalog/0.3` · decay-window change · parameter-access · WED / ATTEST help

S7 lets a Player **declare one focus track**. It is soft intent on the world snapshot. It is not a class, not recognition, and not a cheaper verb.

---

## Doctrine decisions

| Temptation | Verdict |
|------------|---------|
| One declared track on the Player snapshot | **ACCEPT.** Ledgered as persistent player state |
| `FOCUS_DECLARED` / event-catalog/0.3 | **REJECT.** This slice |
| Grant recognition or new verbs | **REJECT.** |
| Change LATENT window | **REJECT.** S3 magnitudes stay |
| Cap 1 | **ACCEPT.** Mastery 1–3 stays later |
| Public line in public rooms / WATCH | **ACCEPT.** Same withhold as titles: LATENT track or hidden room omits |
| Chamber `help` names FOCUS | **ACCEPT.** WED / ATTEST stay omitted |

---

## Slice contract

| Field | Value |
|-------|--------|
| Slice id | `gc1-s7` |
| Catalog | `mastery-catalog/gc1-s7` |
| Verb | existing `COMMIT` · operation `FOCUS` |
| Human | `focus explorer\|surveyor\|broker\|engineer` · `focus clear` |
| Tracks | existing GC1-S1 four |
| Cap | 1 |
| Recognition required | no |
| New events | none |
| Self PLAY | one first-person focus line |
| Public PLAY / WATCH | one third-person line; public rooms only; omit if that track is LATENT |
| Hidden rooms | no public focus |
| Help | FOCUS / `help focus`. No WED / ATTEST |

---

## Lines (pinned)

| Track | Self | Public |
|-------|------|--------|
| explorer | You are focusing on the rooms. | `{handle} is focusing on the rooms.` |
| surveyor | You are focusing on survey work. | `{handle} is focusing on survey work.` |
| broker | You are focusing on exchanges. | `{handle} is focusing on exchanges.` |
| engineer | You are focusing on infrastructure. | `{handle} is focusing on infrastructure.` |

Clear removes the line. Never print XP or track ids.

---

## Runtime rule

Hosted Chamber MUST persist at most one focus track on the Player snapshot, project the self line, and project the public line in public rooms (and WATCH) unless the focused track is LATENT or the room is hidden. Isolated `test.hosted-canonical.gc1-s7`. No Genesis change.
