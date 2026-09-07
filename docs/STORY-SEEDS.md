# Story Seeds

Optional structural hints selected by an **admin** during Genesis.

Catalog: [`specs/story-seeds.v06.json`](../specs/story-seeds.v06.json)  
Schema: [`specs/story-seed.schema.json`](../specs/story-seed.schema.json)

## Invariant

> Story Seeds provide starting pressure and historical texture. They do **not** determine the future.

## Closed set (v0.6)

`FOUNDING_SPLIT` · `OLD_TRADE_NETWORK` · `FAILED_SETTLEMENT` · `RESOURCE_CRISIS` · `LOST_ARCHIVE` · `DISPUTED_SUCCESSION`

Example — `LOST_ARCHIVE` prefers: one old archive/record site, missing/incomplete evidence, at least one unresolved historical question.

Human-authored structured seeds only. No LLM/natural-language compiler requirement. No constraint solver.

## Extension Points

Non-normative future guidance; the existing authorities and frozen behavior remain unchanged.

Human-authored seed guidance can add examples of starting pressure and unresolved evidence within the six frozen v0.6 seed identities. Preserve admin-only Genesis selection and the absence of prescribed outcomes, a language compiler or a constraint solver. A new seed identity or changed machine constraints needs an explicit catalog/schema version decision and owning Genesis review. Validate examples against story-seed.schema.json and the pinned catalog, and demonstrate that generated starting conditions leave the historical question unresolved rather than scripting Player behavior.
