from app.services.read_docx import read_word_to_json
from pathlib import Path
file_path = Path(__file__).parent.parent / "mas.docx"

MAIN_MENU = [
    {"id": "MAIN_1", "title": "התייעצות"},
    {"id": "MAIN_2", "title": "הורדות"},
    {"id": "MAIN_3", "title": "מידע שימושי"},
]

SUB_MENUS = {
    "MAIN_1": [
        {"id": "SUB_1_1", "title": "מאכלי תימן"},
        {"id": "SUB_1_2", "title": "צמחי תימן"},
        {"id": "SUB_1_3", "title": "רפואות תימן"},
    ],
    "MAIN_2": [
        {"id": "SUB_2_1", "title": "תת-אפשרות 2-1"},
        {"id": "SUB_2_2", "title": "תת-אפשרות 2-2"},
        {"id": "SUB_2_3", "title": "תת-אפשרות 2-3"},
    ],
    "MAIN_3": [
        {"id": "SUB_3_1", "title": "תת-אפשרות 3-1"},
        {"id": "SUB_3_2", "title": "תת-אפשרות 3-2"},
        {"id": "SUB_3_3", "title": "תת-אפשרות 3-3"},
    ],
    "SUB_1_1": [
        {"id": "SUB_1_1_A", "title": "קינוחים"},
        {"id": "SUB_1_1_B", "title": "תבלינים"},
        {"id": "SUB_1_1_C", "title": "תבשילים פרווה"},
        {"id": "SUB_1_1_D", "title": "תבשילים חלבים"},
        {"id": "SUB_1_1_E", "title": "מטבלים"},
        {"id": "SUB_1_1_F", "title": "תבשילים בשריים"},
        {"id": "SUB_1_1_G", "title": "תבשילים חלבים"},
        {"id": "SUB_1_1_H", "title": "מאפים"},
        {"id": "SUB_1_1_I", "title": "משקים"},
    ],
    "SUB_1_1_A": [
        {"id": "SUB_1_1_A1", "title": "מקסקס"}
    ]
}


def action_generic(action_id: str, user: str) -> str:
    print(f"⚙️ Running action {action_id} for user {user}")
    return f"✅ הפעולה {action_id} בוצעה בהצלחה"

SUB_ACTIONS = {
    "SUB_1_1_A1": lambda u: read_word_to_json(file_path),
    "SUB_1_2": lambda u: action_generic("SUB_1_2", u),
    "SUB_1_3": lambda u: action_generic("SUB_1_3", u),
    "SUB_2_1": lambda u: action_generic("SUB_2_1", u),
    "SUB_2_2": lambda u: action_generic("SUB_2_2", u),
    "SUB_2_3": lambda u: action_generic("SUB_2_3", u),
    "SUB_3_1": lambda u: action_generic("SUB_3_1", u),
    "SUB_3_2": lambda u: action_generic("SUB_3_2", u),
    "SUB_3_3": lambda u: action_generic("SUB_3_3", u),
}

