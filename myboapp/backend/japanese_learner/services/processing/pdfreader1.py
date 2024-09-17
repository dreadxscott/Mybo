#a program that can read PDFs and extract their text
from PyPDF2 import PdfReader

#function to read text from a PDF
def read_pdf(filepath):
    #Create a PDF reader object
    reader = PdfReader(filepath)

    #create a string to contain the text
    text = ""

    #loop through all the pages and extract the text on each page
    for page_num, page in enumerate(reader.pages):
        text += f"--- Page {page_num + 1} ---\n"
        text += page.extract_text() + '\n'
    
    return text

#Create a function to save the text in a file
def save_pdf_text(filepath, output_file):
    pdf_text = read_pdf(filepath)
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(pdf_text)
    
    print(f"Text saved to {output_file}")

#hardcoded for now but I'll figure out a way to incorporate it into the overall thing
filepath = r"C:\Users\colli\Downloads\Tadoku\w0004e-michikonohoshizora-v2.pdf"
output_file = r"C:\Users\colli\Downloads\Tadoku\w0004e-michikonohoshizora-v2.txt"

save_pdf_text(filepath, output_file)