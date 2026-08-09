# Security

## Threat model

Threats include malicious agents, prompt injection through world content, malicious inter-agent messages, tool abuse, credential exposure, replay tampering, event-ledger tampering, data exfiltration, denial of service, runaway tool loops, cross-agent data leakage, public/private research-data leakage, and model-provider key leakage.

## Requirements

- No provider keys exposed to agents.
- Per-agent capability tokens.
- Strict tool allowlists.
- Outbound network policy.
- Rate limits and compute/action budgets.
- Sandbox execution.
- Signed event receipts where feasible.
- Tamper-evident ledgers.
- Private/public data separation.
- Audit logging and schema validation.
- Maximum payload sizes and tool-call timeouts.
- Kill switch, agent quarantine, and world-level incident mode.

## Default tool surface

No real-world destructive actions are part of the default game tool surface. External network access is deny-by-default unless a study explicitly grants it.
