import streamlit as st
from src.qa_chain import build_chain

st.set_page_config(page_title="📄 Research Paper QA")
st.title("📄 Ask Your Research Paper")

with st.expander("Instructions"):
    st.markdown("""
    1. Upload a PDF or paste the text of a research paper.
    2. Ask a question about the content.
    3. The model will extract relevant parts and answer.
    """)

text = ""  # ✅ Define it at the top to avoid NameError

input_mode = st.radio("Select input type", ["📄 Upload PDF", "📝 Paste text"])

if input_mode == "📄 Upload PDF":
    uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")
    if uploaded_file:
        try:
            import fitz  # PyMuPDF
            pdf = fitz.open(stream=uploaded_file.read(), filetype="pdf")
            text = ""
            for page in pdf:
                text += page.get_text()
        except Exception as e:
            st.error(f"PDF loading failed: {e}")
            st.stop()

elif input_mode == "📝 Paste text":
    text = st.text_area("Paste the research paper text here")

if text.strip():  # ✅ Added `.strip()` to prevent false positives from empty strings
    query = st.text_input("Ask a question about the paper:")
    if query:
        with st.spinner("Running QA..."):
            qa_chain = build_chain(text)
            answer = qa_chain.run(query)
            st.markdown("### 🧠 Answer")
            st.success(answer)
