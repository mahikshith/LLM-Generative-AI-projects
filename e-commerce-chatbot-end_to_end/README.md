## E-commerce Review Chatbot - **end to end implementation with AWS**

What if there is a LLM powered chatbot designed to provide personalized product recommendations and insights based purely  on customer reviews and their sentiments rather than product description.

I mean let's be honest we look at ratings but we can't read all the reviews (nobody has time to read'em). 

so, what if we scrape the reviews of products given by people for the products under same catogery belong different companies and get honest answers be it positive or negative and make a decision to buy it or not.

Project explanation video : https://drive.google.com/file/d/17FeAEHYOKM4AFdKDUU_PDkh1s92C2cFG/view?usp=sharing

Roadmap : 

> Scrape the pdt id , reviews ,sentiments and other info from e-commerce site  [used reviews for building embeddings , rest of the pdt info is used as meta data]
> 
> Bring the data in proper format such as document format for the gemini 1.5 pro to convert them into embedding.
> 
> Create embeddigns used ASTRA DB to store the embeddings in the cloud.
> 
> Build a retriver and create a chain using langchain.
> 
> Demo using streamlit
> 
> don't stop there test the code locally using flask api with postman
> 
> Then use streamlit as front end , create a AWS - EC2 instance , clone the git repo - install dependencies.
>
>  update the port in security inbound rules for the flask
> 
> Test the public API using postman post request to check how the app is responding
> 
> take the public - exposed IP and change the POST request IP in streamlit followed by creating a new inbound rule for streamlit port
> 
> Finally copy the public IP with streamlit port and monitor how the app is wworking.
> 
> Stop the instance, can't bear AWS bill.


The project is built with Langchain for document processing and embeddings, integrated with AstraDB Vector Store to store and search vectors efficiently. 

Trained on product reviews from e-commerce dataset of headphones the chatbot enables users to gain insights about products directly from real customer feedback rather than product description.


The chatbot is deployed using Streamlit, offering an intuitive user interface where users can ask product-related queries and receive responses in real-time. The system is designed for scalability, and with its flexible architecture

it can be extended to support additional brands or languages in the future.


> Check the following video for the end result : 


https://github.com/user-attachments/assets/c4515ee7-8835-4993-bf94-1ca5f3fdeecb


Once I locally experiemnted with streamlit UI , then used flask API to test the functionality using PostMan 

.

.


![flask_demo](https://github.com/user-attachments/assets/f615aaf2-0114-4a01-a040-68b1e09bfd95)
.

.

  Started Pinging in the browser
  .
  .

![Screenshot(12)](https://github.com/user-attachments/assets/de009d68-a509-4f09-93c4-7e4ce988a583)

.
.

Created AWS-EC2 instance , cloned the git repo and installed the dependencies and creaated a inbound rule for flask

.
.

![Screenshot(14)](https://github.com/user-attachments/assets/92a6a707-d0ec-432d-b631-25d961c9f4d9)

.
.

Updated the  public IP in streamlit final code with nano (scared of vim)

.
.


![nanoip](https://github.com/user-attachments/assets/1b81e593-f86d-460d-ad94-8aa44f4676ec)

.
.

And finally tested the public-exposed IP and sent a post request with Postman to keep my sanity.

.
.

![postman publicip](https://github.com/user-attachments/assets/be329e12-8e20-4a7f-a4d0-c2135fdc8128)

