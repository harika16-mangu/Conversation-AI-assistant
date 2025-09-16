# Conversation-AI-assistant
# JSON-RAG Assistant  

A demonstration project showcasing how to build a **Retrieval-Augmented Generation (RAG) pipeline** using a JSON knowledge base, **FAISS** for vector similarity search, **HuggingFace sentence transformers** for embeddings, and **OpenAI LLMs** for context-aware answers.  

This project highlights how semantic search can be enabled over a large JSON corpus, making information retrieval more accurate and efficient.  

---

## 🚀 Features  
- Load and parse a custom **JSON knowledge base** into retrievable documents.  
- Generate **vector embeddings** using HuggingFace `all-MiniLM-L6-V2`.  
- Store embeddings in a **FAISS vector database** for fast similarity search.  
- Perform **semantic search** over the JSON corpus with natural language queries.  
- Use **OpenAI LLMs** to generate contextual answers grounded in retrieved documents.  

---

## 🛠️ Tech Stack  
- **Python 3.10+**  
- **LangChain** (document loader, pipeline management)  
- **HuggingFace SentenceTransformers** (embeddings)  
- **FAISS** (vector similarity search)  
- **OpenAI GPT models** (answer generation)  
- **dotenv** (for API key management)  

---
## Project Structure
  ├── knowledge-base.json # Your custom JSON corpus
  ├── rag_pipeline.py # Main pipeline implementation
  ├── requirements.txt # Dependencies
  └── README.md # Project documentation
  
---
