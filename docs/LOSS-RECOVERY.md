# Loss and Recovery

## Design goal

NOEMA must create consequential failure without turning a single setback into game-over.

Desired pattern:

```text
SETBACK → CONSEQUENCE → ADAPTATION → RECOVERY OPPORTUNITY
```

Forbidden pattern:

```text
SETBACK → RESET
```

## Forms of loss

| Loss type | Typical causes | Visible effects |
|-----------|----------------|-----------------|
| Resource loss | Consumption, theft/seizure, trade failure, overflow | Lower holdings |
| Infrastructure damage | Degradation, sabotage, neglect | Lower condition, reduced production/modifiers |
| Route / access loss | Contested exits, restrictions, blocked paths | Movement and trade friction |
| Territorial loss | Competing presence + infrastructure control | Reduced Realm projection |
| Organization fracture | Member removal, influence collapse, crime fallout | Loss of coordination and regen |
| Reputation / influence loss | Crime, broken agreements, public failure | Harder negotiation and organization actions |
| Information loss | Forgotten knowledge, lost documents, restricted observation | Strategic blindness |

## Recovery paths

Every major loss type has at least one recovery vector:

- Repair (infrastructure)
- Re-harvest / re-trade / re-produce
- Rebuild membership and influence
- Explore alternate routes and nodes
- Form new agreements or organizations
- Wait for world-event pressure to shift
- Convert historical scars into caution or new strategy

## Persistent scars

Losses leave historical records and can create lasting disadvantages (damaged reputation, known vulnerabilities, abandoned infrastructure). Scars are desirable narrative and strategic material. They must not create permanent unwinnable states.

## Anti-snowball

See also [GAME-BALANCE.md](GAME-BALANCE.md). Large successful Realms naturally acquire higher maintenance, larger attack surface, and coordination overhead. These are structural, not arbitrary debuffs.

## Relation to contracts

Loss and recovery must be expressible through existing resources, infrastructure condition, organization membership, and ledgered events ([RESOURCE-ECONOMY.md](RESOURCE-ECONOMY.md), [STRATEGIC-CONFLICT.md](STRATEGIC-CONFLICT.md)).

## Extension Points

Non-normative future guidance; this section does not change the contracts or dated outcomes above.

**Seam.** Recovery scenario coverage can be expanded for combinations of route loss, damaged infrastructure, fractured membership, and strategic information loss using existing action families.

**Preserved invariants.** Keep consequential scars and historical records: recovery is adaptation, not reset, guaranteed victory, or a paid history wipe. Realm scale creates structural costs rather than arbitrary debuffs.

**Compatibility and promotion.** New recovery affordances or resource effects require the relevant Accepted contract and versioned parameters; examples cannot add verbs or override the conflict and resource authorities.

**Validation expectations.** Trace each proposed loss through observable consequences and at least one contract-supported recovery vector; include scarce resources and restricted routes without asserting that every attempted recovery succeeds.
