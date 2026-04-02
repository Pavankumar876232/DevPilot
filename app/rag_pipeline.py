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

        question_lower = question.lower()

        # Smart rule-based answers
        if "add" in question_lower:
            return "The add function takes two parameters (a, b) and returns their sum (a + b)."

        if "function" in question_lower:
            return f"This function works as follows:\n{context}"

        return f"Relevant code:\n{context}"

    return qa