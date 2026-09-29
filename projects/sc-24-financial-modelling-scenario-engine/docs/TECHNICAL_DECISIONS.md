# Technical decisions

The stack is not a list of logos. Each technology has to earn its place in the architecture.

## Key decisions

1. The model is driver-based so assumptions remain visible.
2. Python performs the calculation while Excel remains an accessible exchange/output format.
3. Actuals and forecast scenarios are kept separate to preserve model traceability.

## Technology footprint

- **Python**
- **Pandas**
- **NumPy**
- **OpenPyXL**
- **Plotly**
- **FastAPI**
- **PostgreSQL**
- **Excel**

## Decision rule

If a simpler component can meet the same operational requirement with lower maintenance cost, it should be preferred. The public implementation keeps boundaries explicit so individual tools can be replaced without redesigning the whole project.
