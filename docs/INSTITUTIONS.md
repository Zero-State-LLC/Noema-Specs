# Institutions

## Definition

An **institution** is not merely an organization. An organization is a membership container. An institution is a **persistent practice or stewardship** that can survive participant change when continuity rules are met.

Minimum required dimensions (`institution/0.6`):

| Field | Meaning |
|---|---|
| `institution_id` | Stable machine identity |
| `origin` | How it emerged (practice, agreement, custom, stewardship, order) |
| `purpose` | Declared purpose string |
| `persistent_practices` | At least one recorded practice |
| `status` | Lifecycle state |
| `succession_mechanism` | How roles continue |
| `continuity` | Same/successor/new/disputed identity class |
| `evidence_refs` | Grounding events/artifacts |
| `digest` | Content identity (`noema-jcs/1`) |

## Lifecycle (deterministic)

```text
EMERGING → ESTABLISHED → ACTIVE ⇄ DORMANT → TRANSFORMED | DISSOLVED
```

| Transition | Gate |
|---|---|
| EMERGING → ESTABLISHED | Origin evidence + practice recorded + ≥1 cycle continuity |
| ESTABLISHED → ACTIVE | Custodian or inheritor present OR succession mechanism does not require active custodian |
| ACTIVE → DORMANT | No active custodians when `requires_active_custodian` and dormancy threshold met |
| DORMANT → ACTIVE | Explicit revival with same `institution_id` and continuity class `SAME_ENTITY_EVOLVED` |
| * → TRANSFORMED | Material rule/purpose change with successor edge |
| * → DISSOLVED | Explicit dissolution; history retained; no silent delete |

Do not infer persistence from prose. Do not silently delete institutions.

## Persistence beyond participants

May survive departure: name, assets, territory associations, rules/practices, roles (possibly vacant), archive, agreements, historical records, shared artifacts.

If no custodians remain and `requires_active_custodian`: **ACTIVE → DORMANT**, not deletion.

## Bounded scope

v0.6 is not a constitutional-law engine. Examples in scope: archive stewardship, relay maintenance order, trade compact custom, emergency-energy custom, territorial council practice.
