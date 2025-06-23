# src/csv_agent.py

import pandas as pd
from transformers import pipeline
from langchain.llms import HuggingFacePipeline

def create_csv_agent(df: pd.DataFrame):
    pipe = pipeline("text2text-generation", model="google/flan-t5-large", max_length=512)
    llm = HuggingFacePipeline(pipeline=pipe)

    def answer_query(question: str) -> str:
        # Build a prompt with a small sample of the dataframe
        context = df.head(5).to_markdown()
        prompt = f"Based on this table:\n{context}\n\nAnswer the following question:\n{question}"
        response = llm(prompt)
        return response

    return answer_query
