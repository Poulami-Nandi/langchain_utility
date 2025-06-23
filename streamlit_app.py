import streamlit as st
import pandas as pd
from src.loader import pdf_to_text
from src.qa_chain import build_chain
from src.csv_agent import create_csv_agent

st.set_page_config(page_title="LangChain Utility", layout="centered")
st.title("LangChain Utility – PDF & CSV Agent")

option = st.radio("Choose a Mode:", ("📄 Ask Your PDF", "📊 Ask Your CSV"))

if option == "📄 Ask Your PDF":
    uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")
    if uploaded_file:
        with st.spinner("Reading your paper..."):
            text = pdf_to_text(uploaded_file)
            qa_chain = build_chain(text)

        query = st.text_input("Ask a question about the research paper:")
        if query:
            with st.spinner("Thinking..."):
                answer = qa_chain.run(query)
                st.success(answer)

elif option == "📊 Ask Your CSV":
    uploaded_csv = st.file_uploader("Upload a CSV file", type="csv")
    if uploaded_csv:
        df = pd.read_csv(uploaded_csv)
        st.dataframe(df.head())
        agent = create_csv_agent(df)

        query = st.text_input("Ask a question about your data:")
        if query:
            with st.spinner("Thinking..."):
                result = agent.run(query)
                st.success(result)
