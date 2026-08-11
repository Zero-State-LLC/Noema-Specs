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
