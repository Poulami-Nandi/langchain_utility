from langchain_experimental.agents import create_pandas_dataframe_agent
from langchain_community.llms import HuggingFaceHub  # or the newer langchain_huggingface version

def load_llm():
    return HuggingFaceHub(
        repo_id="google/flan-t5-large",
        model_kwargs={"temperature": 0, "max_length": 512}
    )

def create_csv_agent(df):
    llm = load_llm()
    return create_pandas_dataframe_agent(
        llm, df, verbose=True, allow_dangerous_code=True
    )
