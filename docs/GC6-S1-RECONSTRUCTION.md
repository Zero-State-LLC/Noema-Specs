# GC6-S1 — Historical Reconstruction

**Status:** Executable specification. Runtime authorized with RFC-0024.  
**Parent:** [GC6-FIRST-SLICE.md](GC6-FIRST-SLICE.md) · [SYSTEMIC-DISCOVERY.md](SYSTEMIC-DISCOVERY.md) · [HISTORICAL-RECONSTRUCTION.md](HISTORICAL-RECONSTRUCTION.md)  
**RFC:** [RFC-0024](../rfcs/RFC-0024-historical-reconstruction.md)  
**Does not open:** `QUEST` · oracle · `event-catalog/0.3` · tradition · rumor · Chamber help advertising

S1 is the smallest increment that still satisfies scenario F’s *compile* shape: a Player records an interpretation from evidence they can actually access.

---

## Doctrine

```text
CANONICAL HISTORY
≠ ACCESSIBLE EVIDENCE
≠ PLAYER RECONSTRUCTION
≠ RESEARCH INTERPRETATION
```

| Temptation | Verdict |
|------------|---------|
| `QUEST` / `SOLVE_MYSTERY` / `DISCOVER_TRUTH` | **REJECT** |
| Engine resolves DESTROYED vs OPERATING | **REJECT.** Record `CONTESTED` |
| v0.6 compiler schema as PLAY object | **REJECT.** That schema is compiler output |
| Confidence scalar | **REJECT** |
| Hidden event id as evidence | **REJECT** |
| Tradition score | **DEFER** (GC9-S1) |

Pressures: **uncertainty** (accounts may be incomplete or contested) and **dependency** (you can only cite what you inspected).

---

## Model

A reconstruction is an Information record owned by its author. It is not WorldState geography and not ledger truth.

| Field | Meaning |
|-------|---------|
| `reconstruction_id` | Stable `recon.<hex>` |
| `author_player_id` | Author |
| `subject_ref` | Entity or named subject |
| `claim` | Author account (bounded text) |
| `evidence_refs[]` | Provenanced accessible items |
| `created_cycle` | Create cycle |
| `supersedes_reconstruction_id` | Prior record, if any |
| `status` | `RECORDED` \| `SUPERSEDED` |
| `visibility` | `PRIVATE` \| `INSTITUTIONAL` \| `PUBLIC` |
| `epistemic` | `CONTESTED` if cited archive and inspect disagree; else `OPEN` |
| `org_id` | Required when `INSTITUTIONAL` |

Lifecycle:

```text
RECORDED → SUPERSEDED
```

Supersede appends a new record. The prior record stays readable and becomes `SUPERSEDED`. No destructive rewrite.

v0.6 [`historical-reconstruction.schema.json`](../specs/historical-reconstruction.schema.json) remains the compiler/research output. This slice does not emit that digest.

---

## Evidence

Hosted S1 kinds (must already be accessible to the author):

| Kind | Access gate | Epistemic label |
|------|-------------|-----------------|
| `ARCHIVE_CLAIM` | Author `INSPECT`ed an `ARTIFACT` that already has `archive_subject_entity_id` + `archive_claim` | `RECORDED` |
| `LIVE_INSPECT` | Author `INSPECT`ed the subject entity | `OBSERVED` |

Catalog also names later kinds (`INSTITUTION_NOTICE`, `PUBLIC_RECONSTRUCTION`) but hosted S1 does not accept them.

Each ref stores: `kind`, `subject_ref`, `source_entity_id`, `label` (`DESTROYED`/`OPERATING` where applicable), `cycle`.

Forbidden as evidence: hidden event log, research telemetry, admin state, private messages the author cannot read, backend-only canonical fields, other-world ids.

If archive claim and live inspect disagree, `epistemic=CONTESTED`. That is a valid reconstruction, not a reject.

---

## Operations

| Operation | COMMIT | Evidence |
|-----------|--------|----------|
| Record | `RECONSTRUCT` | `ENTITY_CREATE` (`DOCUMENT`, `location=null`) |
| Revise | `RECONSTRUCT_SUPERSEDE` | `ENTITY_CREATE` (new) + `ENTITY_UPDATE` (prior → `SUPERSEDED`) |
| Publish | `RECONSTRUCT_PUBLISH` | `ENTITY_UPDATE` visibility |

Human adapters (not help): `reconstruct …`, `revise …`.

### Preconditions

| Check | Fail |
|-------|------|
| Author not in world | `NOT_FOUND` |
| Subject missing | `NOT_FOUND` |
| Any evidence ref inaccessible / unknown kind | `FORBIDDEN` |
| Cross-world ref | `FORBIDDEN` |
| Research/admin/hidden class | `FORBIDDEN` |
| Empty claim | `INVALID_REQUEST` |
| `INSTITUTIONAL` without membership office/founder/officer | `FORBIDDEN` |
| Supersede another Player’s `PRIVATE` record | `FORBIDDEN` |
| Publish a record you do not own | `FORBIDDEN` |

Publication does **not** grant archive/inspect access to readers.

Institutional publication uses existing GC4 grants (founder/officer, or any held office). It does not invent an Archivist-only engine and does not need GC4 TRADE/REPAIR.

---

## Projection

Author (and `PUBLIC` readers; `INSTITUTIONAL` members) may see:

```text
Reconstruction: {subject}
Based on: {n} accessible sources
Account: {claim}
Status: Contested | Recorded
```

Never: `known_truth`, quest complete, “what really happened”, mystery score.

WATCH: public reconstructions may show subject + status + author handle. No research partition.

---

## A–J

| Test | Result |
|------|--------|
| A | Information primitive. No quest species |
| B | Uncertainty + dependency |
| C | COMMIT operations; no frozen new verb |
| D | Feeds later tradition without implementing it |
| E | No top-level `RECONSTRUCT` in frozen contracts |
| F | An archive+inspect habit can form |
| G | Evidence refs are accessible inspect/attest items |
| H | Human and agent identical |
| I | Meaningful with STUDY hidden |
| J | Without this, contradiction has no compiled account |

---

## Out of S1

```text
QUEST / JOURNAL / DISCOVER_TRUTH
event-catalog/0.3
tradition scores (GC9-S1)
rumor (GC5-S2)
WATCH contradiction pulse
institution TRADE/REPAIR
automatic LLM historian
```
