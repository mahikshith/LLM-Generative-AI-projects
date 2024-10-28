import streamlit as st
import requests

# Streamlit UI
st.markdown(
    """
    <h1 style='text-align: center;'>🛒 E-commerce <span style="color:red;">Review</span> Chat Bot</h1>
    """, unsafe_allow_html=True
)

st.markdown(
    """<div style='white-space: normal;'>
    This chatbot was only trained on product reviews of [Boat, realme, oneplus, U&I] earphones, and the response 
    depends on product reviews and customer sentiments in the data.
    </div><br><br>""",  
    unsafe_allow_html=True
)

# Text input for user query
query = st.text_area("Enter a product review or question:", height=100)

# Button to trigger query
if st.button("Get Response"):
    if query:
        # Send request to Flask API
        response = requests.post('http://localhost:5000/query', json={"query": query})
        # edit this during EC2 with public-exposed IP

        if response.status_code == 200:
            result = response.json().get('response')
            st.write("Response:")
            st.write(result)
        else:
            st.write("Error:", response.json().get('error'))
    else:
        st.write("Please enter a query.")
