# RFC-0124 — Governance rule contract (GC4-S8)

## Status

**Accepted**

Institutional configuration contract. No new Player verbs. No new events. No
`government` entity class. No Genesis change. No reseed. Acceptance requires
maintainer action; this RFC is the machine-readable half of the gate named in
[RESEARCH-ASSIMILATION-2026-08-21.md](../docs/RESEARCH-ASSIMILATION-2026-08-21.md).

## Problem

The research assimilation note (Specs #245) rules that councils, oligarchies,
charters, rotating offices, confederations, and fragmented authority are
**configurations of existing institutions**, not a new entity class. It then
states that any future governance contract MUST make six dimensions explicit
before it can authorize world mutation, and that charter text is never
executable authority by itself.

Today there is no such contract. An institution can hold offices, succession,
agreements, and access, but there is no way to say *"this body decides that
class of thing, this way, with this quorum, and this is what happens when it
cannot decide."* Without it, governance-shaped play either fails closed with no
explanation or drifts toward free-form charter text being treated as authority.

## Decision

Introduce `governance_rule` as a **published, versioned configuration object on
an existing organization** — not a new entity, not a new verb. A rule is
executable only when all six dimensions resolve; otherwise authority is
undefined and **fails closed**.

| Dimension | Field | Required meaning |
|---|---|---|
| Decision rule | `decision.offices[]`, `decision.quorum` | Which occupied offices may decide; how many must concur |
| Appointment | `appointment.mechanism` | An existing SUCCESSION mechanism: `DESIGNATED` / `RULE_BASED` / `CONSENSUS` / `INHERITED_BY_ORGANIZATION` — no new path |
| Jurisdiction | `jurisdiction.objects[]`, `.rooms[]`, `.members[]` | The bounded set the rule may act on; empty = no jurisdiction, not universal |
| Enforcement | `enforcement.operation` | An existing canonical operation the decision carries out |
| Failure | `failure.on_vacancy`, `.on_deadlock`, `.on_expiry` | Explicit outcomes. **Absent** outcome = undefined authority; a written `REFUSE` is defined and refuses under its own reason |
| Evidence | `evidence.record` | The public or permissioned record establishing the decision |

### Hard rules

1. **Publication is required.** An unpublished rule authorizes nothing. Charter,
   constitution, law, or decree prose is never executable by itself.
2. **Empty jurisdiction is empty**, never universal. A rule with no bounded set
   authorizes nothing — the inverse of the unscoped-office convention, because a
   governance rule is opt-in configuration rather than a standing office.
3. **Enforcement must name an existing operation.** An unknown operation is
   rejected; this RFC adds none.
4. **Undefined failure fails closed — and a written refusal is not undefined.**
   A rule that *omits* `on_vacancy` or `on_deadlock` cannot act at all
   (`undefined_failure`). A rule that *writes* `REFUSE` is fully defined and
   refuses as written when a deciding office is vacant (`vacancy_refused`).
   The two are distinct so a body can deliberately choose to stop.
5. **Office precedence still governs.** A governance rule never overrides
   `INSTITUTIONAL-AUTHORITY` office conflict-precedence or emergency scopes; on
   conflict the existing resolution wins and the decision is refused.
6. **No new authority.** Every decision resolves to an operation the acting
   offices could already perform. A rule may only *constrain and record* who
   decides — never grant reach.

### Rejection vocabulary

`unpublished` · `not_deciding_office` · `quorum_short` · `out_of_jurisdiction` ·
`unknown_enforcement` · `undefined_failure` · `vacancy_refused` · `authority_conflict`

Each maps to exactly one unmet dimension, so a refusal explains itself without
leaking the rule's contents to non-members.

## Machine-readable contracts

- `specs/governance-rule.gc4-s8.schema.json` — the rule object
- `specs/governance-decision-attempt.gc4-s8.schema.json` — a decision attempt
- `specs/authority-catalog.gc4-s8.json` (+ schema) — slice pins and exclusions

Fixtures in `examples/gc4-governance/`: one positive (a quorate council decision
inside jurisdiction with evidence) and one negative per rejection reason.

`VACANT` and `INHERITED_BY_ORGANIZATION` are decided explicitly.
`INHERITED_BY_ORGANIZATION` is **in scope** — a rule may name it, and the office
follows GC4-S7 unchanged. `VACANT` is **out of scope as an appointment**: it is
the absence of appointment, so a rule naming it would fill nothing; a body that
wants an office to stay empty writes `failure.on_vacancy: REFUSE` instead.
Validator: `check_gc4_s8`.

## Visibility

A published rule's **existence, deciding offices, and jurisdiction summary** are
visible to organization members through the existing office surface. Nothing new
reaches public WATCH: no rule text, no member votes, no quorum counts. This
follows the GC3/WATCH redaction rules unchanged.

## Not in scope

No `government` entity. No elections. No free-form language interpretation. No
new verbs, events, or event-catalog bump. No belief or legitimacy score. No
cross-organization federation (a confederation is modeled as agreements between
organizations, each with its own rule). Runtime implementation follows only on
acceptance.
