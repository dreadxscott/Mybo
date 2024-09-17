#using pdf plumber to extract text from pdfs
import pdfplumber

#function to read pdfs
def read_pdf(filepath):
    #Open the PDF with pdfplumber
    with pdfplumber.open(filepath) as pdf:
        #Initialize an empty text string for pdf text
        text = ""

        #loop through all the pages to get the text
        for page, page_num in enumerate(pdf.pages):
            text += f"--- Page: {page_num + 1} ---\n"
            text += page.extract_text() + "\n"

        #return extracted text
        return text

#Define a path to your PDF file
filepath = "C:\Users\colli\Downloads\Tadoku\f0109e-hanasukeyukidaruma-v2.pdf"
pdf_text = read_pdf(filepath)

