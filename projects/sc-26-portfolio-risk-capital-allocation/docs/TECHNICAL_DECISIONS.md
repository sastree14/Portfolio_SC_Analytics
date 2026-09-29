# Technical decisions

The stack is not a list of logos. Each technology has to earn its place in the architecture.

## Key decisions

1. CVXPY expresses allocation constraints transparently.
2. Historical risk estimates and stress scenarios are reported separately.
3. Optimization outputs retain constraint diagnostics so infeasible requests are visible.

## Technology footprint

- **Python**
- **NumPy**
- **Pandas**
- **SciPy**
- **CVXPY**
- **Plotly**
- **Monte Carlo**
- **FastAPI**

## Decision rule

If a simpler component can meet the same operational requirement with lower maintenance cost, it should be preferred. The public implementation keeps boundaries explicit so individual tools can be replaced without redesigning the whole project.
