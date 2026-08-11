# Negative / Invalid Examples

These fixtures are intentionally non-conforming. Schema and catalog validators MUST reject them.

| Fixture | Why it fails |
|---------|----------------|
| `invalid-manifest-missing-required.json` | Missing required `display_name` (minimal identity incomplete) |
| `invalid-world-event-unknown-type.json` | `event_type` not in closed 24-type catalog |
| `invalid-world-event-missing-digest.json` | Missing required `digest` on world-event envelope |
| `invalid-move-payload-missing-fields.json` | MOVE payload missing `from_room_id`, `to_room_id`, `cost_paid` |
| `invalid-world-event-mismatched-payload.json` | Event type `MOVE` carries a LOOK-shaped payload and fails catalog-specific payload binding |
| `invalid-budget-exceeded-not-exceeding.json` | `requested` is not greater than `available` |
| `invalid-observation-claim-label.json` | Claim label outside OBSERVED / INFERRED / SPECULATIVE / NOT_COMPUTABLE |
| `invalid-org-create-empty-members.json` | `initial_members` empty (minItems: 1) |
| `invalid-runtime-manifest-missing-ledger-head.json` | Missing required `ledger_head` |
| `invalid-deployment-config-secret-field.json` | Secret field `auth_secret` rejected by `additionalProperties: false` |
| `invalid-resource-negative-balance.json` | `BUDGET_CONSUMED.remaining` &lt; 0 |
| `invalid-world-state-missing-lineage.json` | Canonical WorldState missing replay-critical catalog, revision, canonicalization, and hash fields |
| `invalid-spectator-mutates-world.json` | `mutates_world` must be `false` |
| `invalid-compiler-result-unknown-status.json` | Compiler status outside COMPILED/NOT_COMPUTABLE/INVALID_EVIDENCE/INCONCLUSIVE/ABORTED/BUDGET_EXHAUSTED |
| `invalid-captured-test-missing-title.json` | Captured test missing required `title` |
| `invalid-capture-intent-wrong-action.json` | `capture_intent` not `CAPTURE_AS_TEST` |
| `invalid-regression-implies-global-rank.json` | `not_a_global_ranking` must be `true` |

Positive fixtures live under `examples/v01-seed/`, `examples/v01-strategic/`, `examples/catalog/`, `examples/onboarding/`, `examples/deployment/`, `examples/v05-compiler/`, and `examples/sample-*.json`.
