import streamlit as st
from streamlit_calendar import calendar
from utils.data_processor import EventProcessor
import pandas as pd
from datetime import datetime

def convert_to_calendar_format(events_df):
    """Convert DataFrame events to calendar-compatible format"""
    calendar_events = []
    
    for _, event in events_df.iterrows():
        try:
            if event['date'] == 'TBD' or event['time'] == 'TBD':
                # Use current datetime for TBD events
                start_datetime = datetime.now()
            else:
                start_datetime = pd.to_datetime(f"{event['date']} {event['time']}")
            
            # Set end time 2 hours after start time
            end_datetime = start_datetime + pd.Timedelta(hours=2)
            
            calendar_events.append({
                'title': event['title'],
                'start': start_datetime.strftime('%Y-%m-%d %H:%M:%S'),
                'end': end_datetime.strftime('%Y-%m-%d %H:%M:%S'),
                'description': f"Host: {event['host']}\nLocation: {event['location']}\n{event['description']}",
                'backgroundColor': '#1E88E5' if event['title'] in st.session_state.get('rsvp_events', set()) else '#4CAF50'
            })
        except Exception as e:
            st.warning(f"Skipping event '{event['title']}' due to invalid date/time format")
            continue
    
    return calendar_events

def main():
    st.title("Calendar View")
    
    # Initialize event processor
    processor = EventProcessor('data/events_caic.csv')
    
    # Get all events with no filters
    events_df = processor.get_events(filters=None)
    
    # Convert to calendar format
    calendar_events = convert_to_calendar_format(events_df)
    
    # Calendar configuration
    calendar_options = {
        "headerToolbar": {
            "left": "today prev,next",
            "center": "title",
            "right": "dayGridMonth,timeGridWeek,timeGridDay"
        },
        "initialView": "dayGridMonth",
        "selectable": True,
        "selectMirror": True,
        "dayMaxEvents": True,
        "weekNumbers": True,
        "navLinks": True,
        "eventClick": {"enabled": True},
        "eventDisplay": "block",
        "displayEventTime": True,
    }
    
    # Display calendar
    calendar(events=calendar_events, options=calendar_options)
    
    # Add legend
    st.markdown("""
    ### Legend:
    - 🔵 RSVP'd Events
    - 🟢 Available Events
    """)

if __name__ == "__main__":
    main()