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

    "SUB_1_1_B1": lambda u: read_word_to_json(file_path / "התייעצות" / "מאכלי תימן" / "תבלינים" / "חוויג למרק.docx"),
    "SUB_1_1_B2": lambda u: read_word_to_json(file_path / "התייעצות" / "מאכלי תימן" / "תבלינים" / "חוויג לקפה.docx"),

    "SUB_1_1_C1": lambda u: read_word_to_json(file_path / "התייעצות" / "מאכלי תימן" / "תבשילים פרווה" / "הריש.docx"),

    "SUB_1_1_D1": lambda u: read_word_to_json(file_path / "התייעצות" / "מאכלי תימן" / "תבשילים חלבים" / "זאום(מטיט).docx"),
    "SUB_1_1_D2": lambda u: read_word_to_json(file_path / "התייעצות" / "מאכלי תימן" / "תבשילים חלבים" / "פתות מצות(חלבי פסח).docx"),

    "SUB_1_1_E1": lambda u: read_word_to_json(file_path / "התייעצות" / "מאכלי תימן" / "מטבלים" / "דוכה לפסח.docx"),
    "SUB_1_1_E2": lambda u: read_word_to_json(file_path / "התייעצות" / "מאכלי תימן" / "מטבלים" / "זחוק יבש.docx"),
    "SUB_1_1_E3": lambda u: read_word_to_json(file_path / "התייעצות" / "מאכלי תימן" / "מטבלים" / "חילבה ירוקה.docx"),
    "SUB_1_1_E4": lambda u: read_word_to_json(file_path / "התייעצות" / "מאכלי תימן" / "מטבלים" / "סחוק  במדאק (די יבש).docx"),
    "SUB_1_1_E5": lambda u: read_word_to_json(file_path / "התייעצות" / "מאכלי תימן" / "מטבלים" / "סמנה.docx"),

    "SUB_1_1_F1": lambda u: read_word_to_json(file_path / "התייעצות" / "מאכלי תימן" / "תבשילים בשריים" / "מרק כורעי - רגל.docx"),
    "SUB_1_1_F2": lambda u: read_word_to_json(file_path / "התייעצות" / "מאכלי תימן" / "תבשילים בשריים" / "מחשוש.docx"),
    "SUB_1_1_F3": lambda u: read_word_to_json(file_path / "התייעצות" / "מאכלי תימן" / "תבשילים בשריים" / "פתות מרק.docx"),
    "SUB_1_1_F4": lambda u: read_word_to_json(file_path / "התייעצות" / "מאכלי תימן" / "תבשילים בשריים" / "מרק עוף.docx"),
    "SUB_1_1_F5": lambda u: read_word_to_json(file_path / "התייעצות" / "מאכלי תימן" / "תבשילים בשריים" / "מרק בשר.docx"),

    "SUB_1_1_H1": lambda u: read_word_to_json(file_path / "התייעצות" / "מאכלי תימן" / "מאפים" / "גחנון.docx"),
    "SUB_1_1_H2": lambda u: read_word_to_json(file_path / "התייעצות" / "מאכלי תימן" / "מאפים" / "כובאנה (חלבית) זלאביות .docx"),
    "SUB_1_1_H3": lambda u: read_word_to_json(file_path / "התייעצות" / "מאכלי תימן" / "מאפים" / "כובאנה (פרווה) מפטלה.docx"),
    "SUB_1_1_H4": lambda u: read_word_to_json(file_path / "התייעצות" / "מאכלי תימן" / "מאפים" / "לחוח.docx"),
    "SUB_1_1_H5": lambda u: read_word_to_json(file_path / "התייעצות" / "מאכלי תימן" / "מאפים" / "מלווח'.docx"),
    "SUB_1_1_H6": lambda u: read_word_to_json(file_path / "התייעצות" / "מאכלי תימן" / "מאפים" / "זלאביא.docx"),
    "SUB_1_1_H7": lambda u: read_word_to_json(file_path / "התייעצות" / "מאכלי תימן" / "מאפים" / "צלוף.docx"),

    "SUB_1_1_I1": lambda u: read_word_to_json(file_path / "התייעצות" / "מאכלי תימן" / "משקים" / "קפה קשר.docx"),

    "SUB_1_2_A": lambda u: read_word_to_json(file_path / "התייעצות" / "צמחי תימן" / "האתרוג.docx"),
    "SUB_1_2_B": lambda u: read_word_to_json(file_path / "התייעצות" / "צמחי תימן" / "הבבונג.docx"),
    "SUB_1_2_C": lambda u: read_word_to_json(file_path / "התייעצות" / "צמחי תימן" / "הגרגיר.docx"),
    "SUB_1_2_D": lambda u: read_word_to_json(file_path / "התייעצות" / "צמחי תימן" / "החילבה.docx"),  
    "SUB_1_2_E": lambda u: read_word_to_json(file_path / "התייעצות" / "צמחי תימן" / "הכחול.docx"),
    "SUB_1_2_F": lambda u: read_word_to_json(file_path / "התייעצות" / "צמחי תימן" / "הכמון.docx"),
    "SUB_1_2_G": lambda u: read_word_to_json(file_path / "התייעצות" / "צמחי תימן" / "המכווה.docx"),
    "SUB_1_2_H": lambda u: read_word_to_json(file_path / "התייעצות" / "צמחי תימן" / "הקאת.docx"),
    "SUB_1_2_I": lambda u: read_word_to_json(file_path / "התייעצות" / "צמחי תימן" / "הרדוף הנחלים.docx"),
    "SUB_1_2_J": lambda u: read_word_to_json(file_path / "התייעצות" / "צמחי תימן" / "הריחאן.docx"),
    "SUB_1_2_K": lambda u: read_word_to_json(file_path / "התייעצות" / "צמחי תימן" / "הרימון.docx"),
    "SUB_1_2_L": lambda u: read_word_to_json(file_path / "התייעצות" / "צמחי תימן" / "השדאב.docx"),
    "SUB_1_2_M": lambda u: read_word_to_json(file_path / "התייעצות" / "צמחי תימן" / "שיער הראש.docx"),

    "SUB_1_3_A": lambda u: read_word_to_json(file_path / "התייעצות" / "רפואות תימן" / "סגולות רפואיות בדומם.docx"),
    "SUB_1_3_B": lambda u: read_word_to_json(file_path / "התייעצות" / "רפואות תימן" / "סגולות רפואיות החי.docx"),
    "SUB_1_3_C": lambda u: read_word_to_json(file_path / "התייעצות" / "רפואות תימן" / "סגולות רפואיות במזון.docx"),
    "SUB_1_3_D": lambda u: read_word_to_json(file_path / "התייעצות" / "רפואות תימן" / "סגולות רפואיות בצומח.docx"),

    "SUB_1_2": lambda u: action_generic("SUB_1_2", u),
    "SUB_1_3": lambda u: action_generic("SUB_1_3", u),
    "SUB_2_1": lambda u: action_generic("SUB_2_1", u),
    "SUB_2_2": lambda u: action_generic("SUB_2_2", u),
    "SUB_2_3": lambda u: action_generic("SUB_2_3", u),
    "SUB_3_1": lambda u: action_generic("SUB_3_1", u),
    "SUB_3_2": lambda u: action_generic("SUB_3_2", u),
    "SUB_3_3": lambda u: action_generic("SUB_3_3", u),
}

