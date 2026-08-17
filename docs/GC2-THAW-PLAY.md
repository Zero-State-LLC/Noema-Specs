# GC2 — first-world BUILD help

**Status:** Executable specification. Runtime authorized with RFC-0090.  
**Parent:** [CONSTRUCTION.md](CONSTRUCTION.md) · [PLAYER-ACTION-MAP.md](PLAYER-ACTION-MAP.md) · [GC2-THAW-READINESS.md](GC2-THAW-READINESS.md)  
**RFC:** [RFC-0090](../rfcs/RFC-0090-build-play-thaw.md)  
**Does not open:** CONTEST/WED/ATTEST help · STRUCTURE_* · sixth SHARE  
**Next:** [WR-S1-ORG-REPORT.md](WR-S1-ORG-REPORT.md)

Chamber PLAY may name BUILD. The operations are the ones already hosted.

---

## Doctrine decisions

| Temptation | Verdict |
|------------|---------|
| New BUILD verb | **REJECT.** |
| Help CONTEST / WED / ATTEST | **REJECT.** |
| WATCH ticker | **REJECT.** |

---

## Slice contract

| Field | Value |
|-------|--------|
| Slice id | `gc2-thaw-play` |
| Catalog | `construction-catalog/gc2-thaw-play` |
| Help BUILD | true |
| Help CONTEST / WED / ATTEST | false |
| New verbs | none |
| WATCH | unchanged |

---

## Runtime rule

Hosted Chamber MUST list BUILD on `help` and list existing construct/dismantle/upgrade/repurpose/restore/vest/share/connect aliases on `help build`. MUST still omit CONTEST, WED, and ATTEST. Isolated tests only. No Genesis change.
