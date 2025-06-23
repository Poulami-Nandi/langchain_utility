from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

from langchain.chains import RetrievalQA
from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.llms import HuggingFacePipeline
from transformers import pipeline


EMBED_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
QA_MODEL = "deepset/roberta-base-squad2"

def build_chain(document_text: str):
    # Chunk the text
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    chunks = splitter.split_text(document_text)

    # Embed & store in FAISS
    embeddings = HuggingFaceEmbeddings(model_name=EMBED_MODEL)
    db = FAISS.from_texts(chunks, embeddings)
    retriever = db.as_retriever()

    # HuggingFace LLM
    pipe = pipeline("question-answering", model=QA_MODEL, tokenizer=QA_MODEL)
    llm = HuggingFacePipeline(pipeline=pipe)

    # Chain
    chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    return chain
