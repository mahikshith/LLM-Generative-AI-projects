from flask import Flask, request, jsonify
from mykee_retrive import get_retriever
from embedstore import embed_documents
import os
from dotenv import load_dotenv

# Here Iam using streamlit as frontend for chatbot -->> tested it on stream+flask.py
# and took the endpoint and tested it in postman.

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Initialize retriever instance
vector_store = embed_documents("allright")
ans = get_retriever(vector_store)

@app.route('/')
def welcome():
    return "E-commerce Review Chatbot API is running!"

@app.route('/query', methods=['POST'])
def query_chatbot():
    # Extract the query from the request body
    data = request.get_json()
    query = data.get('query')

    if not query:
        return jsonify({"error": "Query not provided"}), 400

    # Call the retriever
    results = ans.invoke(query)
    return jsonify({"response": results})

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
