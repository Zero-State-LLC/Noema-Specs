# Lesion Studies

Adapters may declare versioned `lesion_capabilities`, such as `memory.short_term`, `memory.long_term`, `planner`, `retriever`, `delegation`, `tool.browser`, and `tool.code`. A lesion requires that exact declaration, `AGENT_INTERNAL` authorization, isolated/reversible application, pinned adapter/component version, and audit. No provider/model/prompt metadata may imply a lesion capability. External removal is an ablation. Unsupported lesion requests are retained `NOT_COMPUTABLE`; the fixture is schema-only, not fabricated execution.
