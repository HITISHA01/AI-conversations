import streamlit as st
from langchain.llms import OpenAI

st.title('💡 AI Conversations')

# Create a sidebar for API key input
st.sidebar.header('Configuration')
openai_api_key = st.sidebar.text_input('OpenAI API Key', type='password')

def generate_response(input_text: str) -> None:
    """Generate a response from the OpenAI model"""
    llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
    response = llm(input_text)
    st.info(response)

with st.form('my_form'):
    st.header('Chat with the AI')
    text = st.text_area('Enter text:', value='What are the three key pieces of advice for learning how to code?')
    submitted = st.form_submit_button('Submit')

    if submitted:
        if not openai_api_key.startswith('sk-'):
            st.warning('Please enter your OpenAI API key!', icon='⚠')
        else:
            generate_response(text)