from langchain_community.llms import HuggingFacePipeline
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.docstore.document import Document
from transformers import pipeline
from sentence_transformers import SentenceTransformer

def build_chain(paper_text: str):
    # Load embedding model
    embed_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    # Split text
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    splits = splitter.split_documents([Document(page_content=paper_text)])

    # Vector store
    vectorstore = FAISS.from_documents(splits, embed_model)

    # HuggingFace pipeline model
    pipe = pipeline(
        "text2text-generation",
        model="google/flan-t5-base",
        tokenizer="google/flan-t5-base",
        max_length=256,
        do_sample=False,
    )

    llm = HuggingFacePipeline(pipeline=pipe)

    # Retrieval QA chain
    chain = RetrievalQA.from_chain_type(llm=llm, retriever=vectorstore.as_retriever())
    return chain
