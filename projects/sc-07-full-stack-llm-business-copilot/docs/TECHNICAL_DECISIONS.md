# Technical decisions

The stack is not a list of logos. Each technology has to earn its place in the architecture.

## Key decisions

1. Next.js keeps UI and API routes in one deployable application.
2. Zod validates tool payloads before business APIs are called.
3. Supabase handles persistence while model calls stay behind server-side boundaries.

## Technology footprint

- **Next.js**
- **TypeScript**
- **React**
- **PostgreSQL**
- **Supabase**
- **OpenAI**
- **Vercel**
- **Zod**
- **Tailwind CSS**

## Decision rule

If a simpler component can meet the same operational requirement with lower maintenance cost, it should be preferred. The public implementation keeps boundaries explicit so individual tools can be replaced without redesigning the whole project.
