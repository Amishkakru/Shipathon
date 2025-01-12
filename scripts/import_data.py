# scripts/import_data.py
from utils.data_processor import EventDataProcessor

def import_all_data():
    processor = EventDataProcessor()
    
    # Import from text files
    processor.process_directory('data/text_files')
    
    # Import from PDF files
    processor.process_directory('data/pdf_files')

if __name__ == "__main__":
    import_all_data()

