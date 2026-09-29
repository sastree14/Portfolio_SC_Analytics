# Security and permissions

Security is treated as part of the architecture, not as an environment variable checklist.

## Baseline controls

- secrets are injected at runtime and are never committed
- development, staging and production identities are separate
- external write permissions should be narrower than read permissions
- service accounts should receive only the scopes required by their component
- sensitive write operations should be logged and, where appropriate, approval-gated
- public examples use non-production endpoints or deterministic adapters

## Project-specific considerations

- Airflow owns scheduling and dependencies, not transformation semantics.
- Object storage provides a replayable boundary between extraction and downstream processing.
- ClickHouse is used for analytical access; PostgreSQL remains suited to transactional metadata.

## Production hardening

A production deployment should add organization-specific identity, network policy, secret rotation, monitoring, retention and incident-response controls.
