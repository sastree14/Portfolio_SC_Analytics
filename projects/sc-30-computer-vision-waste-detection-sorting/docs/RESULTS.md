# Results

## Public evaluation snapshot

The repository includes a representative evaluation view showing how the system should be assessed.

The important point is not one headline accuracy number. A useful object-detection review separates:

- precision
- recall
- per-class performance
- confidence distribution
- manual-review volume
- inference latency

## Example interpretation

In the public evaluation snapshot:

- rigid classes such as bottles and cans perform more consistently
- residual waste has lower precision/recall because its visual definition is broader
- the review threshold protects the workflow from overconfident low-quality decisions
- latency is tracked because a high-accuracy model that cannot meet the operational timing requirement may still be unusable

## Production acceptance

Before production, acceptance criteria should be agreed for the real environment.

Typical examples:

- maximum missed-item rate
- maximum false-positive rate
- minimum recall for safety-critical classes
- acceptable review percentage
- maximum inference latency
- acceptable performance under occlusion and difficult lighting
