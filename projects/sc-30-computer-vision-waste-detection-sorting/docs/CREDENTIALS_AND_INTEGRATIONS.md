# Credentials and integrations

| Component | Authentication | Purpose | Configuration |
|---|---|---|---|
| Model checkpoint | filesystem / object-store credentials | load detector weights | `MODEL_PATH` |
| Camera / RTSP source | camera-specific credentials | frame ingestion | deployment-specific |
| FastAPI service | API key / network policy | inference requests | `API_KEY` |
| Object storage | cloud/service credentials where used | model and review-image storage | deployment-specific |
| Downstream sorter / application | service token / private network | consume structured detections | deployment-specific |

No credentials are committed.

## Integration contract

A downstream application should receive structured detections such as:

```json
{
  "frame_id": "frame-1042",
  "detections": [
    {
      "class_name": "plastic_bottle",
      "confidence": 0.91,
      "bbox_xyxy": [120, 84, 298, 516],
      "stream": "plastic",
      "decision": "automatic"
    }
  ]
}
```

This is more useful than returning only an annotated image.
