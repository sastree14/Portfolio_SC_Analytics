# Credentials and integrations

Credentials belong to the runtime environment, not source control.

| System | Authentication | Used by | Data exchanged | Environment configuration |
|---|---|---|---|---|
| Redpanda / Kafka | SASL where enabled | event bus | Operational events | `KAFKA_BROKERS / KAFKA_USERNAME / KAFKA_PASSWORD` |
| ClickHouse | service credentials | analytical store | Events and aggregates | `CLICKHOUSE_URL` |
| Grafana | service account / local auth | monitoring UI | Queries and dashboard state | `GRAFANA_ADMIN_PASSWORD` |
| WebSocket clients | application auth | live consumers | Aggregated live metrics | `Application-specific token` |

## Permission principles

- use the narrowest scope compatible with the operation
- separate development, staging and production credentials
- rotate long-lived secrets
- avoid embedding tokens in workflow exports or notebooks
- record external writes when the workflow can modify a business system

## Secret storage

Suitable options include GitHub environment secrets, AWS Secrets Manager, Azure Key Vault or the deployment platform's native secret store.
