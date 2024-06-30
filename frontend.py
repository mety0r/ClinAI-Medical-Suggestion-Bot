import streamlit as st
from backend import setup_query_engine

# Path to your data directory
DATA_DIRECTORY = "Data/"

# Setup query engine
query_engine = setup_query_engine(DATA_DIRECTORY)

# Streamlit UI
st.title("Medical Advice Chatbot")

# Initial query
query = st.text_input("Enter your medical query:", "")

if query:
    response = query_engine.query(query)
    st.write(response)

# Interactive querying
while True:
    query = st.text_input("Ask another question:")
    if query:
        response = query_engine.query(query)
        st.write(response)
