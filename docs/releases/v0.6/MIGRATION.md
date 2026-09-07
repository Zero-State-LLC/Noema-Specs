# v0.6 Deep Time: Migration

## From prior worlds

v0.6 **adds** history-derived structures. It MUST NOT rewrite existing world history.

Derive institution/history indexes, artifact records, and historical views **only** where source evidence supports them.

If historical evidence is insufficient:

```text
NOT_COMPUTABLE
```

Do **not** fabricate backstory for old worlds. Fixtures may provide test histories; they are not future live-world canon.

## Compatibility

- Organizations (`ORG_*`) remain valid membership containers.
- Institutions may reference source orgs without replacing them.
- Event catalog versions 0.1/0.2 unchanged by this package.

## Extension Points

Non-normative future guidance; this section grants no new behavioral authority and does not reopen accepted or deferred slices.

- **Seam:** Migration examples can cover sparse old histories, org-linked institution indexes, and repeatable historical-view rebuilds.
- **Unchanged invariants:** No fabricated backstory or rewritten world history; insufficient evidence remains NOT_COMPUTABLE, ORG_* membership containers survive, and event catalogs 0.1/0.2 remain unchanged.
- **Compatibility, promotion, and verification:** New derivation semantics require explicit version and evidence requirements before promotion. Verify old histories retain their digests and unsupported institution/artifact claims are absent; test fixtures never become future live-world canon.
