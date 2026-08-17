# WR-S5 — public discovery report lines

**Status:** Executable specification. Runtime authorized with RFC-0096.  
**Parent:** [WR-S4-CRIME-REPORT.md](WR-S4-CRIME-REPORT.md) · [WORLD-REPORTS.md](WORLD-REPORTS.md)  
**RFC:** [RFC-0096](../rfcs/RFC-0096-discovery-report.md)  
**Does not open:** NEWS verb · REPORT_* · WATCH ticker · QUEST help · YOUR POSITION · diplomacy · AGREEMENT_FORM · open TRADE rows  
**Next:** [DIPLOMACY-S0.md](DIPLOMACY-S0.md)

S5 adds public reconstructions to the existing 5-cycle report.

---

## Doctrine decisions

| Temptation | Verdict |
|------------|---------|
| NEWS verb | **REJECT.** |
| Hidden subject | **REJECT.** |
| Claim / author / evidence | **REJECT.** |
| Open TRADE as public | **REJECT.** Dyadic. |
| WATCH ticker | **REJECT.** |
| QUEST help | **REJECT.** |
| Diplomacy | **LATER.** No agreement store. |

---

## Slice contract

| Field | Value |
|-------|--------|
| Slice id | `wr-s5` |
| Catalog | `world-report-catalog/wr-s5` |
| Interval | 5 committed cycles (S0) |
| Added | `{label} is reconstructed.` |
| Public | `visibility=PUBLIC` and `status=RECORDED` |
| Events | none |
| PLAY | `report_lines` includes discovery lines after first interval |
| WATCH | silent |
| Help | still omits NEWS and QUEST |

---

## Runtime rule

Hosted Chamber MUST append one public discovery line per public recorded reconstruction whose subject is a public entity or room when rebuilding the last-1 public report. Isolated tests only. Help unchanged. No Genesis change. No AGREEMENT_FORM thaw.
