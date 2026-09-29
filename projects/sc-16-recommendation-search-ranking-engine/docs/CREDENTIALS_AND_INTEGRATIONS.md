# Credentials and integrations

| System | Authentication | Used by | Data exchanged | Configuration |
|---|---|---|---|---|
| PostgreSQL | service credentials | behaviour source | Users, items and interactions | `DATABASE_URL` |
| FAISS | local / service path | vector index | Item embeddings | `VECTOR_INDEX_PATH` |
| Redis | service credentials | online cache | Recent rankings and item features | `REDIS_URL` |
| FastAPI | service auth | serving API | User context and ranked items | `API_KEY` |

Credentials are never committed. Development, staging and production should use separate identities and least-privilege access.
