# GC9-S2 — Practice inheritance and schism

**Authority:** [RFC-0125](../rfcs/RFC-0125-practice-inheritance-and-schism.md) (Accepted).
**Extends:** [GC9-S1-TRADITION.md](GC9-S1-TRADITION.md) / [RFC-0025](../rfcs/RFC-0025-tradition.md).
**Catalog:** `specs/culture-catalog.gc9-s2.json`.

GC9-S2 is the upper half of the culture ladder named in
[RESEARCH-ASSIMILATION-2026-08-21.md](RESEARCH-ASSIMILATION-2026-08-21.md)
Slice A: a practice that **outlives its founders**, and practitioners who
**divide over what it means**. Both are derived. Neither is a religion engine.

## What is derived

Two marks, computed only when the GC9-S1 status is `TRADITION` or `REVIVED`.

| Mark | Holds when | Line |
|---|---|---|
| inherited | A repair by a non-originator occurs at a cycle strictly later than the last originator repair | `This site's maintenance tradition has outlived its founders.` |
| schism | Two `PUBLIC` accounts of the site carry distinct claims and are authored by two distinct agents who both repaired it | `Practitioners of this site keep rival accounts.` |

Originators are the distinct actors of the first `originator_repairs` (3)
repairs in `(cycle, sequence)` order.

## Why the strictness

**Inheritance is not co-practice.** A second agent repairing alongside the
founders has joined the practice, not inherited it. The mark requires the
practice to continue *after* the founders stop. `concurrent-practice-not-inheritance`
pins this: vesper repairs at cycle 4, nacre continues to cycle 6, and the
tradition is not inherited.

**Schism is not disagreement.** GC9-S1 already reports `Accounts of this site
differ.` when two public claims diverge. That is a difference between accounts.
A schism is a division among *practitioners*, so the rival accounts must be
authored by people who actually did the work. Two accounts by one practitioner
are a revision; two accounts by bystanders are commentary. Both are excluded,
and both keep the GC9-S1 competing line.

## What it is not

No deity or supernatural-truth entity. No belief meter, faithfulness score,
conversion, or divine reward. No procedural lore generation — every line is a
fixed catalog string. No gameplay bonus of any kind. No ledger write: a rival
account changes nothing about the relay it describes.

## Privacy

Attribution derives the marks and is never surfaced by them. The play lines
name no originator, no successor, and no account holder, and expose no
per-agent practice count. `check_gc9_s2` asserts this on every fixture by
scanning the projected lines for each fixture's own actor handles.

WATCH receives aggregate pulses only — `A practice has outlived its founders.`
and `Practice at a site has divided.` — naming no site and no agent, following
the GC9-S1 pulse precedent.

## Determinism

Repairs are ordered by `(cycle, sequence, event_id)`. The originator set is the
first three distinct actors in that order. There is no random tie-break and no
implicit stream, per [ADR-008](../adr/ADR-008-replay-conformance-and-deterministic-hardening.md).

## Fixtures

`examples/gc9-schism/`, executed by `check_gc9_s2`. Ten fixtures cover both
positive marks and all five non-derivation reasons, and the check fails if any
reason in the catalog is never exercised.
