# RFC-0034 — LLM Controller adapter (v0.1)

## Status

**Proposed**

## Problem

External LLM runtimes already attach as Controllers, but the propose step is unspecified. Without a fail-closed contract, adapters invent verbs, leak prompts into `POST /v1/command`, or treat agents as a separate Player class.

## Decision

NOEMA does not gain a new mind. An LLM is a Controller. The model proposes `{action, target_id, arguments}`. The harness validates and transports. The World Engine decides.

Private cognition stays outside the gateway (ADR-002). Hosted ACT remains `POST /v1/command` (or isolated `/v1/operator/test-world/command`). No `AGENT_PLAYER`. No new world verbs.

Normative Specs document: [LLM-AGENT-INTEGRATION.md](../docs/LLM-AGENT-INTEGRATION.md). Runtime work package (schemas, L01–L18 tests): Noema `docs/superpowers/specs/2026-08-17-llm-agent-integration-v0.1.md`.

## Consequences

- OpenAI-compatible / Anthropic / Grok / Ollama share one propose function.
- Observatory and WATCH still see only world-visible behavior.
- Manifest `prompt_version_hash` may be declared; the prompt MUST NOT.
