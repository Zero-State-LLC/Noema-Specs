# P0 baseline reconciliation — 2026-09-07

**Status:** documentation reconciliation and local source inventory, not gate promotion.
**Scope:** owner-approved P0 in the existing `docs/gap-closure-baseline` worktree.
**Authority:** [direction governance](../DIRECTION-AUTHORITY.md), [Living Alpha acceptance](../LIVING-ALPHA-ACCEPTANCE.md), [Gate C companion](../LCA-GATE-C-SCENARIO.md), [Gate B preparation](../LCA2-GATE-B-PREPARATION.md).
**Artifacts:** [JSON ledger](P0-BASELINE-LEDGER-2026-09-07.json), [CSV ledger](P0-BASELINE-LEDGER-2026-09-07.csv), [offline verification receipt](P0-BASELINE-CHECKS-2026-09-07.md).

## Decision boundary

Gate A remains historically accepted through [the 2026-08-25 packet](../LCA-GATE-A-PROMOTION-2026-08-25.md). Gate B and Gate C remain **BLOCKED**. Gates D/E/F remain unproven. No current whole-runtime conformance, external Controller population, current live availability, or successor readiness is established here.

This work changes document placement, dated follow-up guidance, and existing state-note/evidence fields only. No runtime, CI, validator, protocol, public schema, milestone, or version domain changes. No new intent/RFC is needed for these documentation corrections. No network, deployment, enrollment, email, paid run, world mutation, push, PR, or merge was performed. The runtime checkout contained another contributor's WATCH edits, which were excluded by reading pinned Git objects.

## Locally observed provenance

`OBSERVED` here means local Git/source/document inspection. Recorded deployment observations below remain attributed to their original capture, not re-probed today. `INFERRED` dispositions and unexecuted requirements are kept separate from runtime results.

| Plane | Pin or observation | Evidence and limit |
|---|---|---|
| Specs inspection baseline | `94286cac7cc200a4ed244bfd7321ef16d0bfc2a1` | Local HEAD at start. Not a new live-build alignment. |
| Runtime inspection baseline | `c1be76650c995972de290d11e78a54d8baab70e9` | Local committed approved plan. Not stale planning baseline `461d81c` or uncommitted WATCH repairs. |
| Historical Gate A source / evidence merge | `61234cc` / `a6b7e4b` | Accepted packet retained. `production_specs_baseline: 492ccc9` is an evidence anchor, not today's Specs head. |
| Recorded deployment source | `418d26293422e2a6fe9a745b6005e92262e77e9b` | Runtime `spec-compat.json:hosted_live.source_commit`, read at `c1be766`. Not inferred from public `/version`. |
| Recorded Worker | `3f9b0e44-98c1-46f9-8232-bb44051a754f` | Same local pin, original `version_evidence.fetched_at` is `2026-09-02T03:41:31.967Z`. No current live probe. |
| Recorded world / Genesis | `world.perihelion-reach-3` / `genesis.94d0961984b2b4f8` | Existing production record retained with seal and room constraints, no reseed or expansion. |
| Live-build Specs alignment | `81ca8c1e6b1d1ca474cf31958439fb0bdb9a465c` | `hosted_live.specs_git`, not repository alignment. |
| Runtime repository Specs alignment | `d0086e4c7b6c82593fb1d579e5671b282b8c1486` | `specs.commit`. Alignment review remains separate from publish. |
| Current recorded official client | `noema-client==0.1.21` | Local #628 merge `681e5f1a3e5730a27814dcae556d5d6854745bdd`; continuation C7 amendment at lines 198–203. Release tag `0a20e2e` is a recorded claim, not an artifact verified in this turn. |
| Current candidate testing | NOT RUN | No Worker/Python runtime suite, product-client wheel/suite, or external acceptance run performed by this workstream. |

The full recorded `hosted_live` object is retained in the ledger, including the historical frozen-world distinctions in its note. Runtime source-to-recorded-live comparison has **40 changed paths**, enumerated in the JSON. This is a file inventory, not 40 missing contracts or proof that deployment is required. The locally computed Specs diff from `d0086e4` to `94286ca`, restricted to `rfcs/`, `protocols/`, `specs/`, `examples/`, and `validation/`, contains only `specs/current-state.v1.yaml`. Neither comparison establishes behavior or authorizes pin movement.

## Dated corrections, not rewritten history

### Client A10 / G01 / G05

Earlier Specs notes name `0.1.15`, and the 2026-08-31 residual register discusses `0.1.20`. Keep those dated records. Current guidance is the locally recorded `0.1.21` pin after #628, not an instruction to downgrade or proof that enrollment works. The owner-authorized amendment explicitly leaves enrollment-bound C7 checks **unrun** and Gate B owner-blocked. Exact installed/released artifact identity, supported enrollment, observe/action/refusal/resync/reconnect, and bounded receipt evidence remain P2/P3 work.

### Readiness A2/A9 / G03

The approved plan records `/ready` returning `players: 0`. This turn did not repeat the request. At runtime `c1be766`, `workers/noema/src/ops.ts:82–123` classifies agent Controllers as `system`, and `countLivePlayers` counts only present `live` actors. `workers/noema/test/ops.test.ts:55–88` includes the corresponding historical presence assertion. These implementation names do not change [Accepted RFC-0120](../../rfcs/RFC-0120-agent-only-player-identity.md): only agents are Players.

The old inference that zero means no enrolled or previously active agents is unsupported. The machine `players_present: 0` value is preserved with an interpretation warning, not converted into a census. A new population metric or actor-classification change needs reviewed semantics and tests. Gate B is blocked by missing participant-bound acceptance evidence, not by this health counter alone. No enrollment history was inspected or inferred.

### Structural repairs

- [ECONOMY-EWM-SPEC](../ECONOMY-EWM-SPEC.md): restore one contiguous deferred table with all five rows. Move the complete Extension Points block after the document body. Preserve every nonempty original line, shipped/deferred claim, and historical scope qualifier.
- [CIVILIZATION-CAPABILITY-MATRIX](../CIVILIZATION-CAPABILITY-MATRIX.md): move the offline research-spine row into the original five-column table, immediately after persistence/recovery. Preserve all 16 capability rows and all prose.

No aspirational economy behavior is activated. Accepted [RFC-0123](../../rfcs/RFC-0123-norm-ratchet-bounds-and-costly-trade-reject.md) and the pinned scope continue to govern the historical economy narrative. Offline research remains downstream of its separate reopen decision.

## Exhaustive ledger scope and counts

There are **125 trace rows**, not 125 distinct independent requirements or passing checks:

- **35 enumerated Gate A–F criteria**, plus **3 adjacent threshold/safety/deploy guards** = 38 gate rows.
- **9** common candidate declarations and **1** complete composite failure clause = 10 supporting acceptance rows.
- **64** Gate C companion rows covering every enumeration and code-list item from prerequisites through verdict, plus explicit strategy and verdict guards.
- **13** plan gap rows, G01–G13, preserving the original classification and closure text.

The eight paths appear in both the acceptance authority and its detailed companion. `GC-PATH-01` through `08` cross-reference `LAA-C-01` through `08`; the ninth companion path row is the conjunctive guard, not a ninth path. Seven strategy dimensions are inventory items, not seven required strategies. The thresholds remain **at least two viable strategies**, differing on **at least three of seven dimensions**, all **eight** coupled paths, at least **one consequential bounded institution**, and restart preservation. Gate E still requires four hours before opening the 24-continuous-hour candidate.

The extraction policy is encoded in JSON and checked against the full pinned documents, not ranked graph hits. This is not a census of all RFCs, residual proposals, all Gate B runbook subfields, runtime callers, or non-normative Extension Points. Those remain linked authority/context, not new enumerated obligations.

| Group | Rows |
|---|---:|
| `GC-DECLARE` | 11 |
| `GC-NONGOAL` | 7 |
| `GC-PACK` | 11 |
| `GC-PATH` | 9 |
| `GC-PREREQ` | 5 |
| `GC-STRATEGY` | 15 |
| `GC-VERDICT` | 6 |
| `LAA-A` | 5 |
| `LAA-B` | 5 |
| `LAA-C` | 9 |
| `LAA-CANDIDATE` | 9 |
| `LAA-D` | 6 |
| `LAA-E` | 5 |
| `LAA-F` | 8 |
| `LAA-FAILURE` | 1 |
| `PLAN-G` | 13 |

### Classification and evidence limits

| Classification | Rows | Meaning in this packet |
|---|---:|---|
| `contract_closed` | 5 | Historical Gate A acceptance only. Not current runtime regression proof. |
| `evidence_gap` | 114 | Required current-candidate evidence not established, even where contracts and tests exist. |
| `ambiguous` | 3 | G03 metric semantics, G11 projection hypothesis, G12 binding integration hypothesis need their stated review/reproduction. |
| `deployment_gap` | 1 | G04 source-to-live delta requires a requirement-level deployment decision, not automatic publish. |
| `runtime_gap` | 1 | G02 preserves the approved plan's verification defect, owned by P1, not modified here. |
| `deferred` | 1 | G10 downstream successor/research decisions, not active runtime work. |

These are non-normative ledger dispositions, not additions to the machine status vocabulary. `OBSERVED` on a row refers to the quoted requirement and inspected homes. It does not label missing behavior as observed, make an ambiguous hypothesis a confirmed defect, or grant acceptance. `NOT_ESTABLISHED_FOR_CURRENT_CANDIDATE` is a ledger description, not a new campaign verdict. An actual acceptance conclusion without required evidence remains `NOT_COMPUTABLE` or blocked under its governing contract.

Each row includes its exact original source line, authority references, explicit dependency, evidence qualification, and any verified source/test/evidence home. Registry entries carry repository, full commit, file digest and line span. The CSV contains the same rows; its home IDs resolve through the JSON registry. Supporting runtime test declarations were inspected but **not run**. Empty mappings mean no suitable home verified in this bounded review, not proof that none exists. The Gate B traceability document is historical representative evidence only. There is no accepted Gate B or Gate C run packet newly supplied here.

## Open decisions and handoff

| Plan rows | Next responsible decision or evidence |
|---|---|
| G01 | Review this baseline and whether repository alignment should move. Preserve historical promotion/live-build pins. No blanket current conformance claim. |
| G02 | P1 verification owner handles existing Specs #324 and runtime CI defect tracking. This owner changed no CI, tests, fixtures, or validators. |
| G03 | Review exact counter semantics and whether a distinct authorized participant metric is needed. Do not repair identity by renaming humans Players. |
| G04–G05 | P2 verifies the pinned candidate and exact client, then decides which receipts need a newer deployment. Separate explicit deploy authorization if needed. |
| G06–G07 | P3 requires supported human approval, three autonomous separate decision contexts, reconnect/contention and redacted evidence review. Three IDs/processes alone do not qualify. |
| G08 | P4 after accepted B: all eight coupled paths, strategy plurality, consequential institution, restart and later-decision receipts in one candidate. |
| G09 | P5 public-only uninvolved WATCH review, then separately approved four-hour and continuous 24-hour endurance/recovery evidence. |
| G10 | P6 explicit successor packet. Hosted STUDY, offline/hosted equivalence, v0.6B/C, v0.8 and deferred mechanics retain separate triggers. |
| G11–G13 | P2 owners reproduce and review projection/privacy, binding serialization and real-boundary coverage. Uncommitted parallel WATCH repairs were not treated as accepted evidence. |

Residual B1/B2/B4/B7b–B7e/B8/B9/B10/PAM proposals remain conditional. RFC-0129 closes the crime payload, not detection/sanction/producer activation. Existing MUD craft remains specs-complete and presentation work belongs to its Native Interaction / R0–R5 handoff, not another campaign.

## Separately reported follow-up: 2026-09-07 05:23 UTC

The coordinator reported the following after this pinned inventory was generated. These are **attributed reports, not independently verified issue/PR or runtime-test results from this workstream**. No network lookup was performed, no ledger row or baseline count was changed, and no current-candidate acceptance follows.

| Reported reference | Reported disposition / required follow-up |
|---|---|
| Noema #632 | Missing runtime CI tracked as a defect. P1 ownership remains separate. |
| Noema #633 | Coordinator reports reproduced private/zero WATCH projection failure. P2 owns the fix and retained regression evidence. The original G11 hypothesis at `c1be766` remains the historical inventory entry. |
| Noema #634 | Coordinator reports real RECONSTRUCT canonical JSON containing `undefined` and a changed round-trip digest. Compatibility/version review is required before any global serializer change. This is a dated follow-up, not a fourteenth original gap row or permission to change serialization. |
| Noema-Specs PR #326 | Coordinator reports publication and independent local full-entrypoint PASS, hosted CI pending. This documentation workstream neither authored nor verified that PR. |
| Runtime full baseline | Coordinator reports exact-Specs `CI=true` run still in progress. No result is recorded here. |

### Execution follow-up reported at 05:27 UTC

The coordinator subsequently supplied these executed results. They supersede
the pending-work descriptions in the 05:23 report for the named checks only.
This workstream has not independently inspected their logs or remote status.
Keep them attributed and separate from its own offline verification receipt.

| Reported execution | Exact reported result and boundary |
|---|---|
| Noema-Specs PR #326 actual CI | Full entrypoint PASS, including 67 Gate B traceability rows. Still review-required, not reported merged. |
| Runtime `c1be766`, Node 24, `CI=true` | Worker suite: 1,642 passed, 0 skipped. Typecheck passed. Source-level result, not a deployment or external acceptance run. |
| Runtime `c1be766`, Python 3.11, exact Specs | 558 passed, 4 skipped. Official-client E2E subsequently passed as a separate 1-test run; three PostgreSQL cases remain. Preserve the separate run counts rather than presenting an unexecuted aggregate suite. |
| Official client `v0.1.21`, isolated installed suite | 165 passed, 0 skipped. This is isolated installed-client validation, not canonical enrollment or completion of C7. |
| WATCH changes, parent-focused checks | 60 passed. The message did not provide an exact candidate commit or retained log reference; do not treat this as a pinned whole-suite or hosted acceptance result. |

The original 125-row inventory, G01–G13 dispositions, source/home digests and
JSON/CSV counts remain unchanged. These results do not promote Gate A anew,
open Gate B/C, resolve the #634 compatibility/version decision, establish live
client enrollment, or authorize deployment. Downstream work need not finish
before this documentation packet is handed off.

### Locally verified integration follow-up at 05:29 UTC

After the coordinator reported PR #326 merged, local `origin/main` resolved to
`061d2b0c6489ca5e004f443e98eb2c5f93a69b8f`, whose commit records that merge.
No network fetch was performed by this workstream. The clean documentation
branch rebased onto that locally available base without conflicts.

The three original documentation commits map to `0461fba` (table repairs),
`7445f3b` (ledger/report), and `c59527e` (attributed execution follow-up).
The inherited full `validation/run.sh` now includes Gate B traceability.
Its actual offline rerun passed **6 tests**, **444 schemas**, **923 example
JSON/JSONL files**, and **67 Gate B traceability rows**, plus internal links,
required structure, direction, and offline freshness. See the separate
[integration validation receipt](P0-BASELINE-CHECKS-2026-09-07.md).

Specs `94286ca` and runtime `c1be766` remain this inventory's original dated
inspection baselines. The 125-row JSON/CSV artifacts and machine gate states
are unchanged. CI and validator changes belong to inherited PR #326, not this
documentation diff against `origin/main`. Earlier pending/review-required
reports above are historical, not the current locally observed merge state.

## Reproduce the exhaustive inventory check

From this Specs worktree, use Python 3 and a local runtime repository containing `c1be766`. The script reads Git objects only and validates coverage independently of the stored row counts. It checks exact JSON/CSV parity and pinned home digests as well as every source enumeration. It neither runs nor modifies repository validators.

```bash
export NOEMA_RUNTIME_REPO=/home/scrimshawlife/work/Noema-gap-watch
python3 - <<'PY_CHECK'
import collections, csv, hashlib, json, os, re, subprocess
from pathlib import Path
p = Path('docs/evidence/P0-BASELINE-LEDGER-2026-09-07')
d = json.loads(p.with_suffix('.json').read_text())
repos = {'specs': '.', 'runtime': os.environ['NOEMA_RUNTIME_REPO']}
def read(meta):
    return subprocess.check_output([
        'git', '-C', repos[meta['repository']], 'show',
        meta['commit'] + ':' + meta['path']]).decode()
sources = {}
for path, meta in d['source_documents'].items():
    text = read(dict(meta, path=path))
    assert hashlib.sha256(text.encode()).hexdigest() == meta['sha256']
    sources[path] = text.splitlines()
expected = []
for policy in d['extraction_policies']:
    lines = sources[policy['source']]
    start = lines.index('## ' + policy['heading']) + 1
    end = next((i for i in range(start, len(lines))
                if lines[i].startswith('## ')), len(lines))
    fenced = False
    for i in range(start, end):
        line = lines[i]
        if line.startswith('```'):
            fenced = not fenced
            continue
        if (re.match(r'^(?:- |\d+\. )', line)
            or (policy['include_code'] and fenced and line.strip())
            or any(line.startswith(x) for x in policy['prose_prefixes'])):
            expected.append((policy['source'], i + 1, line))
plan = 'docs/evidence/SPECS-RUNTIME-GAP-CLOSURE-2026-09-07.md'
expected += [(plan, i, line) for i, line in enumerate(sources[plan], 1)
             if re.match(r'^\| G\d\d \|', line)]
actual = [(r['source'], r['source_line'], r['source_text']) for r in d['rows']]
assert actual == expected
assert len({r['id'] for r in d['rows']}) == len(actual)
assert [r['id'] for r in d['rows'] if r['group'] == 'PLAN-G'] == [
    f'G{i:02}' for i in range(1, 14)]
for home in d['home_registry'].values():
    text = read(home)
    assert hashlib.sha256(text.encode()).hexdigest() == home['file_sha256']
    assert 1 <= home['line_start'] <= home['line_end'] <= len(text.splitlines())
for row in d['rows']:
    for key in ('authority_homes', 'source_homes', 'test_homes', 'evidence_homes'):
        assert all(x in d['home_registry'] for x in row[key])
    assert row['dependency'] and row['mapping_limit']
with p.with_suffix('.csv').open(newline='') as f:
    csv_rows = list(csv.DictReader(f))
assert len(csv_rows) == len(d['rows'])
for a, b in zip(d['rows'], csv_rows):
    for key, value in b.items():
        expected_value = a.get(key)
        if isinstance(expected_value, list):
            assert json.loads(value) == expected_value
        else:
            assert value == ('' if expected_value is None else str(expected_value))
counts = {'total': len(actual),
          'by_group': dict(collections.Counter(r['group'] for r in d['rows'])),
          'by_classification': dict(collections.Counter(
              r['classification'] for r in d['rows']))}
assert counts == d['counts']
assert counts['total'] == 125
print(json.dumps(counts, indent=2, sort_keys=True))
print('PASS: exhaustive pinned-source coverage, home digests and CSV parity')
PY_CHECK
```

## Extension Points

Non-normative evidence-maintenance seams, not authorization to change contracts or run gates.

- Extend a later dated packet by retaining this baseline and replacing unknowns only with candidate-bound receipts and explicit reviewer decisions. Keep source, deployed version, product-client artifact and external acceptance separate.
- Add verified homes when their revision and evidence tier are known. A registry entry is navigation, not conformance. Preserve duplicates across authority levels rather than inflating a unique-requirement total.
- Before adoption, re-run the exhaustive coverage/parity check and current repository validation. A missing path, digest mismatch, missing approval or unrun strategy/restart/endurance item must remain visible, not become a green gate.
- Any changed metric, receipt semantics, threshold, public schema or promotion rule follows its governing RFC/review boundary. EP completion does not activate residual proposals, hosted research, new verbs or new rooms.
