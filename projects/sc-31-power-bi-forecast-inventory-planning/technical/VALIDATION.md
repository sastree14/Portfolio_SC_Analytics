# Validation

The public implementation checks that:

- forecast rows cover all supported horizons
- WAPE and bias calculations are deterministic
- stock coverage is non-negative
- the example planning action is derived from published thresholds

Run:

```bash
python run_project.py
```
