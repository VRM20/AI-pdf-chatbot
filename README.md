# 🤖 AI-Powered PDF Chatbot with Groq, LangChain & Streamlit

Ask anything about your PDFs — this chatbot understands and answers using real-time document context with blazing-fast LLMs.

![Demo Screenshot](./screenshot.png) <!-- optional -->

---

## 🚀 Features

- ✅ Upload any PDF and chat with it instantly
- ⚡ Powered by [Groq](https://groq.com)'s ultra-fast LLMs (`mistral-saba-24b`)
- 🧠 Conversational memory (remembers chat history)
- 🔍 Answers grounded in real source pages
- 🔒 Secure API access with environment secrets
- 📚 Built with LangChain (RAG), ChromaDB, and Streamlit

---
## 🧱 Architecture
---

## 🛠 Tech Stack

- `Streamlit` — Interactive frontend
- `LangChain` — RAG + memory + retrieval
- `Groq` — Hosted LLMs (`mistral-saba-24b`)
- `ChromaDB` — Local vector store
- `HuggingFace Embeddings` — Document chunk encoding
- `PyMuPDF` — PDF parsing

---
## 📦 Installation

```bash
git clone https://github.com/yourusername/ai-pdf-chatbot.git
cd ai-pdf-chatbot

pip install -r requirements.txt
