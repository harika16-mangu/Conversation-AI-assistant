import os
from dotenv import load_dotenv
from langchain_community.document_loaders import JSONLoader
from langchain_community.vectorstores import FAISS
from sentence_transformers import SentenceTransformer
from langchain_huggingface import HuggingFaceEmbeddings

load_dotenv()

file_path="C:/Users/harik/OneDrive/Documents/GitHub/Conversational-AI-assistant/Conversation-AI-assistant/knowledge-base.json"

#load the json file as document which acts as a knowledge base
loader=JSONLoader(file_path=file_path,jq_schema=".[]",text_content=False)
documents=loader.load()

#initialize an open source embeddings model using sentence transformers
model_name="all-MiniLM-L6-V2" #LIGHTWEIGHT AND FREE
#create Huggingfaceembeddings instance which internally uses sentence transformers
embeddings=HuggingFaceEmbeddings(model_name=model_name)

#create a faiss vector embeddings database from documents
faiss_db=FAISS.from_documents(documents,embeddings)

#example query to test
query="what is difference between supervised and unsupervised learning"

#perform similarity search
results =faiss_db.similarity_search(query,)

#print the results
for result in results:
    print(result)

#result.metadata, depending on what we stored