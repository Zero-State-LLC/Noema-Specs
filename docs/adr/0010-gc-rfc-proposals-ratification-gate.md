# ADR-0010: GC1–GC10 RFC Proposal Ratification Gate

- **Status:** Accepted
- **Date:** 2026-11-25
- **Scope:** `rfcs/RFC-PROPOSAL-GC*.md` (GC1, GC2, GC4, GC7, GC8, GC9, GC10)

## Context

`Noema-Specs` contains 13 bounded `RFC-PROPOSAL-GC*.md` draft proposals derived from design seeds and `SPEC-GAP-REGISTER-2026-08-25.md`. Previously, these proposals had no machine-checked registry or uniform ratification gate, making it easy for draft proposals to drift from their seed docs or be implemented ad hoc without Gate C evidence.

## Decision

1. **Machine-checked registry**: All `rfcs/RFC-PROPOSAL-GC*.md` files are registered in `specs/gc-rfc-proposals.v1.json` and validated on every CI run by `tools/check_gc_proposals.py`.
2. **Draft-by-default membrane**: Every proposal stays `status: "draft"` (research/design input only, zero mutation to frozen `v0.1`–`v0.7` or live `world.perihelion-reach-3` rules) until explicitly promoted.
3. **Promotion checklist**: Moving any proposal from `draft` to `accepted` requires:
   - Gate C empirical or scenario evidence justifying the bounded parameter/surface extension,
   - A versioned JSON Schema under `specs/` + positive/negative conformance fixtures under `examples/`,
   - Zero new superuser privileges and zero regression on frozen `v0.1`–`v0.7` conformance,
   - Explicit status update in both the RFC file and `specs/gc-rfc-proposals.v1.json`.

## Consequences

- CI immediately fails if a new `RFC-PROPOSAL-GC*.md` is added without registry metadata or if a referenced seed doc is removed.
- Contributors and agents have one canonical, machine-readable index of all 13 GC proposals and their exact promotion prerequisites.
