import streamlit as st
import google.generativeai as genai
import os
from PIL import Image
    
from dotenv import load_dotenv
load_dotenv()
    
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
    
def get_gemini_response(input, image):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content([input, image[0]])
    return response.text
    
def img_to_bytes(image):
    if image is not None:
        bytes_data = image.getvalue()
        
        image_parts = [
            {
                "mime_type": image.type,
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        return FileNotFoundError("No image found")
    
    
# Intialize streamlit app
st.set_page_config(page_title="Calorie Advisor Bot")
st.header("Gemini Health App")
    
uploaded_image_file = st.file_uploader("Choose an image...", type=["jpeg","jpg","png"])
    
image = ""
    
if uploaded_image_file is not None:
    image = Image.open(uploaded_image_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)
    
submit = st.button("Tell me the total calories")
    
input_prompt = """
You are a nutritionist assistant. You will be given a picture of a food item and you have to answer the following questions:
1. What is the food item?
2. How many calories does it have?
3. Is it healthy or not?
4. Give a brief description of the food item.
"""
    
if submit:
    image_data = img_to_bytes(uploaded_image_file)
    response = get_gemini_response(input_prompt, image_data)
    st.subheader("The response is")
    st.write(response)