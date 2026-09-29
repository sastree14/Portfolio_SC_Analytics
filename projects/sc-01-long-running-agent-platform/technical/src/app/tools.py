import httpx

from app.settings import get_settings


def call_webhook(url: str, payload: dict) -> dict:
    settings = get_settings()
    headers = {"Content-Type": "application/json"}
    if settings.outbound_webhook_token:
        headers["Authorization"] = f"Bearer {settings.outbound_webhook_token}"

    with httpx.Client(timeout=20.0) as client:
        response = client.post(url, json=payload, headers=headers)
        response.raise_for_status()
        content_type = response.headers.get("content-type", "")
        body = response.json() if "application/json" in content_type else {"text": response.text[:2000]}
        return {"status_code": response.status_code, "body": body}
