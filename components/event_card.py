# components/event_card.py
import streamlit as st

def display_event_card(title, host, date, time, location, description, **kwargs):
    """
    Display an event card with the given information.
    
    Parameters:
    - title: str
    - host: str
    - date: str
    - time: str
    - location: str
    - description: str
    - **kwargs: Additional keyword arguments are ignored
    """
    st.markdown(f"""
        <div class="event-card">
            <h3>{title}</h3>
            <p><strong>Host:</strong> {host}</p>
            <p><strong>Date:</strong> {date}</p>
            <p><strong>Time:</strong> {time}</p>
            <p><strong>Location:</strong> {location}</p>
            <p>{description}</p>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        button_label = "Cancel RSVP" if title in st.session_state.rsvp_events else "RSVP"
        if st.button(button_label, key=f"rsvp_{title}"):
            if title not in st.session_state.rsvp_events:
                st.session_state.rsvp_events.add(title)
                st.success(f"RSVP confirmed for {title}")
            else:
                st.session_state.rsvp_events.remove(title)
                st.info(f"RSVP cancelled for {title}")
                
    with col2:
        if st.button("Add to Calendar", key=f"calendar_{title}"):
            st.success("Event added to calendar!")
    with col3:
        if st.button("Share", key=f"share_{title}"):
            st.info("Share links generated!")