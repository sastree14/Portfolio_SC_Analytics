# Business impact

SC-01 is designed for business processes where a useful AI response is not enough: the process must continue after the response, wait safely for decisions and interact with other systems without losing control.

## Operating change

| Without durable orchestration | With SC-01 |
|---|---|
| State can disappear when an interaction ends | Every run is persisted independently from the API request |
| Manual follow-up is needed after pauses | A run can remain waiting for approval and resume later |
| External actions are difficult to control | Sensitive actions can be placed behind an explicit approval gate |
| Temporary integration failures can break the workflow | Asynchronous workers can retry transient failures |
| It is difficult to reconstruct what happened | Run events create an inspectable execution history |
| Model-provider changes can affect application logic | Provider-specific SDKs sit behind one interface |

## Decisions supported

The platform is useful when the business needs to decide:

- whether an AI-prepared action should be executed
- which runs need human attention
- which workflows failed and why
- which external systems were called
- where automation can proceed without human intervention

## Measurable production KPIs

A deployment can monitor:

- completion rate
- failure rate
- approval waiting time
- end-to-end execution time
- retry count
- external-action success rate
- manual interventions per run
- model/API cost per completed process
