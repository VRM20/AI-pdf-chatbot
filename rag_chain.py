from langchain.chains import RetrievalQA
from langchain_groq import ChatGroq
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.memory import ConversationBufferMemory
import os

def get_rag_chain():

    embeddings = OpenAIEmbeddings(openai_api_key=os.getenv("OPENAI_API_KEY"))

    vectordb = Chroma(persist_directory="chroma_db", embedding_function=embeddings)
    retriever = vectordb.as_retriever(search_kwargs={"k": 3})

    llm = ChatGroq(
        api_key=os.getenv("GROQ_API_KEY"),
        temperature=0,
        model_name="llama3-70b-8192"
    )

    memory = ConversationBufferMemory(
        memory_key="chat_history", return_messages=True
    )

    chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff",
        memory=memory,
        return_source_documents=True,
    )

    return chain
