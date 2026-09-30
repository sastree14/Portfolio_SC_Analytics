# Edge deployment

## Why edge inference may be useful

A sorting or verification station often needs low latency and can benefit from keeping camera images on site.

An edge deployment can therefore reduce:

- network dependency
- image-transfer latency
- external image retention
- cloud inference cost

## Deployment options

### CPU workstation

Suitable for lower frame rates or periodic snapshots with a small detector.

### Local GPU workstation

Useful when higher throughput is required and the site already has a fixed camera station.

### NVIDIA edge device

Appropriate when the model needs to run close to the camera in a compact deployment.

### Central / cloud GPU

Useful when several camera stations share infrastructure and network latency is acceptable.

## Optimization

The model can be exported to ONNX from the supplied export script.

Further optimization can include:

- TensorRT
- reduced image size
- smaller detector variants
- half precision
- frame sampling
- asynchronous ingestion

## Operational rule

Hardware should be selected from a latency and accuracy target measured on real camera data, not from model size alone.
