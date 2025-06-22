import arxiv, fitz, tempfile, os

def pdf_to_text(path: str) -> str:
    doc = fitz.open(path)
    text = "\n".join(page.get_text() for page in doc)
    return text

def fetch_arxiv(arxiv_id_or_url: str) -> str:
    if "/" in arxiv_id_or_url:
        arxiv_id_or_url = arxiv_id_or_url.split("/")[-1]
    search = arxiv.Search(id_list=[arxiv_id_or_url])
    paper = next(search.results())
    pdf_path = tempfile.mktemp(suffix=".pdf")
    paper.download_pdf(filename=pdf_path)
    return pdf_path
