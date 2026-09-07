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

## Extension Points (additive, i18n AX R3 Gate B handoff + COMPILATION / CAPTURE)

- **i18n centralization (STRINGS + t())** for "compilation identity", "source trajectory", "candidate interval", "target behavior", "equivalence boundary", "dependency graph", "perturbation space", "policy context", "compiler version", "replay version", "oracle version", "canonicalization version", "capture defaults version", "phenomenon-compile-receipt", "RFC-0003", "noema-jcs/1", "Compiler-only hashing". R3 agent evidence compilation + human S0.
- **Gate B S0-S3 + R3**: Agent-only Player (RFC-0120) for compilation; version comps; human S0 observation.
- **AX**: Semantic tables/lists for inputs/digests/receipts; ARIA roles, keyboard nav for study/compilation views, live regions for status, contrast per omh-audit. CDP proxy for live.
- **Plugin atoms**: For compilation packs (derive identity, validate receipt/digest, load_pack, atomic_replace); Chamber atoms for receipt viewers, digest tools.
- **LCA2/MUD handoff**: MUD native for `COMPILE INTENT` / parser i18n terms; cross to CAPTURE-INTENT-COMPILATION, PHENOMENON-COMPILER, PLAYER-ACTION-MAP, AGENT-*, graft for savings.
- **Cross-refs**: PHENOMENON-COMPILER.md, RFC-0003, GAME-COMPLETENESS, PLAYER-ACTION-MAP, AGENT-ORIENTATION/PLAY/DETERMINISM/GATEWAY, AUTH-AND-IDENTITY, PLATFORM, NOEMA-HIGH-VALUE-ACTIONS-ELEVATION-PLAN, noema-specs-mud-craft, 8765/ui i18n, graft, prior EPs (CAPTURE/DIPLOMACY/ECONOMIC/DEEP-TIME/EMERGENT + full list).
- All real outputs. Additive. Ready for Chamber i18n in study/capture surfaces.
