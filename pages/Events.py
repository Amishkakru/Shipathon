# pages/3_📋_Events.py
import streamlit as st
from components.event_card import display_event_card
from utils.data_processor import EventProcessor

def initialize_session_state():
    if 'rsvp_events' not in st.session_state:
        st.session_state.rsvp_events = set()


def main():
    initialize_session_state()
    st.title("My Events")

    # Initialize event processor
    processor = EventProcessor('data/events_caic.csv')
    
    if not st.session_state.rsvp_events:
        st.write("You haven't RSVP'd to any events yet!")
        st.write("Browse events in the Discover page and click 'RSVP' to add them here.")
    else:
        # Get all events and filter for RSVP'd ones
        all_events = processor.get_events({})
        rsvp_events = all_events[all_events['title'].isin(st.session_state.rsvp_events)]
        
        # Add sorting options
        sort_by = st.selectbox(
            "Sort by:",
            ["Date (Newest First)", "Date (Oldest First)", "Title"]
        )
        
        if sort_by == "Date (Newest First)":
            rsvp_events = rsvp_events.sort_values('date', ascending=False)
        elif sort_by == "Date (Oldest First)":
            rsvp_events = rsvp_events.sort_values('date', ascending=True)
        else:
            rsvp_events = rsvp_events.sort_values('title')
        
        # Display RSVP'd events
        st.write(f"You have RSVP'd to {len(rsvp_events)} events")
        
        for _, event in rsvp_events.iterrows():
            # Convert the event series to a dictionary and select only needed fields
            event_dict = {
                'title': event['title'],
                'host': event['host'],
                'date': event['date'],
                'time': event['time'],
                'location': event['location'],
                'description': event['description']
            }
            display_event_card(**event_dict)


if __name__ == "__main__":
    main()