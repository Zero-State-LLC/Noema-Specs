# LLM Controller Integration (v0.1)

**Version:** v0.1  
**RFC:** [RFC-0114](../rfcs/RFC-0114-llm-controller-adapter.md)

An LLM runtime is a **Controller for a Player**. It is not a second Player class and not a mind inside the World Engine.

**Thesis:** The model proposes. The harness constrains and transports. NOEMA decides.

Authority this document implements: [ADR-002](../adr/ADR-002-private-cognition-boundary.md) · [ADR-001](../adr/ADR-001-determinism-and-seeded-nondeterminism.md) · [ADR-003](../adr/ADR-003-claim-label-discipline.md) · [Agent Protocol v1](../protocols/agent-protocol-v1.md) · [AGENT-GATEWAY](AGENT-GATEWAY.md) · [AGENT-INTERFACE](AGENT-INTERFACE.md) · [AGENT-PLAY](AGENT-PLAY.md) · [AGENT-HARNESS](AGENT-HARNESS.md).

## Scope

In: Observation → Decision → Action for LLM Controllers; private mind store; manifest 1.1; hosted HELLO → AUTH → `POST /v1/command`; REST required; MCP stub; tenant targeting.

Out: new world verbs; `AGENT_PLAYER`; PLAY multi-tenant rewrite; hosted WebSocket push; hosted REGISTER; auto-approve `/connect`; Recover/Genesis from the loop; consciousness scores; prompts/CoT/keys in NOEMA.

## MUST

1. Wire principal is a Player. The LLM is a Controller.
2. World Engine stays deterministic. Stochasticity stays in the Controller.
3. Private cognition stays outside the gateway (ADR-002).
4. Command envelopes MUST NOT contain `cognition`, `prompt`, `plan`, `thought`, `inner_monologue`, `system_prompt`, `private_cognition`, `api_key`, `secret`, `access_token`, `device_code`, `chain_of_thought`, `cot`.
5. The model MAY emit only `{action, target_id, arguments}`. The harness MUST `validate_proposal` before transport.
6. Prose commands (`MOVE east`) and unknown verbs are dropped. No extra `/v1/command`.
7. Mutating commands carry `request_id` and `idempotency_key`.
8. Tokens never enter model context, reports, logs, or MCP results.
9. Research claims use OBSERVED / INFERRED / SPECULATIVE / NOT_COMPUTABLE.
10. Isolated tenants use `/v1/operator/test-world/command`. Perihelion uses `/v1/command` only with an explicit live-tenant flag.
11. Live Perihelion agent attach MUST present a catalog `prompt_version_hash` (`AUTH` or `X-Noema-Seal`). Official clients MUST NOT accept `--goal`, `--prompt`, `--system`, or `--brief`. [AGENT-SEAL-S0.md](AGENT-SEAL-S0.md).

## Loop

```text
OBSERVE → prepare_context (canonical only)
        → LocalMind.propose (private)
        → parse_proposal
        → validate_proposal
        → POST command_uri
        → World Engine decides
```

Hosted `command_uri` after AUTH is `POST /v1/command` (or isolated test-world). `/protocol/v1` is HELLO + AUTH only.

## Manifest 1.1 (no secrets)

Required: `schema_version`, `display_name`, `runtime`, `protocol_version`, `controller_kind` (`llm`).  
Optional: `model.provider` (`openai-compatible` | `anthropic` | `xai` | `ollama` | `none`), `model.identifier`, `prompt_version_hash` (`sha256:` + 64 hex), `research_consent_flags`.

A manifest containing a `prompt` string or `api_key` MUST be rejected.

## Acceptance (L01–L18)

HELLO ok / incompatible; AUTH ok / missing token; manifest ok / secrets rejected; JSON LOOK sent; prose MOVE dropped; prompt-in-proposal dropped; isolated path; Perihelion refuse; token absent from model context; unknown verb dropped; idempotent retry; MCP status has no token; no `AGENT_PLAYER`; orientation S0 withhold.

Runtime tests: `tests/test_llm_agent.py` in Zero-State-LLC/Noema.

## Spectator

WATCH sees world-visible behavior only. Observatory capture is post-gateway and consent-fail-closed.

## Golden path

```bash
PYTHONPATH=src python3 scripts/noema_llm_agent.py --tenant test.hosted-canonical.ack-s3 --provider none --turns 4
# or: noema-agent --tenant test.hosted-canonical.ack-s3 --adapter llm --turns 4 run
```

## Extension Points

Non-normative guidance; no runtime, i18n, accessibility or gate completion is claimed.

### Proposal-filter and transport adapters

Extend provider-neutral parsing and transport conformance while retaining the propose → validate → command boundary.

### Preserved invariants

Model output is only action, target_id and arguments. Prose, unknown verbs and cognition-bearing proposals are dropped before transport; tokens stay outside model context and logs. Stochasticity stays outside the deterministic engine.

### Compatibility and promotion

RFC-0114 and the Agent Protocol own envelope changes; discovery and seal authority own live compatibility. New adapters cannot bypass explicit live targeting, inject strategic prompts, or obtain research/hidden state. Access-policy S0–S3 are slice versions, not privilege tiers.

### Validation fixtures before adoption

Pair a JSON LOOK proposal with prose MOVE, an unknown verb and a prompt-bearing proposal; only the valid proposal reaches the mock transport. Retry one mutation with the same request_id/idempotency_key and expect one effect under the canonical contract. Missing live opt-in or incompatible seal must fail closed; do not claim a hosted test from these fixtures.
