# Credentials and integrations

| System | Authentication | Used by | Data exchanged | Configuration |
|---|---|---|---|---|
| PostgreSQL | service credentials | planning source | Jobs, resources, skills, shifts and constraints | `DATABASE_URL` |
| FastAPI | service auth | optimization API | Planning scenarios and optimized assignments | `API_KEY` |
| Calendar / workforce API | OAuth / bearer token | activation connector | Approved assignments and availability | `WORKFORCE_TOKEN` |

No secrets are committed. Runtime identities should be environment-specific and least-privilege.
