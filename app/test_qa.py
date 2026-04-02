from app.code_parser import load_codebase
from app.rag_pipeline import create_vector_store, create_qa_system

docs = load_codebase("data/sample_repo")

vector_db = create_vector_store(docs)

qa_system = create_qa_system(vector_db)

query = "What does the add function do?"

answer = qa_system(query)

print("\n===== ANSWER =====\n")
print(answer)
print("\n==================\n")