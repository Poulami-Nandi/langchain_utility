import streamlit as st, os, tempfile
from src.loader import pdf_to_text, fetch_arxiv
from src.qa_chain import build_chain

st.set_page_config(page_title="Paper Explainer", page_icon="🧑‍🔬")

st.title("🧑‍🔬 AI Research Paper Explainer")
mode = st.radio("Add paper by…", ["Upload PDF", "arXiv URL / ID"], horizontal=True)

if mode == "Upload PDF":
    pdf = st.file_uploader("Upload a PDF", type="pdf")
    if pdf:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            tmp.write(pdf.getbuffer())
            path = tmp.name
elif mode == "arXiv URL / ID":
    arxiv_id = st.text_input("arXiv ID or URL")
    if arxiv_id:
        with st.spinner("Downloading…"):
            path = fetch_arxiv(arxiv_id)
else:
    path = None

if path:
    with st.spinner("Parsing & indexing…"):
        text = pdf_to_text(path)
        qa = build_chain(text)
    st.success("Ready! Ask anything about the paper ⬇️")
    query = st.text_input("Question")
    if query:
        with st.spinner("Thinking…"):
            answer = qa.run(query)
        st.markdown("#### Answer")
        st.write(answer)
        if st.checkbox("👀 Show raw extraction chunks"):
            st.write(text[:3000] + "…")
