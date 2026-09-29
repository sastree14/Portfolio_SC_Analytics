import json
from pathlib import Path
from src.main import run_example

root = Path(__file__).resolve().parents[2]
out = root / "examples" / "outputs" / "result.json"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(run_example(), indent=2), encoding="utf-8")
print(out)
