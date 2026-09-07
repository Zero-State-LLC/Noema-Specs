# v0.7 LEARN: Architecture Delta

```text
gameplay
  → events / research artifacts (Lab, Compiler, regression)
  → derived LEARN projection (behavior nodes + edges)
  → simple / advanced STUDY views
```

- Graph updates **after** research artifacts settle (not PLAY hot path)
- Projection rebuildable from immutable source evidence
- Ordinary modular-monolith storage (relational/document + indexes) is sufficient
- No Neo4j, dedicated graph service, vector DB, or stream processor required

## Progressive disclosure

Same edges at four levels (simple → reproducibility). See [LEARN.md](../../LEARN.md).

## Extension Points

Non-normative guidance for future maintenance; no new behavior is authorized here.

- **Projection seam:** Extend rebuild and invalidation examples for settled Lab, Compiler, and regression artifacts feeding the existing LEARN graph. Simple-to-reproducibility views can add detail while resolving the same nodes, edges, and evidence references.
- **Compatibility boundary:** Projection-rule changes need an identified version and comparison against the prior rebuild. They must not introduce a PLAY hot-path dependency, a second evidence store, or a required graph service; schema/edge changes belong to CAPABILITY-GRAPH authority.
- **Validation expectations:** Rebuild from immutable sources after cache deletion, ignore unsettled artifacts, and compare stable node/edge identities and tested boundaries. Exercise excluded or superseded evidence and verify simple views do not retain unsupported relationships or turn not-tested contexts into failures.
