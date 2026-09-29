# Credentials and integrations

| System | Authentication | Used by | Data exchanged | Configuration |
|---|---|---|---|---|
| PostgreSQL | service credentials | application source | Applicant, behavioural and outcome data | `DATABASE_URL` |
| FastAPI | service auth | decision API | Application features and decision output | `API_KEY` |
| Model artefact store | service credentials | model registry | Trained model and calibration artefacts | `MODEL_URI` |

Credentials are never committed. Development, staging and production should use separate identities and least-privilege access.
