# Technical decisions

The stack is not a list of logos. Each technology has to earn its place in the architecture.

## Key decisions

1. Financial feasibility remains deterministic even when AI extracts inputs from documents.
2. GeoPandas handles spatial context without making geospatial enrichment a hidden black box.
3. n8n coordinates review steps while the financial model remains version-controlled code.

## Technology footprint

- **Python**
- **FastAPI**
- **PostgreSQL**
- **Pandas**
- **GeoPandas**
- **OpenAI**
- **n8n**
- **Docker**
- **Plotly**

## Decision rule

If a simpler component can meet the same operational requirement with lower maintenance cost, it should be preferred. The public implementation keeps boundaries explicit so individual tools can be replaced without redesigning the whole project.
