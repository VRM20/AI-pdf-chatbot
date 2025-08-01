from fastapi import FastAPI
from rag_chain import get_rag_chain

app = FastAPI()
qa_chain = get_rag_chain()

@app.post("/ask")
async def ask_question(question: str):
    answer = qa_chain.run(question)
    return {"answer": answer}

