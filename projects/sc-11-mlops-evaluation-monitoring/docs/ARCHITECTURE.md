# Architecture

## Objective

A production-oriented layer for model evaluation, version tracking, drift checks and release gates.

```text
Source data / user input
          ↓
Validation and feature layer
          ↓
ML / AI Evaluation & Monitoring Platform
          ↓
Decision / analytical output
          ↓
Integration or user interface
          ↓
Monitoring and review
```

## Technology responsibilities

- **Python** — part of the implemented analytical or serving path.
- **MLflow** — part of the implemented analytical or serving path.
- **Evidently** — part of the implemented analytical or serving path.
- **FastAPI** — part of the implemented analytical or serving path.
- **PostgreSQL** — part of the implemented analytical or serving path.
- **Docker** — part of the implemented analytical or serving path.
- **GitHub Actions** — part of the implemented analytical or serving path.
- **Prometheus** — part of the implemented analytical or serving path.

## Integration boundaries

- **MLflow** — experiment tracking; exchanges parameters, metrics and artefacts.
- **PostgreSQL** — metadata store; exchanges runs, release decisions and model registry metadata.
- **GitHub Actions** — CI release gate; exchanges test and evaluation status.
- **Prometheus** — metrics exporter; exchanges runtime service metrics.
