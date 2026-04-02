import streamlit as st
import requests

st.set_page_config(page_title="DevPilot", layout="centered")

st.title("🚀 DevPilot - AI Code Assistant")

st.write("Ask questions about your codebase")

# Input box
query = st.text_input("Enter your question:")

# Button
if st.button("Ask"):
    if query:
        try:
            response = requests.get(
                "http://127.0.0.1:8000/ask",
                params={"query": query}
            )

            data = response.json()

            st.subheader("💡 Answer:")
            st.write(data["answer"])

        except Exception as e:
            st.error("Error connecting to backend. Make sure FastAPI is running.")
    else:
        st.warning("Please enter a question.")