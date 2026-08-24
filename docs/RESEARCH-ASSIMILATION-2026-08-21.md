# Research Assimilation — Culture, Governance, Conflict, and Material Practice

**Status:** Draft design integration for review. Not an executable release package.
**Scope:** GC2 Construction, GC4 Institutional Authority, GC7 Strategic Conflict,
GC8 Economic Specialization, and GC9 Emergent Culture.
**Does not open:** a new roadmap category, v0.8 Phenomena, a new event catalog,
STUDY redesign, HP combat, a crafting tree, or a procedural lore engine.

This document assimilates a bounded research pull into existing NOEMA
authorities. It is a cross-cutting design note, not a second canon. Accepted
RFCs remain authoritative where this note refers to shipped semantics.

## Research inputs

- [Divergent Cumulative Cultural Evolution](https://arxiv.org/abs/1604.07110): separate cultural memory and horizontal transmission support persistent, diverging practices.
- [Evolved Open-Endedness in Cultural Evolution](https://arxiv.org/abs/2203.13050): cultural evolution is a useful model for bounded-to-open-ended novelty.
- [Cultural Evolution as Distributed Computation](https://arxiv.org/abs/1310.6342): shared artifacts and communication can preserve distributed solutions.
- [Emergent Communication with World Models](https://arxiv.org/abs/2002.09604): communication is grounded by shared world models, not strings alone.
- [Measuring Non-Trivial Compositionality in Emergent Communication](https://arxiv.org/abs/2010.15058): protocol quality includes compositionality and transfer, not only immediate task success.
- [Quantifying Drivers of Institutional Evolution in Online Communities](https://arxiv.org/abs/2204.12521): institutional change can be analyzed through selective, stochastic, and complementary drivers.
- [A Multi-Agent RL Model of Common-Pool Resource Appropriation](https://arxiv.org/abs/1707.06600): repeated interaction, local incentives, and enforcement shape shared-resource outcomes.
- [A Model of Cultural Evolution in Strategic Conflict](https://arxiv.org/abs/2006.01265): cultural transmission and strategic pressure can co-evolve.
- [The Co-evolution of Costly Signaling and Cooperation in Social Dilemmas](https://arxiv.org/abs/2605.13750): a speculative model-based input for observable commitments and cooperation.

These papers are design inputs. They are not evidence that any proposed NOEMA
behavior is established, and none may become hidden world truth or a research
objective for Players.

## Slice A — Religion-like culture without a religion engine

**Existing authority:** [EMERGENT-CULTURE.md](EMERGENT-CULTURE.md),
[DEEP-TIME.md](DEEP-TIME.md), [INSTITUTIONS.md](INSTITUTIONS.md), and
[SEMANTIC-EVOLUTION-SPEC.md](SEMANTIC-EVOLUTION-SPEC.md). GC9-S0/S1 and
[RFC-0013](../rfcs/RFC-0013-maintenance-custom.md) /
[RFC-0025](../rfcs/RFC-0025-tradition.md) are the machine boundary.

Religion-like behavior is a valid cultural interpretation of the existing
ladder:

```text
repeated practice → custom → tradition → institution → inherited interpretation
```

The following may be derived from ledgered practice, evidence, and transmission:

- symbols, names, memorials, taboos, founding accounts, and recurring rituals;
- institutions that preserve a practice beyond its founders;
- schism, reform, dormancy, revival, and competing interpretations;
- costly public commitments only when they use existing resources, offices,
  agreements, maintenance, or exposure.

The following are not world mechanics in this slice:

- deity or supernatural-truth entities;
- conversion quests, belief meters, faithfulness scores, or divine rewards;
- procedural lore generation;
- a ritual that mutates state without an existing canonical action or schedule.

**Acceptance scenario:** Players repeatedly maintain a relay, publicly cite the
practice, and preserve a symbol in an accessible artifact. Later Players can
inherit a tradition and disagree about its meaning. The ledgered repairs remain
the only canonical history; the symbol and interpretation never become physics.

## Slice B — Governance patterns as bounded institutional configuration

**Existing authority:** [INSTITUTIONAL-AUTHORITY.md](INSTITUTIONAL-AUTHORITY.md),
[INSTITUTIONS.md](INSTITUTIONS.md), [SUCCESSION.md](SUCCESSION.md),
[DIPLOMACY.md](DIPLOMACY.md), and `WORLD-ENGINE.md`'s `governance_rule{}`.

NOEMA does not need a `government` entity class. A council, oligarchy, chartered
organization, rotating office, confederation, or fragmented authority is a
configuration of existing institutions, offices, agreements, territory,
access, and enforcement.

Any future governance contract MUST make these dimensions explicit before it
can authorize world mutation:

| Dimension | Required meaning |
|---|---|
| Decision rule | Which occupied offices or members may decide, and quorum if applicable |
| Appointment | How a vacant office is filled using an existing succession mechanism |
| Jurisdiction | The bounded objects, rooms, lots, agreements, or members affected |
| Enforcement | Which existing action or office scope carries the decision out |
| Failure | What happens on vacancy, disagreement, expiry, or dissolution |
| Evidence | Which public or permissioned records establish the decision |

Charter, constitution, law, or decree text is not executable authority by itself.
It must be represented by an authorized versioned rule or accepted canonical
action. Undefined authority fails closed. This preserves the existing office
conflict-precedence, emergency-scope, and succession rules.

**Acceptance scenario:** An institution publishes a bounded decision rule,
fills a vacant office through an existing succession path, authorizes an
existing resource/access/contest action, and later survives a vacancy or
transforms with an evidence-backed successor edge. No government object or
free-form language interpreter is created.

## Slice C — Conflict depth through existing strategic contestation

**Existing authority:** [STRATEGIC-CONFLICT.md](STRATEGIC-CONFLICT.md),
[DIPLOMACY.md](DIPLOMACY.md), [LOSS-RECOVERY.md](LOSS-RECOVERY.md), and accepted
GC7 RFCs [RFC-0011](../rfcs/RFC-0011-contest-rhythm.md),
[RFC-0026](../rfcs/RFC-0026-contest-withdraw.md),
[RFC-0041](../rfcs/RFC-0041-institution-contest-party.md), and
[RFC-0042](../rfcs/RFC-0042-information-contest.md).

The research input reinforces the existing rhythm:

```text
RECON → POSITION → PRESSURE → COUNTER → ESCALATE → COMMIT → RESOLVE → RECOVER
```

The strategic target may be territory, routes, resource sites, institutions,
information, reputation, infrastructure, agreements, or office authority.
Culture and governance affect coordination, commitment, evidence, and recovery;
they do not add hit points or a combat class.

**Acceptance scenario:** Two institutions use visible evidence and existing
`CONTEST_*`, agreement, office, infrastructure, and recovery mechanics to
contest a route. One party may withdraw under the accepted rules. The result
leaves attributable history and a recovery path; no character death, real-time
attack, hidden-fact leak, or new event catalog is introduced.

## Slice D — Items as bounded material practice, not a crafting tree

**Existing authority:** [CONSTRUCTION.md](CONSTRUCTION.md),
[ECONOMIC-SPECIALIZATION.md](ECONOMIC-SPECIALIZATION.md),
[RESOURCE-ECONOMY.md](RESOURCE-ECONOMY.md), [DEEP-TIME.md](DEEP-TIME.md), and
accepted GC2/GC8 RFCs [RFC-0045](../rfcs/RFC-0045-lot-quality.md),
[RFC-0046](../rfcs/RFC-0046-lot-provenance.md),
[RFC-0047](../rfcs/RFC-0047-lot-spoilage.md),
[RFC-0050](../rfcs/RFC-0050-workshop.md), and
[RFC-0057](../rfcs/RFC-0057-workshop-repurpose.md).

In player language, an “item” is one of the existing bounded forms:

- a `ResourceLot` with quantity, quality, holder, location, and provenance;
- an `Artifact` with evidence identity, ownership/visibility, and lineage;
- a constructible infrastructure entity with condition, inputs, outputs, and
  stewardship.

An item transformation is eligible for later specification only when it uses
existing resources and changes a real strategic dependency: production,
storage, movement, communication, access, contest defense, trade, or history.
The transformation must have explicit inputs, outputs, cost, ownership,
visibility, failure, salvage, and replay behavior.

**Acceptance scenario:** A Player obtains a provenance-bearing lot, uses an
existing workshop to construct or repurpose a bounded infrastructure class,
and later Players can observe the strategic consequence and its lineage. No
recipe tree, infinite rarity ladder, loot table, inventory microgame, or new
Player caste is required.

## Cross-cutting exclusions

- No new top-level roadmap category is created.
- No v0.8 Phenomena scope is opened.
- STUDY remains observational and research-isolated; it does not issue build,
  religion, governance, or combat objectives.
- Research metrics do not authorize actions, grant Player rewards, or mutate
  canonical state.
- Existing accepted RFCs and versioned catalogs remain the executable boundary.
- Any future machine-readable governance or culture fields require a dedicated
  RFC, schema/version review, positive and negative fixtures, and validator
  evidence before runtime implementation.

## Review status

This note is ready for maintainer review. It intentionally closes the research
assimilation loop at the design/integration level while leaving new executable
semantics RFC-gated.
