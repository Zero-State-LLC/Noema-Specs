# Succession

## Scope

Succession applies to:

- organization leadership
- institution custodianship
- artifact stewardship
- infrastructure control
- formal roles

## Mechanisms (closed set)

| Mechanism | Meaning |
|---|---|
| `DESIGNATED` | Prior holder named successor |
| `RULE_BASED` | Versioned rule selects successor |
| `CONSENSUS` | Declared consensus procedure completes |
| `VACANT` | Role remains empty until filled |
| `INHERITED_BY_ORGANIZATION` | Holding org retains role; individuals may change |

Schema: [`succession-record.schema.json`](../specs/succession-record.schema.json).

## Determinism

- Ordering: by cycle, then `succession_id` stable sort.
- Failed succession does not dissolve the institution by default; `institution_continues` is explicit.
- Founder departure MUST NOT auto-delete institutions that declare `survives_participant_departure: true`.

## Event-catalog impact

v0.6 foundation records succession as **derived succession records** grounded in existing ledger evidence (`ORG_MEMBER_*`, control changes, agreements). Candidate future events (`ROLE_ASSIGNED`, `ROLE_VACATED`, `SUCCESSION_RECORDED`, `INSTITUTION_TRANSFORMED`) require RFC workflow before catalog expansion. **No silent event-catalog/0.3.**

Playable office semantics (scopes, vacancy, delegation, ultra vires `FORBIDDEN`) live in [INSTITUTIONAL-AUTHORITY.md](INSTITUTIONAL-AUTHORITY.md). This file remains the transfer-mechanism authority.

## Playable DESIGNATED (GC4-S4)

Hosted `DESIGNATED` succession is specified in [GC4-S4-SUCCESSION.md](GC4-S4-SUCCESSION.md) · [RFC-0031](../rfcs/RFC-0031-designated-succession.md).

```text
NO IMPLICIT JUMP
SUCCESSION ≠ PLAYER IDENTITY TRANSFER
CONTROLLER CHANGE ≠ PLAYER SUCCESSION
```

A founder or officer writes an ordered successor list (max two) on an office or emergency scope. Vacate / leave-institution evaluates that list. Disconnect, idle, controller change, DORMANT, and office retirement do not. Emergency successors inherit the remaining validity interval.

## Playable CONSENSUS (GC4-S5)

Hosted `CONSENSUS` succession is specified in [GC4-S5-CONSENSUS.md](GC4-S5-CONSENSUS.md) · [RFC-0060](../rfcs/RFC-0060-consensus-succession.md). Members consent a vacant office. `ceil(members/2)` seats. No elections.

`RULE_BASED` and `INHERITED_BY_ORGANIZATION` remain unspecified.
