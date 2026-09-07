# Lesion Studies

Adapters may declare versioned `lesion_capabilities`, such as `memory.short_term`, `memory.long_term`, `planner`, `retriever`, `delegation`, `tool.browser`, and `tool.code`. A lesion requires that exact declaration, `AGENT_INTERNAL` authorization, isolated/reversible application, pinned adapter/component version, and audit. No provider/model/prompt metadata may imply a lesion capability. External removal is an ablation. Unsupported lesion requests are retained `NOT_COMPUTABLE`; the fixture is schema-only, not fabricated execution.


## Extension Points

Non-normative guidance for future maintenance; this section changes no current behavior or promotion status.

- Adapter documentation can add exact, versioned lesion_capabilities declarations and evidence of reversible application to the named component. Keep capability declaration distinct from provider/model metadata; externally removing a tool remains an ablation unless the lesion contract actually applies.

- A newly supported component or changed adapter behavior needs a versioned declaration and explicit AGENT_INTERNAL authorization scope. Existing plans retain their pinned adapter/component boundary; schema-valid fixtures alone never promote a capability to executed support.

- Prospective validation should pair an authorized declared lesion with undeclared, unauthorized, and non-reversible requests, and verify restoration plus audit lineage. Retain unsupported outcomes as NOT_COMPUTABLE and report absent execution evidence rather than substituting a synthetic successful run.
