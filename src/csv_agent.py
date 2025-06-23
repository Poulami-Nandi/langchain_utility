import pandas as pd
from transformers import pipeline
from langchain.llms import HuggingFacePipeline

def create_csv_agent(df: pd.DataFrame):
    pipe = pipeline("text2text-generation", model="google/flan-t5-large", max_length=512)
    llm = HuggingFacePipeline(pipeline=pipe)

    def answer_query(question: str) -> str:
        context = df.head(5).to_markdown()
        prompt = f"Answer the question based on this CSV table preview:\n\n{context}\n\nQuestion: {question}"
        return llm(prompt)

    return answer_query
