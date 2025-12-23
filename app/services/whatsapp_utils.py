# async def handle_webhook(payload: dict):
#     # כאן תהיה כל הלוגיקה:
#     # זיהוי הודעה
#     # ניתוב לפי תפריט
#     # שליחת תשובה
#     print("📥 Incoming webhook:")
#     print(payload)
import json

import requests
from app.core.config import GRAPH_API_VERSION, PHONE_NUMBER_ID, WHATSAPP_TOKEN
from app.services.whatsapp_menus import MAIN_MENU
def send_main_menu(user: str):
    print("📋 Sending MAIN menu to", user)
    send_buttons(user, "ברוך הבא 👋\nבחר אפשרות:", MAIN_MENU)
    # user_state[user] = {"stage": "MAIN"}
def send_buttons(to: str, text: str, buttons: list):
    payload = {
        "messaging_product": "whatsapp",
        "to": to,
        "type": "interactive",
        "interactive": {
            "type": "button",
            "body": {"text": text},
            "action": {
                "buttons": [
                    {"type": "reply", "reply": {"id": b["id"], "title": b["title"]}}
                    for b in buttons[:3]
                ]
            },
        },
    }
    wa_send(payload)

def wa_send(payload: dict):
    url = f"https://graph.facebook.com/{GRAPH_API_VERSION}/{PHONE_NUMBER_ID}/messages"
    headers = {
        "Authorization": f"Bearer {WHATSAPP_TOKEN}",
        "Content-Type": "application/json",
    }
    print("📤 Sending to WhatsApp:")
    print(json.dumps(payload, ensure_ascii=False))
    r = requests.post(url, headers=headers, json=payload, timeout=15)
    print("📥 WhatsApp response:", r.status_code, r.text if r.text else "")