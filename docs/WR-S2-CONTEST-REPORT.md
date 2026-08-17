# WR-S2 — public contest report lines

**Status:** Executable specification. Runtime authorized with RFC-0092.  
**Parent:** [WR-S1-ORG-REPORT.md](WR-S1-ORG-REPORT.md) · [WORLD-REPORTS.md](WORLD-REPORTS.md)  
**RFC:** [RFC-0092](../rfcs/RFC-0092-contest-report.md)  
**Does not open:** NEWS verb · REPORT_* · WATCH ticker · CONTEST help · YOUR POSITION · crime/access  
**Next:** [WR-S3-ACCESS-REPORT.md](WR-S3-ACCESS-REPORT.md)

S2 adds public open contests to the existing 5-cycle report.

---

## Doctrine decisions

| Temptation | Verdict |
|------------|---------|
| NEWS verb | **REJECT.** |
| Help CONTEST | **REJECT.** |
| Hidden contest | **REJECT.** |
| Stake / party names | **REJECT.** |
| WATCH ticker | **REJECT.** |

---

## Slice contract

| Field | Value |
|-------|--------|
| Slice id | `wr-s2` |
| Catalog | `world-report-catalog/wr-s2` |
| Interval | 5 committed cycles (S0) |
| Added | `{form} is contested.` per OPEN public contest |
| Events | none |
| PLAY | `report_lines` includes contest lines after first interval |
| WATCH | silent |
| Help | still omits CONTEST and NEWS |

---

## Runtime rule

Hosted Chamber MUST append one `{form} is contested.` line per OPEN contest whose `room_id` is a public room when rebuilding the last-1 public report. Isolated tests only. Help still omits CONTEST. No Genesis change.
