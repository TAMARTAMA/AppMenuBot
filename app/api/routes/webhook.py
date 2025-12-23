from fastapi import APIRouter, Request
from flask import json

from app.models.webhook_models import WebhookPayload
from app.core.config import VERIFY_TOKEN
from app.services.state import get_user_state, set_user_state
from app.services.bot_handler import handle_message
router = APIRouter()

@router.get("")
def verify(
    hub_mode: str | None = None,
    hub_challenge: str | None = None,
    hub_verify_token: str | None = None,
):
    if hub_verify_token == VERIFY_TOKEN:
        return int(hub_challenge)
    return {"error": "invalid token"}

@router.post("")
async def receive(payload: WebhookPayload):
    print("📩 Incoming webhook:")
    print(json.dumps(payload.dict(), ensure_ascii=False))

    for entry in payload.entry:
        for change in entry.changes:
            messages = change.value.messages or []
            for msg in messages:
                handle_message(msg)

    return {"status": "ok"}

# if msg.type == "text" and msg.text:
#     print("📩 text:", msg.text.body)
# elif msg.type == "interactive" and msg.interactive:
#     button = msg.interactive.button_reply
#     if button:
#         print("📩 button clicked:", button.id, button.title)



# user_id = msg.from_  # מזהה המשתמש
# # קבלת ה-state הקיים
# state = get_user_state(user_id)

# state["last_message"] = msg.text.body if msg.type == "text" else (
# msg.interactive.button.text if msg.type == "interactive" else None)
# state["last_type"] = msg.type


# # שמירה חזרה ל-Redis
# set_user_state(user_id, state)

# print(f"📩 Updated state for {user_id}:", state)
# handle_message(msg.model_dump(),user_id)  