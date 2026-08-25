# RFC-0032 — Resend Auth Email Delivery

## Status

**Accepted — sole hosted delivery adapter**

Resend is the sole hosted Worker-composed delivery adapter for this specification. Supabase Auth remains the token authority and fallback mailer.

```text
SUPABASE AUTH = TOKEN AUTHORITY + TOKEN VERIFICATION + FALLBACK DELIVERY
RESEND        = SOLE HOSTED WORKER-COMPOSED MESSAGE DELIVERY
NOEMA WORKER  = LINK COMPOSITION + PLAYER/ADMIN POLICY + PROVIDER ADAPTER
```

This RFC supersedes the prior provider-selection decision for RFC-0032. No alternate hosted email provider is specified.

## Problem

The hosted auth flow generates one-time links through Supabase Auth and sends Worker-composed messages for PLAY and privileged ADMIN access. The specification needs one authoritative hosted provider, with identity and delivery responsibilities kept separate.

## Decision

The hosted Worker MUST use Resend for Worker-composed PLAY and ADMIN magic-link messages when `RESEND_API_KEY` is configured.

1. The Worker calls Supabase Auth `admin/generate_link` before composing a provider-delivered message.
2. The Worker constructs the existing `/play/callback` or `/admin/callback` URL.
3. The Worker sends the existing HTML and text bodies through `POST https://api.resend.com/emails`.
4. The Resend API key MUST be a Worker secret named `RESEND_API_KEY`.
5. The sender MAY be overridden with `RESEND_FROM_EMAIL`; otherwise the existing verified PLAY and ADMIN sender identities are preserved. Deployments MUST verify every sender address or domain used.
6. PLAY and ADMIN MUST use distinct provider tags or equivalent metadata: `play-magic-link` and `admin-magic-link`.
7. The public login-request responses MUST remain generic and MUST NOT disclose provider configuration or delivery outcome.
8. Missing Resend configuration or Resend delivery failure MUST preserve the existing fallback behavior: PLAY falls back to Supabase `/otp`; ADMIN falls back to the existing Cloudflare mail binding when available, then Supabase `/otp`.

## Scope

In scope:

- Worker-composed PLAY and ADMIN magic-link mail
- the Resend API delivery adapter
- configuration, deployment documentation, and validation
- delivery-result validation and secret-safe errors

Out of scope:

- changing callback, token verification, allowlist, throttling, JWT, or session semantics
- changing the temporary Cloudflare ADMIN mail fallback
- delivery webhooks or a durable retry queue
- world events, gameplay protocols, schemas, or research evidence

## Provider contract

Request:

```http
POST https://api.resend.com/emails
Authorization: Bearer <secret>
Content-Type: application/json
Accept: application/json
```

Required JSON fields:

```json
{
  "from": "NOEMA <access@noema.guru>",
  "to": ["player@example.com"],
  "subject": "Enter NOEMA",
  "html": "<html>...</html>",
  "text": "...",
  "tags": [{"name": "flow", "value": "play-magic-link"}]
}
```

The ADMIN variant uses the ADMIN sender/display name, subject, bodies, recipient policy, and `admin-magic-link` metadata value.

The adapter MUST accept a response as successful only when HTTP status is 2xx and the provider returns a non-empty message identifier. Errors MUST NOT include the API key, key hash, callback URL, complete message body, or recipient mailbox.

## Configuration

| Variable | Required hosted | Secret | Default | Purpose |
|----------|-----------------|--------|---------|---------|
| `RESEND_API_KEY` | yes for hosted delivery | yes | none | Authenticates Resend API requests |
| `RESEND_FROM_EMAIL` | no | no | existing per-message sender | Optional verified sender override for both auth messages |

`RESEND_API_KEY` MUST NOT appear in repository variables, browser code, health output, exception text returned to callers, or agent credentials.

## Security and compatibility

- Supabase remains authoritative for generating and verifying single-use tokens.
- Resend receives the requested mailbox and temporary callback URL solely to deliver the authentication message.
- ADMIN and Player credentials remain separate. ADMIN delivery occurs only after the allowlist check, and callback consumption rechecks the allowlist.
- Public endpoints, callback URLs, templates, and JWT contracts are unchanged.
- Deployments without Resend retain their current fallback path.

## Failure behavior

| Failure | Required behavior |
|---------|-------------------|
| ADMIN mailbox not allowlisted | Return generic success; call neither Supabase nor Resend |
| Supabase link generation fails | Do not call Resend; continue through the existing fallback behavior |
| Resend not configured | Use the existing provider fallback |
| Resend rejects sender/message | Treat as failed send and use the existing provider fallback |
| Resend network failure | Treat as failed send and use the existing provider fallback |
| Link consume fails | Mint no Player or ADMIN JWT |

## Acceptance checks

1. PLAY and allowlisted ADMIN requests use Supabase `generate_link` followed by Resend `/emails` when `RESEND_API_KEY` is configured.
2. Requests use bearer authorization, both message bodies, and the correct PLAY/ADMIN metadata value.
3. A missing provider message identifier, non-2xx response, and missing key all fail closed at the adapter boundary.
4. Existing Supabase and Cloudflare fallback behavior remains covered.
5. No alternate hosted email provider, alternate provider endpoint, or alternate provider deployment instruction remains in the specification.
6. Existing callback verification, ADMIN JWT, Player/Admin isolation, throttling, and template-content tests pass.
7. Focused type checking for changed email files MUST introduce no new diagnostics. The repository-wide typecheck SHOULD pass; any pre-existing unrelated baseline failures MUST be recorded rather than attributed to this migration.

## Migration

1. Verify the configured `noema.guru` sender or domain in Resend.
2. Store `RESEND_API_KEY` as a Cloudflare Worker secret.
3. Optionally set `RESEND_FROM_EMAIL`.
4. Deploy the Worker and test PLAY and ADMIN magic-link requests.
5. Record successful provider message identifiers without recording links or recipient addresses.

## Rollback

Remove `RESEND_API_KEY` or disable the adapter. The existing Supabase delivery path and temporary Cloudflare ADMIN binding remain available. Do not introduce another hosted provider without a new decision.

## Unresolved

Durable retries, delivery webhooks, bounce suppression policy, and retirement of the remaining fallback paths are separate follow-ups.
