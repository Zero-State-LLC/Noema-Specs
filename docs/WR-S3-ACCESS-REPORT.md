# WR-S3 — public access report lines

**Status:** Executable specification. Runtime authorized with RFC-0093.  
**Parent:** [WR-S2-CONTEST-REPORT.md](WR-S2-CONTEST-REPORT.md) · [WORLD-REPORTS.md](WORLD-REPORTS.md)  
**RFC:** [RFC-0093](../rfcs/RFC-0093-access-report.md)  
**Does not open:** NEWS verb · REPORT_* · WATCH ticker · ACCESS_POLICY help · YOUR POSITION · crime/diplomacy  
**Next:** diplomacy / crime report sections

S3 adds live public access restrictions to the existing 5-cycle report.

---

## Doctrine decisions

| Temptation | Verdict |
|------------|---------|
| NEWS verb | **REJECT.** |
| Hidden restriction | **REJECT.** |
| applies_to / parties | **REJECT.** |
| WATCH ticker | **REJECT.** |
| ACCESS_POLICY help | **REJECT.** |

---

## Slice contract

| Field | Value |
|-------|--------|
| Slice id | `wr-s3` |
| Catalog | `world-report-catalog/wr-s3` |
| Interval | 5 committed cycles (S0) |
| Added | `{room} {dir} is restricted.` / `{room} is restricted.` |
| Live | `cycle <= expires_cycle` |
| Events | none |
| PLAY | `report_lines` includes access lines after first interval |
| WATCH | silent |
| Help | still omits NEWS and ACCESS_POLICY |

---

## Runtime rule

Hosted Chamber MUST append one public access line per live restriction whose room is public when rebuilding the last-1 public report. Isolated tests only. Help unchanged. No Genesis change.
