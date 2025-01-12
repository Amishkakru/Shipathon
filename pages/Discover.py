# pages/1_🔍_Discover.py
import streamlit as st
from components.event_card import display_event_card
from utils.data_processor import EventProcessor

def main():
    st.title("Discover Events")

    # Initialize data processor
    processor = EventProcessor('data/events_caic.csv')
    
    # Sidebar filters
    st.sidebar.header("Filter Events")
    
    try:
        # Date filter
        start_date = st.sidebar.date_input("Start Date")
        end_date = st.sidebar.date_input("End Date")
        
        # Host filter
        all_hosts = processor.get_unique_values('host')
        selected_hosts = st.sidebar.multiselect("Select Hosts", all_hosts)
        
        # Location filter
        all_locations = processor.get_unique_values('location')
        selected_locations = st.sidebar.multiselect("Select Locations", all_locations)
        
        # Apply filters
        filters = {}
        if start_date: filters['start_date'] = start_date
        if end_date: filters['end_date'] = end_date
        if selected_hosts: filters['host'] = selected_hosts
        if selected_locations: filters['location'] = selected_locations
        
        # Get filtered events
        events_df = processor.get_events(filters)
        
        # Add search functionality
        search_query = st.text_input("🔍 Search events...", 
                                    placeholder="Search by title, host, or location")
        if search_query:
            events_df = processor.search_events(events_df, search_query)
        
        # Display event count
        st.write(f"Found {len(events_df)} events")
        
        # Display events
        if events_df.empty:
            st.info("No events found matching your criteria.")
        else:
            for _, event in events_df.iterrows():
                clean_event = processor.clean_event_data(event)
                display_event_card(**clean_event)
                
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        st.write("Please try refreshing the page or contact support if the issue persists.")

if __name__ == "__main__":
    main()