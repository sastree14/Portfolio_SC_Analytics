# Examples

This directory contains inspectable evidence generated from the implementation.

- `inputs/` contains example requests.
- `outputs/` contains actual API responses generated with the mock provider.
- `logs/` contains an execution trace generated from the persisted event history.

The examples can be regenerated with:

```bash
python technical/scripts/generate_examples.py
```
