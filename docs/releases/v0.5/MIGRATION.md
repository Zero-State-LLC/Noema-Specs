# v0.5 Compiler: Migration

## From v0.4 Lab

```text
v0.4 Lab Result (compiler_readiness: READY)
  → v0.5 CaptureIntent
  → CompilationRequest
  → CapturedTest (+ receipt, audit, regression surface)
```

## Compatibility

- Lab experiments/results/candidates are **immutable inputs**.
- No rewrite of world ledgers or Observatory records.
- Existing experience `CAPTURE_AS_TEST` action remains the ordinary trigger; v0.5 supplies the executable destination contracts.
- Capture defaults are versioned (`capture-defaults/0.5.0`). Changing defaults creates a new defaults identity and therefore a new compilation identity when claim-bearing.

## Rollback

Dropping v0.5 leaves v0.4 READY handoffs intact; no Lab mutation is required.
