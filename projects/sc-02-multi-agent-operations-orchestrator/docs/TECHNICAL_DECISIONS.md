# Technical decisions

The stack is not a list of logos. Each technology has to earn its place in the architecture.

## Key decisions

1. LangGraph makes control flow explicit instead of relying on recursive prompting.
2. Pydantic contracts constrain inter-agent payloads.
3. Execution is separated from review so the reviewing agent cannot silently perform the action.

## Technology footprint

- **Python**
- **FastAPI**
- **LangGraph**
- **PostgreSQL**
- **Redis**
- **Docker**
- **OpenAI**
- **Anthropic**
- **Pydantic**

## Decision rule

If a simpler component can meet the same operational requirement with lower maintenance cost, it should be preferred. The public implementation keeps boundaries explicit so individual tools can be replaced without redesigning the whole project.
