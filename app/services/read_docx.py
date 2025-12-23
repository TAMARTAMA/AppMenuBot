from docx import Document
import json

def read_word_to_json(file_path: str) -> dict:
    """
    מקבלת נתיב לקובץ Word (.docx) ומחזירה את תוכנו במבנה JSON.
    כל פסקה בקובץ נשמרת כרשומה ברשימת 'paragraphs'.
    """
    try:
        doc = Document(file_path)
        paragraphs = [p.text for p in doc.paragraphs if p.text.strip() != ""]
        data = {"file_name": file_path, "paragraphs": paragraphs}
        return data
    except Exception as e:
        return {"error": str(e)}

# דוגמה לשימוש:
# file_json = read_word_to_json("example.docx")
# print(json.dumps(file_json, ensure_ascii=False, indent=2))
