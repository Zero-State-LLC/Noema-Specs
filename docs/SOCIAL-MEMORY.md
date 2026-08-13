# Social Memory and Relational Reputation (GC3)

**Status:** Product authority for persistent social memory. P0. Phase GC-A.  
**Campaign:** [GAME-COMPLETENESS-PLAN.md](GAME-COMPLETENESS-PLAN.md)  
**Does not replace:** [INSTITUTIONAL-MEMORY.md](INSTITUTIONAL-MEMORY.md) · [DIPLOMACY.md](DIPLOMACY.md) · [PROGRESSION.md](PROGRESSION.md)  
**Influence** remains a Chamber resource ([RESOURCE-ECONOMY.md](RESOURCE-ECONOMY.md)). It is not reputation.

This document is **not** an executable package. Machine contracts are **SPEC GAP**.

**Doctrine:** evidence-backed edges, not a reputation industry or `reputation = 72` engine ([COMPLEXITY-DOCTRINE.md](COMPLEXITY-DOCTRINE.md)). Memory must be able to change trade, access, agreements, authority, cooperation, conflict, or information sharing — or it is presentation.

---

## Thesis

Avoid:

```text
reputation = 72
```

as the sole model.

Prefer evidence-backed relationship edges:

```text
Player A  →  relationship / memory state  →  Player B
Institution  →  relationship / memory state  →  Player
```

Descriptors such as `reliable`, `dangerous`, `generous`, `deceptive`, `competent`, `reckless`, `loyal`, `indebted`, `trusted`, `unknown` are **derived projections** of evidence, not hidden scalar stats.

Hard invariant:

> Hidden facts MUST NOT leak through reputation projections.

---

## Settled model

### Who may form a memory

| Subject | Object | Legal? |
|---------|--------|--------|
| Player | Player | Yes, from interactions the subject could observe or participate in |
| Institution | Player | Yes, from evidence the institution is authorized to hold |
| Player | Institution | Yes, as the Player’s private interpretation plus public institutional acts |
| WATCH spectator | anyone | No world memory. Spectators do not write relationship edges |
| Research / LEARN | anyone | No. Research graphs are not social memory |
| World Service | Player | Only as a deterministic service record (trade history, registry), never a personality score |

A Player cannot form a memory of a fact they had no observational or participatory path to know.

### Canonical vs derived

| Layer | Status |
|-------|--------|
| Evidence refs (event IDs, agreement IDs, public reports) | Canonical |
| Relationship edge (subject, object, evidence set, polarity counts) | Canonical **or** rebuildable derived — RFC decides. First implementation SHOULD rebuild from the ledger |
| Descriptor bands (`reliable`, `unknown`, …) | Derived presentation |
| Private notes / messages about someone | Remain messages; they are not the public reputation |

Contradictory evidence stays contradictory. The engine MUST NOT collapse “helped me / later betrayed me” into a single integer.

### Certainty and contradiction

Each descriptor projection carries a coarse certainty:

```text
UNKNOWN | CONTESTED | SUPPORTED | STRONG
```

`CONTESTED` is required when supporting and opposing evidence both exist above versioned floors. Players MAY hold different private descriptors of the same third party.

Research-only fields that know which rumor was false MUST NOT appear in PLAY ([CONTRADICTORY-EVIDENCE.md](CONTRADICTORY-EVIDENCE.md)).

---

## Source evidence

Closed families (weights SPEC GAP):

| Family | Examples |
|--------|----------|
| Exchange | Successful / failed-but-legal `TRADE`; withheld acceptance is not automatically “deceptive” |
| Cooperation | Shared repair, joint harvest under agreement, mutual defense |
| Breach | Formal `AGREEMENT_BROKEN`; crime detection ([STRATEGIC-CONFLICT.md](STRATEGIC-CONFLICT.md)) |
| Contest | Contests against the subject; severity by form, not HP |
| Communication | Public messages are evidence of what was said, not of truth |
| Institutional record | Membership, expulsion, issued recognition, office history |
| Witnessed work | Co-located observation of harvest, repair, sabotage |

Private `MESSAGE` text is **not** public reputation evidence. A recipient may form a **private** edge from a message they received. That private edge MUST NOT become a WATCH or third-party descriptor.

---

## Decay, forgiveness, rehabilitation, history

| Process | Rule |
|---------|------|
| Decay | Old evidence loses **weight** for derived descriptors; it remains in history |
| Forgiveness / rehabilitation | New contrary public evidence (kept agreements, restitution trades, institutional pardon records) can move descriptors from `dangerous` / `deceptive` toward `contested` then `supported` positive bands |
| Historical persistence | The ledger and public events never forget. Descriptors may soften; scars and reports remain ([DEEP-TIME.md](DEEP-TIME.md)) |
| Succession | A successor does not inherit another Player’s private edges. They inherit institutional memory of the office/institution ([SUCCESSION.md](SUCCESSION.md)) |

There is no paid “wipe reputation” action.

---

## Visibility: private vs public

| Projection | Contents |
|------------|----------|
| Private (subject only) | Edges the subject formed; private message-derived memory |
| Dyadic | What A and B each know about their shared history; not automatically visible to C |
| Public reputation | Only public events: formal breaches, public recognitions, public crime records, public reports |
| Institutional | What that institution’s authorized records contain |
| WATCH | Public reputation and public events only |
| GUI affordances | MUST NOT expose private edges of others (`NOT_OBSERVABLE`) |

If Player B’s betrayal used a hidden route or hidden stockpile, the public descriptor may become `dangerous` or `deceptive` from the **public** contest/breach event. The projection MUST NOT name the hidden route or stockpile.

---

## Consequences (coupling, not a minigame)

Social memory MAY affect:

| Domain | Effect family |
|--------|---------------|
| Trade | Higher friction, refusal defaults, or preferred counterparties — never automatic hidden price lists that leak private inventories |
| Access | Institutions MAY deny access based on **their** records |
| Authority | Office eligibility MAY consult institutional memory ([INSTITUTIONAL-AUTHORITY.md](INSTITUTIONAL-AUTHORITY.md)) |
| Diplomacy | Informal trust is social; formal agreements remain ledgered ([DIPLOMACY.md](DIPLOMACY.md)) |
| Conflict | Reputation is not a combat stat. It MAY change who joins or who will deal during recovery |
| Communication | Recipients MAY refuse addressability only via existing or later explicit policy, not via a hidden filter that reveals why |

Influence resource effects already specified for crime remain valid. They are not a substitute for edges.

---

## Formation without new verbs

First implementation MUST compose existing actions:

```text
TRADE success / reject
AGREEMENT_FORMED / AGREEMENT_BROKEN
ORG_MEMBER_ADD / ORG_MEMBER_REMOVE
CONTEST_* / CRIME_DETECTED
MESSAGE (private edge for recipient only)
public WORLD_REPORT entries
```

No `REMEMBER` or `REPUTE` verb.

---

## PLAY / WATCH / research / security

| Surface | Rule |
|---------|------|
| PLAY | Own private edges; public descriptors of others; never hidden-fact text |
| WATCH | Public descriptors and public events |
| STUDY | May capture relationship change trajectories; MUST NOT publish private message text by default |
| Security | Partial-observability leak via “why is this button missing?” is forbidden. Unavailable trade/access uses observable reasons only |

---

## SPEC GAP

```text
edge schema vs derived rebuild
descriptor catalog and mapping rules
weights, decay windows, rehabilitation thresholds
whether any new event type is required
fixtures (cooperation → trust → betrayal without leak)
conformance for hidden-fact non-leak
PLAY/WATCH projection rules
```

---

## Acceptance (scenario B)

Two Players complete repeated successful trades or joint repairs; their derived descriptors become `reliable` / `trusted` to each other. One later breaks a formal agreement or commits a detected crime against the other. Dyadic and relevant institutional expectations change. Public projection names the public breach, not any hidden method or inventory.
