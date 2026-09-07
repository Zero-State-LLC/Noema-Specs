# v0.4 Lab: Conformance

`conformance/v0.4/` contains 146 atomic cases: five each for L01–L22 and three each for L23–L34. It requires the v0.3 Observatory suite and retains C/F/O/S prerequisites. The family map is L01 identity, L02 validation, L03 fork integrity, L04 fork points, L05 interventions, L06 perturbations, L07 ablations, L08 lesions, L09 counterfactuals, L10 seed policy, L11 controls, L12 shams, L13 run identity, L14 outcomes, L15 confounds, L16 replication, L17 generalization, L18 nondeterminism, L19 audit, L20 isolation, L21 retained null/failure evidence, L22 Compiler handoff.

The validator checks fixture schemas, negative fixtures, no production mutation, source/fork digest stability, required control downgrade, unsupported lesion behavior, counterfactual completeness, handoff semantics, deterministic intent compilation, claim-preserving simple projection, CAPTURE gating, and same-record advanced disclosure.


## Extension Points

Non-normative guidance for future maintenance; this section changes no current behavior or promotion status.

- Lab conformance can strengthen individual family assertions with explicit controls, fork inputs, authorization conditions, and expected result statuses. In particular, distinguish schema-only lesion fixtures from executed adapter support and retain null/failure evidence alongside successful outcomes.

- Maintain C/F/O/S and Observatory prerequisites and existing case identities when refining coverage. New Lab semantics require the owning versioned contract; increasing or restating the historical case total is not evidence of more executable coverage or of production permission.

- Validate fixture schemas and negative fixtures, then exercise source/fork digest stability, required-control downgrade, unsupported-lesion NOT_COMPUTABLE, and Compiler handoff gates. Report which assertions the validator actually executes and which case records remain descriptive; verify no test mutation crosses into production.
