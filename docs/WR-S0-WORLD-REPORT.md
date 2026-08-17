# WR-S0 — public world report

**Status:** Executable specification. Runtime authorized with RFC-0088.  
**Parent:** [WORLD-REPORTS.md](WORLD-REPORTS.md) · [GAME-CYCLE.md](GAME-CYCLE.md) · [PLAY.md](PLAY.md)  
**RFC:** [RFC-0088](../rfcs/RFC-0088-world-report.md)  
**Does not open:** NEWS/REPORT verb · REPORT_* · WATCH ticker · YOUR POSITION · diplomacy/conflict sections  
**Next:** [WR-S1-ORG-REPORT.md](WR-S1-ORG-REPORT.md)

S0 makes the Chamber take world-time news. A public report is last 1, rebuilt every 5 committed cycles from live public infrastructure.

---

## Doctrine decisions

| Temptation | Verdict |
|------------|---------|
| Operator Digest | **REJECT.** Admin clock |
| NEWS verb | **REJECT.** |
| `REPORT_*` | **REJECT.** Silent projection |
| WATCH ticker | **REJECT.** |
| YOUR POSITION | **REJECT.** Already status |
| Later report sections | **REJECT.** Infra condition only |
| Interval ≠ 5 | **REJECT.** |
| Help news | **REJECT.** |

---

## Slice contract

| Field | Value |
|-------|--------|
| Slice id | `wr-s0` |
| Catalog | `world-report-catalog/wr-s0` |
| Verb | none (WAIT commit rebuilds) |
| Keep | last 1 report |
| Interval | 5 committed cycles |
| Source | public live infrastructure condition |
| Events | none |
| PLAY | `report_lines` after first interval |
| WATCH | silent |
| Help | unchanged |

---

## Out of S0

```text
NEWS / REPORT verb
REPORT_* events
YOUR POSITION
diplomacy / conflict / crime / access
WATCH ticker
Chamber help news
```

---

## Runtime rule

Hosted Chamber MUST rebuild last-1 public `report_lines` when a committed cycle is ≥ 5 and divisible by 5, from public-room live infrastructure condition only. Isolated tests only. Help unchanged. No Genesis change.
