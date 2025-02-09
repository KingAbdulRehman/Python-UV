import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain.schema import AIMessage, HumanMessage, SystemMessage
import os

# Initialize the Gemini model
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash-exp",
    temperature=0.9,  # Corrected spelling from 'temprature' to 'temperature'
    max_tokens=2000,
    max_retries=3,
    verbose=True,
    api_key=os.getenv("GEMINI_API_KEY")
)

# Streamlit app
st.title("Chat with Gemini Model")

# User input
user_input = st.text_input("You: ", "")

if user_input:
    msg = [
        SystemMessage(content="You just continue chat with short messages dont make chat or any topic longer"),
        HumanMessage(content=user_input)
    ]
    response = llm.invoke(msg).content
    st.text_area("Gemini:", value=response, height=200)

if __name__ == "__main__":
    if "__streamlitmagic__" not in locals():
        import streamlit.web.bootstrap
        streamlit.web.bootstrap.run(__file__, False, [], {})
