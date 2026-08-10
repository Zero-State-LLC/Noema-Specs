# Negative / Invalid Examples

These fixtures are intentionally non-conforming. Schema and catalog validators MUST reject them.

| Fixture | Why it fails |
|---------|----------------|
| `invalid-manifest-missing-required.json` | Missing required `display_name` (minimal identity incomplete) |
| `invalid-world-event-unknown-type.json` | `event_type` not in closed 24-type catalog |
| `invalid-world-event-missing-digest.json` | Missing required `digest` on world-event envelope |
| `invalid-move-payload-missing-fields.json` | MOVE payload missing `from_room_id`, `to_room_id`, `cost_paid` |
| `invalid-budget-exceeded-not-exceeding.json` | `requested` is not greater than `available` |
| `invalid-observation-claim-label.json` | Claim label outside OBSERVED / INFERRED / SPECULATIVE / NOT_COMPUTABLE |
| `invalid-org-create-empty-members.json` | `initial_members` empty (minItems: 1) |
| `invalid-runtime-manifest-missing-ledger-head.json` | Missing required `ledger_head` |
| `invalid-deployment-config-secret-field.json` | Secret field `auth_secret` rejected by `additionalProperties: false` |

Positive fixtures live under `examples/v01-seed/`, `examples/onboarding/`, `examples/deployment/`, and `examples/sample-*.json`.
