from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from embedstore import embed_documents


import google.generativeai as genai
from langchain_google_genai import GoogleGenerativeAI
# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))



def get_retriever(vector_store):

    model = GoogleGenerativeAI(model="gemini-pro")

    retriever = vector_store.as_retriever(
        search_type="similarity_score_threshold",
        search_kwargs={"k": 3, "score_threshold": 0.5})
    
    ecom_template = ''' You are a really helpful e-commerce chatbot that provides recommendations based 
    on the product reviews , meta data given by the people in the CONTENT and answer customer queries.
    Always ensure the answer that you generated is relavent to product context and refrain form answering 
    questions that are not relevant to the product. Keep the answer informative and detailed manner with bullet points
    where ever necessary and also display meta data information.
    check the CONTENT : {context} 
    question from the user : {query}

    Your answer : '''

    prompt = ChatPromptTemplate.from_template(template=ecom_template)

    # llm chain 

    output_parser = StrOutputParser()

    ans_chain = ( {"context": retriever, "query": RunnablePassthrough()} | prompt | model | output_parser)

    return ans_chain

# testing

if __name__ == "__main__":


    vector_store = embed_documents("allright")
    ans  = get_retriever(vector_store)
    print(ans.invoke("Please tell me what are the best earbuds with bluetooth connectivity"))

# test the retriver under this block ans :
 
#realme Buds Wireless Bluetooth Headset are the best earbuds with Bluetooth connectivity. 
# They have good build quality, excellent sound and bass, and a long battery life.
    