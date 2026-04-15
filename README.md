# 🤖 RAG Chatbot Pro

A smart AI chatbot that answers questions from uploaded PDFs using Retrieval-Augmented Generation (RAG).

---

## 🚀 Features

- 📄 Upload any PDF
- 🔍 Semantic search using FAISS
- 🧠 Context-aware answers using FLAN-T5
- 📊 Performance dashboard (response time, confidence, context length)
- 💬 Chat-like UI
- 📚 Source highlighting

---

## 🛠️ Tech Stack

- Python
- Streamlit
- LangChain
- FAISS
- HuggingFace Transformers

---

## ⚙️ How It Works

1. PDF is loaded and split into chunks  
2. Chunks are converted into embeddings  
3. Stored in vector database (FAISS)  
4. Query is matched with relevant chunks  
5. LLM generates answer using retrieved context  

---

## ▶️ Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
