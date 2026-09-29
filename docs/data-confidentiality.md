# Data confidentiality

SC-Analytics does not publish client names, credentials, production connections or confidential business records in this repository.

## Public datasets

When a public implementation is based on confidential work, the public dataset may preserve the elements required to reproduce the workflow, including:

- column structure
- data types
- entity relationships
- temporal structure
- validation rules
- relevant constraints

The underlying business values are replaced with synthetic values.

No public sample should be treated as an original client extract unless the project explicitly states otherwise.

## Production connections

Connection strings, API keys, service-account credentials, private endpoints and environment secrets are excluded from the repository.

Projects should provide safe examples such as `.env.example` files where configuration is required.

## Anonymization

Names and identifiers that could disclose a client, employee, customer, supplier or other confidential party should be removed or replaced before publication.
