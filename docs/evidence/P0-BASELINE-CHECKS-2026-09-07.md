# P0 baseline offline verification receipt: 2026-09-07

**Scope:** the [P0 reconciliation packet](P0-BASELINE-RECONCILIATION-2026-09-07.md), its JSON/CSV ledger, two structural repairs, and dated metadata notes. This is Specs/document validation, not runtime, client, hosted, or external gate acceptance.

## Environment and commands

Run from the assigned Specs worktree on the `94286ca` baseline. Dependencies were already provisioned in the canonical Specs validation environment. `PIP_NO_INDEX=1` prevents network package lookup. No network or live operations were used.

```bash
env -u PYTHONPATH -u PYTHONHOME PIP_NO_INDEX=1 \
  NOEMA_VALIDATION_VENV=/home/scrimshawlife/Noema-Specs-current/.venv \
  bash validation/run.sh
/home/scrimshawlife/Noema-Specs-current/.venv/bin/python \
  validation/validate_gateb_traceability.py
git diff --check
```

The existing runner executes unit tests, full Specs validation, direction validation, and offline freshness. Gate B traceability is explicitly run separately because it is not in this baseline runner. CI and validators were not changed to obtain a green result. No remote link availability or live freshness is inferred from offline checks.

## Results

| Check | Observed result |
|---|---|
| Existing `validation/run.sh`, offline | Exit 0. 3 unit tests passed. Full validator PASS, 444 schemas and 923 example JSON/JSONL files parsed. Internal Markdown links resolve and required structure is present. |
| Direction validation | PASS. Complete and status-disciplined direction package. |
| Offline freshness | PASS for structural expectations only. No current live-health conclusion. |
| Standalone Gate B traceability | Exit 0. 67 existing requirement/output rows checked, B/C BLOCKED and independence/redaction boundaries preserved. These 67 are not additional P0 ledger rows. |
| Exact documented ledger reproduction | Exit 0. 125 rows, pinned source/home digests, unique IDs, G01–G13 coverage, JSON/CSV parity and recomputed counts. |
| Table/text preservation | PASS. Five deferred data rows with two columns; 16 capability data rows with five columns; all nonempty original lines preserved as a multiset. |
| Machine metadata preservation | PASS. All gate/capability states, historical evidence pins, numeric readiness and other state values unchanged except the existing note/evidence-list additions. |
| Required-path preservation | PASS. All 2,814 baseline tracked paths remain present. |
| Additional JSON syntax sweep | PASS. 1,992 JSON files parse, including the new ledger outside the validator's schema/example directories. |
| `git diff --check` | An extra EOF blank line in the economy document and trailing spaces in the new report were caught and removed. Final rerun passes. No validator/test/fixture was changed. |

These checks establish document structure and traceability. They are not a rendered-browser or accessibility acceptance test. No Markdown renderer dependency was installed. Runtime test homes in the ledger were inspected, not executed.

## Reproduce targeted structural checks

Run the following with the existing validation Python environment (PyYAML required) from the Specs root. It reads the baseline and current docs only.

```python
from pathlib import Path
from collections import Counter
import subprocess,json,re
import yaml
base='94286cac7cc200a4ed244bfd7321ef16d0bfc2a1'
files=['docs/ECONOMY-EWM-SPEC.md','docs/CIVILIZATION-CAPABILITY-MATRIX.md']
for file in files:
 before=subprocess.check_output(['git','show',base+':'+file]).decode()
 after=Path(file).read_text()
 assert Counter(x for x in before.splitlines() if x)==Counter(x for x in after.splitlines() if x)
 lines=after.splitlines(); header='| Deferred | Actual state in the runtime |' if 'ECONOMY' in file else '| Capability | Existing implementation evidence | Current plane | Remaining integration proof | Campaign gate |'
 start=lines.index(header); n=2 if 'ECONOMY' in file else 5
 assert re.fullmatch(r'\|(?:\s*:?-+:?\s*\|){'+str(n)+'}',lines[start+1])
 end=start+2
 while end<len(lines) and lines[end].startswith('|'):
  assert len(lines[end].split('|'))-2==n
  end+=1
 expected=5 if n==2 else 16
 assert end-start-2==expected,(file,end-start-2)
 print(f'PASS: {file}: {expected} contiguous data rows, {n} columns, every nonempty original line preserved')
state_path='specs/current-state.v1.yaml'
old=yaml.safe_load(subprocess.check_output(['git','show',base+':'+state_path]))
new=yaml.safe_load(Path(state_path).read_text())
assert old['evidence_commits']==new['evidence_commits']
assert old['capabilities']==new['capabilities']
assert old['active_campaign']==new['active_campaign']
old_prod=old['runtimes']['production_alpha']; new_prod=new['runtimes']['production_alpha']
assert all(new_prod[k]==v for k,v in old_prod.items() if k not in ('specs_pin_note','evidence'))
assert new_prod['specs_pin_note'].startswith(old_prod['specs_pin_note'])
assert new_prod['evidence'][:-1]==old_prod['evidence']
assert new_prod['players_present']==0
assert 'noema-client==0.1.21' in new_prod['specs_pin_note'] and 'C7 checks unrun' in new_prod['specs_pin_note']
assert new['capabilities']['external_agent_population_gate_b']['state']=='BLOCKED'
assert new['capabilities']['integrated_small_civilization_run']['state']=='BLOCKED'
old['runtimes']['production_alpha']=new_prod
assert old==new, 'Only the existing production note and evidence list may change semantically'
print('PASS: Gate states, historical pins, numeric readiness and all other state fields preserved')
tracked=subprocess.check_output(['git','ls-tree','-r','--name-only',base]).decode().splitlines()
missing=[p for p in tracked if not Path(p).exists()]
assert not missing, missing
print(f'PASS: all {len(tracked)} baseline tracked paths remain present')
count=0
for p in Path('.').rglob('*.json'):
 if any(x in p.parts for x in ('.git','.venv','node_modules')): continue
 json.loads(p.read_text()); count+=1
print(f'PASS: {count} JSON files parse, including the new non-normative ledger')
```

## Extension Points

Append later verification receipts against their own candidate revisions and commands. Preserve this receipt's offline scope. Runtime execution, released-client identity, current endpoint health, independent Controller acceptance, and browser/accessibility acceptance require separate evidence and are not supplied by these checks.
