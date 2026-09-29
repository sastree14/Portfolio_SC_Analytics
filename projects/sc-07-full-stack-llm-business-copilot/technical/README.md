# Technical implementation

## Main execution path

**Start here → [`run_project.ts`](run_project.ts)**

This is the principal public execution file for **SC-07 · Full-Stack LLM Business Copilot**. It deliberately shows the complete high-level path in one place: **input → validation/context → core logic → business output**.

The supporting folders contain the deeper implementation used by that flow; they are not separate disconnected demos.

## Supporting implementation

- `frontend/`
- `src/`
- `sql/`
- `tests/`
- `infra/`

## Stack

- TypeScript
- Next.js
- React
- Supabase
- OpenAI

## Validation

See [VALIDATION.md](VALIDATION.md) for the checks applied to this project.

## How to review the project

1. Read the project-level README for the business problem.
2. Read the principal execution file above.
3. Inspect the supporting modules only where you want implementation detail.
4. Review SQL, integrations, tests and public outputs.

The principal file is intentionally the fastest way to understand how the project actually runs.
