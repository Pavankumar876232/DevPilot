from fastapi import FastAPI
from app.code_parser import load_codebase
from app.rag_pipeline import create_vector_store, create_qa_system

app = FastAPI()

# Load data once at startup
docs = load_codebase("data/sample_repo")
vector_db = create_vector_store(docs)
qa_system = create_qa_system(vector_db)


@app.get("/")
def home():
    return {"message": "DevPilot API is running 🚀"}


@app.get("/ask")
def ask(query: str):
    answer = qa_system(query)
    return {"question": query, "answer": answer}