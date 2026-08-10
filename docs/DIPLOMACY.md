# Diplomacy

## Scope

Simple strategic diplomacy for v0.1 extension and v0.2.

## Constructs

| Construct | Formality | Ledgered? |
|-----------|-----------|-----------|
| Alliance | Formal | Yes (organization or pairwise contract) |
| Non-aggression | Formal | Yes |
| Trade agreement | Formal or informal | Formal = ledgered; informal = social only |
| Resource commitment | Formal | Yes |
| Access agreement | Formal | Yes |
| Warning / ultimatum | Message | No (social) |
| Informal understanding | Message / behavior | No |

## Formal vs informal

- **Formal** agreements are world events and appear in history and reports.
- **Informal** agreements are pure social behavior. Breaking them has only social consequences unless the parties escalate into formal conflict or crime.

## Breaking agreements

Only formal ledgered agreements produce automatic world-visible mechanical consequences when broken. Informal breaches remain in the realm of reputation and future trust.

## v0.1 baseline

Organizations + messaging already enable the social layer ([ACTION-CONTRACTS.md](ACTION-CONTRACTS.md)). Formal pairwise contracts are the next minimal addition (may require RFC for new event types).

## Coupling

Diplomacy couples to trade, territory, organizations, crime fallout, and reports ([WORLD-REPORTS.md](WORLD-REPORTS.md), [STRATEGIC-CONFLICT.md](STRATEGIC-CONFLICT.md)).
