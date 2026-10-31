# Contributing

## Requirement language

Use MUST, SHOULD, and MAY for normative requirements. Each critical behavior SHOULD include an observable acceptance check.

## RFC-required changes

An RFC is required for changes to protocols, schemas, ontology semantics, reproducibility boundaries, claims policy, security boundaries, version domains, or dataset immutability rules.

## Workflow

For repeatable workflows for specification changes, RFCs, schemas, fixtures, conformance, validation, and continuation analysis, see [SKILLS.md](SKILLS.md). This document remains the contribution-policy surface.

1. Read `CONTEXT.md` and affected docs.
2. Identify impacted protocols, schemas, examples, research files, security boundaries, and versions.
3. Draft changes with stable IDs, explicit lineage, and claim labels.
4. Validate JSON syntax, examples, links, terminology, and `git diff --check`.
5. Update `CHANGELOG.md`, `docs/VERSIONING.md`, and `SPEC-CHECKLIST.md` when contracts move.

Reviewers, human or agent (including `/code-review`), check changes against this file and [SPEC-CHECKLIST.md](SPEC-CHECKLIST.md). Use the vocabulary in [GLOSSARY.md](GLOSSARY.md).

## Style

Avoid hype, unsupported AGI language, and consciousness claims. Prefer precise MUD, protocol, research, replay, and containment language.


## Licensing and contributions

This repository uses the Zero State Proprietary License v1.0 (ZSPL-1.0) for original Zero State materials. See [`LICENSE`](LICENSE) and [`LICENSE_POLICY.md`](LICENSE_POLICY.md).

Contributions are limited to authorized Zero State contributors and agents unless a separate written agreement is approved. Zero State may require a contributor license agreement, intellectual-property assignment, work-for-hire agreement, or other written agreement before accepting an external contribution. Do not add third-party code or assets without documenting their license and preserving required notices.

## Graft context index

[Graft](https://www.npmjs.com/package/@nanonets/graft) (`@nanonets/graft`) is a codebase-context graph for coding agents. It holds linked markdown cards with exact file:line spans, and agents query it with `graft ask` / `graft map` or over MCP.

- **Where it lives:** `graft/` is committed (`graft/INDEX.md` is the entry point). `graft/.cache/` stays local and gitignored.
- **Coverage:** Graft indexes code only, which here means the `validation/*.py` scripts (including the RFC-0126 watch-exposure check). **The Markdown specs are not indexed.** The watch specs live in `docs/WATCH.md`, `docs/WATCH-*.md`, `docs/GC3-S2-WATCH-PUBLIC.md`, `specify/watch-map-p0-gl-poi.md`, `rfcs/RFC-0126-watch-entity-update-exposure.md`, and `docs/evidence/gate-d-watch-where-2026-09-20/`. The runtime watch surface (Ruffian-L's area) is indexed in Zero-State-LLC/Noema under `workers/noema/src/watch*.ts` and `operator-watch.ts`.
- **Refresh (Node 22.12+):** `npm i -g @nanonets/graft@0.26.0`, then `GRAFT_NO_GITIGNORE=1 graft build`, then commit the updated `graft/`. Without `GRAFT_NO_GITIGNORE=1`, graft appends `/graft/` to `.gitignore`; validation fails if that line lands. Opt out of telemetry with `graft telemetry disable`.
- **CI:** the `build` job runs `graft build --check` pinned to the same version, so a stale index fails the PR.
- **Check:** `graft check` (or `graft build --check`) fails if `graft/` is out of date with the code.
- **Agent wiring:** Cursor: `.cursor/rules/graft.mdc` and `.cursor/mcp.json` (`graft mcp`). Claude Code: run `graft init --no-global --agents claude` locally (`.claude/` and `.mcp.json` are gitignored here). AGENTS.md has a Graft section too.
