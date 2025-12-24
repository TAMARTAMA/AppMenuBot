from app.services.read_docx import read_word_to_json
from pathlib import Path
file_path = Path(__file__).parent.parent.parent / "data" 


def action_generic(action_id: str, user: str) -> str:
    print(f"⚙️ Running action {action_id} for user {user}")
    return f"✅ הפעולה {action_id} בוצעה בהצלחה"

SUB_ACTIONS = {
    "SUB_1_1_A1": lambda u: read_word_to_json(file_path / "התייעצות" / "מאכלי תימן" / "קינוחים" / "מקסקס.docx"),
    "SUB_1_1_A2": lambda u: read_word_to_json(file_path / "התייעצות" / "מאכלי תימן" / "קינוחים" / "געלה.docx"),
    "SUB_1_1_A3": lambda u: read_word_to_json(file_path / "התייעצות" / "מאכלי תימן" / "קינוחים" / "כעכות.docx"),
    "SUB_1_1_A4": lambda u: read_word_to_json(file_path / "התייעצות" / "מאכלי תימן" / "קינוחים" / "לסיס.docx"),
    "SUB_1_1_A5": lambda u: read_word_to_json(file_path / "התייעצות" / "מאכלי תימן" / "קינוחים" / "עטאר.docx"),
    "SUB_1_2": lambda u: action_generic("SUB_1_2", u),
    "SUB_1_3": lambda u: action_generic("SUB_1_3", u),
    "SUB_2_1": lambda u: action_generic("SUB_2_1", u),
    "SUB_2_2": lambda u: action_generic("SUB_2_2", u),
    "SUB_2_3": lambda u: action_generic("SUB_2_3", u),
    "SUB_3_1": lambda u: action_generic("SUB_3_1", u),
    "SUB_3_2": lambda u: action_generic("SUB_3_2", u),
    "SUB_3_3": lambda u: action_generic("SUB_3_3", u),
}

