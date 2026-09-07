# Experiment Comparison

Every comparison records run A/B, comparison variable, held constants, pinned feature/metric versions, equivalence boundary, confounds, comparison rule, and effect result. It never uses a current baseline or mutable metric. Missing measure is `NOT_COMPUTABLE`; failed material boundary/severe confound is `NOT_COMPARABLE`; only then may the pinned predicate/fixed-point comparison classify an effect. Interpretation and claim labels cannot override the comparison.

## Extension Points

Non-normative extension guidance; the authorities above remain controlling.

- **Auditable comparison explanation:** An authorized research comparison view can trace the declared variable, held constants, pinned metric/feature versions and comparison predicate to the two run bundles. Display exact machine result alongside localized reasoning and linked confounds.
- **Preserved invariants:** Evaluate missing measures as NOT_COMPUTABLE before material boundary/confound failures as NOT_COMPARABLE; only eligible comparisons reach the effect predicate. Interpretation labels cannot upgrade either failure state.
- **Compatibility and promotion:** Preserve original pins when metrics evolve; a rerun under new versions is a separate comparison, not replacement of the earlier result. This is STUDY evidence, not a PLAY objective, comparative Player rank, or controller privilege.
- **Verification targets:** Use missing-measure, failed-boundary, severe-confound, eligible-null and eligible-effect cases, including simultaneous missing and boundary failures. Confirm predicate ordering, deterministic fixed-point results and retention of negative outcomes; planned tests are not observed effects.
