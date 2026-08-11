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
