# Conversation-AI-assistant
JSON-RAG Assistant

A demonstration project showcasing how to build a Retrieval-Augmented Generation (RAG) pipeline using a JSON knowledge base, FAISS for vector similarity search, HuggingFace sentence transformers for embeddings, and OpenAI LLMs for context-aware answers.

This project highlights how semantic search can be enabled over a large JSON corpus, making information retrieval more accurate and efficient.

🚀 Features

Load and parse a custom JSON knowledge base into retrievable documents.

Generate vector embeddings using HuggingFace all-MiniLM-L6-V2.

Store embeddings in a FAISS vector database for fast similarity search.

Perform semantic search over the JSON corpus with natural language queries.

Use OpenAI LLMs to generate contextual answers grounded in retrieved documents.

🛠️ Tech Stack

Python 3.10+

LangChain (document loader, pipeline management)

HuggingFace SentenceTransformers (embeddings)

FAISS (vector similarity search)

OpenAI GPT models (answer generation)

dotenv (for API key management)

📂 Project Structure
├── knowledge-base.json       # Your custom JSON corpus
├── rag_pipeline.py           # Main pipeline implementation
├── requirements.txt          # Dependencies
└── README.md                 # Project documentation

⚙️ Installation

Clone the repository:

git clone https://github.com/your-username/json-rag-assistant.git
cd json-rag-assistant


Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows


Install dependencies:

pip install -r requirements.txt


Add your OpenAI API key to a .env file:

OPENAI_API_KEY=your_api_key_here

▶️ Usage

Run the pipeline:

python rag_pipeline.py


Example query:

What is the difference between supervised and unsupervised learning?


Example output:

Retrieves the most relevant snippets from the JSON knowledge base.

Generates a concise, contextual answer using OpenAI LLM.

📊 Example Workflow

Load knowledge-base.json with LangChain JSONLoader.

Create embeddings with HuggingFace all-MiniLM-L6-V2.

Store embeddings in FAISS.

Perform semantic similarity search for user queries.

Use OpenAI GPT to generate context-aware answers.

🎯 Impact

Demonstrates how to build a scalable RAG pipeline from scratch.

Enables semantic search across structured JSON data.

Improves accuracy of information retrieval and reduces dependency on raw keyword search.

🔮 Future Enhancements

Add a Streamlit/React frontend for interactive querying.

Extend support to multi-file JSON corpora.

Add evaluation metrics (retrieval accuracy, response relevancy).

Deploy as an API using FastAPI.

📌 License

This project is for educational and demonstration purposes.
