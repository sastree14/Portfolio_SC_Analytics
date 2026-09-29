import fitz

def extract_text(path: str) -> str:
    doc=fitz.open(path)
    return "\n".join(page.get_text("text") for page in doc)
