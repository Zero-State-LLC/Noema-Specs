# WR-S1 — organization report lines

**Status:** Executable specification. Runtime authorized with RFC-0091.  
**Parent:** [WR-S0-WORLD-REPORT.md](WR-S0-WORLD-REPORT.md) · [WORLD-REPORTS.md](WORLD-REPORTS.md)  
**RFC:** [RFC-0091](../rfcs/RFC-0091-org-report.md)  
**Does not open:** NEWS verb · REPORT_* · WATCH ticker · YOUR POSITION · diplomacy/conflict  
**Next:** this report leftover (orgs) is closed

S1 adds public institutions to the existing 5-cycle report.

---

## Doctrine decisions

| Temptation | Verdict |
|------------|---------|
| NEWS verb | **REJECT.** |
| Member roster on report | **REJECT.** |
| WATCH ticker | **REJECT.** |
| Later sections | **REJECT.** |

---

## Slice contract

| Field | Value |
|-------|--------|
| Slice id | `wr-s1` |
| Catalog | `world-report-catalog/wr-s1` |
| Interval | 5 committed cycles (S0) |
| Added | `{name} stands.` per ACTIVE org |
| Events | none |
| PLAY | `report_lines` includes org lines after first interval |
| WATCH | silent |
| Help | still no NEWS |

---

## Runtime rule

Hosted Chamber MUST append one `{name} stands.` line per ACTIVE organization when rebuilding the last-1 public report. Isolated tests only. Help unchanged except RFC-0090 BUILD. No Genesis change.
