from langchain_community.llms import HuggingFaceHub
from langchain.agents import create_pandas_dataframe_agent

def load_llm():
    return HuggingFaceHub(
        repo_id="google/flan-t5-large",
        model_kwargs={"temperature": 0, "max_length": 512}
    )

def create_csv_agent(df):
    llm = load_llm()
    return create_pandas_dataframe_agent(llm, df, verbose=True)
