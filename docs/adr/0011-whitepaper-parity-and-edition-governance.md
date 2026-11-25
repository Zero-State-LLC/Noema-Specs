# ADR-0011: Whitepaper Working Edition Parity and Governance

- **Status:** Accepted
- **Date:** 2026-11-25
- **Supersedes:** Whitepaper Working Edition 0.1 (`2026-08-24`) status claims
- **Authority Alignment:** `specs/current-state.v1.yaml`, `ADR-0009`, `ADR-0010`

## Context

The public whitepaper served at `https://noema.guru/NOEMA-Comprehensive-Whitepaper.docx` (Working Edition 0.1, `24 August 2026`) lagged the live runtime by three months: it described `GC1`–`GC10` as "Specified in staged form", the civilizational runtime as "Not implemented", `WATCH` visual maps as "FUTURE WORK", and `STUDY` simply as a "Stub".

## Decision

1. **Whitepaper Working Edition 0.2 (`25 November 2026`)**:
   - Aligns Section 7 (`Current State`), Section 9 (`WATCH`), and `Appendix A — Status Matrix` with `specs/current-state.v1.yaml` and live Worker `f5233592-3479-4382-b684-05ca0bb28e7d` (`world.perihelion-reach-3`).
   - Records `GC1`–`GC10` core slices and `LCA Gates A–F` as `LIVE_HOSTED` / `COMPLETE`, `WATCH` (`TEXT` / `PIXEL` / `MAP` + Phosphor) as `OBSERVED`, `StudyAdminDO` (`RFC-0131`) + Cloudflare Access as `LIVE_HOSTED`, and the hosted `STUDY` pipeline as `BLOCKED` on human `PSR-1` / `PSR-2` evidence (`ADR-0009`).
   - Preserves all core doctrine, provenance labels (`OBSERVED` / `INFERRED` / `SPECULATIVE` / `NOT_COMPUTABLE`), barter-first internal economy, and `DEFERRED` external crypto economy status.
2. **Parity Rule**:
   - `specs/current-state.v1.yaml` remains the machine-checked authority; future whitepaper editions must not contradict `current-state.v1.yaml` or claim `LIVE_HOSTED` for `BLOCKED`, `DEFERRED`, or `SPECULATIVE` capabilities.

## Consequences

- Public readers and external agents downloading the whitepaper from `noema.guru` see an accurate, provenance-labeled snapshot of the live system.
- `Noema-Specs` records the exact parity baseline in `ADR-0011`.
