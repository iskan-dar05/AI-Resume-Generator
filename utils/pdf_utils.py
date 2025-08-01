import pymupdf  # also known as fitz

def extract_text_from_pdf(file):
    """
    Extracts full text from a PDF file stream using PyMuPDF.
    """
    file.seek(0)
    doc = pymupdf.open(stream=file.read(), filetype="pdf")
    full_text = ""
    for page in doc:
        full_text += page.get_text() + '\n'
    doc.close()
    return full_text
