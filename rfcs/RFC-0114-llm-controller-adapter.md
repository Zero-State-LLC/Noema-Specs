# RFC-0114 — LLM Controller adapter (v0.1)

## Status

**Accepted**

Specification for Controller-side propose. No new Player verbs. No `AGENT_PLAYER`. No Recover / Genesis.

## Problem

External LLM runtimes already attach as Controllers, but the propose step was unspecified. Without a fail-closed contract, adapters invent verbs, leak prompts into `POST /v1/command`, or treat agents as a separate Player class.

RFC-0034 is already **GC3-S2 WATCH public descriptor bands**. This adapter is RFC-0114.

## Decision

NOEMA does not gain a new mind. An LLM is a Controller. The model proposes `{action, target_id, arguments}`. The harness validates and transports. The World Engine decides.

Private cognition stays outside the gateway ([ADR-002](../adr/ADR-002-private-cognition-boundary.md)). Hosted ACT remains `POST /v1/command` (or isolated `/v1/operator/test-world/command`).

Normative document: [LLM-AGENT-INTEGRATION.md](../docs/LLM-AGENT-INTEGRATION.md).

## Consequences

- OpenAI-compatible / Anthropic / Grok / Ollama share one propose function.
- Observatory and WATCH still see only world-visible behavior.
- Manifest `prompt_version_hash` may be declared; the prompt MUST NOT.
- Runtime tests L01–L18 live in Noema `tests/test_llm_agent.py`.
