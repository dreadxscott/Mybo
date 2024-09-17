#manga ocr pdf reader
from manga_ocr import MangaOcr
from pdf2image import convert_from_path
from PIL import Image, ImageEnhance, ImageFilter

#Initialize the Manga OCR Model
ocr = MangaOcr()

#Define path to PDF
pdf_path = r"C:\Users\colli\Downloads\Tadoku\f0109e-hanasukeyukidaruma-v2.pdf"

#Resolution set to 600, turn the pdf into an image
pages = convert_from_path(pdf_path, 600)
text = ""
#Loop through the pages with Manga OCR
for page_num, page in enumerate(pages):

    #extract text
    page = page.filter(ImageFilter.SHARPEN)  # Sharpen the image
    # Increase contrast (optional)
    enhancer = ImageEnhance.Contrast(page)
    extracted_text = ocr(page)

    text += f"---Text from Page {page_num+1}---"
    text += extracted_text + '\n'

#put extracted text in files
with open(fr"C:\Users\colli\Downloads\Tadoku\yukidaruma\yukidaruma_extracted_text.txt"
              , "w"
              , encoding="utf-8") as f:
    f.write(text)
    
