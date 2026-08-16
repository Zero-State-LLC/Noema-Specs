# Social Memory and Relational Reputation (GC3)

**Status:** Product authority for persistent social memory. P0. Phase GC-A.  
**Campaign:** [GAME-COMPLETENESS-PLAN.md](GAME-COMPLETENESS-PLAN.md)  
**Does not replace:** [INSTITUTIONAL-MEMORY.md](INSTITUTIONAL-MEMORY.md) · [DIPLOMACY.md](DIPLOMACY.md) · [PROGRESSION.md](PROGRESSION.md)  
**Influence** remains a Chamber resource ([RESOURCE-ECONOMY.md](RESOURCE-ECONOMY.md)). It is not reputation.

GC3-S0 machine pins: [GC3-FIRST-SLICE.md](GC3-FIRST-SLICE.md) · [RFC-0007](../rfcs/RFC-0007-dyadic-trade-memory.md). GC3-S1 danger pins: [GC3-S1-BETRAYAL.md](GC3-S1-BETRAYAL.md) · [RFC-0022](../rfcs/RFC-0022-betrayal-dangerous.md). Remaining SOCIAL-MEMORY gaps are closed by [RFC-0034](../rfcs/RFC-0034-watch-public-descriptors.md)–[RFC-0038](../rfcs/RFC-0038-deceptive-edge.md) (S2–S6). GC3-S0/S1 stay WATCH-empty.

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

Closed families (weights: [GC3-S4](GC3-S4-DECAY-REHAB.md)):

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
| WATCH | Coarse public descriptor bands only, and only when rebuildable from already-public events (see below). Silence if evidence is insufficient |
| GUI affordances | MUST NOT expose private edges of others (`NOT_OBSERVABLE`) |

If Player B’s betrayal used a hidden route or hidden stockpile, the public descriptor may become `dangerous` or `deceptive` from the **public** contest/breach event. The projection MUST NOT name the hidden route or stockpile.

### WATCH public descriptors

WATCH MAY surface only **coarse public descriptor bands** (`reliable`, `dangerous`, `deceptive`, `unknown`, and the other listed bands) derived exclusively from already-public events: formal breaches, public recognitions, public crime records, public reports. WATCH MUST NOT surface private edges, dyadic-only memory, hidden routes, private inventories, or private `MESSAGE` text. If current public evidence is insufficient to support a band, the projection stays **silent** on descriptors and MAY show only the underlying public event line. Silence is absence, not a hint ([PARTIAL-OBSERVABILITY.md](PARTIAL-OBSERVABILITY.md) leak rule).

GC3-S0 / GC3-S1 remain **WATCH-empty** as closed hosted slices. This pin is the fail-closed product rule for any later public-descriptor surface. It does not add a reputation scalar or a `REMEMBER` / `REPUTE` verb.

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
| WATCH | Coarse public bands from public events only; else silent or the public event text |
| STUDY | May capture relationship change trajectories; MUST NOT publish private message text by default |
| Security | Partial-observability leak via “why is this button missing?” is forbidden. Unavailable trade/access uses observable reasons only |

---

## SPEC GAP

### Closed for GC3-S0

```text
derived Player→Player edges from TRADE_ACCEPTED
thresholds TRADED=1 RELIABLE=3
self PLAY lines only
no reputation scalar
no new verbs or events
WATCH empty
leak tokens forbidden in projection
```

### Closed for GC3-S1

```text
directed victim→actor danger from CONTEST_RESOLVED
AGREEMENT_BROKEN / CRIME_DETECTED rebuild when those events exist
self PLAY line You have found {name} dangerous.
TRADE_REJECTED and CONTEST_DECLARED ignored
no reputation scalar / WATCH / new verbs
```

### Closed for GC3-S2

```text
WATCH / public PLAY coarse bands from already-public events
dangerous from public CONTEST_RESOLVED / public CRIME_DETECTED
deceptive from public AGREEMENT_BROKEN / contradicted public ATTEST
no reliable / unknown band
silence if insufficient
GC3-S0 / GC3-S1 stay WATCH-empty
```

### Closed for GC3-S3

```text
derived org → player edges from that org's authorized records
officer PLAY; member sees self only
WATCH empty
no ROLE_* ; no copy of private Player edges
```

### Closed for GC3-S4

```text
decay_cycles=12 omits a family's line; ledger never forgets
rehab = 3 TRADE_ACCEPTED after last hostile evidence
no wipe / FORGIVE verb
```

### Closed for GC3-S5

```text
+1 compute TRADE_CAUTION on propose when a live hostile edge exists
no auto-refuse
no hidden markup
affordance stays visible
```

### Closed for GC3-S6

```text
distinct deceptive edge from AGREEMENT_BROKEN and contradicted public ATTEST
TRADE_REJECTED / CONTEST_RESOLVED ignored
WATCH empty on this slice
```

### Closed for GC3-S7

```text
live RELIABLE (≥3) waives TRADE_CAUTION extra compute
auto-accept false
other TRADE affordances stay visible
base compute stays 1
```

### Still open

```text
(none — SOCIAL-MEMORY executable gaps closed by RFC-0007, RFC-0022, RFC-0034–0039)
GC1-S2 mechanical benefit (not GC3)
```

---

## Acceptance (scenario B)

Two Players complete repeated successful trades or joint repairs; their derived descriptors become `reliable` / `trusted` to each other. One later breaks a formal agreement or commits a detected crime against the other. Dyadic and relevant institutional expectations change. Public projection names the public breach, not any hidden method or inventory.
