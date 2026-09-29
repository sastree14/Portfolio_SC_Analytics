from src.main import optimize

def test_example_runs():
    result=optimize()
    assert result["project"]=="SC-20"
    assert len(result)>1
