# RFCs

RFCs are required for changes to protocols, schemas, ontology semantics, reproducibility boundary, claims policy, security boundary, version domains, or dataset immutability rules.

## Lifecycle

Draft → Review → Accepted or Rejected → Implemented or Superseded.

## Index

Every RFC in this directory, in number order. The heading previously read "Active
drafts", which was never accurate — one entry is a draft and the rest are Accepted.
`RFC-0000` is the template and is deliberately absent.

| RFC | Status | Topic |
|-----|--------|-------|
| [RFC-0001](RFC-0001-phenomena-self-reference-integration.md) | **Draft — v0.8-blocked** | Phenomena self-reference integration. The file carries no Status section; [SPEC-FREEZE-CORE-LOOP.md](../docs/SPEC-FREEZE-CORE-LOOP.md) records v0.8 Phenomena as not required for the core loop, and §7 puts it out of scope for first implementation |
| [RFC-0002](RFC-0002-strategic-contestation-and-crime-events.md) | **Accepted** | Contestation, crime, agreement events → `event-catalog/0.2` |
| [RFC-0003](RFC-0003-deterministic-contract-hardening.md) | **Accepted / Implemented** | Ordering, canonicalization, catalog admission, persistence, recovery, evidence integrity |
| [RFC-0004](RFC-0004-derived-mastery-projection.md) | **Accepted** | GC1-S0 derived practice projection; no catalog expansion |
| [RFC-0005](RFC-0005-mastery-recognition.md) | **Accepted** | GC1-S1 self-only recognition; no benefits |
| [RFC-0006](RFC-0006-construction-existing-events.md) | **Accepted** | GC2-S0 construct/dismantle via existing ENTITY_* events |
| [RFC-0007](RFC-0007-dyadic-trade-memory.md) | **Accepted** | GC3-S0 dyadic trade memory; no reputation scalar |
| [RFC-0008](RFC-0008-office-authority-pins.md) | **Accepted** | GC4-S0 existing roles as bounded authority; no ROLE_* events |
| [RFC-0009](RFC-0009-relay-message-delivery.md) | **Accepted** | GC5-S0 relay bands on existing MESSAGE; no new verbs |
| [RFC-0010](RFC-0010-discovery-contradiction.md) | **Accepted** | GC6-S0 archive vs live INSPECT; no quest oracle |
| [RFC-0011](RFC-0011-contest-rhythm.md) | **Accepted** | GC7-S0 existing contest rhythm; no event-catalog/0.3 |
| [RFC-0012](RFC-0012-distance-interdependence.md) | **Accepted** | GC8-S0 distance interdependence; not v0.6B |
| [RFC-0013](RFC-0013-maintenance-custom.md) | **Accepted** | GC9-S0 maintenance custom; lore cannot override ledger |
| [RFC-0014](RFC-0014-wed-schedule-pressure.md) | **Accepted** | GC10-S0 seeded mild relay pressure; no Frontier ID share |
| [RFC-0015](RFC-0015-archive-record-source.md) | **Accepted** | GC6-S0 archive-record source: explicit ARTIFACT claim fields; no Genesis pack |
| [RFC-0016](RFC-0016-hosted-durable-world-head.md) | **Accepted** | Hosted durable world head in Postgres; restore if DO world missing; no Genesis reseed |
| [RFC-0017](RFC-0017-hosted-cycle-fence.md) | **Accepted** | Hosted cycle fence, STALE_HEAD, settlement crash/retry; no gameplay |
| [RFC-0018](RFC-0018-archive-claim-writer.md) | **Accepted** | Archive-claim fields: ENTITY_CREATE/UPDATE only; INSPECT not a writer |
| [RFC-0019](RFC-0019-hosted-world-time.md) | **Accepted** | Hosted world-time: WAIT quorum cycle commit; no contest/WED |
| [RFC-0020](RFC-0020-archive-claim-attest.md) | **Accepted** | `COMMIT.ATTEST` writes archive-claim fields; INSPECT not a writer; help omits ATTEST |
| [RFC-0021](RFC-0021-relay-message-delay.md) | **Accepted** | GC5-S1: long-range MESSAGE delays 1 cycle when best relay is 25–49 |
| [RFC-0022](RFC-0022-betrayal-dangerous.md) | **Accepted** | GC3-S1: danger from CONTEST_RESOLVED / breach; no reputation scalar |
| [RFC-0023](RFC-0023-named-offices.md) | **Accepted** | GC4-S1: named offices as persistent seats; no ROLE_* |
| [RFC-0024](RFC-0024-historical-reconstruction.md) | **Accepted** | GC6-S1: Player reconstruction from accessible evidence; not truth |
| [RFC-0025](RFC-0025-tradition.md) | **Accepted** | GC9-S1: tradition from persistent custom; no culture score |
| [RFC-0026](RFC-0026-contest-withdraw.md) | **Accepted** | GC7-S1: withdraw via CONTEST_RESOLVED; no HP |
| [RFC-0027](RFC-0027-additional-world-pressure.md) | **Accepted** | GC10-S1: additional pressure classes via existing events; no Admin spawn |
| [RFC-0028](RFC-0028-rumor-provenance.md) | **Accepted** | GC5-S2: rumor as claim + MESSAGE lineage; no score |
| [RFC-0029](RFC-0029-institution-trade-repair.md) | **Accepted** | Institution TRADE/REPAIR via occupied office profiles; no new verbs |
| [RFC-0030](RFC-0030-emergency-scopes.md) | **Accepted** | Time-bounded emergency AuthorityGrant overlay; no superuser |
| [RFC-0031](RFC-0031-designated-succession.md) | **Accepted** | Designated institutional succession; no implicit jump |
| [RFC-0032](RFC-0032-postmark-admin-email-delivery.md) | **Accepted** | Postmark replaces Resend for Worker-composed PLAY and ADMIN magic links |
| [RFC-0033](RFC-0033-agent-bootstrap-and-game-profile.md) | **Accepted** | Email-assisted bootstrap and optional game-only Controller skill/profile |
| [RFC-0034](RFC-0034-watch-public-descriptors.md) | **Accepted** | GC3-S2: WATCH public descriptor bands from public events; else silent |
| [RFC-0035](RFC-0035-institution-edges.md) | **Accepted** | GC3-S3: institution→player edges from authorized org records; no ROLE_* |
| [RFC-0036](RFC-0036-decay-rehab.md) | **Accepted** | GC3-S4: decay/rehab weights; no wipe; ledger never forgets |
| [RFC-0037](RFC-0037-trade-friction.md) | **Accepted** | GC3-S5: published +1 compute TRADE_CAUTION; no auto-refuse |
| [RFC-0038](RFC-0038-deceptive-edge.md) | **Accepted** | GC3-S6: deceptive as distinct edge; TRADE_REJECTED ignored |
| [RFC-0039](RFC-0039-preferred-counterparty.md) | **Accepted** | GC3-S7: waive TRADE_CAUTION for live RELIABLE; no auto-accept |
| [RFC-0040](RFC-0040-engineer-quality.md) | **Accepted** | GC1-S2: same-asset Engineer REPAIR +5 (total +20, cap 100) |
| [RFC-0041](RFC-0041-institution-contest-party.md) | **Accepted** | GC7-S2: institution contest party via occupied office; treasury pays |
| [RFC-0042](RFC-0042-information-contest.md) | **Accepted** | GC7-S3: INFORMATION_CONTEST on visible public ARTIFACT; INSPECT seal |
| [RFC-0043](RFC-0043-mastery-decay.md) | **Accepted** | GC1-S3: recognized tracks LATENT after 12 idle cycles; 3 works restore |
| [RFC-0044](RFC-0044-prior-work-benefits.md) | **Accepted** | GC1-S4: prior-work LOOK/INSPECT/TRADE_CAUTION waivers |
| [RFC-0045](RFC-0045-lot-quality.md) | **Accepted** | GC8-S1: SOUND/WORN lots; WORN construct storage +1 |
| [RFC-0046](RFC-0046-lot-provenance.md) | **Accepted** | GC8-S2: public origin stamp; hidden/mix clear |
| [RFC-0047](RFC-0047-lot-spoilage.md) | **Accepted** | GC8-S3: WORN lots spoil 1 per cycle; SOUND keeps |
| [RFC-0048](RFC-0048-cargo-move.md) | **Accepted** | GC8-S4: carrying MOVE +1; empty stays 1 |
| [RFC-0049](RFC-0049-route-link.md) | **Accepted** | GC2-S1: route_link waives cargo MOVE extra |
| [RFC-0050](RFC-0050-workshop.md) | **Accepted** | GC2-S2: workshop saves 1 construct/repair storage |
| [RFC-0051](RFC-0051-irreversible-scar.md) | **Accepted** | GC10-S2: public DISMANTLE leaves irreparable scar |
| [RFC-0052](RFC-0052-defensive-work.md) | **Accepted** | GC2-S3: defensive_work +50 contest defense |
| [RFC-0053](RFC-0053-archive-annex.md) | **Accepted** | GC2-S4: archive_annex saves 1 inspect/attest attention |
| [RFC-0054](RFC-0054-message-board.md) | **Accepted** | GC5-S3: MESSAGE board surface; last 3; WATCH silent |
| [RFC-0055](RFC-0055-office-eligibility.md) | **Accepted** | GC1-S5: office requires recognized Engineer/Broker |
| [RFC-0056](RFC-0056-workshop-upgrade.md) | **Accepted** | GC2-S5: workshop UPGRADE storage save 2; once |
| [RFC-0057](RFC-0057-workshop-repurpose.md) | **Accepted** | GC2-S6: workshop → storage_bay REPURPOSE; same entity_id |
| [RFC-0058](RFC-0058-abandonment.md) | **Accepted** | GC2-S7: 12 idle cycles → UNCLAIMED; anyone may DISMANTLE |
| [RFC-0059](RFC-0059-restore.md) | **Accepted** | GC2-S8: owner RESTORE of UNCLAIMED; scars stay dead |
| [RFC-0060](RFC-0060-consensus-succession.md) | **Accepted** | GC4-S5: CONSENSUS vacant-office consent; ceil half |
| [RFC-0061](RFC-0061-multicycle-construct.md) | **Accepted** | GC2-S9: relay CONSTRUCT IN_PROGRESS; live after 1 cycle |
| [RFC-0062](RFC-0062-message-shout.md) | **Accepted** | GC5-S4: MESSAGE shout surface; last 1; WATCH silent |
| [RFC-0063](RFC-0063-board-retention.md) | **Accepted** | GC5-S5: MESSAGE board last 5; WATCH silent |
| [RFC-0064](RFC-0064-institution-notice.md) | **Accepted** | GC5-S6: MESSAGE institution notice; last 1; WATCH silent |
| [RFC-0065](RFC-0065-org-channel.md) | **Accepted** | GC5-S7: MESSAGE org channel; members only; WATCH silent |
| [RFC-0066](RFC-0066-trade-notice.md) | **Accepted** | GC5-S8: MESSAGE trade notice; last 1; WATCH silent |
| [RFC-0067](RFC-0067-institution-own.md) | **Accepted** | GC2-S10: BUILD.VEST to occupied named-asset office |
| [RFC-0068](RFC-0068-shared-own.md) | **Accepted** | GC2-S11: BUILD.SHARE one co-owner; same entity_id |
| [RFC-0069](RFC-0069-rule-based-succession.md) | **Accepted** | GC4-S6: RULE_BASED MEMBER_ORDER; no rule language |
| [RFC-0070](RFC-0070-inherited-org.md) | **Accepted** | GC4-S7: INHERITED_BY_ORGANIZATION; vacate stays vacant |
| [RFC-0071](RFC-0071-connect-dest.md) | **Accepted** | GC2-S12: BUILD.CONNECT dest pin; no new exit |
| [RFC-0072](RFC-0072-workshop-cycle.md) | **Accepted** | GC2-S13 multi-cycle workshop CONSTRUCT |
| [RFC-0073](RFC-0073-generator-cycle.md) | **Accepted** | GC2-S14 multi-cycle generator CONSTRUCT |
| [RFC-0074](RFC-0074-storage-bay-cycle.md) | **Accepted** | GC2-S15 multi-cycle storage_bay CONSTRUCT |
| [RFC-0075](RFC-0075-production-node-cycle.md) | **Accepted** | GC2-S16 multi-cycle production_node CONSTRUCT |
| [RFC-0076](RFC-0076-defensive-work-cycle.md) | **Accepted** | GC2-S17 multi-cycle defensive_work CONSTRUCT |
| [RFC-0077](RFC-0077-archive-annex-cycle.md) | **Accepted** | GC2-S18 multi-cycle archive_annex CONSTRUCT |
| [RFC-0078](RFC-0078-route-link-cycle.md) | **Accepted** | GC2-S19 multi-cycle route_link CONSTRUCT |
| [RFC-0079](RFC-0079-second-co-owner.md) | **Accepted** | GC2-S20 second co-owner |
| [RFC-0080](RFC-0080-shout-expiry.md) | **Accepted** | GC5-S9 shout cycle expiry |
| [RFC-0081](RFC-0081-board-expiry.md) | **Accepted** | GC5-S10 board cycle expiry |
| [RFC-0082](RFC-0082-notice-expiry.md) | **Accepted** | GC5-S11 notice cycle expiry |
| [RFC-0083](RFC-0083-channel-expiry.md) | **Accepted** | GC5-S12 channel cycle expiry |
| [RFC-0084](RFC-0084-trade-notice-expiry.md) | **Accepted** | GC5-S13 trade-notice cycle expiry |
| [RFC-0085](RFC-0085-third-co-owner.md) | **Accepted** | GC2-S21 third co-owner |
| [RFC-0086](RFC-0086-fourth-co-owner.md) | **Accepted** | GC2-S22 fourth co-owner |
| [RFC-0087](RFC-0087-fifth-co-owner.md) | **Accepted** | GC2-S23 fifth co-owner |
| [RFC-0088](RFC-0088-world-report.md) | **Accepted** | WR-S0 public world report |
| [RFC-0089](RFC-0089-share-closeout.md) | **Accepted** | GC2-S24 SHARE family closeout |
| [RFC-0090](RFC-0090-build-play-thaw.md) | **Accepted** | GC2 first-world BUILD help |
| [RFC-0091](RFC-0091-org-report.md) | **Accepted** | WR-S1 organization report lines |
| [RFC-0092](RFC-0092-contest-report.md) | **Accepted** | WR-S2 public contest report lines |
| [RFC-0093](RFC-0093-access-report.md) | **Accepted** | WR-S3 public access report lines |
| [RFC-0094](RFC-0094-crime-report.md) | **Accepted** | WR-S4 public crime report lines |
| [RFC-0095](RFC-0095-contest-play-thaw.md) | **Accepted** | GC7 first-world CONTEST help |
| [RFC-0096](RFC-0096-discovery-report.md) | **Accepted** | WR-S5 public discovery report lines |
| [RFC-0097](RFC-0097-diplomacy-trade.md) | **Accepted** | Diplomacy S0 TRADE agreement form |
| [RFC-0098](RFC-0098-diplomacy-terminate.md) | **Accepted** | Diplomacy S1 AGREEMENT_TERMINATE |
| [RFC-0099](RFC-0099-diplomacy-report.md) | **Accepted** | WR-S6 public diplomacy report lines |
| [RFC-0100](RFC-0100-diplomacy-closeout.md) | **Accepted** | Diplomacy S2 remaining types, effects, and help |
| [RFC-0101](RFC-0101-access-policy.md) | **Accepted** | ACCESS_POLICY S0 GRANT_ACCESS exit deny / clear |
| [RFC-0102](RFC-0102-access-policy-room.md) | **Accepted** | ACCESS_POLICY S1 ROOM deny / clear |
| [RFC-0103](RFC-0103-access-policy-allow-only.md) | **Accepted** | ACCESS_POLICY S2 ALLOW_ONLY |
| [RFC-0104](RFC-0104-access-policy-help.md) | **Accepted** | ACCESS_POLICY S3 Chamber ACCESS help |
| [RFC-0105](RFC-0105-public-titles.md) | **Accepted** | GC1-S6 public titles |
| [RFC-0106](RFC-0106-agent-orientation.md) | **Accepted** | Agent orientation S0 first-OBSERVE withhold |
| [RFC-0107](RFC-0107-agent-orientation-situation.md) | **Accepted** | Agent orientation S1 situation fields |
| [RFC-0108](RFC-0108-agent-orientation-connect.md) | **Accepted** | Agent orientation S2 CONNECT / skill withhold |
| [RFC-0109](RFC-0109-human-orientation.md) | **Accepted** | Human first-screen withhold |
| [RFC-0110](RFC-0110-focus-declaration.md) | **Accepted** | GC1-S7 focus declaration |
| [RFC-0111](RFC-0111-agent-harness.md) | **Accepted** | Headless Agent Gameplay Harness |
| [RFC-0112](RFC-0112-parameter-access.md) | **Accepted** | GC1-S8 Engineer overhaul parameter |
| [RFC-0113](RFC-0113-hosted-multiplayer-contention.md) | **Accepted** | Hosted first-accepted harvest; MESSAGE remains mail; no live chat |
| [RFC-0114](RFC-0114-llm-controller-adapter.md) | **Accepted** | LLM Controller propose contract; no AGENT_PLAYER; no new verbs |
| [RFC-0115](RFC-0115-sealed-live-attach.md) | **Accepted** | Live agent attach requires published sealed-prompt hash |
| [RFC-0116](RFC-0116-official-agent-client.md) | **Accepted** | Official external client `scrimshawlife-ctrl/noema-client` |
| [RFC-0117](RFC-0117-lockout-wait-rest.md) | **Accepted** | Lockout WAIT rest |
| [RFC-0118](RFC-0118-work-consumes-cargo.md) | **Accepted** | Work consumes cargo |
| [RFC-0119](RFC-0119-wait-cargo-fuel.md) | **Accepted** | WAIT burns cargo for energy |
| [RFC-0120](RFC-0120-agent-only-player-identity.md) | **Accepted** | Only agents are Players; humans are platform principals |
| [RFC-0121](RFC-0121-perihelion-successor-world-version.md) | **Accepted** | Perihelion successor `world.perihelion-reach-2`; 10-room CHAMBER-MAP; no live reseed |
| [RFC-0122](RFC-0122-perihelion-ewm-product-world.md) | **Accepted** | Perihelion EWM product world_version |
| [RFC-0123](RFC-0123-norm-ratchet-bounds-and-costly-trade-reject.md) | **Accepted** | Bounded upward norm ratchet; costly TRADE-reject punishment pinned |
| [RFC-0124](RFC-0124-governance-rule-contract.md) | **Accepted** | Governance rule contract (GC4-S8) |
| [RFC-0125](RFC-0125-practice-inheritance-and-schism.md) | **Accepted** | Practice inheritance and schism (GC9-S2) |

## Required review lenses

Compatibility, data impact, research impact, security impact, migration, validation evidence, rollback, and documentation updates.
