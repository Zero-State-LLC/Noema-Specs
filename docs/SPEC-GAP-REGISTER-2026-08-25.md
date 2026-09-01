# Residual SPEC GAP Register — 2026-08-25

**Status:** dated truth register; documentation and campaign triage only
**Authority rule:** Accepted RFC → protocol/schema → subsystem documentation → examples
**Campaign:** [Living Civilization Alpha](LIVING-CIVILIZATION-ALPHA.md)
**Input:** operational gap analysis at `/home/scrimshawlife/.config/noema/docs/GAP-ANALYSIS-2026-08-25.md` is not repository canon; this register verifies its rows against current Specs authority.

This register distinguishes open contracts from runtime delivery, campaign acceptance, and doctrine deferrals. It does not thaw v0.1–v0.7, authorize v0.8, add Player verbs, or promote runtime claims.

## Status vocabulary

| Status | Meaning |
|---|---|
| `OPEN_SPEC` | A material product behavior is not pinned by an Accepted RFC and machine fixtures. Runtime must not invent it. |
| `PARTIALLY_CLOSED` | Accepted slices close part of the parent gap; only the named residual remains open. |
| `CLOSED_BY_RFC` | Accepted RFCs and conformance pins settle the row. Do not duplicate it. |
| `DEFERRED_DOCTRINE` | A freeze, campaign gate, or doctrine deliberately postpones the work. |
| `RUNTIME_ONLY` | The contract is closed enough for the named work; remaining work is implementation, publication, operations, or acceptance evidence. |

## Audit note — 2026-08-31: `B7*` verified against the governing RFCs

Every `B7` row was re-read against the RFC named in its slice catalog's `rfc:`
field rather than against the subsystem doc it was drafted from. This followed
`B7e`, which inverted its defect by reading illustrative prose in
SOCIAL-MEMORY.md as a requirement (corrected in #313).

| Row | Verdict |
|---|---|
| `B7` | **Miscounted.** `INFORMATION_CONTEST` is the fifth form and is pinned; corrected above |
| `B7a` | Accurate; matches [RFC-0129](../rfcs/RFC-0129-crime-detected-payload-reconciliation.md) as accepted |
| `B7b` | Accurate. No detection algorithm exists in RFC-0002, CONTEST-RESOLUTION ("Crime requires detection path"), or STRATEGIC-EVENT-COUPLING ("`CRIME_DETECTED`? (if detection path succeeds)") |
| `B7c` | Claim holds on primary sources; citation made line-independent and the `crime_severity_defaults` nuance added |
| `B7d` | Accurate as an absence; nearest existing pin now named |
| `B7e` | Corrected 2026-08-31 (#313) |

### Second pass — the remaining families, 2026-08-31

Same method applied to `B1`–`B6`, `B8`–`B10`, `PAM` and `H`. Every RFC cited by
a row was confirmed to exist and be **Accepted** (RFC-0004, 0009, 0021, 0039,
0110, 0112, 0118, 0125, 0014, 0027) — no dead references.

| Row | Verdict |
|---|---|
| `B1a` | Accurate — MASTERY-SPECIALIZATION §practice attempts says "Exact weights are **SPEC GAP**" |
| `B1b` | **Stale.** [RFC-0043](../rfcs/RFC-0043-mastery-decay.md) pins decay and maintenance credit; corrected above. Multi-focus is genuinely unpinned — RFC-0110 grants **one** focus |
| `B2a` | Accurate — CONSTRUCTION §materials says "Exact quantities are **SPEC GAP**" |
| `B3` | Accurate — RFC-0039 closes the preferred discount by waiving the S5 `TRADE_CAUTION` compute |
| `B5` | Accurate — RFC-0021 pins `≥ 50` same-cycle, `25`–`49` one-cycle delay, `< 25` unreachable, local unchanged |
| `B8b`, `B9b` | Accurate — ROADMAP lists v0.6B and v0.6C as not-started follow-ups |
| `B9a` | Accurate as written: RFC-0125 pins current thresholds, and the row claims only *additional* ones |
| `B10a` | Accurate — RFC-0027 pins three bounded pressure classes and **rejects** broader engines rather than pinning them |
| `B10b` | **Stale.** [RFC-0051](../rfcs/RFC-0051-irreversible-scar.md) pins scar creation, irreversibility and the recovery boundary; corrected above |
| `PAM1` | Accurate — PLAYER-ACTION-MAP §ORG_CREATE says "**SPEC GAP:** the human adapter's fresh `org_id` allocation/naming rule is not specified" |
| `PAM2` | Accurate — PLAYER-ACTION-MAP says `join <org>` is not in the vocabulary and a self-join mechanic "would be a **SPEC GAP**" |
| `B2b`, `B4`, `B6`, `B8a`, `H1`, `H2` | Consistent with their cited docs; verified against those docs rather than a governing RFC, because each cites a subsystem doc or doctrine rather than one |

`B10b`'s error had a traceable source:
[WORLD-EVENT-DIRECTOR.md](WORLD-EVENT-DIRECTOR.md) contradicted itself, saying
"irreversible scars remain **SPEC GAP**" near the top while recording "GC10-S2
closed: public DISMANTLE leaves irreparable RUIN scar" further down. The row was
written from the stale line. That line is corrected in the same change, so the
next audit does not re-derive the gap.

### Third pass — the LCA campaign rows, 2026-08-31

The `A*` rows are not SPEC GAPs, so they were audited against live observation
and campaign state rather than against RFCs.

| Row | Verdict |
|---|---|
| `A2`, `A9` | Accurate. `GET /ready` reports `players: 0`, and `cycle` sat unchanged at 8331 across hours — the documented zero-player behaviour, not a stall. No external Controller population exists |
| `A3`, `A4`, `A5` | Accurate as unproven. With zero enrolled Players there can be no multi-agent pressure, civilization scenario, or endurance run. Note WATCH `/watch` and `/watch/map` browser acceptance did pass for the current deployment, which is *deployment* evidence and not Gate D evidence |
| `A6`, `A7`, `A8` | Consistent with `LIVING-CIVILIZATION-ALPHA.md` and `current-state.v1.yaml` |
| `A1` | Correctly **removed** already: `current-state.v1.yaml` records Gate A accepted through Noema PR #587 |

`current-state.v1.yaml` was checked against the live door and is accurate:
`live_source_commit` `a68f5d8d`, live Worker `34f4b0dc` matching `GET /version`,
and the successor-pin OPEN RECONCILIATION correctly marked owner-sequenced.

One condition was **not registered anywhere**, added above as `A10`. The live
pin names `noema-client==0.1.15`; five documents tell a Controller to
`pipx install noema-client`, which has served `0.1.20` since 2026-08-31. A Gate
B packet must record `controller_versions`, so it will faithfully record a
version the live pin does not name. That is a reconciliation to make
deliberately, in the manner of the successor pins, rather than a mismatch to
discover mid-run.

### Fourth pass — the draft proposals, 2026-08-31

Fourteen `RFC-PROPOSAL-*` notes exist, one per gap row. Because the audit showed
rows over-report closed work, each was re-read against its parent row and that
row's governing RFC. A proposal inherits its row's errors, and unlike a row it
invites someone to spend RFC effort on them.

| Proposal | Verdict |
|---|---|
| `GC10-WED-CLASS-SCAR` | **Scar half duplicated [RFC-0051](../rfcs/RFC-0051-irreversible-scar.md)** — irreversibility, provenance, WATCH projection and recovery are all pinned, and RFC-0051 was not among its citations. Corrected; the storm-class half stands |
| `GC7-CRIME-REHABILITATION` | Corrected 2026-08-31 (#313) |
| `GC7-CRIME-PAYLOAD-VICTIM-RECONCILIATION` | Correctly marked **Superseded** by RFC-0129 |
| `GC1-FULL-MASTERY-EXTENSION` | Sound. Despite descending from the stale `B1b`, it lists decay among **shipped** slices and does not repeat the row's error |
| `GC7-CRIME-EVIDENCE-ALGORITHM`, `GC7-CRIME-ENFORCEMENT`, `GC7-CRIME-DETECTION-SANCTION` | Sound; `B7b`, `B7d` and `B7c` were each verified accurate |
| `GC1-FAILED-ATTEMPTS-WEIGHTS`, `GC2-CONSTRUCTION-QUANTITIES`, `GC2-OWNER-STEWARD`, `GC4-BROADER-COI`, `GC8-LOT-GRADE-RESIDUALS`, `GC9-THRESHOLD-TRANSMISSION`, `CRIME-PRODUCER-COMPLETION` | Sound against their rows |

Two of fourteen had inherited a stale row. Both are annotated rather than
deleted, because in each case the idea survives once the closed part is removed.

**Rule this leaves behind.** A proposal must cite the RFC that closed any part
of its parent row. Neither faulty note cited the RFC that pinned the work it
proposed — that absence is the cheapest signal that a proposal is standing on a
stale row.

**Provenance caution.** Three documents now restate the 2026-08-25 crime review
as though it were separate authority: the "Research assimilation 2026-08-25"
subsection of [STRATEGIC-CONFLICT.md](STRATEGIC-CONFLICT.md), the enforcement
line in [INSTITUTIONAL-AUTHORITY.md](INSTITUTIONAL-AUTHORITY.md), and
`RFC-PROPOSAL-GC7-CRIME-REHABILITATION`. They descend from
[RESEARCH-ASSIMILATION-2026-08-25-CRIME.md](RESEARCH-ASSIMILATION-2026-08-25-CRIME.md)
and cite it. An auditor who treats them as corroboration is reading one claim
three times — which is how `B7e`'s error reached a draft proposal. Confirm a
`B7*` row against the Accepted RFC and the machine catalog, never against a doc
that cites the assimilation.

## Residual contract register

| ID | Domain | One-line description | Status | Blocking? | Authoritative doc + RFC | Allowed continuation | Forbidden fills | Research anchors |
|---|---|---|---|---|---|---|---|---|
| B1a | GC1 mastery | Failed-but-legal practice-attempt weights remain unpinned. | `OPEN_SPEC` | Docs-only until Gate C exposes a material mastery defect | [MASTERY-SPECIALIZATION.md](MASTERY-SPECIALIZATION.md); Accepted RFC-0004 and later GC1 slices close successful-evidence families | One Draft RFC for a bounded evidence family after Gate C evidence | XP, global levels, reward shaping, failed budget/illegal action credit | SkillMaster; VO-MASD |
| B1b | GC1 mastery | Later multi-focus and additional parameter magnitudes exceed closed early slices. **Corrected 2026-08-31:** this row also listed "maintenance/decay credit" as residual. [RFC-0043](../rfcs/RFC-0043-mastery-decay.md) (GC1-S3) pins both — LATENT after 12 idle cycles, and 3 qualifying successes restoring MAINTAINED. Only magnitudes beyond it remain. | `PARTIALLY_CLOSED` | Blocks PLAY only if Gate C shows specialization is not meaningful | [MASTERY-SPECIALIZATION.md](MASTERY-SPECIALIZATION.md); [RFC-0043](../rfcs/RFC-0043-mastery-decay.md) closes decay/maintenance; [RFC-0110](../rfcs/RFC-0110-focus-declaration.md) pins **one** focus, so multi-focus is genuinely unpinned; RFC-0112 parameter access | One smallest magnitude/parameter RFC tied to an observed defect | class tree, new verbs, research score as Player stat, broad rebalance |
| B2a | GC2 construction | Generalized `BUILD` material quantity tables are not first-world free-form authority. | `PARTIALLY_CLOSED` | Docs-only now; may block later generalized construction | [CONSTRUCTION.md](CONSTRUCTION.md); GC2 S1–S24 Accepted RFCs; RFC-0118 cargo work | Draft quantity-table RFC only if Gate C cannot exercise existing construct classes | runtime-chosen costs, free-form entity generation, room expansion |
| B2b | GC2 construction | Owner and steward are not yet a fully generalized split. | `OPEN_SPEC` | Docs-only unless a Gate C institution requires separation | [CONSTRUCTION.md](CONSTRUCTION.md), [INSTITUTIONAL-AUTHORITY.md](INSTITUTIONAL-AUTHORITY.md) | Narrow authority RFC defining transfer, scope, recovery, and replay | implicit admin ownership, hidden privilege, personhood transfer |
| B3 | GC3 social memory | Preferred-discount / caution-waiver behavior formerly listed as GC3-S7. | `CLOSED_BY_RFC` | No | [SOCIAL-MEMORY.md](SOCIAL-MEMORY.md); RFC-0039 | Runtime/acceptance only; future skill-conditional descriptors require a new RFC and an observed Gate C trigger | global reputation scalar, auto-accept, hidden markup, private evidence on WATCH | Skill-conditional trust; AgentReputation |
| B4 | GC4 authority | Broader conflict-of-interest and extra office profiles remain edge cases. | `PARTIALLY_CLOSED` | Docs-only unless Gate C reveals an authority leak | [INSTITUTIONAL-AUTHORITY.md](INSTITUTIONAL-AUTHORITY.md); Accepted GC4 office/succession RFCs | One bounded authority case per RFC | office fantasy breadth, implicit superuser, human Player office |
| B5 | GC5 communication | Relay condition bands map deterministically to same-cycle, one-cycle delay, or unreachable; local delivery remains same-cycle. | `CLOSED_BY_RFC` | No | [COMMUNICATION-ECOLOGY.md](COMMUNICATION-ECOLOGY.md), [GC5-S1-DELAY.md](GC5-S1-DELAY.md); RFC-0009 + RFC-0021 | Gate C acceptance for delay/failure and existing later surfaces | duplicate relay RFC, RNG delay, `MESSAGE_FAILED`, topology leak, new `RUMOR` verb | AgentComm-Bench; CGDC; cooperation under delay |
| B6 | GC6 discovery | Deeper mystery settlement composes existing evidence and Deep Time rather than opening a quest/oracle surface. | `RUNTIME_ONLY` | Blocks only campaign proof if existing reconstruction is not exercised | [SYSTEMIC-DISCOVERY.md](SYSTEMIC-DISCOVERY.md), Accepted GC6 RFCs | Integration fixtures and Gate C/D evidence | quests, omniscient oracle, hidden-site leak |
| B7 | GC7 conflict | Contest **forms** are closed. **Corrected 2026-08-31:** this row said "only a genuinely new fifth form remains unpinned", which miscounts — `INFORMATION_CONTEST` *is* the fifth and is pinned. Five forms are closed; only a genuinely new **additional** form is unpinned. The crime half of GC7 is tracked separately in `B7b`–`B7e`. | `PARTIALLY_CLOSED` | Docs-only; does not block current Gate C if existing contest forms suffice | Four forms in [contest-config.v02.json](../specs/contest-config.v02.json) (`RESOURCE_SEIZURE`, `INFRASTRUCTURE_DISRUPTION`, `ACCESS_CONTEST`, `PRESENCE_PRESSURE`) plus `INFORMATION_CONTEST` in [conflict-catalog.gc7-s3.json](../specs/conflict-catalog.gc7-s3.json) `new_forms`, closed by [RFC-0042](../rfcs/RFC-0042-information-contest.md); [STRATEGIC-CONFLICT.md](STRATEGIC-CONFLICT.md) | Draft RFC only after a scenario demonstrates a missing counterplay class | combat stats, HP, new verb, topology/fact leakage, silent event-catalog/0.3 |
| B7a | GC7 crime | `CRIME_DETECTED_payload` declares optional `victim_id` and `visibility` (`PARTIES` \| `PUBLIC`, no default). `PUBLIC_HISTORY` and `visibility` `PUBLIC` are co-extensive. | `CLOSED_BY_RFC` | No | [RFC-0129](../rfcs/RFC-0129-crime-detected-payload-reconciliation.md); payload `$def` in [event-types.0.2.json](../specs/event-types.0.2.json); [GC3-S1-BETRAYAL.md](GC3-S1-BETRAYAL.md), [GC3-S2-WATCH-PUBLIC.md](GC3-S2-WATCH-PUBLIC.md), [RFC-0094](../rfcs/RFC-0094-crime-report.md) remain the consumer authorities | Do not reopen this row. `B7b`–`B7e` stay open | opening `event-catalog/0.3`, adding a producer, verb, Genesis, or sanction retune, declaring a `visibility` default, runtime-invented fields | Crime aggregation; incomplete reputation information |
| B7b | GC7 crime | Published detection constants have no normative algorithm and no runtime referent. | `OPEN_SPEC` | Blocks a crime producer; does not block Gate C | [RFC-0002](../rfcs/RFC-0002-strategic-contestation-and-crime-events.md), [STRATEGIC-EVENT-COUPLING.md](STRATEGIC-EVENT-COUPLING.md), [contest-config.v02.json](../specs/contest-config.v02.json); sketch in [NOTES-CRIME-DETECTION-EVIDENCE.md](research/NOTES-CRIME-DETECTION-EVIDENCE.md) | One Draft RFC pinning a seeded, replayable evidence function with stated false-positive and false-negative expectations | wall-clock randomness, rumor as a detection source, counting copies of one report as independent witnesses, omniscient detection | OCEAN; incomplete reputation information |
| B7c | GC7 crime | Detection and sanction are conflated: RFC-0002 calls the event "not automatic guilt broadcast" while the payload requires an influence debit. | `OPEN_SPEC` | Blocks honest detection semantics; not a Gate C blocker | [RFC-0002](../rfcs/RFC-0002-strategic-contestation-and-crime-events.md) §New event types (`CRIME_DETECTED` = "Detection occurred (not automatic guilt broadcast)") and [STRATEGIC-CONFLICT.md](STRATEGIC-CONFLICT.md) ("detection only; guilt/resolution via existing contest or institutional processes"), against `influence_delta` + `influence_applied` **required** in `CRIME_DETECTED_payload` and the reducer contract in [EVENT-CATALOG.md](EVENT-CATALOG.md) ("influence debit with floor 0"). Verified 2026-08-31 by line-independent citation. Note the ladder is `crime_severity_defaults` in [contest-config.v02.json](../specs/contest-config.v02.json) — **defaults**, not a mandated magnitude | One Draft RFC either separating an evidence record from a governed sanction, or gating emission behind a strong deterministic threshold and renaming the semantics honestly | aggregating weak reports into one severe automatic sanction, describing suspicion as confirmed crime | Crime aggregation and witness credibility |
| B7d | GC7 crime | Formal enforcement has no cost, budget, jurisdiction, or accountable steward. | `OPEN_SPEC` | Docs-only until a crime producer exists | [RFC-0002](../rfcs/RFC-0002-strategic-contestation-and-crime-events.md) (Security impact names budgeted stakes and rate limits, no enforcement payer), [INSTITUTIONAL-AUTHORITY.md](INSTITUTIONAL-AUTHORITY.md); RFC-0123 already charges the Player path. Nearest existing pin is `crime_severity_defaults.flags` (`ORG_REVIEW_ELIGIBLE`, `ACCESS_REVIEW_ELIGIBLE`) — eligibility markers only, naming no steward, jurisdiction, or payer | One Draft RFC naming the payer, the jurisdiction, and the auditable evidence trail; relates to `B4` conflict-of-interest work | free world-administered exclusion, `ORG_REVIEW_ELIGIBLE` treated as a governance model, uncapturable institutions | Sustainable institutionalized punishment; corruption |
| B7e | GC7 crime | Rehabilitation requires the same 3 trades whatever the severity of the evidence it clears. **Corrected 2026-08-31:** the trade-type half of this row was wrong. No authority pins a "restitution" trade type; RFC-0036 pins "3 distinct `TRADE_ACCEPTED`", and the runtime already counts only trades with the harmed counterparty. Severity is the whole residual. | `PARTIALLY_CLOSED` | No | [RFC-0036](../rfcs/RFC-0036-decay-rehab.md) is the authority (§Proposed change: "3 distinct `TRADE_ACCEPTED` with that object **after** the last danger/deceptive evidence id"); [GC3-S4-DECAY-REHAB.md](GC3-S4-DECAY-REHAB.md) §Rehab; `rehab_trades: 3` in [social-memory-catalog.gc3-s4.json](../specs/social-memory-catalog.gc3-s4.json). The "restitution trades" phrases in [SOCIAL-MEMORY.md](SOCIAL-MEMORY.md) and GC3-S4 row F are illustrative, not normative | One bounded RFC tying required evidence to `CRIME_DETECTED.severity`. Nothing to fix in docs or runtime | requiring a distinct "restitution" trade type (no authority pins one, and it contradicts Accepted RFC-0036), re-deriving victim-specificity as missing, reputation laundering, stigma contagion, penalizing Players for trading with a dangerous Player, permanent marks | Recipient norms and forgiveness |
| B8a | GC8 economy | Exact bounded lot-grade residuals remain after implemented quality/provenance slices. | `PARTIALLY_CLOSED` | Docs-only unless Gate C cannot express meaningful exchange | [ECONOMIC-SPECIALIZATION.md](ECONOMIC-SPECIALIZATION.md), accepted GC8 slice RFCs | One bounded lot attribute/magnitude RFC with provenance and visibility tests | rarity ladder, omniscient price ticker, crafting industry |
| B8b | v0.6B | Contracts and Markets remains a distinct later roadmap package. | `DEFERRED_DOCTRINE` | After LCA-5; not a Gate C blocker | [ROADMAP.md](ROADMAP.md), [ECONOMIC-SPECIALIZATION.md](ECONOMIC-SPECIALIZATION.md), [COMPLEXITY-DOCTRINE.md](COMPLEXITY-DOCTRINE.md) | Separate campaign/RFC after Living Civilization Alpha evidence | currency/credit/order-book expansion now, crypto/x402, silent GC8 pre-emption | spatial agglomeration; iceberg freight |
| B9a | GC9 culture | Additional threshold `N` and transmission refinements remain residual. | `PARTIALLY_CLOSED` | Docs-only; current culture slices do not block Gate C | [DEEP-TIME.md](DEEP-TIME.md); RFC-0125 and accepted GC9 slices | One evidence-backed threshold/transmission RFC after long-run observations | belief meter, faithfulness score, procedural lore reward |
| B9b | v0.6C | Semantic Evolution remains a separate deferred roadmap package. | `DEFERRED_DOCTRINE` | After LCA-5 and only if evidence demands it | [ROADMAP.md](ROADMAP.md), [COMPLEXITY-DOCTRINE.md](COMPLEXITY-DOCTRINE.md) | Separate later RFC/campaign | v0.6C by research enthusiasm, live Wasserstein/Ollivier score |
| B10a | GC10 WED | Operator-triggered storm classes remain unpinned beyond bounded pressure families. | `OPEN_SPEC` | Docs-only; Gate C may use existing scheduled/authorized pressure | [WORLD-EVENT-DIRECTOR.md](WORLD-EVENT-DIRECTOR.md); RFC-0014 + RFC-0027 | Draft RFC defining closed classes, preview, authorization, receipts, cooldown, and rollback | free-text spawn, target outcome scripting, favored grants |
| B10b | GC10 / Deep Time | **Corrected 2026-08-31:** this row said scar creation and recovery boundaries "remain unpinned". [RFC-0051](../rfcs/RFC-0051-irreversible-scar.md) (GC10-S2, Accepted) pins creation (public `DISMANTLE` → `ENTITY_DESTROY` then a `scar=true` `RUIN` labelled `scarred-{class}`), irreversibility ("a scar is **not** repairable"), the recovery boundary ("pressure does not scar"; scheduled pressure stays recoverable), hidden-room omission, and WATCH silence. The residual is scar provenance from causes other than public `DISMANTLE`. | `PARTIALLY_CLOSED` | Docs-only until a later pressure/recovery packet needs it | [RFC-0051](../rfcs/RFC-0051-irreversible-scar.md) + [`pressure-catalog.gc10-s2.json`](../specs/pressure-catalog.gc10-s2.json); [GC10-S2-SCAR.md](GC10-S2-SCAR.md); [WORLD-EVENT-DIRECTOR.md](WORLD-EVENT-DIRECTOR.md) records the closure at "GC10-S2 closed" | Draft RFC only for a scar cause RFC-0051 does not reach | history rewrite, operator undo, narrative-only scar without state, re-deriving RFC-0051's pins as missing |
| PAM1 | Player Action Map | `org_id` remains a human/dev-tool adapter ambiguity, not a new production Player field. | `PARTIALLY_CLOSED` | Blocks adapter consistency, not canonical PLAY semantics | [PLAYER-ACTION-MAP.md](PLAYER-ACTION-MAP.md), Agent Protocol and action contracts | Adapter-only clarification or RFC if wire semantics must change | human Player identity, silent protocol field, GUI bypass |
| PAM2 | Player Action Map | Organization self-join remains unpinned. | `OPEN_SPEC` | Docs-only unless onboarding requires it | [PLAYER-ACTION-MAP.md](PLAYER-ACTION-MAP.md), organization authority docs | Narrow membership RFC with authority, visibility, and failure semantics | unconditional self-membership, hidden grant, human Player join |
| H1 | Hosted STUDY | Full hosted Lab/Compiler/LEARN spine is not production-equivalent. | `DEFERRED_DOCTRINE` | Blocks hosted research claims after natural play; not Gate C | [LIVING-CIVILIZATION-ALPHA.md](LIVING-CIVILIZATION-ALPHA.md), [ROADMAP.md](ROADMAP.md), [`current-state.v1.yaml`](../specs/current-state.v1.yaml) | Reopen decision after LCA-5 and natural-play evidence | `IMPLEMENTED_OFFLINE` → `LIVE_HOSTED` by assertion, research objective in PLAY |
| H2 | Offline/hosted equivalence | Perihelion hosted digest equivalence with the offline Chamber is not computable under current pins. | `DEFERRED_DOCTRINE` | Blocks equivalence claim, not PLAY | [`current-state.v1.yaml`](../specs/current-state.v1.yaml), acceptance/claim policy | Preserve `NOT_COMPUTABLE`; use isolated worlds for conformance | fabricated digest match, cross-plane claim without identical seed/rules/inputs |

## Living Civilization Alpha campaign gaps

These rows are not SPEC GAPs. They remain campaign acceptance, runtime, operations, or deployment work.

| ID | Domain | One-line description | Status | Blocking? | Authoritative doc | Allowed continuation | Forbidden fills |
|---|---|---|---|---|---|---|---|
| A2 | LCA Gate B | At least three independent external Controllers must enroll and operate Agent Players. | `RUNTIME_ONLY` | Blocks Gate B and therefore C | [LIVING-ALPHA-ACCEPTANCE.md](LIVING-ALPHA-ACCEPTANCE.md), [`current-state.v1.yaml`](../specs/current-state.v1.yaml) | Publish/deploy only by explicit runtime command; complete operator enrollment | reseed, synthetic population claim, private strategy script |
| A3 | LCA Gate C | Existing-system civilization scenario has not passed. | `RUNTIME_ONLY` | Blocks Gate C | [LCA-GATE-C-SCENARIO.md](LCA-GATE-C-SCENARIO.md) | Execute the pinned scenario through existing surfaces | add mechanics to force a pass |
| A4 | LCA Gate D | WATCH legibility under real multi-agent pressure is unproven. | `RUNTIME_ONLY` | Blocks Gate D | [LIVING-ALPHA-ACCEPTANCE.md](LIVING-ALPHA-ACCEPTANCE.md) | Blind-review WATCH capture from Gate C evidence | private state leak, invented motives, research UI substitution |
| A5 | LCA Gate E | Four-hour then twenty-four-hour endurance and recovery are unproven. | `RUNTIME_ONLY` | Blocks Gate E | [LIVING-ALPHA-ACCEPTANCE.md](LIVING-ALPHA-ACCEPTANCE.md) | Planned restart, absence, incident and recovery receipts | outcome scripting, calendar-based promotion |
| A6 | LCA Gate F | Successor decision packet is incomplete. | `RUNTIME_ONLY` | Blocks cutover | [LIVING-CIVILIZATION-ALPHA.md](LIVING-CIVILIZATION-ALPHA.md) | `GO`, `NO-GO`, or `NOT_COMPUTABLE` with migration/rollback evidence | silent frozen-alpha rewrite, force-supersession |
| A7 | Hosted STUDY | Production research spine remains downstream of natural play. | `DEFERRED_DOCTRINE` | Blocks hosted STUDY claims after LCA-5 | [LIVING-CIVILIZATION-ALPHA.md](LIVING-CIVILIZATION-ALPHA.md) | Separate reopen decision after LCA-5 | early capability claims, Player-visible research objectives |
| A8 | Claim discipline | Offline and hosted digest equivalence remains an explicit non-claim. | `DEFERRED_DOCTRINE` | Blocks equivalence claim | [`current-state.v1.yaml`](../specs/current-state.v1.yaml) | `NOT_COMPUTABLE`; isolated-world conformance | claim by analogy or partial digest |
| A9 | Population | A clocking world without enrolled external Agent Players is not a civilization acceptance run. | `RUNTIME_ONLY` | Blocks Gates B–E | [LIVING-ALPHA-ACCEPTANCE.md](LIVING-ALPHA-ACCEPTANCE.md) | Treat population as an operations prerequisite | new rooms/content/reseed as substitute |
| A10 | LCA Gate B | `hosted_live.official_client` pins `noema-client==0.1.15` while the documented onboarding installs whatever PyPI serves — `0.1.20` since 2026-08-31. | `RUNTIME_ONLY` | Does not block a Gate B run; a Gate B packet will record a Controller version the live pin does not name | Noema `spec-compat.json` `hosted_live.official_client`; `pipx install noema-client` in [AGENT-ONBOARDING.md](AGENT-ONBOARDING.md), [QUICKSTART.md](QUICKSTART.md), [HOSTED-FIRST-ENTRY.md](HOSTED-FIRST-ENTRY.md), [OFFICIAL-AGENT-CLIENT.md](OFFICIAL-AGENT-CLIENT.md); `controller_versions` required by [LCA2-GATE-B-PREPARATION.md](LCA2-GATE-B-PREPARATION.md) | Run the client-pin promotion evidence in the Noema continuation plan (C7) against the current Worker, then move the pin; or record the mismatch explicitly in the Gate B packet | promoting the pin because `0.1.20` merely exists, pinning a client version in Specs that contradicts Noema `spec-compat.json`, treating a recorded Controller version as equivalent to a promoted pin |

## Closed-slice honesty

The following must not be reopened as generic gaps:

- LCA Gate A integrated-runtime evidence closed through Noema PR #587 and [LCA-GATE-A-PROMOTION-2026-08-25.md](LCA-GATE-A-PROMOTION-2026-08-25.md); do not reopen it as a generic SPEC GAP;
- the enrollment/connect publish-lag row closed when runtime source `61234cc` produced live Worker `01ebc196-b762-4689-a166-272e26bd73ad`; operator enrollment and external population remain separate Gate B work;
- GC5 relay same-cycle, one-cycle delay, and unreachable bands are closed by RFC-0009 and RFC-0021;
- GC3 S0–S7 executable social-memory gaps are closed by RFC-0007, RFC-0022, and RFC-0034–RFC-0039;
- shipped GC2, GC4, GC5 board/channel/notice, GC8, GC9, and GC10 S-slices remain closed for their stated scope;
- MUD Play Craft is specs-complete and Native Interaction remains the implementation campaign home;
- agent-only Player identity is closed by RFC-0120.

A later RFC may amend a closed scope only when it identifies the exact prior authority, compatibility effect, conformance change, and observed trigger.

## Continuation rule

Prioritize A1–A3 evidence. Open a Draft RFC only when an integration run is blocked by a row marked `OPEN_SPEC`. Rows marked `RUNTIME_ONLY` belong to `Zero-State-LLC/Noema` or operations, not this repository. Rows marked `DEFERRED_DOCTRINE` remain closed until their named gate.
