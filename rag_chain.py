from langchain.chains import RetrievalQA
from langchain_groq import ChatGroq
from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.memory import ConversationBufferMemory

def get_rag_chain():

    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vectordb = Chroma(persist_directory="chroma_db", embedding_function=embeddings)
    retriever = vectordb.as_retriever(search_kwargs = {"k":3})

    llm = ChatGroq(
        api_key = "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",
        temperature = 0,
        model_name = "llama-3.3-70b-versatile"
    )

    memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True,
        output_key="result"
    )

    chain = RetrievalQA.from_chain_type(
        llm=llm, 
        retriever=retriever, 
        chain_type="stuff",
        memory=memory,
        return_source_documents=True,
        output_key="result"
        )

    return chain

