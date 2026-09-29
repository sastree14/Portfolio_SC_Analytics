# Credentials and integrations

| System | Authentication | Used by | Data exchanged | Configuration |
|---|---|---|---|---|
| Public web sources | HTTP / browser access | research collectors | Market and company evidence | `SOURCE_ALLOWLIST` |
| PostgreSQL | service credentials | evidence store | Sources, claims, questions and review state | `DATABASE_URL` |
| DuckDB | local analytics | analysis layer | Structured research extracts | `DUCKDB_PATH` |
| OpenAI | API key | structured synthesis | Selected evidence and review questions | `OPENAI_API_KEY` |

No secrets are committed. Runtime identities should be environment-specific and least-privilege.
