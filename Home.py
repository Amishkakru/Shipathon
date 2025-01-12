# Directory structure:
# - pages/
#   - 1_Discover.py
#   - 2_Calendar.py
#   - 3_Events.py
#   - 4_Profile.py
# - components/
#   - filters.py
#   - event_card.py
#   - chat.py
# - utils/
#   - config.py
#   - data_preproessor.py
# - scripts/
#   - import_data.py
# - data/
#   -text_files/
# - Home.py



# Home.py (main page)
import streamlit as st
from utils.config import load_config, init_styles
from components.chat import chatbot

def main():
    st.set_page_config(
        page_title="EventConnect",
        page_icon="🎉",
        layout="wide"
    )
    
    load_config()
    init_styles()

    st.title("EventConnect")
    st.subheader("Your Personalized Campus Activity Hub")
    
    # Search Bar
    st.text_input("Search for events...", key="search_bar")
    
    # Display chatbot
    st.header("Need help?")
    chatbot()

if __name__ == "__main__":
    main()