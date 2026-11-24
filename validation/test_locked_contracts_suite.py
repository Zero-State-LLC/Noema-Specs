import unittest

from tests import test_locked_contracts as locked


class LockedContractsSuiteTest(unittest.TestCase):
    def test_psr1_enrollment_receipt(self) -> None:
        locked.test_psr1_enrollment_receipt_valid_and_invalid()

    def test_psr1_cohort_summary(self) -> None:
        locked.test_psr1_cohort_summary_valid_and_invalid()

    def test_study_promotion_receipt(self) -> None:
        locked.test_study_promotion_receipt_valid_and_invalid()

    def test_rfc0131_invite_request(self) -> None:
        locked.test_rfc0131_invite_request_valid_and_invalid()


if __name__ == "__main__":
    unittest.main()
