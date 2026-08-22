# GC4-S8 — Governance rule as bounded institutional configuration

**Status:** Draft slice contract pending [RFC-0124](../rfcs/RFC-0124-governance-rule-contract.md).
**Catalog:** [`authority-catalog.gc4-s8.json`](../specs/authority-catalog.gc4-s8.json).
**Kind:** institutional configuration. No new Player verbs. No new events. No
`government` entity. No Genesis change.

Related: [INSTITUTIONAL-AUTHORITY.md](INSTITUTIONAL-AUTHORITY.md) ·
[INSTITUTIONS.md](INSTITUTIONS.md) · [SUCCESSION.md](SUCCESSION.md) ·
[DIPLOMACY.md](DIPLOMACY.md) ·
[RESEARCH-ASSIMILATION-2026-08-21.md](RESEARCH-ASSIMILATION-2026-08-21.md) (Slice B).

## Boundary

A council, oligarchy, chartered organization, rotating office, confederation, or
fragmented authority is a **configuration of existing institutions** — offices,
succession, agreements, territory, access, and enforcement. This slice adds the
configuration object and its refusal semantics. It adds no reach: every decision
resolves to an operation the acting offices could already perform.

## The six dimensions

A `governance_rule` is executable only when all six resolve. Any unmet dimension
refuses the decision.

| Dimension | Field | Required meaning |
|---|---|---|
| Decision rule | `decision.offices[]`, `decision.quorum` | Which occupied offices may decide, and how many must concur |
| Appointment | `appointment.mechanism` | An existing SUCCESSION mechanism: `DESIGNATED` / `RULE_BASED` / `CONSENSUS` / `INHERITED_BY_ORGANIZATION` |
| Jurisdiction | `jurisdiction.objects[] / .rooms[] / .members[]` | The bounded set the rule may act on |
| Enforcement | `enforcement.operation` | An existing canonical operation |
| Failure | `failure.on_vacancy`, `.on_deadlock`, `.on_expiry` | Explicit outcomes. Absent = undefined authority; written `REFUSE` = defined refusal |
| Evidence | `evidence.record` | The public or permissioned record establishing the decision |

## Fail-closed rules

- **Unpublished rules authorize nothing.** Charter, constitution, law, or decree
  prose is not executable authority by itself.
- **Empty jurisdiction is empty, never universal.** Unlike a standing office, a
  governance rule is opt-in configuration; an unbounded rule authorizes nothing.
- **Unknown enforcement refuses.** The operation must already exist.
- **Undefined failure refuses** (`undefined_failure`): a rule that *omits*
  `on_vacancy` or `on_deadlock` cannot act at all.
- **A written refusal is not undefined** (`vacancy_refused`): a rule that writes
  `REFUSE` is fully defined and stops as it chose to.
- **`VACANT` is not an appointment mechanism** — it is the absence of one. To
  keep an office empty, write `failure.on_vacancy: REFUSE`.
- **Office precedence still governs.** On conflict with
  `INSTITUTIONAL-AUTHORITY` precedence or an emergency scope, the existing
  resolution wins and the decision is refused.

Rejection vocabulary: `unpublished`, `not_deciding_office`, `quorum_short`,
`out_of_jurisdiction`, `unknown_enforcement`, `undefined_failure`,
`vacancy_refused`, `authority_conflict`.

## Visibility

Members may see that a rule exists, its deciding offices, and a jurisdiction
summary through the existing office surface. Rule text, votes, and quorum counts
are not public. Nothing new reaches WATCH.

## Acceptance scenario

An institution publishes a bounded decision rule, fills a vacant office through
an existing succession path, authorizes an existing resource/access/contest
action within jurisdiction, and later survives a vacancy or refuses cleanly when
a dimension is unmet. No government object and no language interpreter is created.

## Conformance

Positive and negative fixtures in `examples/gc4-governance/` — one accepting
case and one per rejection reason — are evaluated by `check_gc4_s8` in
`validation/validate_all.py`.
