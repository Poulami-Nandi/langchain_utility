from PyPDF2 import PdfReader
from typing import Union

def pdf_to_text(uploaded_file: Union[str, bytes]) -> str:
    reader = PdfReader(uploaded_file)
    return "\n".join([page.extract_text() or "" for page in reader.pages])
