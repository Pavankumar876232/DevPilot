import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import streamlit as st
from app.code_parser import load_codebase
from app.rag_pipeline import create_vector_store, create_qa_system

st.title("🚀 DevPilot - AI Code Assistant")

@st.cache_resource
def load_system():
    docs = load_codebase("data/sample_repo")
    vector_db = create_vector_store(docs)
    qa = create_qa_system(vector_db)
    return qa

qa = load_system()

question = st.text_input("Enter your question:")

if st.button("Ask"):
    if question:
        answer = qa(question)
        st.success("💡 Answer:")
        st.write(answer)
    else:
        st.warning("Please enter a question")