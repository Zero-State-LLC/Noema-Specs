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

## Extension Points

Non-normative guidance for future maintenance; no new behavior is authorized here.

- **Migration seam:** Extend worked migrations from immutable READY Lab results through CaptureIntent and CompilationRequest to CapturedTest, retaining receipt/audit references and the source experiment identity. Include old capture-defaults/0.5.0 inputs rather than assuming current defaults.
- **Compatibility boundary:** Claim-bearing default changes create new defaults and compilation identities; never rewrite an existing captured test or upstream Lab record to make it resemble a newer run. Dropping the Compiler leaves the READY handoff and its evidence intact.
- **Validation expectations:** Compare repeat compilation under the same pins, changed defaults under a new identity, non-READY refusal, and rollback with upstream records unchanged. Verify provenance, exclusions, source digests, and regression references survive conversion without mutating world ledgers or Observatory candidates.
