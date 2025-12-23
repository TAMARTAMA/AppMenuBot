from app.services.whatsapp_utils import  send_main_menu , send_sub_menu, send_text
from app.services.whatsapp_menus import SUB_MENUS, SUB_ACTIONS
from app.models.webhook_models import Message
def handle_message(msg: Message) -> None:
    if msg.type == "text" and msg.text:
        print("📩 text:", msg.text.body)
        handle_text_message(msg)
    elif msg.type == "interactive" and msg.interactive:
        button = msg.interactive.button_reply
        if button:
            print("📩 button clicked:", button.id, button.title)
        handle_interactive_message(msg)
    else:
        send_text(msg.from_, "בחירה לא מוכרת.")
        send_main_menu(msg.from_)
    return

def handle_text_message(msg: Message) -> None:
    send_main_menu(msg.from_)

def handle_interactive_message(msg: Message) -> None:
    button_id = msg.interactive.button_reply.id if msg.interactive.button_reply else None
    if not button_id:
        # send_text(user, "לא הבנתי את הבחירה. נסה שוב.")
        send_main_menu(msg.from_)
        return

    if button_id in SUB_MENUS:
        send_sub_menu(msg.from_, button_id)
        return

    if button_id in SUB_ACTIONS:
        result = SUB_ACTIONS[button_id](msg.from_)
        send_text(msg.from_, result)
        # send_main_menu(msg.from_)
        return
    send_text(msg.from_, "בחירה לא מוכרת.")
    send_main_menu(msg.from_)
    return
# def handle_message(msg: dict,user_id) -> None:
#     if not user_id:
#         return

#     mtype = msg.type

#     if mtype == "interactive":
#         button_id = get_button_reply_id(msg)
#         if not button_id:
#             send_text(user, "לא הבנתי את הבחירה. נסה שוב.")
#             send_main_menu(user)
#             return

#         if button_id in SUB_MENUS:
#             send_sub_menu(user, button_id)
#             return

#         if button_id in SUB_ACTIONS:
#             result = SUB_ACTIONS[button_id](user)
#             send_text(user, result)
#             send_main_menu(user)
#             return

#         send_text(user, "בחירה לא מוכרת.")
#         send_main_menu(user)
#         return

#     # הודעה טקסטואלית
#     if mtype == "text":
#         send_main_menu(user)
#         return

#     # סוג הודעה אחר
#     send_text(user, "כרגע אני תומך רק בהודעות טקסט וכפתורים.")
#     send_main_menu(user)
