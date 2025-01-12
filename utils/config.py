# utils/config.py
import streamlit as st

def load_config():
    if 'user_preferences' not in st.session_state:
        st.session_state.user_preferences = {
            'interests': [],
            'departments': [],
            'notification_preferences': []
        }

def init_styles():
    st.markdown("""
        <style>
        .event-card {
            padding: 20px;
            border-radius: 10px;
            border: 1px solid #e0e0e0;
            margin: 10px 0;
        }
        .stTabs > div > div:first-child {
            align-items: center;
            justify-content: center;
        }
        </style>
    """, unsafe_allow_html=True)
