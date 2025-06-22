"""
Paper Explainer – Streamlit front-end
------------------------------------

Upload a PDF or paste an arXiv ID ➜ we extract the text, build a
LangChain Retrieval-QA pipeline (FAISS + OpenAI), and let the user
ask questions about the paper.

Prerequisites
-------------
•   pip install -U streamlit langchain langchain-community faiss-cpu
•   Set OPENAI_API_KEY in your environment (or Streamlit Secrets)
"""

import os
import tempfile
import streamlit as st

# ――― Internal utility wrappers ――― #
from src.loader import pdf_to_text, fetch_arxiv     #  ➜ text extraction helpers
from src.qa_chain import build_chain                #  ➜ LangChain pipeline
#os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]
os.environ["OPENAI_API_KEY"] = "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"

# -------------------------------------------------------------------------- #
# Page set-up
# -------------------------------------------------------------------------- #
st.set_page_config(page_title="Paper Explainer", page_icon="🧑‍🔬")
st.title("🧑‍🔬📄  Paper Explainer")
st.markdown(
    "Ask questions about scientific papers. Upload a PDF **or** enter an arXiv ID, "
    "then query away!"
)

# -------------------------------------------------------------------------- #
# 1️⃣  Paper input
# -------------------------------------------------------------------------- #
col1, col2 = st.columns(2)
with col1:
    uploaded_file = st.file_uploader("**Upload PDF**", type=["pdf"])

with col2:
    arxiv_id = st.text_input(
        "**…or enter arXiv ID**",
        placeholder="e.g. 2403.12345",
        help="We’ll fetch the PDF directly from arXiv."
    )

# Resolve to a local temp-file called `file_path`
file_path: str | None = None

if uploaded_file is not None:
    # Save user PDF to a named temp file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(uploaded_file.read())
        file_path = tmp.name

elif arxiv_id:
    try:
        with st.spinner("Fetching PDF from arXiv…"):
            file_path = fetch_arxiv(arxiv_id)       # returns local path
    except Exception as e:
        st.error(f"❌ Could not fetch arXiv paper: {e}")
        file_path = None

# -------------------------------------------------------------------------- #
# 2️⃣  When we have a file, build the QA chain
# -------------------------------------------------------------------------- #
if file_path:
    try:
        with st.spinner("🔍 Extracting text…"):
            paper_text = pdf_to_text(file_path)

        # Build (or cache) the Retrieval-QA chain
        with st.spinner("⚙️ Building QA chain…"):
            qa_chain = build_chain(paper_text)

        st.success("Ready! Ask a question about the paper below.")
        user_q = st.text_input("**Your question**")

        if user_q:
            with st.spinner("🤖 Generating answer…"):
                response = qa_chain({"query": user_q})
            st.markdown("**Answer**")
            st.write(response["result"])

    finally:
        # Clean up temp file
        if os.path.exists(file_path):
            os.remove(file_path)

else:
    st.info("👆 Upload a PDF or enter an arXiv ID to get started.")
