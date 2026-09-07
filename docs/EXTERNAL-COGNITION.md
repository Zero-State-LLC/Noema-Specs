# External Cognition Signals (v0.3)

Observable artifacts agents create and reuse:

ledgers · journals · maps · procedures · checklists · shared archives · protocols · memory institutions · structured message conventions

## Detection (deterministic heuristics)

| Signal | Evidence |
|--------|----------|
| `artifact_create_reuse` | ENTITY_CREATE DOCUMENT/ARTIFACT + repeated INSPECT/MESSAGE reference |
| `shared_ledger_use` | multi-agent MESSAGE/TRADE citing same entity |
| `procedure_protocol` | DOCUMENT with procedure markers + repeated COMMIT/org use |

Do not infer private internal memory deficiency. Emit signals + capability candidates for Lab testing.

## Extension Points

Non-normative guidance for future work; existing authorities and closed-slice boundaries remain unchanged.

- **Seam and invariants.** Additional artifact-use heuristics can enrich the signal inventory when each names observable creation, reuse and citation evidence. Preserve the distinction between an external artifact signal and a claim about private cognition or memory deficiency.
- **Compatibility and validation.** Pin heuristic and evidence-schema versions alongside source event references; test repeated references, distinct agents, absent reuse and inaccessible documents. Promote capability candidates through Lab testing rather than treating a heuristic hit as a validated capability or Player reward.
