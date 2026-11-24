#!/usr/bin/env python3
"""Validators for operator-locked PSR-1 (#383/#363), STUDY (#362), and RFC-0131 (#396) contracts."""

from __future__ import annotations

from typing import Any


def validate_psr1_enrollment_receipt(doc: dict[str, Any]) -> list[str]:
    errs: list[str] = []
    if doc.get("receipt_type") != "psr1_tier3_enrollment":
        errs.append("receipt_type must be 'psr1_tier3_enrollment'")
    if doc.get("operator_tier") != 3:
        errs.append("operator_tier must be 3")
    if doc.get("enrollment_route") != "device-code:/connect":
        errs.append("enrollment_route must be 'device-code:/connect'")
    if doc.get("client_package") != "noema-client==0.1.24":
        errs.append("client_package must be 'noema-client==0.1.24'")
    if doc.get("first_observe_ok") is not True:
        errs.append("first_observe_ok must be true")
    for field in ("recorded_at", "operator_org", "server_origin", "worker_version_id", "world_id"):
        if not doc.get(field):
            errs.append(f"missing required field: {field}")
    return errs


def validate_psr1_cohort_summary(doc: dict[str, Any]) -> list[str]:
    errs: list[str] = []
    if doc.get("total_controllers", 0) < 6:
        errs.append("total_controllers must be >= 6")
    if doc.get("non_first_party_controllers", 0) < 2:
        errs.append("non_first_party_controllers must be >= 2")
    styles = set(doc.get("non_first_party_styles", []))
    if not {"framework-adapter", "custom-http-ws"}.issubset(styles):
        errs.append("non_first_party_styles must include both 'framework-adapter' and 'custom-http-ws'")
    if doc.get("tier3_operators", 0) < 1:
        errs.append("tier3_operators must be >= 1")
    if doc.get("delta_cycle", 0) < 24:
        errs.append("delta_cycle must be >= 24")
    if doc.get("min_actions_per_player", 0) < 20:
        errs.append("min_actions_per_player must be >= 20")
    if doc.get("total_actions", 0) < 60:
        errs.append("total_actions must be >= 60")
    if doc.get("protocol_regressions", 1) != 0:
        errs.append("protocol_regressions must be 0")
    return errs


def validate_study_promotion_receipt(doc: dict[str, Any]) -> list[str]:
    errs: list[str] = []
    if doc.get("receipt_type") != "hosted_study_promotion":
        errs.append("receipt_type must be 'hosted_study_promotion'")
    if doc.get("reconstruction_verified") is not True:
        errs.append("reconstruction_verified must be true")
    if doc.get("automated_redaction_exit_code") != 0:
        errs.append("automated_redaction_exit_code must be 0")
    if doc.get("steward_spot_check_passed") is not True:
        errs.append("steward_spot_check_passed must be true")
    if doc.get("verdict") not in {"PROMOTE_HOSTED_STUDY", "HOLD"}:
        errs.append("verdict must be 'PROMOTE_HOSTED_STUDY' or 'HOLD'")
    for field in ("recorded_at", "worker_version_id", "world_id", "psr1_receipt_ref", "evidence_pack_ref", "steward"):
        if not doc.get(field):
            errs.append(f"missing required field: {field}")
    return errs


def validate_rfc0131_invite_request(doc: dict[str, Any]) -> list[str]:
    errs: list[str] = []
    if not doc.get("human_principal_id"):
        errs.append("human_principal_id is required (contact-only targets deferred)")
    role = doc.get("role", "study-admin")
    if role != "study-admin":
        errs.append("v1 role must be 'study-admin'")
    ttl = doc.get("ttl_days", 7)
    if not isinstance(ttl, int) or ttl < 1 or ttl > 14:
        errs.append("ttl_days must be an integer between 1 and 14")
    return errs
