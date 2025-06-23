import streamlit as st, os
from src.loader import pdf_to_text, fetch_arxiv
from src.qa_chain import build_chain

st.set_page_config(page_title="🧑‍🔬 Paper Explainer – (100 % HF free tier)")

st.title("🧑‍🔬📄  Paper Explainer")
st.markdown(
"""
Upload a **scientific PDF** or paste an **arXiv link / ID**.  
The app builds an in-memory FAISS index with sentence-transformer embeddings and
uses the free **Mistral-7B-Instruct** endpoint on Hugging Face to answer questions.
""")

import os
os.environ["HUGGINGFACEHUB_API_TOKEN"] = st.secrets["HUGGINGFACEHUB_API_TOKEN"]

# ---------- SIDEBAR: Hugging Face token (optional) ----------
with st.sidebar:
    st.header("🔑 Hugging Face token (optional)")
    if "HUGGINGFACEHUB_API_TOKEN" not in os.environ:
        token = st.text_input("HF token (leave blank for anonymous):",
                              type="password", help="Needed for higher rate-limit")
        if token:
            os.environ["HUGGINGFACEHUB_API_TOKEN"] = token

# ---------- Input ---------- #
mode = st.radio("Choose input source:", ["Upload PDF", "arXiv ID/URL"])
paper_text = None

if mode == "Upload PDF":
    uploaded = st.file_uploader("Drag a PDF here", type=["pdf"])
    if uploaded:
        with st.spinner("📑 Reading PDF…"):
            paper_text = pdf_to_text(uploaded)
else:
    arx = st.text_input("arXiv ID or URL", placeholder="2406.01234  or  https://arxiv.org/abs/2406.01234")
    if arx:
        with st.spinner("⬇️  Fetching & parsing…"):
            paper_text = fetch_arxiv(arx.strip())

# ---------- Build QA chain ----------
if paper_text:
    st.success("✅ Paper text loaded.")
    if st.checkbox("Show raw text (debug)", False):
        st.write(paper_text[:4000] + "…")
    with st.spinner("⚙️  Building embeddings + LLM chain… (first run ~30 s)"):
        qa_chain = build_chain(paper_text)

    # QA loop
    st.success("Ready! Ask a question👇")
    user_q = st.text_input("**Your question**")
    if user_q:
        with st.spinner("🤔 Thinking…"):
            answer = qa_chain.invoke({"query": user_q})["result"]
        st.markdown("**Answer:**")
        st.write(answer)
