# Strategic Conflict Acceptance (RFC-0002 / catalog 0.2)

## Acceptance items (S01–S18)

| # | Family | Requirement |
|---|--------|-------------|
| 1 | S01 Contest Declaration | Schema + stake + form/target rules |
| 2 | S02 Stake Reservation | Minimum stakes; no double-spend |
| 3 | S03 Contest Defense | Defend reservation; passive modifiers |
| 4 | S04 Deterministic Resolution | Integer algorithm + digest |
| 5 | S05 Resource Seizure | Transfer follow-on only |
| 6 | S06 Infrastructure Disruption | condition_before/after; floor 0 |
| 7 | S07 Access Restriction | EXIT/ROOM; DENY/ALLOW_ONLY/CLEAR; cycle expiry |
| 8 | S08 Presence Pressure | No permanent removal; bounded disable/move |
| 9 | S09 Crime Detection | Evidence path required |
| 10 | S10 Crime Consequences | Severity bands; influence floor 0 |
| 11 | S11 Agreement Formation | Machine terms; ≥2 parties |
| 12 | S12 Agreement Breach | Objective breach; influence map |
| 13 | S13 Event Coupling | Valid/forbidden sequences |
| 14 | S14 Partial Observability | Redactions honored |
| 15 | S15 Spectator Projection | Seven projection ids |
| 16 | S16 Replay Equivalence | Digests + boundary |
| 17 | S17 Catalog Isolation | 0.1 rejects 0.2 types |
| 18 | S18 Migration | Explicit pin; no silent upgrade |

## Evidence package

- `specs/event-types.0.2.json`
- `specs/contest-config.v02.json`
- `specs/action-contracts.v02.json`
- `examples/v02-strategic-conflict/`
- `conformance/v0.2-strategic/`
- `docs/CONTEST-RESOLUTION.md`
- `docs/STRATEGIC-EVENT-COUPLING.md`
- RFC-0002 **Accepted**

## Extension Points

Non-normative guidance for future maintenance; no new behavior is authorized here.

- **Acceptance seam:** Extend concrete positive and rejection cases within S01–S18, especially reservation settlement and permitted event coupling. Keep this release checklist mapped to RFC-0002 and its evidence package, not a competing contest algorithm.
- **Compatibility boundary:** Preserve catalog 0.1 rejection of 0.2 types and explicit world pin migration. Later contest slices require their own catalog/contract evidence; they do not silently change the meaning of the original S-family acceptance record.
- **Validation expectations:** Reconcile declaration/defense stake ledgers with resolution follow-ons, test forbidden sequences and private stake redaction, compare replay digests, and reject unapproved upgrades. Attach exact fixtures and runner results for each strengthened coverage claim, retaining previous release evidence and any non-comparable cases.
