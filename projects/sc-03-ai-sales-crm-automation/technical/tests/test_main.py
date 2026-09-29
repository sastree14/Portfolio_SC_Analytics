from src.main import run_example


def test_example_completes():
    result = run_example()
    assert result["project"] == "SC-03"
    assert result["status"] == "completed"
    assert result["summary"]["peak_example_metric"] >= result["summary"]["average_example_metric"]
