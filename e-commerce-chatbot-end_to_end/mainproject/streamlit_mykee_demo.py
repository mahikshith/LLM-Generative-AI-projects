import streamlit as st
from mykee_retrive import get_retriever
from embedstore import embed_documents
import os
from dotenv import load_dotenv
load_dotenv()

st.markdown(
    """
    <h1 style='text-align: center;'>🛒 E-commerce <span style="color:red;">Review</span> Chat Bot</h1>
    """,
    unsafe_allow_html=True)

st.markdown(
    """<div style='white-space: normal;'>
    This chatbot was only trained on product reviews of [Boat, realme, oneplus, U&I] ear phones and the response 
    depends on product reviews and sentiment of customers in the data.
    </div><br><br>""",  
    unsafe_allow_html=True
)
# Create a retriever instance
vector_store = embed_documents("allright")
ans = get_retriever(vector_store)

# Define a query function
def query_retriever(query):
    results = ans.invoke(query)
    return results

# Create a text input for the user to enter a query
query = st.text_area("Enter a product review or question:", height=100)

# Create a button to trigger the query
if st.button("Get Response"):
    results = query_retriever(query)
    st.write("Response:")
    st.write(results)
