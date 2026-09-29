# Limitations

SC-01 implements the core durable-agent pattern, but it is not presented as a finished multi-tenant enterprise product.

Current limitations include:

- no organization/user authorization model
- no distributed tracing
- no dead-letter queue UI
- no model evaluation dashboard
- no workflow DSL for processes lasting days or weeks
- no idempotency-key implementation for destructive external actions
- no webhook signature verification

These are explicit production-hardening areas rather than hidden assumptions.
