import streamlit as st
import tempfile
from read_pdf import extract_text_from_pdf
from split_chunks import split_into_chunks
from embed_store import store_chunks_in_chroma
from rag_chain import get_rag_chain

st.set_page_config(page_title="🧠 Ask Your PDF", layout="centered")

st.title("🧠 Ask Your PDF")
st.caption("Ask questions to your PDF using Groq + ChromaDB + LangChain")

pdf_file = st.file_uploader("📄 Upload your PDF", type=["pdf"])

if pdf_file:
    with st.spinner("Reading and processing PDF..."):
        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            tmp.write(pdf_file.read())
            tmp_path = tmp.name

        text = extract_text_from_pdf(tmp_path)
        chunks = split_into_chunks(text)

        store_chunks_in_chroma(chunks)

        st.success("✅ PDF processed and indexed!")

    user_question = st.text_input("💬 Ask a question about your PDF")

    if user_question:
        qa_chain = get_rag_chain()
        with st.spinner("Thinking..."):
            response = qa_chain.invoke({"query": user_question})
            answer = response["result"]
        st.markdown("### 🤖 Answer")
        st.success(answer)
