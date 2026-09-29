# Technical decisions

The stack is not a list of logos. Each technology has to earn its place in the architecture.

## Key decisions

1. Evidence is stored before synthesis so conclusions can be traced back to sources.
2. DuckDB supports fast local analysis of structured research extracts.
3. Browser collection and model synthesis are separate stages with explicit source allowlisting.

## Technology footprint

- **Python**
- **Pandas**
- **DuckDB**
- **FastAPI**
- **Playwright**
- **BeautifulSoup**
- **OpenAI**
- **PostgreSQL**
- **Plotly**

## Decision rule

If a simpler component can meet the same operational requirement with lower maintenance cost, it should be preferred. The public implementation keeps boundaries explicit so individual tools can be replaced without redesigning the whole project.
