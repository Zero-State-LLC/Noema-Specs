# validation/test_validate_direction.py

- load_validator · function · L14-L20 — def load_validator()
- CampaignInvariantTests · class · L23-L60 — class CampaignInvariantTests(unittest.TestCase)
- campaign · method · L24-L32 — def campaign(self, **fields)
- assert_fails_with · method · L34-L39 — def assert_fails_with(self, campaign, *fragments: str) -> None
- test_active_campaign_with_open_gate_passes · method · L41-L42 — def test_active_campaign_with_open_gate_passes(self) -> None
- test_active_campaign_without_unproven_gates_fails · method · L44-L46 — def test_active_campaign_without_unproven_gates_fails(self) -> None: # The #361 state: ACTIVE_INTEGRATION with nothing left to prove.
- test_active_campaign_whose_active_gate_is_complete_fails · method · L48-L52 — def test_active_campaign_whose_active_gate_is_complete_fails(self) -> None
- test_paused_campaign_without_unproven_gates_passes · method · L54-L57 — def test_paused_campaign_without_unproven_gates_passes(self) -> None
- test_paused_campaign_listing_unproven_gates_fails · method · L59-L60 — def test_paused_campaign_listing_unproven_gates_fails(self) -> None
