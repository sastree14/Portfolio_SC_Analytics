# Technical decisions

The stack is not a list of logos. Each technology has to earn its place in the architecture.

## Key decisions

1. OR-Tools covers discrete scheduling efficiently while Pyomo provides a transparent algebraic alternative.
2. Skill and capacity constraints are data-driven rather than hardcoded.
3. The objective can be changed without redesigning the scheduling data model.

## Technology footprint

- **Python**
- **OR-Tools**
- **Pyomo**
- **Pandas**
- **FastAPI**
- **PostgreSQL**
- **Docker**
- **Plotly**

## Decision rule

If a simpler component can meet the same operational requirement with lower maintenance cost, it should be preferred. The public implementation keeps boundaries explicit so individual tools can be replaced without redesigning the whole project.
