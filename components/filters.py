
# components/filters.py
import streamlit as st
from datetime import datetime, timedelta

def sidebar_filters():
    with st.sidebar:
        st.header("Filters")
        
        st.subheader("Date Range")
        start_date = st.date_input("Start Date", datetime.now())
        end_date = st.date_input("End Date", datetime.now() + timedelta(days=30))
        
        st.subheader("Event Type")
        event_types = st.multiselect(
            "Select Event Types",
            ["Technical", "Cultural", "Sports", "Academic", "Club Activities"]
        )
        
        st.subheader("Department")
        departments = st.multiselect(
            "Select Departments",
            ["Computer Science", "Electrical", "Mechanical", "Chemical", "Physics"]
        )
        
        if st.button("Apply Filters"):
            st.success("Filters applied successfully!")
            return {
                "start_date": start_date,
                "end_date": end_date,
                "event_types": event_types,
                "departments": departments
            }
    return None
