# Domain Docs

How the engineering skills should consume this repo's domain documentation.

**Layout: single-context.** One root `GLOSSARY.md` and one `docs/adr/`.

## Before exploring, read these

- **`GLOSSARY.md`** at the repo root: canonical NOEMA vocabulary.
- **`CONTEXT.md`** at the repo root: authority order and non-negotiable invariants. In this repo `CONTEXT.md` is **not** a legacy glossary. Never rename it to `GLOSSARY.md` or merge it into the glossary.
- **`docs/adr/`**: read ADRs that touch the area you're about to work in.
- **`rfcs/`**: Accepted RFCs outrank ADRs, schemas, and docs for their stated scope. Check affected RFCs before proposing a decision.

If any of these files don't exist, **proceed silently**.

## File structure

```
/
├── CONTEXT.md        ← authority and invariants (not a glossary)
├── GLOSSARY.md       ← domain vocabulary
├── SKILLS.md         ← repo-specific SKILL.* procedures
├── docs/adr/
│   ├── README.md     ← ADR index
│   ├── 0001-determinism-and-seeded-nondeterminism.md
│   └── 0008-replay-conformance-and-deterministic-hardening.md
├── rfcs/
├── intent/ → specify/ ← SDLC for non-trivial features (see AGENTS.md)
└── specs/, protocols/, conformance/, examples/, validation/
```

This is a specifications-only repository. Runtime code lives in `Zero-State-LLC/Noema`. Code-implementation skills (`tdd`, `implement`, `implement-spec`, `diagnosing-bugs`, `improve-codebase-architecture`) target that repo, not this one. The only code here is `validation/*.py`.

## ADR conventions

- File name: `docs/adr/NNNN-slug.md`, numbered by scanning for the highest number.
- Title line: `# ADR-NNN: {title}` (three digits). Existing docs cite ADRs as `ADR-001`…`ADR-008`; keep that citation form.
- Sections: `Status`, then `Context` / `Decision` / `Consequences` (Nygard). Add the new row to `docs/adr/README.md`.
- An ADR never overrides an Accepted RFC. A decision that changes a protocol, schema, ontology, claims, or security boundary needs an RFC, not only an ADR.

## Use the glossary's vocabulary

When your output names a domain concept (an issue title, a spec section, a fixture ID), use the term as defined in `GLOSSARY.md`. Don't drift to synonyms the glossary avoids. Respect its `## Avoid` rules. Player-facing copy follows `docs/EXPERIENCE-TERMINOLOGY.md` and `docs/PLAYER-BRAND.md`.

If the concept you need isn't in the glossary yet, either you're inventing language the project doesn't use (reconsider) or there's a real gap (note it for `/domain-modeling`).

## Flag ADR and RFC conflicts

If your output contradicts an existing ADR or RFC, surface it explicitly rather than silently overriding:

> _Contradicts ADR-007 (atomic rooms), but worth reopening because…_

A conflict between authorities is a `SPEC DEFECT` (see `SKILLS.md`). Do not silently pick a side.
