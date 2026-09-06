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

- **i18n (STRINGS + t() in ui.py / 8765)**: Centralize labels for diplomacy constructs (Alliance, Non-aggression, Trade agreement, Resource commitment, Access agreement, Warning / ultimatum, Informal understanding), formality/ledgered columns, "Formal vs informal", "Breaking agreements", "v0.1 baseline", "v0.2 formal agreements", mechanical effects (NON_AGGRESSION, ACCESS, RESOURCE_COMMITMENT, MUTUAL_DEFENSE, TRADE), "Coupling", agreement types, breach consequences in diplomacy UI surfaces, reports, study, play organization/trade views.

- **R3 Chamber**: Full diplomacy surfaces (construct tables, formal agreements, ledger events, coupling) in controller/agent-only mode per RFC-0120; human WATCH limited public projections (public agreements, basic reputation); STUDY permissioned diplomacy evidence / agreement ledgers / breach traces; PLAY isolated diplomacy simulations and social contracts. Agent-only full access in R3+ controller.

- **Gate B S0-S3**: S0 human public diplomacy views (visible agreements, basic constructs); S1-S2 limited agreement visibility / social layer; S3 controller full formal agreements / ledger writes / breach mechanics / coupling config. Controller policies for diplomacy access/rebuild. Version comparisons for agreement catalog.

- **AX**: Semantic tables for constructs (role="table", "row"), ARIA labels for formality/ledgered/effects, keyboard navigation on tables, aria-live for agreement updates/breaches, contrast via theme vars. Live regions for coupling notes.

- **noema skill/plugin atoms**: Diplomacy registry atom (list constructs, agreement viewer, ledger browser, breach simulator); integration with gateway ui for STUDY diplomacy explorer and PLAY org/trade interfaces; desktop plugin for agreement diff / reputation graph; ties to contest resolution and civilization matrix.

- **handoff / LCA2 MUD**: Cross-refs to GAME-COMPLETENESS-PLAN, R3 Chamber fixtures, WORLD-REPORTS, STRATEGIC-CONFLICT, ACTION-CONTRACTS, other EPs (CAPABILITY-*, CONTEST-RESOLUTION, CIVILIZATION-CAPABILITY-MATRIX); include in R3 evidence bundle for diplomacy; MUD craft support for agreement events and social mechanics.

- Elevation: UX discoverable diplomacy explorer and agreement ledger in Chamber; DX modular constructs + clean i18n + graft; AX semantic + keyboard + live. Additive only. 

(Part of Gate B controller independence and R3 agent-only Chamber per RFC-0120.)
