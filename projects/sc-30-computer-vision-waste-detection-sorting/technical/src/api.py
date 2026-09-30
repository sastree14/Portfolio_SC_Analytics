from __future__ import annotations

import os
import tempfile
from pathlib import Path

from fastapi import FastAPI, File, Header, HTTPException, UploadFile

from inference import predict

app = FastAPI(title="SC-30 Waste Detection API", version="1.0.0")


def require_api_key(x_api_key: str | None) -> None:
    expected = os.getenv("API_KEY")
    if expected and x_api_key != expected:
        raise HTTPException(status_code=401, detail="Invalid API key")


@app.get("/health")
def health():
    return {"status": "ok", "service": "sc-30-waste-detection"}


@app.post("/detect")
async def detect(
    image: UploadFile = File(...),
    x_api_key: str | None = Header(default=None),
):
    require_api_key(x_api_key)

    model_path = os.getenv("MODEL_PATH")
    if not model_path:
        raise HTTPException(status_code=503, detail="MODEL_PATH is not configured")

    suffix = Path(image.filename or "frame.jpg").suffix or ".jpg"
    payload = await image.read()

    with tempfile.NamedTemporaryFile(suffix=suffix, delete=True) as tmp:
        tmp.write(payload)
        tmp.flush()
        return predict(model_path, tmp.name)
