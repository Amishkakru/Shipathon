# components/chat.py
import streamlit as st
from streamlit_chat import message

def chatbot():
    if 'messages' not in st.session_state:
        st.session_state.messages = []

    user_input = st.text_input("You: ", key="input")

    if user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})
        response = f"You said: {user_input}"  # Replace with actual chatbot logic
        st.session_state.messages.append({"role": "bot", "content": response})

    for msg in st.session_state.messages:
        message(msg["content"], is_user=(msg["role"] == "user"))

