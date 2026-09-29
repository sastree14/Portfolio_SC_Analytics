# Limitations

- The public stack is sized for local demonstration rather than production throughput
- Exactly-once business semantics still require idempotency at the consumer boundary
- Production observability would normally use managed metrics and alerting

The project is complete enough to inspect and run locally, while these items define the additional hardening or organization-specific work expected before a production rollout.
