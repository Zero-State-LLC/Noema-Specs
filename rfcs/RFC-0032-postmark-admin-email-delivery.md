# RFC-0032 — Postmark Auth Email Delivery

## Status

**Accepted**

Replaces Resend as the hosted Worker's preferred transactional provider for Worker-composed PLAY and ADMIN magic-link mail. Supabase Auth remains the identity-proof, magic-link-token, and fallback delivery authority. The existing Cloudflare ADMIN mail binding remains a temporary fallback.

## Problem

The hosted auth flow generates one-time links through Supabase Auth and currently sends Worker-composed messages through Resend when `RESEND_API_KEY` is configured. This makes the runtime, deployment scripts, and operator documentation depend on a provider that is no longer preferred.

The identity and delivery responsibilities must remain separate:

```text
SUPABASE AUTH = TOKEN AUTHORITY + TOKEN VERIFICATION + FALLBACK DELIVERY
POSTMARK      = PREFERRED WORKER-COMPOSED MESSAGE DELIVERY
NOEMA WORKER  = LINK COMPOSITION + PLAYER/ADMIN POLICY + PROVIDER ADAPTER
```

## Decision

The hosted Worker MUST use Postmark instead of Resend for Worker-composed PLAY and ADMIN magic-link messages.

1. The Worker calls Supabase Auth `admin/generate_link` before composing a provider-delivered message.
2. The Worker constructs the existing `/play/callback` or `/admin/callback` URL.
3. The Worker sends the existing HTML and text bodies through `POST https://api.postmarkapp.com/email`.
4. The Postmark server token MUST be a Worker secret named `POSTMARK_SERVER_TOKEN`.
5. The sender MAY be overridden with `POSTMARK_FROM_EMAIL`; otherwise the existing verified PLAY and ADMIN sender identities are preserved. Deployments MUST verify every sender address or domain used.
6. The message stream MAY be configured as `POSTMARK_MESSAGE_STREAM`; it defaults to `outbound`.
7. PLAY and ADMIN MUST use distinct Postmark tags: `play-magic-link` and `admin-magic-link`.
8. The public login-request responses MUST remain generic and MUST NOT disclose provider configuration or delivery outcome.
9. Missing Postmark configuration or Postmark delivery failure MUST preserve the existing fallback behavior: PLAY falls back to Supabase `/otp`; ADMIN falls back to the existing Cloudflare mail binding when available, then Supabase `/otp`.
10. Resend code, configuration, tests, and operational instructions MUST be removed.

## Scope

In scope:

- Worker-composed PLAY and ADMIN magic-link mail
- replacement of the Resend adapter with a Postmark API adapter
- configuration, deployment scripts, documentation, and tests
- delivery-result validation and secret-safe errors

Out of scope:

- changing callback, token verification, allowlist, throttling, JWT, or session semantics
- Postmark inbound mail, templates, broadcasts, or marketing streams
- changing the temporary Cloudflare ADMIN mail fallback
- delivery webhooks or a durable retry queue
- world events, gameplay protocols, schemas, or research evidence

## Provider contract

Request:

```http
POST https://api.postmarkapp.com/email
X-Postmark-Server-Token: <secret>
Content-Type: application/json
Accept: application/json
```

Required JSON fields:

```json
{
  "From": "NOEMA <access@noema.guru>",
  "To": "player@example.com",
  "Subject": "Enter NOEMA",
  "HtmlBody": "<html>...</html>",
  "TextBody": "...",
  "MessageStream": "outbound",
  "Tag": "play-magic-link"
}
```

The ADMIN variant uses the ADMIN sender/display name, subject, bodies, recipient policy, and `admin-magic-link` tag.

The adapter MUST accept a response as successful only when HTTP status is 2xx, `ErrorCode` is `0`, and `MessageID` is a non-empty string. Errors MUST NOT include the server token, token hash, callback URL, complete message body, or recipient mailbox.

## Configuration

| Variable | Required hosted | Secret | Default | Purpose |
|----------|-----------------|--------|---------|---------|
| `POSTMARK_SERVER_TOKEN` | yes for preferred delivery | yes | none | Authenticates Postmark server API requests |
| `POSTMARK_FROM_EMAIL` | no | no | existing per-message sender | Optional verified sender override for both auth messages |
| `POSTMARK_MESSAGE_STREAM` | no | no | `outbound` | Transactional message stream |

`POSTMARK_SERVER_TOKEN` MUST NOT appear in repository variables, browser code, health output, exception text returned to callers, or agent credentials.

## Security and compatibility

- Supabase remains authoritative for generating and verifying single-use tokens.
- Postmark receives the requested mailbox and temporary callback URL solely to deliver the authentication message.
- ADMIN and Player credentials remain separate. ADMIN delivery occurs only after the allowlist check, and callback consumption rechecks the allowlist.
- Public endpoints, callback URLs, templates, and JWT contracts are unchanged.
- Deployments without Postmark retain their current fallback path.

## Failure behavior

| Failure | Required behavior |
|---------|-------------------|
| ADMIN mailbox not allowlisted | Return generic success; call neither Supabase nor Postmark |
| Supabase link generation fails | Do not call Postmark; continue through the existing fallback behavior |
| Postmark not configured | Use the existing provider fallback |
| Postmark rejects sender/message | Treat as failed send and use the existing provider fallback |
| Postmark network failure | Treat as failed send and use the existing provider fallback |
| Link consume fails | Mint no Player or ADMIN JWT |

## Acceptance checks

1. PLAY and allowlisted ADMIN requests use Supabase `generate_link` followed by Postmark `/email` when `POSTMARK_SERVER_TOKEN` is configured.
2. Requests use `X-Postmark-Server-Token`, both message bodies, `outbound` by default, and the correct PLAY/ADMIN tag.
3. A nonzero Postmark `ErrorCode`, missing `MessageID`, non-2xx response, and missing token all fail closed at the adapter boundary.
4. Existing Supabase and Cloudflare fallback behavior remains covered.
5. No `RESEND_API_KEY`, Resend endpoint, Resend source file, or Resend deployment instruction remains.
6. Existing callback verification, ADMIN JWT, Player/Admin isolation, throttling, and template-content tests pass.
7. Focused type checking for changed email files MUST introduce no new diagnostics. The repository-wide typecheck SHOULD pass; any pre-existing unrelated baseline failures MUST be recorded rather than attributed to this migration.

## Migration

1. Verify the configured `noema.guru` sender or domain in Postmark.
2. Create or select a transactional `outbound` message stream.
3. Store `POSTMARK_SERVER_TOKEN` as a Cloudflare Worker secret.
4. Optionally set `POSTMARK_FROM_EMAIL` and `POSTMARK_MESSAGE_STREAM`.
5. Deploy the Worker and test PLAY and ADMIN magic-link requests.
6. Record successful Postmark MessageIDs without recording links or recipient addresses.
7. Remove `RESEND_API_KEY` from the Worker after Postmark delivery is verified.

## Rollback

Remove `POSTMARK_SERVER_TOKEN` or revert the adapter. The existing Supabase delivery path and temporary Cloudflare ADMIN binding remain available. Do not restore Resend without a new decision.

## Unresolved

Durable retries, delivery webhooks, bounce suppression policy, and retirement of the remaining fallback paths are separate follow-ups.
