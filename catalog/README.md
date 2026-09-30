# Portfolio Catalog

The catalog is the machine-facing entry point to the SC-Analytics portfolio.

## Files

- `projects.yml` — global project index.
- `project-schema.yml` — Project Manifest v2 template.
- `sc-XX-*.yml` — one factual manifest per project.

## Project Manifest v2

The manifest is deliberately smaller than the full project documentation.

It answers:

- what the project is;
- who / what operating context it is designed for;
- why it matters;
- which technologies are documented;
- what kind of evidence the public portfolio provides;
- where deeper evidence lives;
- where the main visual and technical execution path live.

The manifest does not duplicate results, architecture or code.

## Evidence model

The deeper evidence remains under the project folder:

- `docs/BUSINESS_IMPACT.md`
- `docs/RESULTS.md`
- `docs/ARCHITECTURE.md`
- `docs/TECHNICAL_DECISIONS.md`
- `docs/LIMITATIONS.md`
- `examples/README.md`
- `technical/README.md`

Editorial or CRM systems should resolve the manifest first and read only the evidence required for the selected content angle.

## Provenance policy

Every current public manifest defaults to:

```yaml
provenance:
  evidence_class: public_portfolio_implementation
  client_claim_allowed: false
  confidentiality: public_safe_example
```

This means the project is valid capability and implementation proof.

It must not automatically be presented as named client work or as a documented client outcome. A stronger client claim requires separate approved evidence.

## Validation

Run:

```bash
python scripts/validate_portfolio.py
```

The full audit also validates manifest coverage:

```bash
python scripts/audit_portfolio.py
```
