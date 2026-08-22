# RFC-0125 — Practice inheritance and schism (GC9-S2)

## Status

**Draft**

Derived culture contract. No new Player verbs. No new events. No new entity
class. No ledger write. No Genesis change. No reseed. This RFC is the
machine-readable half of the Slice A gate named in
[RESEARCH-ASSIMILATION-2026-08-21.md](../docs/RESEARCH-ASSIMILATION-2026-08-21.md),
which requires a dedicated RFC, schema review, positive and negative fixtures,
and validator evidence before any runtime implementation.

## Problem

Specs #245 rules that religion-like behavior is a valid **interpretation** of
the existing ladder — repeated practice → custom → tradition → institution →
inherited interpretation — and never a religion engine. GC9-S0
([RFC-0013](RFC-0013-maintenance-custom.md)) and GC9-S1
([RFC-0025](RFC-0025-tradition.md)) already ship the lower rungs: `PRACTICING`,
`CUSTOM`, `TRADITION`, `DORMANT`, `REVIVED`, and a competing-accounts line.

Two rungs the slice explicitly names are absent, and both are absent for the
same underlying reason:

1. **"institutions that preserve a practice beyond its founders."** A tradition
   is currently derived from a flat count of repairs and a flat set of
   accessors. Nothing in the derived state distinguishes *the founders kept
   doing it* from *someone else carried it on after them*. Continuity beyond
   the originators is the actual religion-like property, and it is not
   representable.

2. **"schism … and competing interpretations."** GC9-S1 surfaces `Accounts of
   this site differ.` when two distinct public claims exist. But a difference
   between two accounts is not a division among practitioners. Claims are not
   attributed to anyone, so a genuine split — practitioners of the same site
   keeping rival accounts of it — is likewise not representable.

The missing primitive in both cases is **attribution of practice and accounts
to actors**. The ledger already records `actor_id` on every event; the derived
culture state discards it.

Without this, "religion-like culture" can only ever be asserted in prose. With
it, inheritance and division are *derived from what agents actually did*, which
is the standing rule for all NOEMA culture.

## Decision

GC9-S2 adds **two derived marks** on an existing tradition. It does not extend
the GC9-S1 status enum, and it does not change any GC9-S1 derivation — every
GC9-S1 fixture keeps its exact expected output.

Both marks are computed only when the GC9-S1 status is `TRADITION` or
`REVIVED`.

### Mark 1 — inheritance

Let the site's repairs be ordered by `(cycle, sequence)`.

```text
originators = distinct actor_id of the first `originator_repairs` repairs
successors  = distinct repair actor_id not in originators
```

The tradition is **inherited** when at least one successor repair occurs at a
cycle strictly later than the last originator repair.

The strict ordering is the point. A second agent repairing alongside the
founders is a co-practitioner, not an heir; the practice has only outlived its
founders once it continues *after* they stop. Concurrent practice is
deliberately not inheritance.

Line: `This site's maintenance tradition has outlived its founders.`

### Mark 2 — schism

The tradition is **schismed** when at least two distinct `PUBLIC` accounts of
the site carry distinct claims, **and** at least two of those accounts are
authored by distinct agents who are themselves repair actors at that site.

Accounts by non-practitioners are commentary, not schism. Two accounts by the
same agent are a revision, not a division. Both are excluded.

Line: `Practitioners of this site keep rival accounts.`

Where both GC9-S1 and GC9-S2 lines apply, GC9-S1 lines come first in ledger
order of derivation — base status line, then `competing_line` — followed by
`inherited_line`, then `schism_line`. Fixed order, because replay conformance
compares line arrays.

The GC9-S1 `competing_line` is unchanged and still fires on claim difference
alone; schism is strictly narrower and may appear alongside it.

### Hard rules

1. **Derived only.** No new entity class, no new verbs, no new events, no
   ledger write. Both marks are recomputed from ledgered events and existing
   reconstruction records.
2. **No religion engine.** No deity or supernatural-truth entity, no belief
   meter, no faithfulness or devotion score, no conversion, no divine reward.
3. **No procedural generation.** The lines are fixed catalog strings. No
   generated names, titles, doctrines, or narrative text.
4. **Lore never overrides ledger.** A rival account changes no entity state,
   no condition, and no ownership. A schism is a fact about accounts, not
   about the world they describe.
5. **No gameplay bonus.** Neither mark grants resources, discounts, contest
   advantage, office authority, or reputation.
6. **Privacy.** The play line must never name which agents hold which account,
   never name the originators or successors, and never expose per-agent
   practice counts. Attribution is used to *derive* the mark and is not
   surfaced by it.
7. **Determinism (ADR-008).** Repair order is `(cycle, sequence)`; the
   originator set is the first `originator_repairs` distinct actors in that
   order. No random tie-break and no implicit stream. The same events must
   produce the same marks on replay.
8. **Non-regression.** GC9-S1 status derivation and lines are unchanged.

### Non-derivation vocabulary

When a mark does not apply, the reason is one of a closed set. These are not
Player-facing refusals — there is no action to refuse — but they are what
fixtures assert and what the validator checks.

| Reason | Meaning |
|---|---|
| `not_a_tradition` | GC9-S1 status is not `TRADITION` or `REVIVED` — this includes `DORMANT`, which is not "below" tradition but is not a live one either |
| `founders_only` | No successor repair after the last originator repair |
| `single_account` | Fewer than two distinct public claims |
| `unattributed_accounts` | Rival claims exist but not by distinct site practitioners |
| `no_public_account` | Accounts exist but none are `PUBLIC` |

## Machine-readable contracts

| Artifact | Purpose |
|---|---|
| `specs/culture-catalog.gc9-s2.json` | Thresholds and fixed lines; `extends: culture-catalog/gc9-s1` |
| `specs/culture-catalog.gc9-s2.schema.json` | Catalog shape, with the forbidden-projection guard list |
| `specs/culture-rebuild.gc9-s2.schema.json` | Rebuild fixture shape; adds the two marks and the non-derivation reason to `expected` |
| `examples/gc9-schism/` | Positive and negative fixtures for every reason above |
| `check_gc9_s2` in `validation/validate_all.py` | Executes the fixtures |

No new input field is required. Events already carry `actor_id`, and the
GC9-S1 reconstruction shape already carries an optional `author_id` — both were
specified but never consumed by a derivation. GC9-S2 is the contract that reads
them. The fixture shape extends only `expected`, with `inherited`, `schism`,
and `non_derivation` alongside the existing GC9-S1 assertions.

## Visibility

| Surface | What appears |
|---|---|
| PLAY (`culture_lines`) | The two fixed lines, to **site accessors only**, exactly as GC9-S1 gates its lines |
| WATCH | Aggregate pulses only — `A practice has outlived its founders.` and `Practice at a site has divided.` No site named, no agent named, no counts |
| STUDY | Unchanged. No new research objective, no per-agent culture metric |

The WATCH pulses follow the GC9-S1 precedent: they report that *something of
this kind happened somewhere*, never where or to whom.

## Not in scope

Named here so later readers do not treat them as implied by this RFC.

| Deferred | Why |
|---|---|
| Taboos | Requires a prohibition primitive with enforcement and failure semantics — that is a governance contract, not a derivation |
| Symbols, names, memorials | Requires artifact-identity work (Slice D adjacency) and a naming path that does not become procedural generation |
| Founding accounts | Same, plus a provenance question about who may author one |
| Reform | Needs a distinction between reform and revival that current data cannot support |
| Costly public commitments | Needs existing resources/offices/agreements; a separate RFC with its own cost and failure model |
| Institutions inheriting a practice as an org | This RFC derives inheritance from *practitioners*. Binding a practice to an organization is a further step needing org-lifecycle rules for what happens when the org dissolves |

## Runtime authorization

None. Acceptance of this RFC authorizes runtime implementation of exactly the
two derived marks, their two play lines, and their two aggregate WATCH pulses —
nothing else in Slice A.
