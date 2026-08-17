# GC7 — first-world CONTEST help

**Status:** Executable specification. Runtime authorized with RFC-0095.  
**Parent:** [GC7-FIRST-SLICE.md](GC7-FIRST-SLICE.md) · [GC7-S3-INFORMATION-CONTEST.md](GC7-S3-INFORMATION-CONTEST.md) · [PLAYER-ACTION-MAP.md](PLAYER-ACTION-MAP.md)  
**RFC:** [RFC-0095](../rfcs/RFC-0095-contest-play-thaw.md)  
**Does not open:** WED/ATTEST help · HP · SCAN/ATTACK · event-catalog/0.3 · AGREEMENT_FORM  
**Next:** WED / ATTEST help stay parked

Chamber PLAY may name CONTEST. The operations are the ones already hosted.

---

## Doctrine decisions

| Temptation | Verdict |
|------------|---------|
| New CONTEST verb | **REJECT.** |
| Help WED / ATTEST | **REJECT.** |
| HP / SCAN / ATTACK | **REJECT.** |
| WATCH ticker | **REJECT.** |

---

## Slice contract

| Field | Value |
|-------|--------|
| Slice id | `gc7-thaw-play` |
| Catalog | `conflict-catalog/gc7-thaw-play` |
| Help CONTEST | true |
| Help WED / ATTEST | false |
| New verbs | none |
| WATCH | unchanged |

---

## Runtime rule

Hosted Chamber MUST list CONTEST on `help` and list existing contest/defend/withdraw aliases on `help contest`. MUST still omit WED and ATTEST. Isolated tests only. No Genesis change.
