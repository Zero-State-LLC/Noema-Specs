# Security Policy

## Scope

This policy covers the NOEMA specification repository and the security requirements it imposes on implementation repositories. See [docs/SECURITY.md](docs/SECURITY.md) for the full threat model.

## Reporting

Report suspected vulnerabilities privately to repository maintainers. Do not publish exploit details until maintainers have triaged containment, data exposure, replay tampering, or key leakage risk.

## Baseline rules

- Do not commit real credentials, provider keys, private prompts, private agent metadata, or production datasets.
- Default game tools MUST NOT perform real-world destructive actions.
- Agent provider keys MUST NOT be exposed to agents or other participants.
- Research fixtures MUST be synthetic, consented, or explicitly licensed.
