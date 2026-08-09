# Agent Protocol Fixtures

Positive and negative wire-level examples for `agent-protocol/v1`.

| File | Role |
|------|------|
| `hello-ok.json` | Compatible HELLO |
| `hello-incompatible.json` | Incompatible HELLO (must fail negotiation) |
| `error-no-compatible-protocol.json` | Expected ERROR shape |
| `act-cross-agent-forbidden.json` | Cross-agent ACT (must DENY) |
| `error-forbidden.json` | FORBIDDEN error |
| `act-look-idempotent.json` | Idempotent LOOK ACT |
| `reconnect-resume.json` | Resume AUTH after disconnect |
| `tool-denied-network.json` | Tool call blocked by deny-by-default egress |
| `error-tool-denied.json` | TOOL_DENIED error |
| `export-public-bundle-request.json` | Public export request (consent partition) |
| `operator-request-private-cognition.json` | Forbidden private cognition read |
| `error-private-cognition-forbidden.json` | PRIVATE_COGNITION_FORBIDDEN error |

These fixtures support `conformance/v0.1/` cases C01–C10.
