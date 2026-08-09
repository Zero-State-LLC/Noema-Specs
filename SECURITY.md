# Security Policy

## Scope

This repository defines the Noema protocols, schemas, datasets, and acceptance
contracts. Security issues may therefore be defects in the specification itself,
in reference data, or in an implementation that follows the specification.

The detailed threat model and normative containment requirements are in
[`docs/SECURITY.md`](docs/SECURITY.md). The required security verification is in
[`docs/TESTING.md`](docs/TESTING.md).

## Reporting a vulnerability

Do not open a public issue for a suspected vulnerability that could expose a
secret, private dataset content, an exploitable parser or protocol flaw, or a
containment bypass.

Use GitHub's **Report a vulnerability** flow on the Security tab of this
repository. Include, when available:

- the affected document, schema, protocol version, or implementation;
- the security property that is violated;
- minimal reproduction steps or a reduced fixture;
- likely impact and preconditions;
- whether the report contains personal, proprietary, or regulated data; and
- a safe contact method for follow-up.

Do not include live credentials, access tokens, private user content, or an
unredacted production dataset. Replace them with synthetic values.

Maintainers should acknowledge a report within **5 business days**, provide an
initial assessment within **10 business days**, and coordinate disclosure after
a fix or mitigation is available. These are response targets, not guarantees.

## Supported versions

Until a stable release exists, only the latest revision of the `main` branch
and the latest tagged v0.x release receive specification security fixes. A
superseded draft may be unsafe even when its schema identifier is still valid.

## Safe-harbor expectations

Good-faith research that avoids privacy violations, persistence, destructive
actions, service disruption, and access beyond what is necessary to demonstrate
the issue is welcome. Stop testing and report immediately if you encounter real
secrets, personal data, or evidence of unauthorized access.

## Public security discussions

Public issues are appropriate for hardening proposals that do not disclose an
active weakness. Maintainers may move a report to a private channel when public
discussion would materially increase risk.
