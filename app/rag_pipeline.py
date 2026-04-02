# version 2 fix
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

        # Extract function name dynamically
        if "def" in context:
            lines = context.split("\n")
            for line in lines:
                if line.strip().startswith("def"):
                    return f"This function is defined as:\n{line}\n\nIt performs the operation described in the code."

        return f"Relevant code:\n{context}"

    return qa