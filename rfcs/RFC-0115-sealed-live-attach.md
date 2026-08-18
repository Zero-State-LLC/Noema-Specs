# RFC-0115 — Sealed live attach

## Status

**Accepted**

Specification for operator-non-injection on live agent attach. No new Player verbs. No `AGENT_PLAYER`. No Recover / Genesis. No private prompt text on the wire.

## Problem

S0–S2 withhold what **NOEMA** says to a Player. They do not stop the **operator** from coaching an agent (`--goal`, a custom system prompt, a play brief). That injection means the agent does not discover the world. The live game is broken.

RFC-0114 is already **LLM Controller propose**. This seal is RFC-0115.

## Proposed change

Accept AGENT-SEAL-S0. Live Perihelion is a sealed attach:

- Agent controllers on live MUST present a `prompt_version_hash` listed in [`sealed-prompt-catalog.s0.json`](../specs/sealed-prompt-catalog.s0.json)
- The hash is of the public file [`examples/sealed-prompt/s0.txt`](../examples/sealed-prompt/s0.txt). The prompt itself MUST NOT appear on the wire
- Isolated test worlds and human PLAY are not checked
- Official client MUST refuse `--goal`, `--prompt`, `--system`, and `--brief` before opening a socket
- Connect MUST NOT tell operators to drive a live agent token through `/play`

Authority: [AGENT-SEAL-S0.md](../docs/AGENT-SEAL-S0.md).  
Catalog: [`sealed-prompt-catalog.s0.json`](../specs/sealed-prompt-catalog.s0.json).

## Alternatives rejected

| Alternative | Why |
|-------------|-----|
| Honor-system official path only | Operator can still attach any runtime with a thesis |
| Detect coaching from first-session play | Easy to evade; does not prevent the break |
| Scan Admin / in-world mail | Changes Admin; still misses off-platform briefs |
| Read private prompts | Violates ADR-002 |

## Compatibility

Additive attach check. Isolated tester freedom unchanged. Human Chamber unchanged except that an **agent** token pasted into Advanced on live is `SEAL_REQUIRED` (principal, not page).

## Data / security

No new world fields, verbs, or events. Hash is a declaration, not world truth. Prompt text, `system_prompt`, and goal fields remain dropped. Tokens still never enter model context.

## Validation

`check_sealed_live_attach`: live matching hash ACCEPT; live missing `SEAL_REQUIRED`; live wrong `SEAL_MISMATCH`; isolated / human without hash ACCEPT; prompt text on wire REJECT; published prompt withhold ACCEPT; thesis planted in prompt REJECT; catalog hash matches file bytes.

## Rollback

Stop requiring the hash. S0–S2 withhold remains. Isolated and human PLAY remain.

## Unresolved

None for this slice. Third-party clients that send the published hash and use a different private prompt stay outside the boundary.
