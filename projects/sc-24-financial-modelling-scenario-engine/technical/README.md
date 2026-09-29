# Technical implementation

## Map

- `src/` — project-specific analytical logic
- `tests/` — deterministic smoke test
- `sql/` — storage / monitoring queries
- `data/` — representative input
- `infra/` — local container notes

## Run

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python src/main.py
pytest -q
```

## Stack

- Python
- Pandas
- NumPy
- OpenPyXL
- Plotly
- FastAPI
- PostgreSQL
- Excel
