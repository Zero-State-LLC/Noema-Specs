# Machine-Contract Inventory Micro-Note (GC5–GC7) — Design Note

**Status:** Inventory note per GAME-COMPLETENESS-PLAN section 8. No invention.

**GC5:** delivery/latency model; rumor provenance schema; MESSAGE policy extension (if needed beyond existing).

**GC6:** mostly composition of Deep Time / contradiction (prefer reuse).

**GC7:** possible contest-config / catalog increment (no mutation of 0.2 here).

**Boundaries:** Lists only; no schemas created. Cites GAME-COMPLETENESS-PLAN.md section 8, RFC-0002, PR #305 + main.

Smallest unit (step 14 partial).

## Extension Points

Non-normative guidance for future maintenance; no new behavior is authorized here.

- **Inventory seam:** Future maintenance can annotate each GC5–GC7 candidate with the actual owning RFC, schema/catalog version, fixtures, and whether the need was closed or remains deferred. Preserve this as an inventory rather than creating duplicate delivery, provenance, contradiction, or contest contracts.
- **Promotion boundary:** Consult accepted GC5 delivery/rumor and GC7 contest slices before treating these early candidates as open. Reuse Deep Time for GC6 composition; a catalog increment follows explicit RFC change control, never mutation of event-catalog/0.2 in place.
- **Validation expectations:** Resolve inventory entries to concrete authority and positive/negative examples, check replay and exposure implications at each seam, and distinguish a candidate list from executable specification or hosted evidence. Missing machine coverage remains an identified dependency, not an invented schema.
