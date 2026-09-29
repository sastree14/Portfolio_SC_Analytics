from app.providers import MockProvider


def test_mock_provider_returns_controlled_plan() -> None:
    result = MockProvider().plan("Prepare a follow-up")
    assert "approval" in result.lower()
    assert "Prepare a follow-up" in result
