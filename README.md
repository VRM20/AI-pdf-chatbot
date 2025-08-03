# 🤖 AI-Powered PDF Chatbot with Groq, LangChain & Streamlit

Ask anything about your PDFs — this chatbot understands and answers using real-time document context with blazing-fast LLMs.

---

## 🚀 Features

- ✅ Upload any PDF and chat with it instantly  
- ⚡ Powered by [Groq](https://groq.com)'s ultra-fast LLMs (`llama-3.3-70b-versatile`)  
- 🧠 Conversational memory (remembers chat history)  
- 🔍 Answers grounded in real source pages  
- 🔒 Secure API access with environment secrets  
- 📚 Built with LangChain (RAG), ChromaDB, and Streamlit  

---

## 🧱 Architecture

1. 📄 PDF uploaded via Streamlit UI  
2. 📃 Text extracted using PyMuPDF  
3. 📚 Split into chunks for better context  
4. 🧠 Embedded with HuggingFace + stored in ChromaDB  
5. 💬 User asks question → Groq LLM with LangChain retrieves + answers  

---

## 🛠 Tech Stack

- `Streamlit` — Interactive frontend  
- `LangChain` — RAG + memory + retrieval  
- `Groq` — Hosted LLMs (`llama-3.3-70b-versatile`)  
- `ChromaDB` — Local vector store  
- `HuggingFace Embeddings` — Document chunk encoding  
- `PyMuPDF` — PDF parsing  

---

## 📦 Installation

```bash
git clone https://github.com/yourusername/ai-pdf-chatbot.git
cd ai-pdf-chatbot

pip install -r requirements.txt

To run this app locally:
streamlit run app.py
