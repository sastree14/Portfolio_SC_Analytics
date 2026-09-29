# Business impact

A streaming architecture for ingesting events, updating analytical state and exposing low-latency operational views.

## Operating impact

1. Reduce the delay between an operational event and analytical visibility
2. Separate event ingestion from analytical querying
3. Provide a scalable path for dashboards and downstream alerts
4. Retain event history for replay and investigation

## Decisions supported

The implementation is designed to make the following questions easier to answer and act on:

- How is **event-to-query latency** changing?
- How is **events per second** changing?
- How is **consumer lag** changing?
- How is **failed events** changing?
- How is **dashboard freshness** changing?

## Example operating scenario

Order events are published to the event bus, consumed into ClickHouse, aggregated continuously and exposed through an API/WebSocket layer for live operational monitoring.

## Measurement

The public example exposes measurable technical and operating indicators without claiming production impact that has not been measured in a live organization.

Relevant KPIs include:

- event-to-query latency
- events per second
- consumer lag
- failed events
- dashboard freshness
