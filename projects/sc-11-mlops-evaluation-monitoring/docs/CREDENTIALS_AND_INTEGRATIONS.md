# Credentials and integrations

| System | Authentication | Used by | Data exchanged | Configuration |
|---|---|---|---|---|
| MLflow | tracking URI / auth | experiment tracking | Parameters, metrics and artefacts | `MLFLOW_TRACKING_URI` |
| PostgreSQL | service credentials | metadata store | Runs, release decisions and model registry metadata | `DATABASE_URL` |
| GitHub Actions | repository permissions | CI release gate | Test and evaluation status | `GitHub environment` |
| Prometheus | network endpoint | metrics exporter | Runtime service metrics | `PROMETHEUS_PORT` |

Credentials are never committed. Development, staging and production should use separate identities and least-privilege access.
