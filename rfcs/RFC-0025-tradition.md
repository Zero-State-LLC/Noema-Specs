# RFC-0025 — GC9-S1 Tradition

## Status

**Accepted**

Closes the GC9-S0 tradition SPEC GAP. A tradition is a derived recognition of persistent, transmitted practice. It is not canonical history, not a bonus, and not a lore engine.

## Problem

[EMERGENT-CULTURE.md](../docs/EMERGENT-CULTURE.md) and [RFC-0013](RFC-0013-maintenance-custom.md) left tradition, decay, and institution adoption as SPEC GAP. An implementer would invent `CREATE_TRADITION`, a culture score, or write lore into the ledger.

## Proposed change

Accept GC9-S1:

```text
CANONICAL HISTORY ≠ PRACTICE ≠ CUSTOM ≠ TRADITION ≠ CULTURAL INTERPRETATION
```

- Extends GC9-S0 `CUSTOM`. Does not replace it. Does not auto-promote every custom.
- Derived rebuildable projection. No new table. No `CULTURE_*` / `TRADITION_*` events. No new top-level verb.
- Tradition when a site already has `CUSTOM` **and** (practice spans ≥ 3 distinct cycles with ≥ 2 accessors **or** ≥ 2 public reconstructions cite the site).
- Status: `TRADITION` → `DORMANT` after 8 cycles without repair/inspect → `REVIVED` when practice resumes after such a gap.
- Competing public reconstructions may coexist; neither rewrites the ledger.
- Grants no authority, access, XP, or cheaper repair.
- WATCH may pulse a **public** tradition or a **public contested reconstruction** without private evidence or `known_truth`.

Catalog: [`culture-catalog.gc9-s1.json`](../specs/culture-catalog.gc9-s1.json).  
Slice: [GC9-S1-TRADITION.md](../docs/GC9-S1-TRADITION.md).

## Alternatives rejected

| Alternative | Why |
|-------------|-----|
| `CREATE_TRADITION` / `RITUAL` | Verb inflation; practice is existing `REPAIR` |
| Auto-promote every custom | S0 custom is weaker persistence |
| Culture / civilization score | Research coupling |
| Holiday / religion engine | Out of slice |
| Tradition as WorldState | Would compete with the ledger |
| WATCH as truth oracle | `known_truth` stays research-only |

## Compatibility

Additive. GC9-S0 custom line unchanged below the tradition threshold. Frozen catalogs unchanged. GC6-S1 reconstructions remain interpretations.

## Data / security

Rebuildable cache on WorldRuntime culture + public reconstruction records. Private reconstructions and research labels are not recognition evidence. Cross-world refs rejected by existing world isolation.

## Validation

`check_gc9_s1`: custom does not become tradition from one actor/one cycle; tradition after persistence + transmission; dormant/revived; competing public accounts; no bonus; no ledger rewrite; WATCH pulse has no private/research tokens.

## Rollback

Omit the tradition projection. GC9-S0 custom remains.

## Unresolved

Institution TRADE/REPAIR, emergency scopes, designated succession, rumor, v0.6C.
