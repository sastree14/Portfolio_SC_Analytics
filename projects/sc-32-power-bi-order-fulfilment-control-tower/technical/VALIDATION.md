# Validation

The public implementation checks that:

- delivered orders cannot pre-date order creation
- lead time is non-negative
- service level is calculated from an explicit commitment rule
- open exceptions are counted independently of closed service performance

Run:

```bash
python run_project.py
```
