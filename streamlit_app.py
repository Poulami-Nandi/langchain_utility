import streamlit as st
from src.loader import pdf_to_text
from src.qa_chain import build_chain

st.set_page_config(page_title="📄 Research Paper QA")
st.title("📄 Ask Your Research Paper")

uploaded_file = st.file_uploader("Upload a PDF paper", type=["pdf"])

if uploaded_file:
    text = pdf_to_text(uploaded_file)
    st.success("PDF Loaded. Generating embeddings...")

    with st.spinner("Building QA system..."):
        qa_chain = build_chain(text)

    st.success("Ready! Ask a question below.")

    query = st.text_input("Your question:")
    if query:
        with st.spinner("Thinking..."):
            answer = qa_chain.run(query)
        st.write("### 💡 Answer:")
        st.write(answer)
