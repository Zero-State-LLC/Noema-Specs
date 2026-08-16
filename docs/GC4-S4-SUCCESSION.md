# GC4-S4 — Designated Institutional Succession

**Status:** Executable specification. Runtime authorized with RFC-0031.  
**Parent:** [SUCCESSION.md](SUCCESSION.md) · [GC4-S3-EMERGENCY-SCOPES.md](GC4-S3-EMERGENCY-SCOPES.md) · [INSTITUTIONAL-AUTHORITY.md](INSTITUTIONAL-AUTHORITY.md)  
**RFC:** [RFC-0031](../rfcs/RFC-0031-designated-succession.md)  
**Does not open:** elections · dynasties · dormancy clocks · `event-catalog/0.3` · GC1-S2 benefits

S4 answers: when the holder of an office or emergency scope becomes unavailable, who—if anyone—receives a **predeclared** successor authority?

---

## Doctrine

```text
NO IMPLICIT JUMP
OFFICE CONTINUITY ≠ PLAYER CONTINUITY
CONTROLLER CHANGE ≠ PLAYER SUCCESSION
succession cannot extend emergency expiry by default
```

| Temptation | Verdict |
|------------|---------|
| Nearest / oldest / most active | **REJECT** |
| Disconnect / idle / controller swap | **REJECT** |
| DORMANT alone | **REJECT** |
| Reset emergency window | **REJECT** |
| Transfer reputation / private knowledge | **REJECT** |
| Current holder designates unless founder/officer | **REJECT** |
| Retired office succeeds | **REJECT** |
| Dissolved institution activates | **REJECT** |

---

## Rule

Stored on the office or emergency scope (not a new table):

| Field | Meaning |
|-------|---------|
| `successors[]` | Ordered Player ids. Hosted max **2** |
| `designated_by` | Founder/officer who wrote the rule |
| `designated_cycle` | World cycle |

Mechanism is `DESIGNATED` only. Consensus / rule-based / inherited-by-org stay out.

`COMMIT.ORG_SUCCESSION_DESIGNATE` — founder or officer of an ACTIVE org. Successor must be a current member, same world. Overwrite replaces the list (one rule per seat/scope). Two competing sources in this slice do not exist; a second designate is an explicit rewrite, not a silent pick.

Human alias (org help only):

```text
succession <office> <player> [player2]
succession scope <scope> <player> [player2]
```

---

## Triggers

Evaluate immediately in the same settlement after:

```text
ORG_OFFICE_VACATE (resign / remove-from-office)
ORG_MEMBER_REMOVE / leave-org of the current holder
```

Do **not** evaluate on:

```text
LEAVE_WORLD / disconnect / idle
controller replacement
DORMANT
ORG_OFFICE_RETIRE (seat ends; no successor)
institution not ACTIVE
```

---

## Eligibility (at activation)

```text
successor exists in this world
org ACTIVE
successor is a current member
office is not RETIRED
successor ≠ departed holder
```

Check candidate 1, then candidate 2. No dynamic ranking. If none pass: office stays `VACANT` or emergency scope becomes unstaffed (no holder; cannot authorize).

---

## Transfer

Office:

```text
VACANT
→ first eligible successor
→ OCCUPIED, same office_id and profile
→ history records VACATED then ASSIGNED
```

Emergency scope:

```text
old holder ends
new holder = successor
end_cycle unchanged
capability, target, spent unchanged
```

Treasury and institution-owned assets do not move. Personal danger/trade memory does not copy.

---

## Events

`ENTITY_UPDATE` on the office or scope. No `SUCCESSION_*` types. Payload MAY include `succession_from`, `succession_to`, `designated_by`.

---

## Visibility

| Surface | Sees |
|---------|------|
| PLAY (members) | `Designated successor — {handle}` on public offices |
| WATCH | `A designated successor has taken an institution office.` when activation is public |
| Admin | Full rule, candidates, last activation |

---

## Out of S4

```text
elections / parties / dynasty
DORMANT-for-N-cycles rule
consensus — closed in [GC4-S5-CONSENSUS.md](GC4-S5-CONSENSUS.md)
rule-based mechanisms
SUCCESSION_* catalog
leadership XP
```

---

## Runtime rule

Hosted Chamber evaluates designation only after an explicit vacancy/leave-org trigger. Do not reseed Genesis.

## Acceptance

1. Designate then resign → successor occupies the same office.
2. No designation → vacancy remains.
3. Emergency successor keeps the original `end_cycle`.
4. Disconnect / controller change does not fire.
5. Ineligible / cross-world successor does not activate.
6. Human and agent successors are equivalent.
