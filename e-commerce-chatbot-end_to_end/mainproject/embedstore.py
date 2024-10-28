# Take the data from the documents in pre_process.py and embed it into cassandra database

import os
import pandas as pd
from dotenv import load_dotenv

from langchain_astradb import AstraDBVectorStore

from langchain_google_genai import GoogleGenerativeAIEmbeddings
# getting data 
from pre_process import convert_to_doc

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

ASTRA_DB_API_ENDPOINT = os.getenv("ASTRA_END_POINT")

ASTRA_DB_APPLICATION_TOKEN = os.getenv("ASTRA_TOKEN")

ASTRA_DB_NAMESPACE = os.getenv("ASTRA_KEYSPACE")

embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

def embed_documents(run_state):
# vector store creation
    vector_store = AstraDBVectorStore(
        collection_name="mykee_powerful_collection",
        embedding=embeddings,
        api_endpoint=ASTRA_DB_API_ENDPOINT,
        token=ASTRA_DB_APPLICATION_TOKEN,
        namespace=ASTRA_DB_NAMESPACE,)
# Astra db data base id :   0a582d13-f1b1-4ab9-a137-14627ad24396
    
    if run_state is None:
        docs= convert_to_doc()
        inserted_ids = vector_store.add_documents(docs)
    else:
        return vector_store
    return vector_store, inserted_ids

# testing  

if __name__ == "__main__":
    vector_store, inserted_ids = embed_documents(None)
    print(len(inserted_ids))

    ans = vector_store.similarity_search('''tell me what are all the earphones available in flipkart and what is the best
                                         quality earphones among them''', 3)
    for each_ans in ans : 
        print(f"{each_ans.page_content} --- {each_ans.metadata}")

# ran it for testing -- got results , always make sure to specifyt the embedding model if google api is used

