from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma

def store_chunks_in_chroma(chunks):
    embeddings = OpenAIEmbeddings(openai_api_key=os.getenv("OPENAI_API_KEY"))
    vectordb = Chroma.from_texts(chunks, embeddings, persist_directory="chroma_db")
    vectordb.persist()

    return vectordb
