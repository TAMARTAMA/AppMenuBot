from docx import Document
import json

def read_word_to_text(file_path: str, max_chars: int = 4000) -> str:
    """
    קוראת קובץ Word (.docx) ומחזירה מחרוזת טקסט
    שמתאימה לשליחה בהודעת WhatsApp.

    max_chars – הגבלה למניעת חריגה ממגבלת WhatsApp
    """
    try:
        doc = Document(file_path)

        paragraphs = [
            p.text.strip()
            for p in doc.paragraphs
            if p.text and p.text.strip()
        ]

        text = "\n\n".join(paragraphs)

        # WhatsApp מגביל אורך הודעה
        if len(text) > max_chars:
            text = text[:max_chars] + "\n\n… (הטקסט קוצר)"

        return text

    except Exception as e:
        return f"שגיאה בקריאת הקובץ: {e}"
# דוגמה לשימוש:
# file_json = read_word_to_json("example.docx")
# print(json.dumps(file_json, ensure_ascii=False, indent=2))
