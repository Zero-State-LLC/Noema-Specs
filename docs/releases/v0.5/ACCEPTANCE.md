# v0.5 Compiler: Acceptance

1. All prior suites remain green (C/F/O/S/L + RFC-0003).
2. Only eligible Lab Results (`compiler_readiness == READY` + admission gates) enter normal compilation.
3. CAPTURE AS TEST deterministically compiles to a canonical compilation request.
4. Source replay preserves target before minimization.
5. Target behavior cannot be weakened after failures.
6. Removal ordering is deterministic (layer order, stable unit IDs).
7. Dependency closure is deterministic.
8. Protected units remain protected.
9. INVALID/INCONCLUSIVE oracle results never authorize removal.
10. Final one-unit sweep occurs.
11. Minimality claims remain bounded (`ONE_MINIMAL` ≠ global minimum).
12. Budget exhaustion does not imply minimality (`PARTIALLY_MINIMIZED` / `NOT_MINIMIZED`).
13. Required-control failure blocks promotion.
14. Invalid provenance blocks promotion.
15. Captured-test identity is stable under identical claim-bearing inputs.
16. Evidence lineage remains complete (receipt + audit root).
17. Simple view cannot overclaim relative to machine claim_label/status.
18. Ordinary capture does not require Compiler jargon.
19. Advanced/reproducibility detail remains available.
20. Regression FAIL does not imply global model inferiority (`not_a_global_ranking: true`).
21. Exact scenario cannot silently claim behavior-family generalization.
22. Failed capture remains queryable with status + reason + next action.
23. RFC-0003 provenance/canonicalization is reused.
24. No runtime Compiler implementation is added to this repository.
25. Simple and advanced STUDY capture views derive from the same captured test; simple labels map exactly to `OBSERVED` / `INFERRED` / `SPECULATIVE` / `NOT_COMPUTABLE`.
26. A regression result is scoped to a captured test and carries `not_a_global_ranking: true`.
27. A captured test declares its generalization boundary; a scenario-exact result never implies behavior-family coverage.
28. Counterexamples remain queryable after a later passing run; a pass never deletes recorded failure evidence.
29. Research partition access never exposes private cognition, prompts, or provider completions; unauthorized research detail is refused.
30. Compiler receipts and captured-test identities reuse RFC-0003 canonicalization and content hashing; no second provenance scheme is introduced.
