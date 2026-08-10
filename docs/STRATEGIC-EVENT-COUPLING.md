# Strategic Event Coupling (event-catalog/0.2)

## Purpose

Normative allowed and forbidden sequences among contestation, crime, access, infrastructure, and agreement events. Reducers apply one event at a time; command resolution may append an ordered batch.

## Valid sequences

### Infrastructure contest (canonical package)

```text
AGREEMENT_FORMED? (optional prior)
→ CONTEST_DECLARED
→ CONTEST_RESOLVED
→ INFRASTRUCTURE_DISRUPTED? (success/partial)
→ CRIME_DETECTED? (if detection path succeeds)
→ ACCESS_RESTRICTED? (policy/crime/contest)
→ AGREEMENT_BROKEN? (if terms forbid form)
```

### Resource seizure

```text
CONTEST_DECLARED (RESOURCE_SEIZURE)
→ CONTEST_RESOLVED
→ RESOURCE_TRANSFER? (success/partial, amount rules)
→ CRIME_DETECTED?
```

### Access contest

```text
CONTEST_DECLARED (ACCESS_CONTEST)
→ CONTEST_RESOLVED
→ ACCESS_RESTRICTED
→ CRIME_DETECTED?
```

### Presence pressure

```text
CONTEST_DECLARED (PRESENCE_PRESSURE)
→ CONTEST_RESOLVED
→ MOVE? and/or ENTITY_UPDATE (disable flag)
→ CRIME_DETECTED?
```

### Formal access without contest

```text
AGREEMENT_FORMED (ACCESS)
→ ACCESS_RESTRICTED (mode ALLOW_ONLY or CLEAR) optional
```

### Breach

```text
AGREEMENT_FORMED
→ … violating world event(s) …
→ AGREEMENT_BROKEN
→ optional ACCESS_RESTRICTED / CRIME_DETECTED
```

## Forbidden / reject

| Pattern | Reason |
|---------|--------|
| `CONTEST_RESOLVED` twice for same `contest_id` | Contest not OPEN |
| `CONTEST_RESOLVED` without prior `CONTEST_DECLARED` | Missing record |
| `INFRASTRUCTURE_DISRUPTED` with unknown entity | Invalid target |
| `INFRASTRUCTURE_DISRUPTED` with `condition_before` ≠ live condition | Stale |
| `CRIME_DETECTED` with empty `source_event_ids` | No evidence |
| Sensor crime when sensor condition &lt; `sensor_min_condition` | No coverage |
| Witness crime with empty `witness_ids` | Method mismatch |
| `ACCESS_RESTRICTED` scope not EXIT/ROOM | Schema |
| `AGREEMENT_BROKEN` for non-ACTIVE agreement | Lifecycle |
| Breach without objective term violation or explicit terminate | Social-only |
| 0.1 catalog accepting 0.2 types | Catalog isolation |
| Condition mutation only inside `CONTEST_RESOLVED` | Use disruption event |

## Transaction boundaries

| Command | Atomic batch |
|---------|--------------|
| `COMMIT.CONTEST_DECLARE` | `CONTEST_DECLARED` (+ optional `BUDGET_CONSUMED` for declare base cost if not folded into stake) |
| `COMMIT.CONTEST_DEFEND` | No ledger event; reserves defender stake on OPEN contest in engine reservation table (replayed from command log / resolve payload) |
| World resolve contest | `CONTEST_RESOLVED` then follow-ons in fixed order: transfer → disruption → access → crime → agreement_broken → move |
| `COMMIT.AGREEMENT_FORM` | `AGREEMENT_FORMED` |
| `COMMIT.AGREEMENT_TERMINATE` | `AGREEMENT_BROKEN` |
| `COMMIT.ACCESS_POLICY` | `ACCESS_RESTRICTED` |

If any event in a multi-event resolve batch fails preconditions, the **entire batch is rejected** before append (no half-settled stakes). Implementations that append only after full validation satisfy this.

## Unauthorized vs detected

| Concept | Ledger |
|---------|--------|
| Unauthorized action | May already be a world event (e.g. contest, move reject path) |
| Detected crime | Only `CRIME_DETECTED` |

Crime can exist socially without `CRIME_DETECTED`. Detection is not omniscient.

## Observability summary

| Event | Parties | Co-located | Public spectator | Research |
|-------|---------|------------|------------------|----------|
| CONTEST_DECLARED | full | form + room | banded stakes | full |
| CONTEST_RESOLVED | full | outcome | outcome band | full |
| CRIME_DETECTED | subject + witnesses | if public flag | if PUBLIC_HISTORY | full |
| ACCESS_RESTRICTED | all who LOOK exits | — | route status | full |
| INFRASTRUCTURE_DISRUPTED | co-located / owners | condition band | band | full |
| AGREEMENT_* | parties | if PUBLIC | summary | full |

## Replay equivalence

Exact match required on: contest records, reservations settled, outcomes, resources, infrastructure condition, restrictions, crime records, agreements, event order, digests.
Excluded: host timestamps, narrative formatting.
