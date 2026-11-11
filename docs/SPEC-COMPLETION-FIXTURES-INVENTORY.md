# Spec Completion fixtures: per-GC inventory

**Status:** Inventory for [#388](https://github.com/Zero-State-LLC/Noema-Specs/issues/388), part of [#364](https://github.com/Zero-State-LLC/Noema-Specs/issues/364). Follow-up to [SPEC-COMPLETION-FIXTURES-SEED.md](SPEC-COMPLETION-FIXTURES-SEED.md). Docs only: no contract, schema, catalog, fixture, validator or RFC status changes.

**Source:** Specs `main` at `be212ecc414976cb2d05ec90d1419e817399be6d` (2026-11-11). `validation/run.sh` passed at that commit.

## Evidence classes

This inventory keeps four classes apart and never promotes one into another.

| Class | Meaning | Established here |
|---|---|---|
| 1. Fixture exists | A JSON file under `examples/gcN-*` | Yes, for every row below |
| 2. Executed Specs assertion | `validation/validate_all.py` loads the fixture, validates it against its schema, recomputes the expected result from the contract model, and requires the governing RFC to be Accepted | Yes, for every row below |
| 3. Runtime behaviour | The Noema runtime implements the contract | No |
| 4. Hosted behaviour or historical gate acceptance | A hosted receipt or a gate verdict | No |

A row below is evidence of classes 1 and 2 only. It is not a runtime receipt, hosted evidence or gate acceptance.

## Method

- **Pack:** one `examples/gcN-*` directory. There are 83 packs holding 458 fixtures.
- **Check:** the `check_gc*` function in `validation/validate_all.py` that loads the pack. Every check is reached from `main()`, and every fixture file in every pack is loaded by its check: none is present but unexecuted.
- **Authority:** the slice document the pack's README names (or the slice document for the two packs without a README) and every RFC the check requires to be Accepted. All of those RFCs are Accepted at the source commit.
- **+ and −:** for packs whose fixtures carry `expected.outcome`, + is `ACCEPT` and − is `REJECT`, listed with the `reason` code as recorded. Derivation packs carry an expected projection instead of an outcome. For them, − means the fixture's expected note withholds, excludes or refuses the effect the slice adds, or keeps it off a surface; + means the effect is derived. Controls are boundary cases that are neither: two in `gc8-lot-quality` and one in `gc8-transport`.

## Per-GC disposition

| GC | Goal | Packs | Fixtures | + | − | Disposition |
|---|---|---|---|---|---|---|
| GC1 | Mastery and specialization | 8 | 44 | 24 | 20 | Positive and negative, classes 1–2 |
| GC2 | Construction and world modification | 26 | 117 | 62 | 55 | Positive and negative, classes 1–2 |
| GC3 | Social memory and relational reputation | 8 | 18 | 10 | 8 | Positive and negative, classes 1–2 |
| GC4 | Institutional roles and bounded authority | 9 | 84 | 32 | 52 | Positive and negative, classes 1–2 |
| GC5 | Communication ecology | 14 | 72 | 42 | 30 | Positive and negative, classes 1–2 |
| GC6 | Systemic mystery and discovery | 2 | 19 | 8 | 11 | Positive and negative, classes 1–2 |
| GC7 | Strategic conflict v2 | 5 | 29 | 11 | 18 | Positive and negative, classes 1–2 |
| GC8 | Economic specialization | 5 | 21 | 10 | 8 | Positive and negative, classes 1–2 (3 controls) |
| GC9 | Emergent culture | 3 | 23 | 8 | 15 | Positive and negative, classes 1–2 |
| GC10 | World Steward pressure | 3 | 31 | 8 | 23 | Positive and negative, classes 1–2 |
| **All** | | **83** | **458** | **215** | **240** | |

Every GC has at least one positive and one negative fixture executed against an Accepted RFC. Runtime, hosted and gate evidence (classes 3 and 4) is not inventoried for any GC.

## Packs

### GC1

| Pack | Check | Authority | Fixtures | + | − | Negative cases |
|---|---|---|---|---|---|---|
| [`gc1-mastery`](../examples/gc1-mastery/) | `check_gc1_s0`, `check_gc1_s1` | [GC1-FIRST-SLICE](GC1-FIRST-SLICE.md) · [GC1-S1-RECOGNITION](GC1-S1-RECOGNITION.md) · [RFC-0004](../rfcs/RFC-0004-derived-mastery-projection.md) · [RFC-0005](../rfcs/RFC-0005-mastery-recognition.md) | 4 | 2 | 2 | `rebuild-negative`, `rebuild-s1-below-threshold` |
| [`gc1-s2`](../examples/gc1-s2/) | `check_gc1_s2` | [GC1-S2-ENGINEER-QUALITY](GC1-S2-ENGINEER-QUALITY.md) · [RFC-0020](../rfcs/RFC-0020-archive-claim-attest.md) · [RFC-0040](../rfcs/RFC-0040-engineer-quality.md) | 4 | 3 | 1 | `attempt-first-asset` |
| [`gc1-s3`](../examples/gc1-s3/) | `check_gc1_s3` | [GC1-S3-DECAY](GC1-S3-DECAY.md) · [RFC-0043](../rfcs/RFC-0043-mastery-decay.md) | 4 | 2 | 2 | `attempt-idle-latent`, `attempt-unrecognized` |
| [`gc1-s4`](../examples/gc1-s4/) | `check_gc1_s4` | [GC1-S4-PRIOR-WORK](GC1-S4-PRIOR-WORK.md) · [RFC-0044](../rfcs/RFC-0044-prior-work-benefits.md) | 6 | 3 | 3 | `attempt-broker-stranger`, `attempt-explorer-first`, `attempt-latent` |
| [`gc1-s5`](../examples/gc1-s5/) | `check_gc1_s5` | [GC1-S5-OFFICE-ELIGIBILITY](GC1-S5-OFFICE-ELIGIBILITY.md) · [RFC-0055](../rfcs/RFC-0055-office-eligibility.md) | 6 | 4 | 2 | REJECT `ineligible`×2 |
| [`gc1-s6`](../examples/gc1-s6/) | `check_gc1_s6` | [GC1-S6-PUBLIC-TITLES](GC1-S6-PUBLIC-TITLES.md) · [RFC-0105](../rfcs/RFC-0105-public-titles.md) | 8 | 4 | 4 | REJECT `HIDDEN_ROOM`, `LATENT`, `SELF_ONLY`, `UNRECOGNIZED` |
| [`gc1-s7`](../examples/gc1-s7/) | `check_gc1_s7` | [GC1-S7-FOCUS](GC1-S7-FOCUS.md) · [RFC-0110](../rfcs/RFC-0110-focus-declaration.md) | 6 | 4 | 2 | REJECT `HIDDEN_ROOM`, `LATENT` |
| [`gc1-s8`](../examples/gc1-s8/) | `check_gc1_s8` | [GC1-S8-PARAMETER-ACCESS](GC1-S8-PARAMETER-ACCESS.md) · [RFC-0112](../rfcs/RFC-0112-parameter-access.md) | 6 | 2 | 4 | REJECT `BUDGET`, `LATENT`, `LOCKED`×2 |

### GC2

| Pack | Check | Authority | Fixtures | + | − | Negative cases |
|---|---|---|---|---|---|---|
| [`gc2-construction`](../examples/gc2-construction/) | `check_gc2_s0` | [GC2-FIRST-SLICE](GC2-FIRST-SLICE.md) · [RFC-0006](../rfcs/RFC-0006-construction-existing-events.md) | 6 | 2 | 4 | REJECT `BUDGET_EXCEEDED`, `NOT_OBSERVABLE`, `NOT_OWNER`, `SLOT_OCCUPIED` |
| [`gc2-route-link`](../examples/gc2-route-link/) | `check_gc2_s1` | [GC2-S1-ROUTE-LINK](GC2-S1-ROUTE-LINK.md) · [RFC-0049](../rfcs/RFC-0049-route-link.md) | 4 | 3 | 1 | REJECT `hidden` |
| [`gc2-workshop`](../examples/gc2-workshop/) | `check_gc2_s2` | [GC2-S2-WORKSHOP](GC2-S2-WORKSHOP.md) · [RFC-0050](../rfcs/RFC-0050-workshop.md) | 4 | 3 | 1 | REJECT `hidden` |
| [`gc2-defensive`](../examples/gc2-defensive/) | `check_gc2_s3` | [GC2-S3-DEFENSIVE-WORK](GC2-S3-DEFENSIVE-WORK.md) · [RFC-0052](../rfcs/RFC-0052-defensive-work.md) | 4 | 3 | 1 | REJECT `hidden` |
| [`gc2-annex`](../examples/gc2-annex/) | `check_gc2_s4` | [GC2-S4-ARCHIVE-ANNEX](GC2-S4-ARCHIVE-ANNEX.md) · [RFC-0053](../rfcs/RFC-0053-archive-annex.md) | 4 | 3 | 1 | REJECT `hidden` |
| [`gc2-upgrade`](../examples/gc2-upgrade/) | `check_gc2_s5` | [GC2-S5-UPGRADE](GC2-S5-UPGRADE.md) · [RFC-0056](../rfcs/RFC-0056-workshop-upgrade.md) | 5 | 2 | 3 | REJECT `class`, `hidden`, `tier` |
| [`gc2-repurpose`](../examples/gc2-repurpose/) | `check_gc2_s6` | [GC2-S6-REPURPOSE](GC2-S6-REPURPOSE.md) · [RFC-0057](../rfcs/RFC-0057-workshop-repurpose.md) | 4 | 1 | 3 | REJECT `conversion`, `hidden`, `owner` |
| [`gc2-abandon`](../examples/gc2-abandon/) | `check_gc2_s7` | [GC2-S7-ABANDON](GC2-S7-ABANDON.md) · [RFC-0058](../rfcs/RFC-0058-abandonment.md) | 5 | 2 | 3 | REJECT `hidden`, `idle`, `reset` |
| [`gc2-restore`](../examples/gc2-restore/) | `check_gc2_s8` | [GC2-S8-RESTORE](GC2-S8-RESTORE.md) · [RFC-0059](../rfcs/RFC-0059-restore.md) | 5 | 1 | 4 | REJECT `claimed`, `hidden`, `owner`, `scar` |
| [`gc2-multicycle`](../examples/gc2-multicycle/) | `check_gc2_s9` | [GC2-S9-MULTICYCLE](GC2-S9-MULTICYCLE.md) · [RFC-0061](../rfcs/RFC-0061-multicycle-construct.md) | 4 | 3 | 1 | REJECT `hidden` |
| [`gc2-institution`](../examples/gc2-institution/) | `check_gc2_s10` | [GC2-S10-INSTITUTION](GC2-S10-INSTITUTION.md) · [RFC-0067](../rfcs/RFC-0067-institution-own.md) | 4 | 1 | 3 | REJECT `hidden`, `not_owner`, `unauthorized` |
| [`gc2-shared`](../examples/gc2-shared/) | `check_gc2_s11` | [GC2-S11-SHARED](GC2-S11-SHARED.md) · [RFC-0068](../rfcs/RFC-0068-shared-own.md) | 4 | 1 | 3 | REJECT `already_shared`, `hidden`, `not_owner` |
| [`gc2-connect`](../examples/gc2-connect/) | `check_gc2_s12` | [GC2-S12-CONNECT](GC2-S12-CONNECT.md) · [RFC-0071](../rfcs/RFC-0071-connect-dest.md) | 4 | 1 | 3 | REJECT `not_observable`×2, `not_owner` |
| [`gc2-workshop-cycle`](../examples/gc2-workshop-cycle/) | `check_gc2_s13` | [GC2-S13-WORKSHOP-CYCLE](GC2-S13-WORKSHOP-CYCLE.md) · [RFC-0072](../rfcs/RFC-0072-workshop-cycle.md) | 6 | 3 | 3 | REJECT `hidden`, `in_progress`×2 |
| [`gc2-generator-cycle`](../examples/gc2-generator-cycle/) | `check_gc2_s14` | [GC2-S14-GENERATOR-CYCLE](GC2-S14-GENERATOR-CYCLE.md) · [RFC-0073](../rfcs/RFC-0073-generator-cycle.md) | 4 | 3 | 1 | REJECT `hidden` |
| [`gc2-storage-bay-cycle`](../examples/gc2-storage-bay-cycle/) | `check_gc2_s15` | [GC2-S15-STORAGE-BAY-CYCLE](GC2-S15-STORAGE-BAY-CYCLE.md) · [RFC-0074](../rfcs/RFC-0074-storage-bay-cycle.md) | 4 | 3 | 1 | REJECT `hidden` |
| [`gc2-production-node-cycle`](../examples/gc2-production-node-cycle/) | `check_gc2_s16` | [GC2-S16-PRODUCTION-NODE-CYCLE](GC2-S16-PRODUCTION-NODE-CYCLE.md) · [RFC-0075](../rfcs/RFC-0075-production-node-cycle.md) | 4 | 3 | 1 | REJECT `hidden` |
| [`gc2-defensive-work-cycle`](../examples/gc2-defensive-work-cycle/) | `check_gc2_s17` | [GC2-S17-DEFENSIVE-WORK-CYCLE](GC2-S17-DEFENSIVE-WORK-CYCLE.md) · [RFC-0076](../rfcs/RFC-0076-defensive-work-cycle.md) | 6 | 5 | 1 | REJECT `hidden` |
| [`gc2-archive-annex-cycle`](../examples/gc2-archive-annex-cycle/) | `check_gc2_s18` | [GC2-S18-ARCHIVE-ANNEX-CYCLE](GC2-S18-ARCHIVE-ANNEX-CYCLE.md) · [RFC-0077](../rfcs/RFC-0077-archive-annex-cycle.md) | 6 | 5 | 1 | REJECT `hidden` |
| [`gc2-route-link-cycle`](../examples/gc2-route-link-cycle/) | `check_gc2_s19` | [GC2-S19-ROUTE-LINK-CYCLE](GC2-S19-ROUTE-LINK-CYCLE.md) · [RFC-0078](../rfcs/RFC-0078-route-link-cycle.md) | 6 | 5 | 1 | REJECT `hidden` |
| [`gc2-second-co-owner`](../examples/gc2-second-co-owner/) | `check_gc2_s20` | [GC2-S20-SECOND-CO-OWNER](GC2-S20-SECOND-CO-OWNER.md) · [RFC-0079](../rfcs/RFC-0079-second-co-owner.md) | 4 | 1 | 3 | REJECT `already_shared`, `hidden`, `not_owner` |
| [`gc2-third-co-owner`](../examples/gc2-third-co-owner/) | `check_gc2_s21` | [GC2-S21-THIRD-CO-OWNER](GC2-S21-THIRD-CO-OWNER.md) · [RFC-0085](../rfcs/RFC-0085-third-co-owner.md) | 4 | 1 | 3 | REJECT `already_shared`, `hidden`, `not_owner` |
| [`gc2-fourth-co-owner`](../examples/gc2-fourth-co-owner/) | `check_gc2_s22` | [GC2-S22-FOURTH-CO-OWNER](GC2-S22-FOURTH-CO-OWNER.md) · [RFC-0086](../rfcs/RFC-0086-fourth-co-owner.md) | 4 | 1 | 3 | REJECT `already_shared`, `hidden`, `not_owner` |
| [`gc2-fifth-co-owner`](../examples/gc2-fifth-co-owner/) | `check_gc2_s23` | [GC2-S23-FIFTH-CO-OWNER](GC2-S23-FIFTH-CO-OWNER.md) · [RFC-0087](../rfcs/RFC-0087-fifth-co-owner.md) | 4 | 1 | 3 | REJECT `already_shared`, `hidden`, `not_owner` |
| [`gc2-share-closeout`](../examples/gc2-share-closeout/) | `check_gc2_s24` | [GC2-S24-SHARE-CLOSEOUT](GC2-S24-SHARE-CLOSEOUT.md) · [RFC-0089](../rfcs/RFC-0089-share-closeout.md) | 4 | 1 | 3 | REJECT `already_shared`, `hidden`, `not_owner` |
| [`gc2-thaw-play`](../examples/gc2-thaw-play/) | `check_gc2_thaw_play` | [GC2-THAW-PLAY](GC2-THAW-PLAY.md) · [RFC-0090](../rfcs/RFC-0090-build-play-thaw.md) | 4 | 4 | 0 | none in pack |

### GC3

| Pack | Check | Authority | Fixtures | + | − | Negative cases |
|---|---|---|---|---|---|---|
| [`gc3-social-memory`](../examples/gc3-social-memory/) | `check_gc3_s0` | [GC3-FIRST-SLICE](GC3-FIRST-SLICE.md) · [RFC-0007](../rfcs/RFC-0007-dyadic-trade-memory.md) | 2 | 1 | 1 | `rebuild-rejects-ignored` |
| [`gc3-betrayal`](../examples/gc3-betrayal/) | `check_gc3_s1` | [GC3-S1-BETRAYAL](GC3-S1-BETRAYAL.md) · [RFC-0022](../rfcs/RFC-0022-betrayal-dangerous.md) | 2 | 1 | 1 | `rebuild-rejects-ignored` |
| [`gc3-watch-public`](../examples/gc3-watch-public/) | `check_gc3_s2` | [GC3-S2-WATCH-PUBLIC](GC3-S2-WATCH-PUBLIC.md) · [RFC-0034](../rfcs/RFC-0034-watch-public-descriptors.md) | 2 | 1 | 1 | `rebuild-private-trades-silent` |
| [`gc3-institution-edges`](../examples/gc3-institution-edges/) | `check_gc3_s3` | [GC3-S3-INSTITUTION-EDGES](GC3-S3-INSTITUTION-EDGES.md) · [RFC-0035](../rfcs/RFC-0035-institution-edges.md) | 2 | 1 | 1 | `rebuild-other-empty` |
| [`gc3-decay-rehab`](../examples/gc3-decay-rehab/) | `check_gc3_s4` | [GC3-S4-DECAY-REHAB](GC3-S4-DECAY-REHAB.md) · [RFC-0036](../rfcs/RFC-0036-decay-rehab.md) | 2 | 2 | 0 | none in pack |
| [`gc3-trade-friction`](../examples/gc3-trade-friction/) | `check_gc3_s5` | [GC3-S5-TRADE-FRICTION](GC3-S5-TRADE-FRICTION.md) · [RFC-0037](../rfcs/RFC-0037-trade-friction.md) | 2 | 1 | 1 | `attempt-no-edge` |
| [`gc3-deceptive`](../examples/gc3-deceptive/) | `check_gc3_s6` | [GC3-S6-DECEPTIVE](GC3-S6-DECEPTIVE.md) · [RFC-0038](../rfcs/RFC-0038-deceptive-edge.md) | 3 | 2 | 1 | `rebuild-reject-ignored` |
| [`gc3-preferred`](../examples/gc3-preferred/) | `check_gc3_s7` | [GC3-S7-PREFERRED](GC3-S7-PREFERRED.md) · [RFC-0039](../rfcs/RFC-0039-preferred-counterparty.md) | 3 | 1 | 2 | `attempt-caution-only`, `attempt-none` |

### GC4

| Pack | Check | Authority | Fixtures | + | − | Negative cases |
|---|---|---|---|---|---|---|
| [`gc4-authority`](../examples/gc4-authority/) | `check_gc4_s0` | [GC4-FIRST-SLICE](GC4-FIRST-SLICE.md) · [RFC-0008](../rfcs/RFC-0008-office-authority-pins.md) | 7 | 2 | 5 | REJECT `FORBIDDEN`×5 |
| [`gc4-offices`](../examples/gc4-offices/) | `check_gc4_s1` | [GC4-S1-OFFICES](GC4-S1-OFFICES.md) · [RFC-0023](../rfcs/RFC-0023-named-offices.md) | 13 | 5 | 8 | REJECT `FORBIDDEN`×7, `NOT_FOUND` |
| [`gc4-institution-actions`](../examples/gc4-institution-actions/) | `check_gc4_s2` | [GC4-S2-INSTITUTION-ACTIONS](GC4-S2-INSTITUTION-ACTIONS.md) · [RFC-0029](../rfcs/RFC-0029-institution-trade-repair.md) | 14 | 4 | 10 | REJECT `BUDGET_EXCEEDED`, `FORBIDDEN`×7, `NOT_FOUND`×2 |
| [`gc4-emergency`](../examples/gc4-emergency/) | `check_gc4_s3` | [GC4-S3-EMERGENCY-SCOPES](GC4-S3-EMERGENCY-SCOPES.md) · [RFC-0030](../rfcs/RFC-0030-emergency-scopes.md) | 14 | 5 | 9 | REJECT `FORBIDDEN`×8, `NOT_FOUND` |
| [`gc4-succession`](../examples/gc4-succession/) | `check_gc4_s4` | [GC4-S4-SUCCESSION](GC4-S4-SUCCESSION.md) · [RFC-0031](../rfcs/RFC-0031-designated-succession.md) | 15 | 8 | 7 | REJECT `FORBIDDEN`×6, `NOT_FOUND` |
| [`gc4-consensus`](../examples/gc4-consensus/) | `check_gc4_s5` | [GC4-S5-CONSENSUS](GC4-S5-CONSENSUS.md) · [RFC-0060](../rfcs/RFC-0060-consensus-succession.md) | 4 | 2 | 2 | REJECT `member`, `occupied` |
| [`gc4-rule`](../examples/gc4-rule/) | `check_gc4_s6` | [GC4-S6-RULE](GC4-S6-RULE.md) · [RFC-0069](../rfcs/RFC-0069-rule-based-succession.md) | 4 | 3 | 1 | REJECT `unknown` |
| [`gc4-inherited`](../examples/gc4-inherited/) | `check_gc4_s7` | [GC4-S7-INHERITED](GC4-S7-INHERITED.md) · [RFC-0070](../rfcs/RFC-0070-inherited-org.md) | 3 | 2 | 1 | REJECT `unknown` |
| [`gc4-governance`](../examples/gc4-governance/) | `check_gc4_s8` | [GC4-S8-GOVERNANCE-RULE](GC4-S8-GOVERNANCE-RULE.md) · [RFC-0124](../rfcs/RFC-0124-governance-rule-contract.md) | 10 | 1 | 9 | REJECT `authority_conflict`, `not_deciding_office`, `out_of_jurisdiction`×2, `quorum_short`, `undefined_failure`, `unknown_enforcement`, `unpublished`, `vacancy_refused` |

### GC5

| Pack | Check | Authority | Fixtures | + | − | Negative cases |
|---|---|---|---|---|---|---|
| [`gc5-communication`](../examples/gc5-communication/) | `check_gc5_s0` | [GC5-FIRST-SLICE](GC5-FIRST-SLICE.md) · [RFC-0009](../rfcs/RFC-0009-relay-message-delivery.md) | 5 | 2 | 3 | REJECT `UNREACHABLE`×3 |
| [`gc5-delay`](../examples/gc5-delay/) | `check_gc5_s1` | [GC5-S1-DELAY](GC5-S1-DELAY.md) · [RFC-0021](../rfcs/RFC-0021-relay-message-delay.md) | 4 | 2 | 2 | REJECT `UNREACHABLE`, `VERB_FORBIDDEN` |
| [`gc5-rumor`](../examples/gc5-rumor/) | `check_gc5_s2` | [GC5-S2-RUMOR](GC5-S2-RUMOR.md) · [RFC-0028](../rfcs/RFC-0028-rumor-provenance.md) | 22 | 11 | 11 | REJECT `COPIES_NOT_INDEPENDENT`, `CROSS_WORLD`, `DUPLICATE`, `FORGE_FORBIDDEN`, `LABEL_LEAK`, `NOT_FOUND`, `ORIGIN_FORBIDDEN`×2, `TRUTH_MUTATION`, `UNREACHABLE`, `VERB_FORBIDDEN` |
| [`gc5-board`](../examples/gc5-board/) | `check_gc5_s3` | [GC5-S3-BOARD](GC5-S3-BOARD.md) · [RFC-0054](../rfcs/RFC-0054-message-board.md) | 3 | 2 | 1 | REJECT `hidden` |
| [`gc5-shout`](../examples/gc5-shout/) | `check_gc5_s4` | [GC5-S4-SHOUT](GC5-S4-SHOUT.md) · [RFC-0062](../rfcs/RFC-0062-message-shout.md) | 3 | 2 | 1 | REJECT `hidden` |
| [`gc5-retention`](../examples/gc5-retention/) | `check_gc5_s5` | [GC5-S5-RETENTION](GC5-S5-RETENTION.md) · [RFC-0063](../rfcs/RFC-0063-board-retention.md) | 3 | 2 | 1 | REJECT `hidden` |
| [`gc5-notice`](../examples/gc5-notice/) | `check_gc5_s6` | [GC5-S6-NOTICE](GC5-S6-NOTICE.md) · [RFC-0064](../rfcs/RFC-0064-institution-notice.md) | 4 | 2 | 2 | REJECT `hidden`, `unauthorized` |
| [`gc5-channel`](../examples/gc5-channel/) | `check_gc5_s7` | [GC5-S7-CHANNEL](GC5-S7-CHANNEL.md) · [RFC-0065](../rfcs/RFC-0065-org-channel.md) | 5 | 2 | 3 | REJECT `hidden`, `not_addressable`×2 |
| [`gc5-trade-notice`](../examples/gc5-trade-notice/) | `check_gc5_s8` | [GC5-S8-TRADE-NOTICE](GC5-S8-TRADE-NOTICE.md) · [RFC-0066](../rfcs/RFC-0066-trade-notice.md) | 3 | 2 | 1 | REJECT `hidden` |
| [`gc5-shout-expiry`](../examples/gc5-shout-expiry/) | `check_gc5_s9` | [GC5-S9-SHOUT-EXPIRY](GC5-S9-SHOUT-EXPIRY.md) · [RFC-0080](../rfcs/RFC-0080-shout-expiry.md) | 4 | 3 | 1 | REJECT `hidden` |
| [`gc5-board-expiry`](../examples/gc5-board-expiry/) | `check_gc5_s10` | [GC5-S10-BOARD-EXPIRY](GC5-S10-BOARD-EXPIRY.md) · [RFC-0081](../rfcs/RFC-0081-board-expiry.md) | 4 | 3 | 1 | REJECT `hidden` |
| [`gc5-notice-expiry`](../examples/gc5-notice-expiry/) | `check_gc5_s11` | [GC5-S11-NOTICE-EXPIRY](GC5-S11-NOTICE-EXPIRY.md) · [RFC-0082](../rfcs/RFC-0082-notice-expiry.md) | 4 | 3 | 1 | REJECT `hidden` |
| [`gc5-channel-expiry`](../examples/gc5-channel-expiry/) | `check_gc5_s12` | [GC5-S12-CHANNEL-EXPIRY](GC5-S12-CHANNEL-EXPIRY.md) · [RFC-0083](../rfcs/RFC-0083-channel-expiry.md) | 4 | 3 | 1 | REJECT `hidden` |
| [`gc5-trade-notice-expiry`](../examples/gc5-trade-notice-expiry/) | `check_gc5_s13` | [GC5-S13-TRADE-NOTICE-EXPIRY](GC5-S13-TRADE-NOTICE-EXPIRY.md) · [RFC-0084](../rfcs/RFC-0084-trade-notice-expiry.md) | 4 | 3 | 1 | REJECT `hidden` |

### GC6

| Pack | Check | Authority | Fixtures | + | − | Negative cases |
|---|---|---|---|---|---|---|
| [`gc6-discovery`](../examples/gc6-discovery/) | `check_gc6_s0` | [GC6-FIRST-SLICE](GC6-FIRST-SLICE.md) · [RFC-0010](../rfcs/RFC-0010-discovery-contradiction.md) · [RFC-0015](../rfcs/RFC-0015-archive-record-source.md) | 4 | 1 | 3 | `rebuild-agreeing`, `rebuild-archive-only`, `rebuild-inspect-only` |
| [`gc6-reconstruction`](../examples/gc6-reconstruction/) | `check_gc6_s1` | [GC6-S1-RECONSTRUCTION](GC6-S1-RECONSTRUCTION.md) · [RFC-0024](../rfcs/RFC-0024-historical-reconstruction.md) | 15 | 7 | 8 | REJECT `FORBIDDEN`×8 |

### GC7

| Pack | Check | Authority | Fixtures | + | − | Negative cases |
|---|---|---|---|---|---|---|
| [`gc7-conflict`](../examples/gc7-conflict/) | `check_gc7_s0` | [GC7-FIRST-SLICE](GC7-FIRST-SLICE.md) · [RFC-0011](../rfcs/RFC-0011-contest-rhythm.md) | 5 | 1 | 4 | REJECT `DEATH_FORBIDDEN`, `FORM_FORBIDDEN`, `LEAK`, `VERB_FORBIDDEN` |
| [`gc7-withdraw`](../examples/gc7-withdraw/) | `check_gc7_s1` | [GC7-S1-WITHDRAW](GC7-S1-WITHDRAW.md) · [RFC-0026](../rfcs/RFC-0026-contest-withdraw.md) | 11 | 4 | 7 | REJECT `FORBIDDEN`×3, `NOT_FOUND`×3, `STALE_HEAD` |
| [`gc7-institution-party`](../examples/gc7-institution-party/) | `check_gc7_s2` | [GC7-S2-INSTITUTION-PARTY](GC7-S2-INSTITUTION-PARTY.md) · [RFC-0041](../rfcs/RFC-0041-institution-contest-party.md) | 4 | 1 | 3 | REJECT `FORBIDDEN`×3 |
| [`gc7-information-contest`](../examples/gc7-information-contest/) | `check_gc7_s3` | [GC7-S3-INFORMATION-CONTEST](GC7-S3-INFORMATION-CONTEST.md) · [RFC-0042](../rfcs/RFC-0042-information-contest.md) | 5 | 1 | 4 | REJECT `FORBIDDEN`, `FORM_FORBIDDEN`, `LEAK`, `NOT_FOUND` |
| [`gc7-thaw-play`](../examples/gc7-thaw-play/) | `check_gc7_thaw_play` | [GC7-THAW-PLAY](GC7-THAW-PLAY.md) · [RFC-0095](../rfcs/RFC-0095-contest-play-thaw.md) | 4 | 4 | 0 | none in pack |

### GC8

| Pack | Check | Authority | Fixtures | + | − | Negative cases |
|---|---|---|---|---|---|---|
| [`gc8-economy`](../examples/gc8-economy/) | `check_gc8_s0` | [GC8-FIRST-SLICE](GC8-FIRST-SLICE.md) · [RFC-0012](../rfcs/RFC-0012-distance-interdependence.md) | 6 | 2 | 4 | REJECT `BONUS_FORBIDDEN`, `FEATURE_FORBIDDEN`×3 |
| [`gc8-lot-quality`](../examples/gc8-lot-quality/) | `check_gc8_s1` | [GC8-S1-LOT-QUALITY](GC8-S1-LOT-QUALITY.md) · [RFC-0045](../rfcs/RFC-0045-lot-quality.md) | 5 | 3 | 0 | none in pack; controls `attempt-sound-harvest`, `attempt-sound-construct` |
| [`gc8-provenance`](../examples/gc8-provenance/) | `check_gc8_s2` | [GC8-S2-PROVENANCE](GC8-S2-PROVENANCE.md) · [RFC-0046](../rfcs/RFC-0046-lot-provenance.md) | 4 | 2 | 2 | `attempt-hidden-clear`, `attempt-mix-clear` |
| [`gc8-spoilage`](../examples/gc8-spoilage/) | `check_gc8_s3` | [GC8-S3-SPOILAGE](GC8-S3-SPOILAGE.md) · [RFC-0047](../rfcs/RFC-0047-lot-spoilage.md) | 3 | 2 | 1 | `attempt-sound-keep` |
| [`gc8-transport`](../examples/gc8-transport/) | `check_gc8_s4` | [GC8-S4-TRANSPORT](GC8-S4-TRANSPORT.md) · [RFC-0048](../rfcs/RFC-0048-cargo-move.md) | 3 | 1 | 1 | `attempt-cargo-empty-hold`; controls `attempt-empty-move` |

### GC9

| Pack | Check | Authority | Fixtures | + | − | Negative cases |
|---|---|---|---|---|---|---|
| [`gc9-culture`](../examples/gc9-culture/) | `check_gc9_s0` | [GC9-FIRST-SLICE](GC9-FIRST-SLICE.md) · [RFC-0013](../rfcs/RFC-0013-maintenance-custom.md) | 4 | 1 | 3 | `rebuild-below-threshold`, `rebuild-lore-cannot-override`, `rebuild-no-access` |
| [`gc9-tradition`](../examples/gc9-tradition/) | `check_gc9_s1`, `check_gc9_s2` | [GC9-S1-TRADITION](GC9-S1-TRADITION.md) · [RFC-0025](../rfcs/RFC-0025-tradition.md) · [RFC-0125](../rfcs/RFC-0125-practice-inheritance-and-schism.md) | 9 | 5 | 4 | `custom-not-tradition`, `private-recon-no-watch`, `single-action-forbidden`, `competing-accounts` |
| [`gc9-schism`](../examples/gc9-schism/) | `check_gc9_s2` | [RFC-0125](../rfcs/RFC-0125-practice-inheritance-and-schism.md) | 10 | 2 | 8 | `founders-only-no-inheritance`, `concurrent-practice-not-inheritance`, `single-account-no-schism`, `unattributed-accounts-no-schism`, `same-author-revision-no-schism`, `private-accounts-no-schism`, `not-a-tradition-no-marks`, `dormant-no-marks` |

### GC10

| Pack | Check | Authority | Fixtures | + | − | Negative cases |
|---|---|---|---|---|---|---|
| [`gc10-pressure`](../examples/gc10-pressure/) | `check_gc10_s0` | [GC10-FIRST-SLICE](GC10-FIRST-SLICE.md) · [RFC-0014](../rfcs/RFC-0014-wed-schedule-pressure.md) | 6 | 1 | 5 | REJECT `AUTHOR_FORBIDDEN`, `FORCED_OUTCOME`, `FRONTIER_ID_FORBIDDEN`, `LABEL_LEAK`, `PREVIEW_MISMATCH` |
| [`gc10-s1-pressure`](../examples/gc10-s1-pressure/) | `check_gc10_s1` | [GC10-S1-PRESSURE](GC10-S1-PRESSURE.md) · [RFC-0027](../rfcs/RFC-0027-additional-world-pressure.md) | 21 | 4 | 17 | REJECT `AUTHOR_FORBIDDEN`, `BELOW_FLOOR`×2, `CLASS_UNSUPPORTED`×3, `CONTROLLER_TARGET`, `CROSS_WORLD`, `DUPLICATE`, `LABEL_LEAK`×2, `MAGNITUDE_INVALID`, `PLAYER_TARGET`, `PREVIEW_MISMATCH`, `RESEARCH_TARGET`, `RUBBER_BAND`, `VERDICT_FORBIDDEN` |
| [`gc10-scar`](../examples/gc10-scar/) | `check_gc10_s2` | [GC10-S2-SCAR](GC10-S2-SCAR.md) · [RFC-0051](../rfcs/RFC-0051-irreversible-scar.md) | 4 | 3 | 1 | REJECT `irreversible` |

## The seed's starting points

The [seed](SPEC-COMPLETION-FIXTURES-SEED.md) named starting fixtures for GC1–GC3 and left GC4–GC10 for later slices. Against current sources:

| Seed entry | Executed fixtures now | Design seeds without fixtures |
|---|---|---|
| GC1: RFC-0004/0005 plus S9–S11 seeds | `gc1-mastery` (RFC-0004, RFC-0005), also run as the conformance packs [`conformance/gc1-s0`](../conformance/gc1-s0/) (4 cases) and [`conformance/gc1-s1`](../conformance/gc1-s1/) (2 cases). S2–S8 packs above. | [GC1-S9](GC1-S9-MULTI-FOCUS.md), [GC1-S10](GC1-S10-DECAY-CREDIT.md), [GC1-S11](GC1-S11-FURTHER-PARAMETERS.md), [failed attempts](GC1-FAILED-ATTEMPTS-SEED.md), [multi-focus magnitudes](GC1-MULTI-FOCUS-MAGNITUDES-SEED.md) |
| GC2: RFC-0006 plus B2 seeds | `gc2-construction` (RFC-0006) and the S1–S24 and thaw-play packs above | [construction quantities](GC2-CONSTRUCTION-QUANTITIES-SEED.md), [owner/steward](GC2-OWNER-STEWARD-SEED.md) |
| GC3: RFC-0007 plus S1–S7 | `gc3-social-memory` (RFC-0007) and one pack for each of S1–S7 | none named |
| GC4–GC10: seeds give starting cases such as COI, pressure and custom inheritance | GC4 S0–S8, GC5 S0–S13, GC6 S0–S1, GC7 S0–S3 and thaw play, GC8 S0–S4, GC9 S0–S2, GC10 S0–S2. Pressure is `gc10-pressure`, `gc10-s1-pressure` and `gc10-scar`. Custom inheritance is `gc9-culture` and `gc9-schism`. | COI ([GC4 broader COI](GC4-BROADER-COI-SEED.md)) has no fixture. Neither do [GC4 crime expulsion](GC4-CRIME-EXPULSION-SEED.md), the GC7 crime seeds B7a–B7d ([payload/victim](GC7-CRIME-PAYLOAD-VICTIM-SEED.md), [evidence algorithm](GC7-CRIME-EVIDENCE-ALGORITHM-SEED.md), [detection/sanction](GC7-CRIME-DETECTION-SANCTION-SEED.md), [enforcement](GC7-CRIME-ENFORCEMENT-SEED.md)), [GC8 lot grade](GC8-LOT-GRADE-SEED.md), [GC9 threshold](GC9-THRESHOLD-SEED.md), [GC10 WED class](GC10-WED-CLASS-SEED.md) or the coupling seeds. |

A design seed is not a fixture. The two GC7 crime seeds that cite JSON cite contract files (`specs/event-types.0.2.json`, `specs/contest-config.v02.json`), not fixtures.

## Gaps and observations

Recorded, not filled. No fixture, expected result or threshold is added here.

- **Packs with no negative of their own:** `gc2-thaw-play` and `gc7-thaw-play` (all `ACCEPT`), `gc3-decay-rehab` (both fixtures derive the omission the slice adds) and `gc8-lot-quality` (three positives, two controls). Each GC has negatives in other packs, so the per-GC disposition holds; the slice-level gap stays open.
- **Packs without a README:** `gc1-s8` and `gc4-governance`. Their checks run every fixture; the authority above comes from the slice document and the RFC the check requires.
- **Refusal families:** the seed's Extension Points name legal evidence, duplicate evidence, authorization failure and visibility refusal. This inventory lists reason codes as recorded and does not map them onto those families. That mapping belongs with each owning RFC.
- **Classes 3 and 4:** no runtime, hosted or gate evidence is claimed for any GC.

## Reproduce

From the repository root at the source commit:

```bash
validation/run.sh
find examples -path 'examples/gc*' -name '*.json' | wc -l
grep -rhoE '"outcome": *"(ACCEPT|REJECT)"' examples/gc* | sort | uniq -c
```

The first prints the validator's OK lines and exits 0. The second counts 458 fixtures. The third counts the outcome-carrying fixtures; derivation packs are classified by hand from each fixture's `expected.note`, as listed in the tables above.

## Extension Points

Non-normative prospective guidance; existing outcomes and contract authority are unchanged.

### Keeping the inventory current

When a GC pack is added, or a fixture's expected result changes under a versioned fixture identity, add or update its row and re-run the counts. Keep design seeds out of the fixture columns until a pack and an executing check exist. Do not record runtime, hosted or gate evidence here; link it from the owning slice instead.
