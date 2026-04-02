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
    from transformers import pipeline

    generator = pipeline("text-generation", model="gpt2")

    def ask_question(query):
        docs = vector_db.similarity_search(query)

        context = "\n".join([doc.page_content for doc in docs])

        prompt = f"""
        You are a coding assistant.
        
        Only answer based on the given code.

        Code:
        {context}
        
        Question: {query}
        
        Answer in ONE short sentence only:
        """

        response = generator(
            prompt,
            max_new_tokens=50,
            temperature=0.0,
            do_sample=False,
            repetition_penalty=1.5,
            return_full_text=False
        )

        return response[0]["generated_text"].strip()

    return ask_question