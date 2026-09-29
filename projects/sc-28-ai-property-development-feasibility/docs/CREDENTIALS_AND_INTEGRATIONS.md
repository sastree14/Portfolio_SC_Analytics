# Credentials and integrations

| System | Authentication | Used by | Data exchanged | Configuration |
|---|---|---|---|---|
| PostgreSQL | service credentials | project data store | Sites, costs, assumptions and decisions | `DATABASE_URL` |
| OpenAI | API key | document extraction | Selected planning / deal document text | `OPENAI_API_KEY` |
| n8n | workflow credential | operations automation | Approval and task events | `N8N_WEBHOOK_URL` |
| Geospatial source | API key where required | location enrichment | Coordinates and area context | `GEO_API_TOKEN` |

No secrets are committed. Runtime identities should be environment-specific and least-privilege.
