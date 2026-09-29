# Technical implementation

## Main execution path

**Start here → [`run_project.py`](run_project.py)**

This is the principal public execution file for **SC-17 · Customer Intelligence: Churn, CLV & Segmentation**. It shows the end-to-end path in one place: **input → validation/context → core logic → business output**.

The files below are supporting implementation details used by that main path.

## Supporting implementation

- `src/survival.py`
- `src/`
- `sql/`
- `tests/`
- `data/`

## Stack

- Python
- XGBoost
- Lifelines
- SHAP
- FastAPI

## Validation

See [VALIDATION.md](VALIDATION.md).

## Review order

1. Project README
2. Principal execution file
3. Supporting modules
4. SQL / integrations / tests / outputs

The principal execution file is intentionally the fastest technical route through the project.
