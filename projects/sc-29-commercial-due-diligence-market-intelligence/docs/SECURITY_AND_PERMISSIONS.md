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

- Evidence is stored before synthesis so conclusions can be traced back to sources.
- DuckDB supports fast local analysis of structured research extracts.
- Browser collection and model synthesis are separate stages with explicit source allowlisting.

## Production hardening

A production deployment should add organization-specific identity, network policy, secret rotation, monitoring, retention and incident-response controls.
