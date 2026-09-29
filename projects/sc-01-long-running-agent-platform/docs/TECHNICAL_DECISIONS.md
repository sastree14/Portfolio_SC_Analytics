# Technical decisions

The stack is not a list of logos. Each technology has to earn its place in the architecture.

## Key decisions

1. PostgreSQL is the source of truth; Redis is transport, not business state.
2. Provider adapters keep orchestration independent from one model vendor.
3. Human approval is a first-class state transition rather than a prompt instruction.

## Technology footprint

- **Python**
- **FastAPI**
- **PostgreSQL**
- **Redis**
- **Celery**
- **Docker**
- **OpenAI**
- **Anthropic**
- **SQL**

## Decision rule

If a simpler component can meet the same operational requirement with lower maintenance cost, it should be preferred. The public implementation keeps boundaries explicit so individual tools can be replaced without redesigning the whole project.
