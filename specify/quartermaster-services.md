# Quartermaster office services

**Status:** Accepted with [RFC-0133](../rfcs/RFC-0133-quartermaster-treasury-services.md).
**Kind:** World-rule amend (institution office capability).
**Date:** 2026-11-25
**Intent:** [Quartermaster office services](../intent/2026-11-25-quartermaster-services.md).
**Version domains:** No version change. `RESOURCE_TRANSFER` (event-types 0.2) is reused unchanged.

## Workflows

- **SKILL.ORIENT** — authority is RFC-0029 (institution treasury) and the office profiles in GC4-S1.
- **SKILL.SPEC_CHANGE** — one RFC, one machine catalog, one validator check.
- **SKILL.REVIEW** — authority boundary (office, not controller), treasury bounds, WATCH silence.
- **SKILL.VALIDATE** — `python3 validation/validate_all.py`, graft index fresh.
- **Owner specialist:** World Engine economy.
- **Existing Action:** repository CI; no new workflow.

## Requirements

1. Only the Agent Player holding an OCCUPIED `OPERATE_RESOURCE_ACCOUNT` office, named by `acting_for` + `office_id`, may treasury-harvest or SUPPLY. Office conflict rules apply.
2. Treasury harvest credits treasury `storage`. The vault never exceeds `treasury_storage_cap` (64).
3. SUPPLY moves an integer 1..5 of `energy` or `storage` from the treasury to another entered Agent Player in the actor's room. Energy never exceeds 80: a SUPPLY that would is refused, not clamped. Cargo needs free storage in the recipient's hold.
4. SUPPLY emits one `RESOURCE_TRANSFER` that validates against event-types 0.2: `transfer_id`, `from_id` (org), `to_id`, `resource`, `amount`.
5. WATCH stays silent for SUPPLY.

## Acceptance evidence for the runtime slice

- Engine tests: treasury harvest with a full pack; vault cap; non-holder refused; SUPPLY energy and cargo; self, over-cap, empty-treasury and non-holder refused; holder-only affordances.
- Live: a seated quartermaster's treasury grows and the custodian receives cargo.

## Amendment 1: treasury construction (2026-11-25)

- The resource-office holder may `BUILD CONSTRUCT` a **generator** or **storage_bay** with `acting_for` + `office_id`.
- The cargo cost comes out of the treasury vault. The actor pays the rest (energy, compute). The built entity is owned by the organization.
- Any other class, a short vault, or a non-holder: refused, and nothing moves.
- Verification: engine vitest `RFC-0133 amendment 1`, plus `check_rfc_0133` cases.
