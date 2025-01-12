# utils/data_processor.py
import pandas as pd
import numpy as np

class EventProcessor:
    def __init__(self, csv_path):
        # Read CSV and fill NaN values with appropriate defaults
        self.events_df = pd.read_csv(csv_path)
        self.events_df = self.events_df.fillna({
            'title': 'Untitled Event',
            'host': 'Unspecified Host',
            'date': 'TBD',
            'time': 'TBD',
            'location': 'TBD',
            'description': 'No description available'
        })

    def get_unique_values(self, column):
        """Get unique values from a column, handling NaN and empty values"""
        # Filter out NaN and empty values, convert to strings
        values = self.events_df[column].astype(str)
        values = values[values != 'N/A']
        values = values[values != '']
        return sorted(values.unique())

    def get_events(self, filters =None):
        """Get filtered events with proper handling of NaN values"""
        filtered_df = self.events_df.copy()
        
        if filters:
            if 'start_date' in filters and filters['start_date']:
                filtered_df = filtered_df[filtered_df['date'] >= str(filters['start_date'])]
            if 'end_date' in filters and filters['end_date']:
                filtered_df = filtered_df[filtered_df['date'] <= str(filters['end_date'])]
            if 'host' in filters and filters['host']:
                filtered_df = filtered_df[filtered_df['host'].isin(filters['host'])]
            if 'location' in filters and filters['location']:
                filtered_df = filtered_df[filtered_df['location'].isin(filters['location'])]
        
        # Ensure all string columns have proper string values
        string_columns = ['title', 'host', 'date', 'time', 'location', 'description']
        for col in string_columns:
            if col in filtered_df.columns:
                filtered_df[col] = filtered_df[col].fillna('').astype(str)
        
        return filtered_df

    def search_events(self, df, query):
        """Search events with proper handling of NaN values"""
        query = str(query).lower()
        return df[
            df['title'].str.lower().str.contains(query, na=False) |
            df['host'].str.lower().str.contains(query, na=False) |
            df['location'].str.lower().str.contains(query, na=False)
        ]

    def clean_event_data(self, event_series):
        """Clean event data and ensure proper string formatting"""
        return {
            'title': str(event_series.get('title', 'Untitled Event')),
            'host': str(event_series.get('host', 'Unspecified Host')),
            'date': str(event_series.get('date', 'TBD')),
            'time': str(event_series.get('time', 'TBD')),
            'location': str(event_series.get('location', 'TBD')),
            'description': str(event_series.get('description', 'No description available'))
        }