from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma

def store_chunks_in_chroma(chunks):
    embeddings = HuggingFaceEmbeddings(model_name = "all-MiniLM-L6-v2")
    vectordb = Chroma.from_texts(chunks, embeddings, persist_directory="chroma_db")
    vectordb.persist()

    return vectordb

