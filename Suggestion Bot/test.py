import streamlit as st
import asyncio
from langchain_community.llms import Ollama
from langchain.prompts import ChatPromptTemplate
from langchain.schema import StrOutputParser
from langchain.schema.runnable import Runnable
from langchain.schema.runnable.config import RunnableConfig
from datetime import datetime

# Initialize model and prompt
model = Ollama(model="mini")
prompt = ChatPromptTemplate.from_messages([
    ("system", "Please provide information to the concern I shall do my best to answer you."),
    ("human", "{question}"),
])
runnable = prompt | model | StrOutputParser()

# Function to process question asynchronously
async def process_question(question):
    response = ""
    async for chunk in runnable.astream({"question": question}, config=RunnableConfig()):
        response += chunk
    return response

# Streamlit UI
st.title("ClinAI - Medical Chatbot")

# CSS for styling chat messages
st.markdown(
    """
    <style>
    .chat-container {
        display: flex;
        flex-direction: column;
        padding: 10px;
        width: 100%;
    }
    .message-container {
        display: flex;
        margin-bottom: 10px;
    }
    .message-user {
        background-color: #007bff;
        color: #ffffff;
        padding: 10px;
        border-radius: 10px;
        max-width: 70%;
        align-self: flex-end;
        margin-left: auto;
    }
    .message-bot {
        background-color: #f0f0f0;
        color: #000000;
        padding: 10px;
        border-radius: 10px;
        max-width: 70%;
        align-self: flex-start;
        margin-right: auto;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Sidebar (navbar)
st.sidebar.title("Navigation")
navigation = st.sidebar.radio("Go to", ["Home", "Chat"])

if navigation == "Home":
    st.header("Welcome to ClinAI")
    st.write("This is a medical chatbot powered by LangChain.")
    st.image("logo.JPG", caption="ClinAI Logo")

elif navigation == "Chat":
     # Function to display chat messages
    def display_message(message, sender):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        if sender == 'user':
            st.markdown(f'<div class="message-container"><div class="message-user">{message}</div></div>', unsafe_allow_html=True)
        elif sender == 'bot':
            st.markdown(f'<div class="message-container"><div class="message-bot">{message}</div></div>', unsafe_allow_html=True)


    # Initialize conversation history
    if 'conversation' not in st.session_state:
        st.session_state.conversation = []


    # Main chat loop
    question = st.text_input("You: ", "")
    if st.button("Send"):
        if question:
            # Add user message to conversation history
            st.session_state.conversation.append(("user", question))

            # Process question and get response
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            response = loop.run_until_complete(process_question(question))
            loop.close()

            # Add bot response to conversation history
            st.session_state.conversation.append(("bot", response))

    # Display conversation
    st.markdown('<div class="chat-container">', unsafe_allow_html=True)
    for sender, message in st.session_state.conversation:
        display_message(message, sender)
    st.markdown('</div>', unsafe_allow_html=True)
    
