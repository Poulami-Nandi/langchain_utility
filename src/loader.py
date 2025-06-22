"""
Light-weight helpers for (1) converting a local or remote PDF to text,
and (2) pulling the plain-text abstract + body from an arXiv paper.
"""
from pathlib import Path
import tempfile, os, requests, fitz

# -------- PDF ---------- #
def pdf_to_text(uploaded_file) -> str:
    """Streamlit UploadedFile -> str (all pages concatenated)."""
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(uploaded_file.read())
        tmp.flush()
        doc = fitz.open(tmp.name)
        text = "\n".join(page.get_text() for page in doc)
    os.unlink(tmp.name)
    return text or "❌ Could not extract any text."

# -------- arXiv -------- #
def fetch_arxiv(arxiv_id_or_url: str) -> str:
    """Return raw text of arXiv PDF given an ID or https link."""
    if arxiv_id_or_url.startswith("http"):
        pdf_url = arxiv_id_or_url.replace("abs", "pdf") + ".pdf"
    else:
        pdf_url = f"https://ar5iv.org/pdf/{arxiv_id_or_url}.pdf"
    response = requests.get(pdf_url, timeout=30)
    response.raise_for_status()
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as f:
        f.write(response.content)
        f.flush()
        text = pdf_to_text(Path(f.name).open("rb"))
    os.unlink(f.name)
    return text
