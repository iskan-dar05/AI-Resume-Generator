import re
import nltk
from nltk.corpus import stopwords

# Ensure nltk resources are downloaded
nltk.download('punkt')
nltk.download('stopwords')

def clean_text(pdf_text):
    """
    Cleans and tokenizes PDF text:
    - Removes bullet symbols, punctuation
    - Normalizes whitespace
    - Tokenizes into sentences
    """
    lines = pdf_text.splitlines()
    cleaned_lines = []

    for line in lines:
        line = re.sub(r"[-•–]+", "", line)              # Remove bullet symbols
        line = re.sub(r"[^a-zA-Z0-9\s]", "", line)       # Remove most punctuation
        line = re.sub(r"\s+", " ", line).strip()         # Normalize whitespace
        sentence = nltk.sent_tokenize(line)              # Tokenize sentences
        cleaned_lines.extend(sentence)

    return cleaned_lines

