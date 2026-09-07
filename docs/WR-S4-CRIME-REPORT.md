# WR-S4 — public crime report lines

**Status:** Executable specification. Runtime authorized with RFC-0094.  
**Parent:** [WR-S3-ACCESS-REPORT.md](WR-S3-ACCESS-REPORT.md) · [WORLD-REPORTS.md](WORLD-REPORTS.md)  
**RFC:** [RFC-0094](../rfcs/RFC-0094-crime-report.md)  
**Does not open:** NEWS verb · REPORT_* · WATCH ticker · CRIME help · YOUR POSITION · diplomacy · AGREEMENT_FORM  
**Next:** [WR-S5-DISCOVERY-REPORT.md](WR-S5-DISCOVERY-REPORT.md)

S4 adds public `CRIME_DETECTED` lines to the existing 5-cycle report.

---

## Doctrine decisions

| Temptation | Verdict |
|------------|---------|
| NEWS verb | **REJECT.** |
| Hidden-room crime | **REJECT.** |
| Subject / method / severity | **REJECT.** |
| WATCH ticker | **REJECT.** |
| CRIME help | **REJECT.** |
| Diplomacy | **LATER.** No agreement store. |

---

## Slice contract

| Field | Value |
|-------|--------|
| Slice id | `wr-s4` |
| Catalog | `world-report-catalog/wr-s4` |
| Interval | 5 committed cycles (S0) |
| Added | `{category} is detected.` |
| Public | `PUBLIC_HISTORY` or host `visibility=PUBLIC` |
| Events | none |
| PLAY | `report_lines` includes crime lines after first interval |
| WATCH | silent |
| Help | still omits NEWS and CRIME |

---

## Runtime rule

Hosted Chamber MUST append one public crime line per public `CRIME_DETECTED` on the existing social-event cache whose room is public when rebuilding the last-1 public report. Isolated tests only. Help unchanged. No Genesis change. No AGREEMENT_FORM thaw.


## Extension Points

Non-normative guidance for future maintenance; this section changes no current behavior or promotion status.

- Report fixtures can add combinations of public crime events and public-room eligibility inside the existing five-committed-cycle rebuild. Keep the line category-only and preserve last-1 report behavior rather than introducing a live crime feed.

- RFC-0094 and world-report-catalog/wr-s4 own this projection boundary; a new crime producer is separate from report rendering. Subject, method, severity, new events, WATCH ticker, or help exposure require their own accepted contract and version review rather than enrichment of the template.

- Validate PUBLIC_HISTORY and host PUBLIC eligibility, hidden-room suppression, interval boundaries, and repeated rebuilds with the same source cache. Confirm each eligible event produces its specified line without subject or investigation leakage, extra events, or a second report generation side effect.
