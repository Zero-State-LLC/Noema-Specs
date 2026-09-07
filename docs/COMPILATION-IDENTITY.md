# Compilation Identity

## Rule

Changing any claim-bearing input creates a new compilation identity.

## Inputs that bind identity

- source trajectory (digest + versions)
- candidate interval
- target behavior (predicates + versions + claim label)
- equivalence boundary
- removable units
- dependency graph + closure rules version
- required controls
- perturbation space
- budgets
- policy context
- compiler version, replay version, oracle version
- canonicalization version (`noema-jcs/1`)
- capture defaults version
- corpus / schema bundle / provider-adapter identities

## Receipt

Every compilation (including unsuccessful statuses) emits a [phenomenon-compile-receipt](../specs/phenomenon-compile-receipt.schema.json) reusing RFC-0003 receipt/hash patterns. See [PHENOMENON-COMPILER.md](PHENOMENON-COMPILER.md) and [RFC-0003](../rfcs/RFC-0003-deterministic-contract-hardening.md).

## Digests

Content digests use RFC-0003 canonical serialization (`noema-jcs/1`). Do not invent Compiler-only hashing rules.

## Extension Points

Non-normative maintenance and integration guidance; the contracts cited above remain authoritative.

### Document-specific seam

Extend receipt comparison with a field-by-field explanation of which claim-bearing input caused a new compile identity. A research viewer may group source, boundary, controls, budgets, and toolchain identities while retaining the original receipt bytes.

### Compatibility and promotion

Reuse RFC-0003 noema-jcs/1 serialization; no Compiler-specific hash convention or COMPILE INTENT gameplay command is introduced. Compilation is a permissioned research workflow, not an agent-only entitlement. Localized labels and display formatting remain outside canonical digest inputs.

### Verification before adoption

Verify identical canonical inputs reuse identity, while changing source interval, boundary, defaults, policy, or compiler/oracle/replay version creates a new identity. Check unsuccessful statuses still have receipts. Include canonicalization and digest-field exclusion cases, and ensure comparisons never rewrite a prior receipt.
