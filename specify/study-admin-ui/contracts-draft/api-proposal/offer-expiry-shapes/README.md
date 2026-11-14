# D10 offered-expiry record-shape proposal

**Status: isolated Draft only, unaccepted, unregistered and unimplemented.** A is selected for Draft design, not field adoption or policy. D01-D10 remain unresolved at the full contract/qualification level.

## Scope and lineage

`records.schema.json` is a frozen derived proposal: it copies all 15 inherited definitions, selects only Invitation and Grant, uses an isolated draft URN and adds one required candidate offered_grant_expires_at field referencing the inherited UtcInstant definition. Other definitions are inherited support content, not additional tested record families. `lineage.json` pins the original schema/checker/fixtures/design/catalogue and identifier rules; no original file is overwritten. All existing representation constraints, legacy world spelling and custom UTC-second format remain inherited proposals, not adopted configuration or wire values.

This is a server-owned logical representation, not a client request DTO, credential verifier, state machine or service. Synthetic identities, dates, all-zero digests and active-state labels are not real identities/credentials/grants. No new duration value, equality policy, clock, provider, adapter or route is selected. The [selected design](../OFFER-EXPIRY-DESIGN.md) and [parent packet](../../README.md) retain the authoritative scope and limits.

## Inventory and limits

The local DS-101 through DS-116 roster contains16independent record-shape expectations:10shape-valid and6shape-invalid, including8shape-valid limitation records. These local fixture IDs allocate no canonical conformance family. The original56record expectations/eight CLI tests are unchanged and separate; do not add overlapping tiers into an acceptance total.

`pair-index.json` declares four synthetic diagnostic controls: later recorded issue with the same deadline, mismatched grant deadline, recorded issue after the offered deadline, and a different valid world. Each member is intentionally shape-valid. The independent operator check compares only declared field relationships/recorded date ordering; it is not an application validator, authoritative server clock or transition. A pair that violates the proposed runtime promise is still a valid demonstration of JSON Schema's limitation, never permission to grant access. Equal deadlines and linked references likewise prove no authenticated acceptance, atomicity, consent, revocation, persistence or output fence.

## Explicit opt-in check

Use an existing qualified interpreter with jsonschema and referencing. From the repository root, run the following Python with that interpreter and an existing owned scratch TMPDIR. It copies the unchanged parent CLI and three proposal data files into a test-owned temporary directory and cleans up. It writes no repository file, makes no service call and installs nothing. The checksum/roster/pair controls in the operator execution receipt remain separate from this ordinary CLI output.

    import os, shutil, subprocess, sys, tempfile
    from pathlib import Path
    repo = Path.cwd()
    packet = repo / "specify/study-admin-ui/contracts-draft/api-proposal/offer-expiry-shapes"
    tmp = os.environ.get("TMPDIR")
    assert tmp and Path(tmp).is_dir(), "set TMPDIR to an existing owned scratch directory"
    with tempfile.TemporaryDirectory(prefix="d10-shape-", dir=tmp) as directory:
        target = Path(directory)
        for name in ("records.schema.json", "case-index.json", "examples.json"):
            shutil.copyfile(packet / name, target / name)
        shutil.copyfile(repo / "specify/study-admin-ui/contracts-draft/validate.py", target / "validate.py")
        result = subprocess.run([sys.executable, "-I", str(target / "validate.py"), "--json"], capture_output=True, text=True, timeout=30)
        print(result.stdout, end="")
        if result.stderr:
            raise RuntimeError("checker emitted stderr; retain private failure evidence")
        raise SystemExit(result.returncode)

Expect two selected record shapes,16matched expectations,10shape-valid/6shape-invalid and8limitation records. Native CI does not automatically execute this opt-in packet or the private operator relationship check. Capture actual output rather than treating these expected counts as a test receipt.

## Remaining qualification

Schema-required presence, format rejection and closed-object checks do not establish immutability over time or binding from issuer→offer→identity-verified display→acceptance→grant→retry/reissue→protected output. All six OF observations and owning SA requirements still need the confirmed mounted Worker authorization plus controlled-browser seam with injected identity/persistence, accepted contracts, qualified clock/policy/account/bootstrap/durable/output-fence behavior and formal security review. No such behavior or future test is executed by this packet.

Issue396staysOPEN/notruntime-ready and RFC0131Draft/unaccepted/unimplemented. No invitation/account/role/auth/provider/resource/data/migration/deploy/research/export/hosting action, nominee/partner assignment or acceptance promotion follows. Keep all prior holds and per-PR review/CI/approval gates; prior admin exceptions are consumed. Refs #396.
