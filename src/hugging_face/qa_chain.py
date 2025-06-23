from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.llms import HuggingFaceHub
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA

# ---- Free HF models ---- #
EMBED_MODEL   = "sentence-transformers/all-MiniLM-L6-v2"
CHAT_MODEL_ID = "mistralai/Mistral-7B-Instruct-v0.3"
#CHAT_MODEL_ID = "HuggingFaceH4/zephyr-7b-alpha"
from langchain_community.llms import HuggingFaceHub

def build_chain(paper_text: str):
    # 1. Split paper into chunks
    splitter = RecursiveCharacterTextSplitter(chunk_size=1300, chunk_overlap=200)
    chunks = splitter.split_text(paper_text)

    # 2. Convert chunks to vector embeddings
    embedder = HuggingFaceEmbeddings(model_name=EMBED_MODEL)
    db = FAISS.from_texts(chunks, embedder)
    retriever = db.as_retriever(search_kwargs={"k": 4})

    # 3. Use HuggingFaceHub wrapper (not HuggingFaceEndpoint!)
    from langchain_community.llms import HuggingFaceHub

    llm = HuggingFaceHub(
        repo_id="HuggingFaceH4/zephyr-7b-beta",  # or another supported repo_id
        model_kwargs={
            "temperature": 0.5,
            "max_new_tokens": 512
        },
        task="text-generation",
        huggingfacehub_api_token=os.environ["HUGGINGFACEHUB_API_TOKEN"]
    )

    # 4. Return the retrieval-augmented QA chain
    return RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        return_source_documents=False
    )
