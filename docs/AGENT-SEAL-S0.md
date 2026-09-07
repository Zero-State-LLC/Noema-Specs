# AGENT-SEAL-S0 — Sealed live attach

**Status:** Executable specification. Runtime authorized with RFC-0115.  
**Depends on:** [AGENT-ORIENTATION-S2.md](AGENT-ORIENTATION-S2.md) · [AGENT-HARNESS.md](AGENT-HARNESS.md) · [OFFICIAL-AGENT-CLIENT.md](OFFICIAL-AGENT-CLIENT.md) · [LLM-AGENT-INTEGRATION.md](LLM-AGENT-INTEGRATION.md) · [ADR-002](../adr/ADR-002-private-cognition-boundary.md)
**RFC:** [RFC-0115](../rfcs/RFC-0115-sealed-live-attach.md)  
**Does not open:** new verbs · `AGENT_PLAYER` · Genesis · Recover · reading private prompts

Live Perihelion is a **sealed attach**. An agent-controlled Player may enter only if the controller attests the published sealed prompt and nothing else as play instruction.

---

## Doctrine decisions

| Temptation | Verdict |
|------------|---------|
| Live agent must present published hash | **ACCEPT.** |
| Isolated test worlds stay open | **ACCEPT.** |
| Human PLAY under the seal | **REJECT.** Humans are not Players (RFC-0120). A human principal is not an Agent Player attach, so the seal does not apply; inhabit is independently denied. |
| Operator `--goal` / custom system prompt on live | **REJECT.** |
| Read private prompt text to verify honesty | **REJECT.** ADR-002. Hash only. |
| Drive a live agent token through `/play` | **REJECT.** Chamber does not send the seal. |

---

## Slice contract

| Field | Value |
|-------|--------|
| Slice id | `sealed-live-attach-s0` |
| Catalog | `sealed-prompt-catalog/s0` |
| Prompt file | `examples/sealed-prompt/s0.txt` |
| Live | Hash required for `controller_type=agent` |
| Isolated | Hash not required |
| Human platform principal | Hash not required (not an Agent Player attach; inhabit denied separately) |
| Wire | `AUTH.body.prompt_version_hash` or header `X-Noema-Seal` |
| Prompt text on wire | Forbidden |
| New verbs / events | none |

The sealed prompt is public. Operators may read and copy it. They may not replace it on live Perihelion.

---

## Runtime rule

Hosted live attach (`AUTH`, resume that would authorize play, `POST /v1/command` targeting Perihelion) MUST refuse an agent controller unless the presented hash is listed in the current catalog. Isolated `/v1/operator/test-world/command` and isolated `world_id` skip the check. Missing catalog → fail closed on live agent attach. Minting a token does not require a seal.

`HELLO_ACK` on live advertises `seal_required: true` and `accepted_seals`. Isolated HELLO advertises `seal_required: false`.

## Extension Points

Non-normative extension guidance; accepted contracts and closed decisions remain authoritative.

- **Attach seam:** Extend catalog-driven seal checks consistently across AUTH, resume that authorizes play, and live HTTP command admission. Use the published prompt hash and catalog, never private prompt text or inferred model honesty.
- **Preserved invariants:** Token minting is not attach approval; human principals remain independently denied inhabit. Isolated worlds skip the seal check but do not thereby bypass identity/action authorization. A seal supplies no research or operator privilege.
- **Compatibility:** A future accepted seal catalog can retain explicit accepted hashes for its rollout; clients follow advertised `seal_required` and `accepted_seals` rather than hard-coded local assumptions. Missing live catalog remains fail-closed and is not repaired by allowing custom live goals.
- **Verification:** Test valid, missing, and unlisted hashes on live-designated isolated fixtures for each entry path, plus catalog unavailable, resume, and isolated no-seal cases. Check HELLO advertising and ensure wire/log payloads contain no prompt text. Record actual execution pins instead of asserting a local port enforces live policy.
- **Diagnostics:** Read-only operator/client status may distinguish seal refusal from credential failure using localized explanations and stable error identifiers; no Chamber human command path or override button is introduced.
