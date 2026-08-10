# Deployment fixtures

Reference non-secret configuration and runtime identity for the v0.1 modular-monolith golden path.

| File | Purpose |
|------|---------|
| `local-deployment-config.json` | Resolved non-secret deployment config (schema: `deployment-config.schema.json`) |
| `local-runtime-manifest.json` | Instance identity / version pinning (schema: `runtime-manifest.schema.json`) |
| `docker-compose.reference.yml` | Normative local compose *shape* for the runtime repo |
| `verify-pass.example.txt` | Successful `noema verify` output |

See [docs/QUICKSTART.md](../../docs/QUICKSTART.md), [docs/DEPLOYMENT.md](../../docs/DEPLOYMENT.md), and [docs/OPERATIONS.md](../../docs/OPERATIONS.md).

## Configuration digest

`configuration_digest` is `sha256:` + hex of the UTF-8 bytes of the **canonical JSON** of a document that validates against `specs/deployment-config.schema.json`:

1. Resolve environment into a non-secret object (never include `AUTH_SECRET`, `DATABASE_URL` password, provider keys, storage secrets, etc.).
2. Validate against `deployment-config.schema.json`.
3. Serialize with sorted object keys, no insignificant whitespace, UTF-8.
4. Hash with SHA-256; prefix with `sha256:`.

Example digests in fixtures are placeholders unless a runtime publishes a pinned value.
