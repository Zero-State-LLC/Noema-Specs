# Direction Authority and Promotion

**Status:** governance authority for current state and future-work sequencing

## Authority order

Resolve conflicts in this order:

1. Accepted RFCs and ADRs
2. Versioned protocols, schemas, catalogs, and conformance fixtures
3. Subsystem specifications
4. Freeze and operational authorities
5. [`current-state.v1.yaml`](../specs/current-state.v1.yaml) for evidence-backed implementation-plane status
6. [ROADMAP.md](ROADMAP.md) and the active campaign for sequencing
7. Execution plans and examples

Planning chooses when work occurs. It does not change normative semantics.

## Status vocabulary

| Status | Meaning |
|---|---|
| LIVE_HOSTED | Deployed and acceptance-observed at noema.guru |
| IMPLEMENTED_RUNTIME | Implemented with runtime tests but not promoted through hosted acceptance |
| IMPLEMENTED_OFFLINE | Executable in the reference runtime but not hosted-equivalent |
| SPEC_COMPLETE | Normative behavior and conformance are settled |
| ACTIVE_INTEGRATION | Existing systems are being integrated into an outcome |
| NEXT | Next authorized work after the active gate |
| BLOCKED | Named prerequisites are incomplete |
| DEFERRED | Intentionally outside the active campaign |
| SPECULATIVE | Direction without implementation authority |
| RETIRED | No longer a valid product path |

“Done,” “complete,” and “implemented” must identify the plane they describe.

## Promotion rule

A capability moves between planes only with evidence:

```text
SPEC_COMPLETE
  → implementation + tests
IMPLEMENTED_RUNTIME
  → integrated acceptance + operational evidence
LIVE_HOSTED
```

Offline implementation does not imply Worker implementation. Worker implementation does not imply production deployment. Production deployment does not imply a research claim.

## Required metadata for direction work

Every new campaign or execution packet states:

- existing implementation and evidence commit;
- status and scope;
- authorities it depends on and does not replace;
- production-alpha delta;
- current-state entries affected;
- acceptance or exit gate;
- blocker and non-goals;
- superseded direction, if any.

## Supersession

When an accepted decision changes earlier prose, update live guidance and link to the new authority while preserving historical RFC problem statements and provenance. Never rewrite canonical world history merely to simplify documentation.

## Future-work admission

A task is authorized only if it closes the earliest unproven integration edge, exercises or safely promotes existing implementation, defines observable acceptance, and does not silently expand frozen semantics. Otherwise it remains an idea.
