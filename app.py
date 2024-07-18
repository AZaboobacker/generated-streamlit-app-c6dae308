import streamlit as st
import openai

# CSS for modern and sleek UI
st.markdown('''
    <style>
    body {
        background-color: #f5f5f5;
        color: #333333;
        font-family: 'Arial', sans-serif;
    }
    .main {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
    .sidebar .sidebar-content {
        background-color: #2E4053;
        color: #ffffff;
    }
    .css-8kuttl {
        font-size: 18px;
    }
    .css-pjb7f7 {
        background-color: #007bff;
        color: #ffffff;
        border-radius: 10px;
    }
    .css-pjb7f7:hover {
        background-color: #0056b3;
    }
    </style>
''', unsafe_allow_html=True)

# Page Title
st.title("Personal Finance Advisor 💰")

# API Key Input
api_key = st.text_input("Enter your OpenAI API Key:", type="password")

if not api_key:
    st.warning('Please enter your OpenAI API Key.')
    st.stop()

# Initialize OpenAI with the provided API key
openai.api_key = api_key

# Financial Query Input
query = st.text_input("Ask a finance-related question:")

if st.button("Get Advice"):
    if not query:
        st.error('Please enter a finance-related query.')
    else:
        try:
            # Calling OpenAI's GPT-4 model to generate the response
            response = openai.chat.completions.create(
                model='gpt-4',
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": query}
                ]
            )
            message_content = response.choices[0].message.content.strip()
            st.success(message_content)
        except Exception as e:
            st.error(f"An error occurred: {e}")