# WR-S3 — public access report lines

**Status:** Executable specification. Runtime authorized with RFC-0093.  
**Parent:** [WR-S2-CONTEST-REPORT.md](WR-S2-CONTEST-REPORT.md) · [WORLD-REPORTS.md](WORLD-REPORTS.md)  
**RFC:** [RFC-0093](../rfcs/RFC-0093-access-report.md)  
**Does not open:** NEWS verb · REPORT_* · WATCH ticker · ACCESS_POLICY help · YOUR POSITION · crime/diplomacy  
**Next:** [WR-S4-CRIME-REPORT.md](WR-S4-CRIME-REPORT.md)

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

## Extension Points

Non-normative guidance for future maintenance; no new behavior is authorized here.

- **Report seam:** Extend cases for the existing last-1, five-committed-cycle public report projection, distinguishing room-wide restrictions from directional restrictions. This is a report-line contract, not a historical execution report or a new news feed.
- **Compatibility boundary:** RFC-0093 and world-report-catalog/wr-s3 retain the live predicate cycle <= expires_cycle and public-room filter. Later crime/diplomacy report slices belong to their own authority; richer private-party details or WATCH exposure need explicit versioned approval.
- **Validation expectations:** Rebuild at the first interval and subsequent intervals, compare exact expiry and the following cycle, and include hidden rooms plus multiple restrictions. Verify one line per eligible restriction, no applies_to/party leakage, no emitted events, and unchanged WATCH silence and help exclusions.
