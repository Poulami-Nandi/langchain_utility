# streamlit_app.py

import streamlit as st
import pandas as pd
from src.loader import pdf_to_text
from src.qa_chain import build_chain
from src.csv_agent import create_csv_agent

st.set_page_config(page_title="LangChain Utility", layout="centered")
st.title("LangChain Utility – PDF & CSV Explainer")

mode = st.radio("Choose file type to analyze:", ("PDF (Research Paper)", "CSV File"), horizontal=True)

if mode == "PDF (Research Paper)":
    uploaded_pdf = st.file_uploader("Upload a PDF file", type="pdf")
    if uploaded_pdf:
        try:
            with st.spinner("Extracting text..."):
                text = pdf_to_text(uploaded_pdf)
            st.success("PDF loaded and processed!")
            qa_chain = build_chain(text)

            query = st.text_input("Ask a question about the paper:")
            if query:
                with st.spinner("Thinking..."):
                    answer = qa_chain(query)
                    st.success(answer)
        except Exception as e:
            st.error(f"Error: {e}")

elif mode == "CSV File":
    uploaded_csv = st.file_uploader("Upload a CSV file", type="csv")
    if uploaded_csv:
        try:
            df = pd.read_csv(uploaded_csv)
            st.dataframe(df.head())
            csv_agent = create_csv_agent(df)

            query = st.text_input("Ask a question about your data:")
            if query:
                with st.spinner("Thinking..."):
                    result = csv_agent(query)
                    st.success(result)
        except Exception as e:
            st.error(f"Error: {e}")
