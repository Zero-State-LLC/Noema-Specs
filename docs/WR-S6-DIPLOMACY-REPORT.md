# WR-S6 — public diplomacy report lines

**Status:** Executable specification. Runtime authorized with RFC-0099.  
**Parent:** [WR-S5-DISCOVERY-REPORT.md](WR-S5-DISCOVERY-REPORT.md) · [DIPLOMACY-S1.md](DIPLOMACY-S1.md) · [WORLD-REPORTS.md](WORLD-REPORTS.md)  
**RFC:** [RFC-0099](../rfcs/RFC-0099-diplomacy-report.md)  
**Does not open:** NEWS verb · REPORT_* · WATCH ticker · AGREEMENT help · other types · YOUR POSITION · WED/ATTEST  
**Next:** remaining agreement types

S6 adds ACTIVE public agreements to the existing 5-cycle report.

---

## Doctrine decisions

| Temptation | Verdict |
|------------|---------|
| NEWS verb | **REJECT.** |
| Party names / terms | **REJECT.** |
| Offered / broken | **REJECT.** |
| WATCH ticker | **REJECT.** |
| AGREEMENT help | **REJECT.** |
| Other types | **LATER.** |

---

## Slice contract

| Field | Value |
|-------|--------|
| Slice id | `wr-s6` |
| Catalog | `world-report-catalog/wr-s6` |
| Interval | 5 committed cycles (S0) |
| Added | `{type} is agreed.` |
| Live | `status=ACTIVE` and `visibility=PUBLIC` |
| Events | none |
| PLAY | `report_lines` includes diplomacy lines after first interval |
| WATCH | silent |
| Help | still omits NEWS and AGREEMENT |

---

## Runtime rule

Hosted Chamber MUST append one public diplomacy line per ACTIVE public agreement when rebuilding the last-1 public report. Isolated tests only. Help unchanged. No Genesis change. No new agreement types.
