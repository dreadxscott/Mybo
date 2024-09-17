#PyMuPDF pdfreader
import fitz #PyMuPDF

def extract_text_with_positions(pdf_file):
    #Open the pdf
    doc = fitz.open(pdf_file)
    text = ""
    #Loop through the pages
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        blocks = page.get_text("blocks")

        #Loop through all the blocks in the page
        for block in blocks:
            bbox = block[:4]
            line = block[4]

            text += f"Page {page_num + 1} : {line}"
    
    with open(r"c:\Users\colli\Downloads\Tadoku\data\f0109e-hanasukeyukidaruma-v2.txt", "w", encoding="utf-8") as f:
        f.write(text)

    
    doc.close()

pdf_file = r"c:\Users\colli\Downloads\Tadoku\f0109e-hanasukeyukidaruma-v2.pdf"
extract_text_with_positions(pdf_file)
