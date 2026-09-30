# Environments

## Local

- Python environment
- deterministic `run_project.py`
- CPU inference supported for small models
- sample outputs without external credentials

## Development

- labeled development dataset
- training and inference scripts
- experiment checkpoints
- local or shared GPU
- verbose logging

## Testing

- post-processing unit tests
- class mapping tests
- confidence-policy tests
- deterministic public example
- dataset configuration checks

## Staging

Staging should reproduce:

- production camera resolution
- approximate lighting
- camera angle
- hardware target
- inference API
- operational thresholds

## Production

Depending on latency and connectivity, production can run on:

- local GPU workstation
- NVIDIA edge device
- central inference server
- cloud GPU service

Production should include model versioning, latency monitoring, review sampling and drift monitoring.
