from src.main import run_example

def test_example_runs():
    result=run_example()
    assert result["project"]=="SC-26"
    assert len(result)>1
