import os
from transformers import pipeline
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

def create_vector_store(documents):
    texts = [doc["content"] for doc in documents]

    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )

    vector_db = FAISS.from_texts(texts, embeddings)

    return vector_db

def create_qa_system(vector_db):
    def qa(question):
        docs = vector_db.similarity_search(question)
        context = "\n".join([doc.page_content for doc in docs])

        # Simple rule-based answer
        if "add" in context.lower():
            return "The add function takes two inputs (a, b) and returns their sum."

        return f"Based on code:\n{context}"

    return qa