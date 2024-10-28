from dotenv import load_dotenv
load_dotenv() # loading the env variables 
import streamlit as st
import os
from PIL import Image # to read images

import google.generativeai as genai 

os.getenv("GOOGLE_API_KEY") # configure google api from env file
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

#Help
#https://colab.research.google.com/github/google/generative-ai-docs/blob/main/site/en/gemini-api/docs/get-started/python.ipynb#scrollTo=FTl5NjtrhA0J

# func to load and generate responses

def gemini_response(behave,image,prompt): 
    model= genai.GenerativeModel('gemini-pro-vision') # using vision model for the images
    answer = model.generate_content([behave,image[0],prompt])
    return answer.text 


# Function to prepare image data for the API
def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image_parts = [
            {
                "mime_type": uploaded_file.type,
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")

behaviour = '''You are an expert in understanding the invoices
in multiple languages, you will receive imput as images of invoice and you
need to answer questions based on the input image provided'''

# streamlit intialize 
st.header("Gemini Invoice Reader") 
input = st.text_input("enter the input",key="input")
uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
image = ""
if uploaded_image is not None : 
    image= Image.open(uploaded_image)
    st.image(image, caption="uploaded_image",use_column_width=True)

submit= st.button("What's the image is saying")

if submit :
    img_data= input_image_setup(uploaded_image)
    ans = gemini_response(behaviour,img_data,input)
    st.subheader("Gemini's response")
    st.write(ans)

