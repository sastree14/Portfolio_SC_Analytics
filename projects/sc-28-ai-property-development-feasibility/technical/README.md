# Technical implementation

## Main execution path

**Start here → [`run_project.py`](run_project.py)**

This is the principal public execution file for **SC-28 · AI Property Development Feasibility & Operations System**. It shows the complete high-level execution path in one place: **input → validation/context → core logic → business output**.

The supporting implementation below exists to make the main path deeper and replaceable, not to fragment the project.

## Supporting implementation

- `src/geospatial.py`
- `src/document_extract.py`
- `workflows/`
- `src/api.py`
- `tests/`

## Stack

- Python
- GeoPandas
- OpenAI
- n8n
- FastAPI

## Validation

See [VALIDATION.md](VALIDATION.md).

## Review order

1. Project README
2. Principal execution file
3. Supporting modules
4. SQL / integrations / tests / outputs
