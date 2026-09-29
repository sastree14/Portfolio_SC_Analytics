# Business impact

A full-stack web application that combines conversational analysis, structured tools and persistent business context.

## Operating impact

1. Give users one interface for asking questions and taking structured actions
2. Keep business tools separate from free-form model output
3. Persist conversations and tool results for later review
4. Support a product experience rather than a standalone prompt

## Decisions supported

The implementation is designed to make the following questions easier to answer and act on:

- How is **task completion rate** changing?
- How is **tool-use success rate** changing?
- How is **time to answer** changing?
- How is **user corrections** changing?
- How is **actions completed from the copilot** changing?

## Example operating scenario

A manager asks why pipeline conversion changed, requests the supporting records and then creates a follow-up task from the same interface.

## Measurement

The public example exposes measurable technical and operating indicators without claiming production impact that has not been measured in a live organization.

Relevant KPIs include:

- task completion rate
- tool-use success rate
- time to answer
- user corrections
- actions completed from the copilot
