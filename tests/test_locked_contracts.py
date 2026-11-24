from tools.validate_locked_contracts import (
    validate_psr1_cohort_summary,
    validate_psr1_enrollment_receipt,
    validate_rfc0131_invite_request,
    validate_study_promotion_receipt,
)


def test_psr1_enrollment_receipt_valid_and_invalid() -> None:
    valid = {
        "receipt_type": "psr1_tier3_enrollment",
        "recorded_at": "2026-11-24T05:00:00Z",
        "operator_tier": 3,
        "operator_org": "external-lab",
        "server_origin": "https://noema.guru",
        "worker_version_id": "42a45e7e-8e0f-4461-8ec6-b09a03805360",
        "world_id": "world.perihelion-reach-3",
        "client_package": "noema-client==0.1.24",
        "enrollment_route": "device-code:/connect",
        "first_observe_ok": True,
    }
    assert validate_psr1_enrollment_receipt(valid) == []
    bad = {**valid, "client_package": "noema-client==0.1.21", "operator_tier": 1}
    assert len(validate_psr1_enrollment_receipt(bad)) == 2


def test_psr1_cohort_summary_valid_and_invalid() -> None:
    valid = {
        "total_controllers": 6,
        "non_first_party_controllers": 2,
        "non_first_party_styles": ["framework-adapter", "custom-http-ws"],
        "tier3_operators": 1,
        "delta_cycle": 24,
        "min_actions_per_player": 20,
        "total_actions": 60,
        "protocol_regressions": 0,
    }
    assert validate_psr1_cohort_summary(valid) == []
    bad = {**valid, "non_first_party_styles": ["framework-adapter"], "protocol_regressions": 1}
    assert len(validate_psr1_cohort_summary(bad)) == 2


def test_study_promotion_receipt_valid_and_invalid() -> None:
    valid = {
        "receipt_type": "hosted_study_promotion",
        "recorded_at": "2026-11-24T05:00:00Z",
        "worker_version_id": "42a45e7e-8e0f-4461-8ec6-b09a03805360",
        "world_id": "world.perihelion-reach-3",
        "psr1_receipt_ref": "docs/evidence/psr1.json",
        "evidence_pack_ref": "sha256:abc123",
        "reconstruction_verified": True,
        "automated_redaction_exit_code": 0,
        "steward": "Zero-State operator",
        "steward_spot_check_passed": True,
        "verdict": "PROMOTE_HOSTED_STUDY",
    }
    assert validate_study_promotion_receipt(valid) == []
    bad = {**valid, "automated_redaction_exit_code": 1}
    assert len(validate_study_promotion_receipt(bad)) == 1


def test_rfc0131_invite_request_valid_and_invalid() -> None:
    assert validate_rfc0131_invite_request({"human_principal_id": "hp_123", "ttl_days": 7}) == []
    bad = {"human_principal_id": "", "role": "global-admin", "ttl_days": 30}
    assert len(validate_rfc0131_invite_request(bad)) == 3
