# Agent Instructions

## Mission

Maintain the canonical NOEMA specification surface for a persistent science-fiction world that is instrumented for research. Player-facing presentation is game-first ([docs/PLAYER-BRAND.md](docs/PLAYER-BRAND.md)). Prefer durable contracts, machine-readable protocols, reproducible evidence, and implementation-neutral requirements. Do not implement runtime code in this repository.

For deterministic procedures for recurring specification work, see [SKILLS.md](SKILLS.md). This file remains the behavioral constraint surface.

Non-trivial RFCs and features are intent-first: start from [intent/README.md](intent/README.md) before `specify/spec.md` or an RFC draft.

## Required first actions

1. Read `CONTEXT.md` before editing.
2. Read `docs/TERMINOLOGY.md` and every affected subsystem document.
3. Inspect related protocols, schemas, examples, research files, and RFCs.
4. Check `git status` and avoid overwriting another contributor's work.

## Editing rules

- Use canonical terminology exactly.
- Do not invent protocol fields without a spec change and version review.
- Do not modify public schemas silently.
- Do not conflate OBSERVED, INFERRED, SPECULATIVE, or NOT_COMPUTABLE claims.
- Do not make unsupported consciousness or AGI claims.
- Do not create a scalar consciousness score.
- Reproducibility-critical changes require validation evidence.
- Protocol, schema, ontology semantics, reproducibility boundary, claims policy, and security boundary changes require the RFC process.
- Maintain backward compatibility where required.
- Avoid hidden coupling between subsystems.
- Prefer deterministic state transitions and explicit seeded nondeterminism.
- Preserve event provenance and lineage.
- Never commit real secrets, private prompts, or proprietary architecture details in fixtures.
- Update roadmap and versioning docs when changing milestones or version domains.
- Do not implement runtime code in this repository.

## SDLC

Non-trivial RFCs and features start here:

1. `intent.md` — copy [intent/_TEMPLATE.md](intent/_TEMPLATE.md); see [intent/README.md](intent/README.md).
2. `specify/spec.md` — include `## Workflows` (see [SKILLS.md](SKILLS.md)).
3. plan
4. implement (runtime repositories; not this specifications repository)

Clarifications, adapters, and docs-only hygiene that do not change contracts may skip this sequence. Do not invent intent records for existing RFCs.

## Escalation

If CI or validation looks wrong, open a labeled defect (`bug` or `type:bug`). Do not patch tests, fixtures, or validators to obtain a green result.

## Validation

Before finishing, run available repository validation, validate JSON syntax, inspect Markdown links, run `git diff --check`, and ensure the final tree still contains every required path.

<!-- graft:start -->
## Graft — repo context graph

This repo is indexed in `graft/`: small linked markdown nodes that explain each
system and carry exact file:line spans, kept in sync with the code through git.

For ANY task here — understanding how something works, finding where code lives,
or scoping a change — get context from the graph before grepping or opening
source files. Re-ask freely (it's cheap) and reuse literal identifiers you
already have (symbol, error string, file name) as the query. New to this repo?
Run `graft map` first — a token-budgeted orientation (dir clusters, hubs,
hotspots), no LLM, no key.

- Run `graft ask "<your question>" --source` → ranked nodes with the relevant
  code spans inlined (each hit's ≤8-line crux by default; `--full` for whole
  definitions when the crux isn't enough). Match the tool to the task shape:
  for understanding or editing, the top node IS the answer — cite its
  `covers:` file:line spans and edit straight from `--source`. For
  exhaustive tasks ("every occurrence / every caller of this pattern"), ranked
  results are top-N, not complete — run `graft grep "<literal>"` instead
  (exhaustive over indexed files, grouped by enclosing symbol), falling back
  to raw `grep -rn` only for unindexed files.
- `graft skeleton <file>` → every definition's signature + span, ~10× cheaper
  than reading the file; use it to skim an API surface.
- `graft callers <symbol>` gives precomputed, exact edges — who calls this.
  Add `--direction out` for what it calls, or `--depth N` to walk
  transitively for the full blast radius. For structural questions, skip
  ranking and use this directly.
- Or browse: `graft/INDEX.md` lists every node; follow the links.
- Monorepos and folders of multiple repos rank fairly across sub-projects —
  hits carry `[scope/]` labels naming which one they're from. Narrow with
  `graft ask "<task>" --in <scope>/` once you know where you're working.

If a returned span is truncated ("+N more lines"), open the file at that exact
range before finalizing. Only open source files when a node genuinely lacks a
needed detail, and then at the exact file:line the node points to — never
re-read whole files.

After big code changes, refresh the graph with `graft build` (deterministic,
no API key, $0).
<!-- graft:end -->

## Graft index: maintenance notes

[Graft](https://www.npmjs.com/package/@nanonets/graft) (`@nanonets/graft`) is a codebase-context graph for coding agents. It holds linked markdown cards with exact file:line spans, and agents query it with `graft ask` / `graft map` or over MCP.

- **Where it lives:** `graft/` is committed (`graft/INDEX.md` is the entry point). `graft/.cache/` stays local and gitignored.
- **Coverage:** Graft indexes code only, which here means the `validation/*.py` scripts (including the RFC-0126 watch-exposure check). **The Markdown specs are not indexed.** The watch specs live in `docs/WATCH.md`, `docs/WATCH-*.md`, `docs/GC3-S2-WATCH-PUBLIC.md`, `specify/watch-map-p0-gl-poi.md`, `rfcs/RFC-0126-watch-entity-update-exposure.md`, and `docs/evidence/gate-d-watch-where-2026-09-20/`. The runtime watch surface (Ruffian-L's area) is indexed in Zero-State-LLC/Noema under `workers/noema/src/watch*.ts` and `operator-watch.ts`.
- **Refresh (Node 22.12+):** `npm i -g @nanonets/graft`, then `graft build`, then commit the updated `graft/`. Opt out of telemetry with `graft telemetry disable`.
- **Check:** `graft check` fails if `graft/` is out of date with the code.
- **Agent wiring:** Cursor: `.cursor/rules/graft.mdc` and `.cursor/mcp.json` (`graft mcp`). Claude Code: run `graft init --no-global --agents claude` locally (`.claude/` and `.mcp.json` are gitignored here). AGENTS.md has a Graft section too.
