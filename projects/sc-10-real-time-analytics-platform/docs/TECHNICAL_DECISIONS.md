# Technical decisions

The stack is not a list of logos. Each technology has to earn its place in the architecture.

## Key decisions

1. Kafka-compatible transport decouples producers and consumers.
2. ClickHouse is chosen for high-rate analytical inserts and queries.
3. Grafana reads operational metrics; it is not the system of record.

## Technology footprint

- **Redpanda / Kafka**
- **ClickHouse**
- **Python**
- **FastAPI**
- **WebSockets**
- **Grafana**
- **Docker**
- **SQL**

## Decision rule

If a simpler component can meet the same operational requirement with lower maintenance cost, it should be preferred. The public implementation keeps boundaries explicit so individual tools can be replaced without redesigning the whole project.
