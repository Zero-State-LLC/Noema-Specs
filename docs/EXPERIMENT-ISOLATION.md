# Experiment Isolation

Each interventional run uses isolated fork, separate ledger identity, storage namespace isolation, contained tool/network policy, secret isolation, research data partition, retention/cleanup policy, and a preserved reproducibility bundle. Production state, ledgers, credentials, and operational namespaces are read-only. Cleanup is allowed only after retaining audit chain, inputs, outputs, and bundles, and cannot delete failed, null, aborted, or confounded evidence.

## Extension Points

Non-normative extension guidance; the authorities above remain controlling.

- **Isolation and retention audit:** A research operations checklist can connect fork/ledger/storage identities to contained tools, network policy, secret partitions and reproducibility bundles. Expose policy identifiers and verification outcomes, never credential values.
- **Preserved invariants:** Production state, credentials and namespaces remain read-only. Cleanup cannot erase failed, null, aborted or confounded outcomes and cannot precede preservation of the audit chain, inputs, outputs and bundle.
- **Compatibility and promotion:** Reuse EXPERIMENT-FORK and EXPERIMENT-IDENTITY boundaries across storage or worker adapters. New retention or containment behavior needs explicit reviewed policy compatibility; no research-isolation configuration becomes a PLAY control.
- **Verification targets:** Attempt cross-namespace writes, production credential use and disallowed network/tool access and require denial without source mutation. Test cleanup blocked before bundle preservation, retained failure/null evidence afterward, and reproducibility from the retained bundle without production secrets.
