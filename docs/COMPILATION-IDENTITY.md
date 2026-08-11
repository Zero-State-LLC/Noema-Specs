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
