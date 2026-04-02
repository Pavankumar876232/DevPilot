from app.code_parser import load_codebase
from app.rag_pipeline import create_vector_store

docs = load_codebase("data/sample_repo")

vector_db = create_vector_store(docs)

query = "What does this code do?"

results = vector_db.similarity_search(query)

for res in results:
    print(res.page_content)
    print("-" * 40)