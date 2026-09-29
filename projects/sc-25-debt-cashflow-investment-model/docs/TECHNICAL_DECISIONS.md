# Technical decisions

The stack is not a list of logos. Each technology has to earn its place in the architecture.

## Key decisions

1. Debt schedules are generated explicitly rather than approximated as a single financing cost.
2. Irregular cash-flow return calculations use dated cash flows.
3. Excel exports remain reviewable while the calculation engine stays version-controlled.

## Technology footprint

- **Python**
- **Pandas**
- **NumPy**
- **OpenPyXL**
- **Plotly**
- **XIRR**
- **PostgreSQL**
- **Excel**

## Decision rule

If a simpler component can meet the same operational requirement with lower maintenance cost, it should be preferred. The public implementation keeps boundaries explicit so individual tools can be replaced without redesigning the whole project.
