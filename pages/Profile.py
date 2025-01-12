# pages/3_👤_Profile.py
import streamlit as st

st.title("Profile & Preferences")

with st.expander("Personal Information"):
    st.text_input("Name")
    st.text_input("Department")
    st.text_input("Year of Study")
    
with st.expander("Interests"):
    st.multiselect(
        "Select your interests",
        ["Technology", "Arts", "Sports", "Research", "Social Activities"]
    )
    
with st.expander("Notification Settings"):
    st.checkbox("Email Notifications")
    st.checkbox("Push Notifications")
    st.checkbox("Event Reminders")