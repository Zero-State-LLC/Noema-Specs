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

Organizations + messaging enable the social layer ([ACTION-CONTRACTS.md](ACTION-CONTRACTS.md)).

Hosted family: [DIPLOMACY-S0.md](DIPLOMACY-S0.md) · [DIPLOMACY-S1.md](DIPLOMACY-S1.md) · [DIPLOMACY-S2.md](DIPLOMACY-S2.md) · [RFC-0100](../rfcs/RFC-0100-diplomacy-closeout.md).

## v0.2 formal agreements (RFC-0002 Accepted)

Ledgered via `AGREEMENT_FORMED` / `AGREEMENT_BROKEN` on `event-catalog/0.2`.

| Type | Mechanical effect |
|------|-------------------|
| `NON_AGGRESSION` | Listed `forbidden_contest_forms` → breach if party declares matching contest |
| `ACCESS` | Machine `access_exit_ids` / `access_room_ids` consulted as allow exceptions |
| `RESOURCE_COMMITMENT` | Exact amount/resource/by_cycle; miss → breach |
| `MUTUAL_DEFENSE` | `defense_support_millipoints` enters contest score for defender |
| `TRADE` | Optional preferential flag only; transfers still use TRADE events |

Informal understandings remain non-ledgered.

## Coupling

Diplomacy couples to trade, territory, organizations, crime fallout, and reports ([WORLD-REPORTS.md](WORLD-REPORTS.md), [STRATEGIC-CONFLICT.md](STRATEGIC-CONFLICT.md)).

## Extension Points

Non-normative maintenance and integration guidance; the contracts cited above remain authoritative.

### Document-specific seam

Extend coupling tests by following a formal agreement into its existing trade, access, commitment, or contest effect and contrasting an informal message-based understanding. A display may explain evidence of breach without promoting social interpretation into automatic sanctions.

### Compatibility and promotion

RFC-0002 and the accepted hosted family govern signatories, types, machine effects, and visibility. No full-Controller tier grants ledger writes, breach configuration, or hidden terms. New agreement semantics need an RFC; informal understandings remain social and the world does not infer a binding contract from prose.

### Verification before adoption

Compare an accepted formal agreement with a similar informal promise, then exercise the relevant deadline or breach condition. Check ordinary transfers remain TRADE events and access/defense effects use existing pins. Replay the same events and confirm equivalent state and public projections without exposing private agreement data.
