import fitz  # PyMuPDF
import io

# Function to add a border and watermark to each page
def add_border_and_watermark(pdf_file, output_file, watermark_text):
    pdf_document = fitz.open(pdf_file)
    
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)

        # Add a border
        page.insertRect(page.MediaBox, width=20, color=(1, 1, 1), overlay=True)

        # Add a watermark
        page.insert_text(page.MediaBox.width / 2, page.MediaBox.height / 2, watermark_text, fontname="Helvetica", fontsize=40, overlay=True)

    pdf_document.save(output_file)
    return output_file

# Provide your input and output file paths
input_pdf_file = "C:\Users\user\Downloads\DigitalClippings_7Nov.pdf"
output_pdf_file = "C:\Users\user\Downloads\output.pdf"
watermark_text = "Z-DIVISION"

# Usage example
with open(input_pdf_file, "rb") as pdf_file:
    output_path = add_border_and_watermark(pdf_file, output_pdf_file, watermark_text)

print("PDF with border and watermark saved to", output_path)
