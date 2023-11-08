import streamlit as st
import PyPDF2
from PyPDF2 import PdfFileReader, PdfFileWriter, PageObject
import io

# Function to add a border and watermark to each page
def add_border_and_watermark(pdf_file, output_file, watermark_text):
    pdf_reader = PdfFileReader(pdf_file)
    pdf_writer = PdfFileWriter()

    for page_num in range(pdf_reader.getNumPages()):
        page = pdf_reader.getPage(page_num)

        page2 = PageObject.createBlankPage(width=page.mediaBox.getWidth(), height=page.mediaBox.getHeight())
        page2.mergeTranslatedPage(page, 0, 0)
        page2.mergeTranslatedPage(page, 20, 20)  # Add border (adjust the values as needed)

        watermark = PageObject.createTextObject(watermark_text)
        watermark.mergeTranslatedPage(page2, (page2.mediaBox.getWidth() - watermark.mediaBox.getWidth()) / 2, (page2.mediaBox.getHeight() - watermark.mediaBox.getHeight()) / 2)
        page2.merge_page(watermark)

        pdf_writer.addPage(page2)

    with open(output_file, "wb") as output:
        pdf_writer.write(output)

    return output_file

st.title("PDF Page Border and Watermark")

uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file is not None:
    st.write("PDF file uploaded!")

    watermark_text = st.text_input("Watermark Text", "Z-DIVISION")
    output_file = "output.pdf"

    if st.button("Add Border and Watermark"):
        try:
            with io.BytesIO(uploaded_file.read()) as pdf_file:
                output_file = add_border_and_watermark(pdf_file, output_file, watermark_text)
            st.success("Border and watermark added successfully!")
            st.download_button("Download PDF", output_file)
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
