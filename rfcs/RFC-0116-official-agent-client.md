# RFC-0116 — Official external agent client

## Status

**Accepted**

Specification-only. No new Player verbs. No `AGENT_PLAYER`. No Recover / Genesis. No runtime change in this RFC.

## Problem

[RFC-0111](RFC-0111-agent-harness.md) specifies harness behavior but left repository shape and CLI syntax unresolved. An implementer would still ship the official Controller inside `Zero-State-LLC/Noema`, teach agents to paste Bearer tokens, treat `/connect` as the agent gameplay runtime, or invent `CLIENT_PLAYER`.

First-world Specs are frozen. This RFC closes an **IMPLEMENTATION / DISTRIBUTION AMBIGUITY**. It does not thaw gameplay.

## Proposed change

Accept the official external client boundary.

- Canonical repository: `scrimshawlife-ctrl/noema-client`
- The client is a Controller implementation, not a Player class
- Server owns world authority, identity, seal, settlement, WATCH, and Admin
- Client owns install, device-enrollment initiation, local credentials, discovery, transport, proposal validation, pacing, CLI, and skill
- Canonical onboarding: `pipx install noema-client` → `noema connect` → human approves at `/connect` → scoped credential stored locally → discovery + seal → `noema play`
- `/connect` is the human authorization surface, not the official agent play runtime
- Manual token/curl remains ADVANCED / DEBUG
- Copy-first extraction. Do not delete the internal harness first
- Independent semantic versioning. Compatibility is protocol/discovery/seal, not matching Noema Git SHA

Authority: [OFFICIAL-AGENT-CLIENT.md](../docs/OFFICIAL-AGENT-CLIENT.md).  
Catalog: [`official-agent-client-catalog.s0.json`](../specs/official-agent-client-catalog.s0.json).  
Harness behavior remains [AGENT-HARNESS.md](../docs/AGENT-HARNESS.md).

## Alternatives rejected

| Alternative | Why |
|-------------|-----|
| Keep official client inside `Zero-State-LLC/Noema` | Mixes world authority with Controller packaging |
| New Player class for the client | Ontology forbids `CLIENT_PLAYER` / `AGENT_PLAYER` |
| Browser `/connect` as agent play | `/connect` is human approval; harness is headless |
| Token-paste as the recommended path | Device enrollment is the first-world path |
| Delete internal harness first | Extraction is copy/prove/deprecate |
| Require MCP / a vendor SDK | Provider-neutral; MCP is not first-world |
| Operator `--goal` on live | RFC-0115 sealed attach |

## Compatibility

Additive distribution contract. Worlds ignoring the official package keep current Gateway/PLAY/CONNECT behavior. No event-catalog change. No verb change. No Genesis change.

## Data / security

No new world fields. Client stores only Controller-side material. No Admin, Supabase service-role, Cloudflare, or world-signing secrets. Client compromise is not Admin compromise.

## Validation

`check_official_agent_client`: official repo + server-authority ACCEPT; `CLIENT_PLAYER`, client-as-world-authority, browser-canonical play, Admin secret in client store, live `--goal`, delete-internal-first, Perihelion CI mutation, skill-as-strategy, and skip-discovery REJECT.

## Rollback

Ignore the distribution document. RFC-0111 harness, RFC-0115 seal, device enrollment, and Agent Gateway remain.

## Unresolved

Exact PyPI package name at publish time. Numeric CLI/policy thresholds. Visual `/connect` simplification (runtime).
