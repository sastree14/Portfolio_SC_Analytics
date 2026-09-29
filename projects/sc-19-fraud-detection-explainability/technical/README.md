# Technical implementation

## Structure

- `src/` — core analytical logic
- `tests/` — deterministic smoke tests
- `sql/` — persistence and reporting queries
- `data/` — compact representative data
- `scripts/` — output-generation utilities

## Technology

- Python
- XGBoost
- SHAP
- Scikit-learn
- Imbalanced-learn
- FastAPI
- PostgreSQL
- Plotly

## Run

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python src/main.py
pytest -q
```
