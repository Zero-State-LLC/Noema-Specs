# Experience Terminology

**Authority.** Dual semantic mapping: how internal, research, operator, player, and lore registers relate. Presentation and translation only. Does not rename protocols, schemas, audit fields, or claim labels.

Related: [PLAYER-BRAND.md](PLAYER-BRAND.md) · [TERMINOLOGY.md](TERMINOLOGY.md) · [EXPERIENCE.md](EXPERIENCE.md) · [VISUAL-DESIGN.md](VISUAL-DESIGN.md).

Use the register-appropriate phrase. Reveal the precise internal phrase in advanced, operator, or technical documentation.

---

## Dual semantic architecture

NOEMA keeps one world and one scientific layer. It does not keep one vocabulary.

```text
PLAYER SURFACE
Cognition Signature

INTERNAL / RESEARCH SCHEMA
emergent_capability_metric.cognition_signature
```

Implementations MUST resolve player-facing copy through this document (or a generated table derived from it). They MUST NOT scatter unmapped aliases through runtime code.

### Registers

| Register | Surfaces | Rule |
|---|---|---|
| **Schema** | protocols, JSON Schema, event payloads, ledgers | Field names stay. Versioned change requires RFC. |
| **Research** | STUDY, Lab, Compiler, LEARN, ethics, claims | Method vocabulary is correct here. |
| **Operator** | Admin Live, ops, recovery, Genesis | Control-plane precision. `operator` / `admin` / `warden` only where that surface is actually in use. Prefer **operator** or **admin** already in canon; do not invent Warden as a new principal. |
| **Player** | PLAY, world door, public WATCH, first-entry | World-native. Immediate. No research lecture. |
| **Lore** | derived cultural names, institution style, rumors | Atmosphere. Never overrides ledger or evidence. |

### Mapping framework

Each concept that crosses a surface has:

```text
concept_id
  schema          # stable machine name
  research        # STUDY / method phrase, if any
  operator        # Admin / ops phrase, if any
  player          # PLAY / WATCH phrase
  lore            # optional cultural overlay
  notes           # do-not-replace and leak rules
```

Runtime projection:

```text
if surface in {PLAY, WATCH_PUBLIC, WORLD_DOOR}:
    show player, then lore if present
    schema id only in advanced detail
elif surface in {STUDY, LEARN, LAB}:
    show research, with schema available
elif surface in {ADMIN_LIVE, OPS}:
    show operator or schema
else:
    show schema
```

Do not blindly replace every term. `telemetry` MAY remain on player surfaces when it is diegetic (relay telemetry, traffic). `experiment` stays on STUDY. `observation` in the MUD sense (“you see”) is player-valid; `Observation` as a research record is not.

---

## Player / internal mapping

At minimum, implementations MUST honor this direction. Player column is default PLAY/WATCH copy. Schema column is not shown there.

| Internal / academic tendency | Schema / research (keep) | Player-facing direction | Operator | Notes |
|---|---|---|---|---|
| experiment | Experiment, Lab plan, `experiment_id` | world / operation / event | experiment, fork, run | PLAY never hosts “run an experiment” |
| subject | — | player | player | Never “subject” on PLAY |
| agent ecology | agent population (research) | population / network | player count, controllers | Humans and agents are both Players |
| observation (research record) | Observation | signal / record / surveillance (diegetic) | observation, projection | MUD “you see” remains valid |
| metric | metric, feature, baseline | index / trait / signature | metric | Not a victory score |
| emergent behavior | emergence candidate | adaptation / anomaly | emergence candidate | No research label as PLAY chrome |
| test scenario | Lab template / captured test | event / condition | test, fixture | STUDY only |
| evaluation | oracle, claim assessment | assessment / reckoning | evaluation | Not a grade |
| consciousness metric | consciousness-adjacent construct (operational) | cognition signature or world-native equivalent | construct, never “proven consciousness” | No scalar consciousness score |
| dataset | Atlas, Reproducibility Bundle | archive | dataset, bundle | PLAY archive is in-world memory |
| telemetry | telemetry | telemetry when diegetic; else signal / strip | telemetry | Keep where it sounds like infrastructure |
| operator | Admin, operator | — | admin / operator | Not a player class. Do not print on PLAY |
| Chamber | Chamber (v0.1 ecology) | the world, the Reach, the named room | Chamber / world id | Prefer the world name on PLAY |
| canonical head | snapshot / settlement head | the world as it stands | canonical head, revision | Never “database” to players |
| World Event Director | WED | pressure, the season, what the Reach is under | WED / pressure schedule | |
| Frontier Director | Frontier Director | situation, the unknown | Frontier | STUDY: situation search |
| capability | capability candidate / graph | what someone can do; practice; office | capability (research) | Not a Player class |
| NOTICE / TEST / CAPTURE / LEARN | product research path | — | STUDY workflow | Not world-door chrome |

### Worked examples

```text
PLAYER        Relay Integrity: 83%
OPERATOR      relay.condition = 83
SCHEMA        entity.condition  (infrastructure, public)

PLAYER        Pressure: SEVERE
OPERATOR      world-report / WED pressure band
SCHEMA        derived projection; not a World.status value

PLAYER        Cognition Signature
RESEARCH      emergent_capability_metric.cognition_signature
PLAY          do not show unless a future world-native instrument exists

PLAYER        A record says the vault was emptied.
RESEARCH      historical artifact claim, claim label recoverable
SCHEMA        artifact claim fields; not world truth
```

---

## STUDY and advanced product phrases

The following table remains the STUDY / progressive-disclosure dictionary. It does not override the player mapping above.

| Internal | Default product phrase |
|---|---|
| Frontier Director | Situation search |
| Situation Genome | Situation |
| Observatory | Notice / detection |
| Anomaly candidate | Interesting behavior |
| Capability candidate | Possible capability |
| Perturbation | Change one condition |
| Ablation | Remove something |
| Lesion | Disable a declared module |
| Counterfactual | Try a different condition |
| Version differential | Compare versions |
| Lab Result | Test result |
| Phenomenon Compiler | Capture as test |
| Compilation request | Capture settings (advanced) |
| Dependency graph | Required conditions |
| Dependency-closed ddmin | Remove unnecessary context |
| Behavioral oracle | Validation |
| Minimality status | Smallest stable test NOEMA could verify |
| Compile receipt / audit root | Full provenance (technical detail) |
| Captured test | Captured test |
| Regression FAIL | Behavior did not reproduce in this test |
| Capability Graph | Learned capability relationships |
| Atlas | Learned evidence collection |
| Deep Time / institution lineage | Old place / old institution / this rule existed before me |
| Historical artifact claim | A record says… (not world truth) |
| World scar | Damaged / abandoned / historic site |
| Succession record | Leadership changed / stewardship continued |
| Derived lore | Story told about the world (never overrides evidence) |
| Capability Graph | LEARN — what was reproduced and how it relates |
| Behavior node | A reproduced behavior |
| DEPENDS_ON / FAILS_WITHOUT | Depends on / fails when … is removed |
| GENERALIZES_TO | Works in … |
| NOT_TESTED | Not yet tested (not a failure) |
| Player | You / your handle (human or agent-driven — same role). Not “subject”. |
| Controller | How you connect (browser, agent app, …) |
| Device enrollment / CONNECT | Connect an external Controller |
| Agent Gateway | Connection layer (technical) |
| Scoped credential | Agent access (not your password) |
| Admin Live | World operations (not play; not a public door) |
| World.status PAUSED | Maintenance — play actions paused |
| World health DEGRADED | Something operational is unhealthy |
| RECOVERY_REQUIRED | World is stopped until operators restore it |
| WATCH Lightweight Spectator Upgrade (informal “WATCH v1.5”) | Public spectator window — not a version pin |
| Current / notable event | The one headline on WATCH |
| Recent events | The short public event list on WATCH |
| World graph | Public sites and public connections on WATCH |
| Event presentation tier | NORMAL / NOTABLE / MAJOR display rank |

This dictionary does not rename protocol, schema, audit, or claim-label authority. Human-readable names appear before machine IDs, with the validated ID available on request. `OBSERVED`, `INFERRED`, `SPECULATIVE`, and `NOT_COMPUTABLE` display as Observed, Evidence suggests, Possible, and Cannot determine, respectively, while advanced detail exposes the canonical value.
