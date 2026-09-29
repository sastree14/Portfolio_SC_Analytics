# Technical decisions

The stack is not a list of logos. Each technology has to earn its place in the architecture.

## Key decisions

1. The mathematical model makes constraints explicit rather than hiding them in procedural code.
2. A heuristic baseline is retained to quantify the value of optimization.
3. ERP write-back is treated as a controlled integration after the solution is reviewed.

## Technology footprint

- **Python**
- **OR-Tools**
- **Pandas**
- **NumPy**
- **FastAPI**
- **PostgreSQL**
- **Plotly**
- **Docker**

## Decision rule

If a simpler component can meet the same operational requirement with lower maintenance cost, it should be preferred. The public implementation keeps boundaries explicit so individual tools can be replaced without redesigning the whole project.
