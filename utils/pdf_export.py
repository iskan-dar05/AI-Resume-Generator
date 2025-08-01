from fpdf import FPDF
import os

def save_to_pdf(text, filename="outputs/ai_resume.pdf"):
    """
    Converts a block of text into a formatted PDF file.
    """

    os.makedirs(os.path.dirname(filename), exist_ok=True)
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=12)

    for line in text.split('\n'):
        pdf.multi_cell(0, 10, line)

    pdf.output(filename)
    return filename
