from fastapi import APIRouter, Request
from app.models.webhook_models import WebhookPayload

router = APIRouter()

@router.get("")
def verify(
    hub_mode: str | None = None,
    hub_challenge: str | None = None,
    hub_verify_token: str | None = None,
):
    if hub_verify_token == "my_verify_token":
        return int(hub_challenge)
    return {"error": "invalid token"}

@router.post("")
async def receive(payload: WebhookPayload):
    for entry in payload.entry:
        for change in entry.changes:
            messages = change.value.messages or []
            for msg in messages:
                if msg.type == "text" and msg.text:
                    print("📩 text:", msg.text.body)
    return {"status": "ok"}
