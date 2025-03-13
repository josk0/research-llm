from PyPDF2 import PdfReader
from markdowncleaner import MarkdownCleaner
import re

def extract_text_from_pdf(file_path):
    """Extracts text from a PDF file."""
    text = ""
    try:
        reader = PdfReader(file_path)
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text
        return clean_text(text)
    except Exception as e:
        print(f"Failed to process {file_path}: {e}")
        return None

def clean_text(text):
    """Cleans extracted text using markdowncleaner package with default configuration."""
    cleaner = MarkdownCleaner()
    return cleaner.clean_markdown_string(text)
