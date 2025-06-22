from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.llms import HuggingFaceEndpoint
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA
from huggingface_hub import login           # reads token from env

# ---- Free HF models ---- #
EMBED_MODEL   = "sentence-transformers/all-MiniLM-L6-v2"
CHAT_MODEL_ID = "mistralai/Mistral-7B-Instruct-v0.3"

# NB: many cpu-friendly models will work; choose any that allows free-tier inference

def build_chain(paper_text: str):
    # 1. split
    splitter = RecursiveCharacterTextSplitter(chunk_size=1300, chunk_overlap=200)
    chunks   = splitter.split_text(paper_text)

    # 2. local (free) sentence-transformer embeddings
    embedder = HuggingFaceEmbeddings(model_name=EMBED_MODEL)
    db       = FAISS.from_texts(chunks, embedder)
    retriever = db.as_retriever(search_kwargs={"k": 4})

    # 3. HF Inference-API LLM (streaming=false => free tier OK)
    llm = HuggingFaceEndpoint(
        repo_id   = CHAT_MODEL_ID,
        max_length=1024,
        temperature=0.1,
        huggingfacehub_api_token = None  # pulls from env var if present
    )

    # 4. compose Retrieval-QA chain
    return RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        return_source_documents=False,
    )
