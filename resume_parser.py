
import fitz
import docx
def extract_resume_text(file):
    text=""
    if file.name.endswith('.pdf'):
        doc=fitz.open(stream=file.read(), filetype="pdf")
        for page in doc:
            text+=page.get_text()
    else:
        d=docx.Document(file)
        text="\n".join([p.text for p in d.paragraphs])
    return text
