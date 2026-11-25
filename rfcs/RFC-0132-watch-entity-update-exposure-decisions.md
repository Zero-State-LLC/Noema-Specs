# RFC-0132: WATCH `ENTITY_UPDATE` exposure decisions (RESTORE, VEST, PROMOTE, SHARE, CONNECT, CONSENT, RULE)

## Status

**Accepted**

Owner approval: Danny, in chat, 2026-11-24 11:09 PM PT ("All spec changes are approved let's get this cracking"). He was answering the research page *Noema watch surface: making it fun to watch*, which proposed exposure decisions for these operations.

This RFC is the separate exposure decision that [RFC-0126](RFC-0126-watch-entity-update-exposure.md) requires before any `ENTITY_UPDATE` operation can reach public WATCH. RFC-0126 stays Accepted, and its fail-closed default is unchanged: an operation absent from both contracts is silent.

## Problem

The public WATCH feed is sparse. A four-minute live sample (2026-11-24, OBSERVED) showed mostly moves, harvests and "a report is circulating". Several operations that change public sites stay silent because their founding RFCs said "WATCH silent" when no exposure decision existed. Each needs a deliberate decision: open it with a bounded public line, or keep it closed and say why.

## Decisions

| Operation | Founding RFC | Decision | Public projection | Public line | Reasoning |
|---|---|---|---|---|---|
| `RESTORE` | [RFC-0059](RFC-0059-restore.md) | **Open** | `production` | `An abandoned asset was restored at <site>` | The target is a live public `UNCLAIMED` constructible in a public room (RFC-0059; ruins and scars are excluded and stay irreparable). Its unclaimed state is already public in LOOK. Restoration is a visible change to a public place and reveals no private holding. The actor is named only under the existing public-handle rules (§6); otherwise the line has no actor. |
| `VEST` | [RFC-0067](RFC-0067-institution-own.md) | **Open, without the institution** | `organization` | `An asset at <site> passed into institutional hands` | The asset is public and in a public room, and the ownership change is a civic fact. The receiving organization is **not** named: membership and holdings of an organization are not otherwise public, so the line withholds it. The actor follows the public-handle rules. |
| `PROMOTE` | system tick (multi-cycle construction completes) | **Open** | `production` | `Construction finished at <site>` | A system act with no actor, in a public room only (hidden rooms are skipped at the source). The finished entity is visible in LOOK from then on. The line carries no class, owner or quantity. `in_progress` updates (construction start or progress) stay silent. |
| `SHARE` | [RFC-0079](RFC-0079-second-co-owner.md), RFC-0085–0087 | **Closed** | — | — | Co-ownership is a private tie between two Players. A public line would disclose a pairwise relationship that has no other public counterpart. |
| `CONNECT` | [RFC-0071](RFC-0071-connect-dest.md) | **Closed** | — | — | A route link faces a destination. RFC-0071 records that naming it can leak hidden topology. WS3-02 forbids inferring hidden routes, and a "connected" line is exactly such a hint. |
| `CONSENT` / `CONSENSUS` | [RFC-0060](RFC-0060-consensus-succession.md) | **Closed** | — | — | Individual consents reveal a member's political stance before any outcome. The outcome (a seat) already reuses the public pulse `A designated successor has taken an institution office.` |
| `RULE` | [RFC-0069](RFC-0069-rule-based-succession.md) | **Closed** | — | — | Publishing a succession rule is internal institution procedure. The seat it produces already reaches WATCH through the reused pulse, and a second line would duplicate it (the RFC-0126 HARVEST defect). |

Unchanged: `REPURPOSE` ([RFC-0057](RFC-0057-workshop-repurpose.md)), `ABANDON` ([RFC-0058](RFC-0058-abandonment.md)), RFC-0070 inherited-org updates, the four RFC-0126 silent operations, and every unknown operation stay silent.

Machine contract: [`watch-entity-update-exposure-decisions.rfc-0132.json`](../specs/watch-entity-update-exposure-decisions.rfc-0132.json).

## Rules for the opened operations

1. The event must resolve a public site through the existing entity-home rule. An unlocated or hidden-room event produces no WATCH item.
2. No identifier, quantity, entity class, owner, co-owner or organization name appears in the line, the `consequence` or the `detail`.
3. Tiers come from the existing projection table (`production`, `organization`). No new projection id, tier or field is added, so `watch-live/1.0` is unchanged.
4. Each opened operation produces exactly one WATCH line per act.

## Alternatives rejected

| Alternative | Why |
|---|---|
| Open all seven | SHARE, CONNECT, CONSENT and RULE each disclose private ties, hidden topology, stances or duplicate lines |
| Name the institution on VEST | Organization holdings are not otherwise public |
| New projection ids (`restoration`, `construction`) | Would change the public catalog; the existing ids carry these honestly |

## Compatibility

Additive public presentation for three operations. Ledger events, PLAY, Admin, world state and event catalogs are unchanged. The founding RFCs' "WATCH silent" clauses for `RESTORE`, `VEST` and `PROMOTE` are superseded by this RFC for public WATCH only. PLAY copy is unchanged.

## Data / security

No stored data changes. Hidden-room and entity-site redaction stay unchanged. The RFC-0126 hidden-room sweep must cover the three opened operations.

## Validation

Runtime tests MUST pin:

1. `RESTORE`, `VEST` and `PROMOTE` in a public room produce exactly one WATCH item, with the projection and line above;
2. the same operations in a hidden room, or unlocated, produce none;
3. `VEST` lines never contain the organization name or id;
4. `SHARE`, `CONNECT`, `CONSENT`, `CONSENSUS`, `RULE` and unknown operations stay silent; and
5. the RFC-0126 contract and hidden-room sweep stay green.

The runtime pins that currently assert `RESTORE` and `VEST` are silent (`gc2-s8`, `gc2-s10`) change for this contract; that test change needs the owner's review.

The Specs validator MUST load this contract, confirm its open and closed sets are disjoint and disjoint from the RFC-0126 sets, and confirm the default stays silent.

## Rollback

Move the three operations back to closed. Presentation-only rollback; no data migration.

## Unresolved

None.
