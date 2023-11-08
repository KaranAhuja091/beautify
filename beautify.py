import streamlit as st
import PyPDF2
from PyPDF2 import PdfReader, PdfWriter, PageObject
import io

# Function to add a border and watermark to each page
def add_border_and_watermark(pdf_file, output_file, watermark_text):
    pdf_reader = PdfReader(pdf_file)
    pdf_writer = PdfWriter()

    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]

        page2 = PageObject.create_blank_page(width=page.mediabox[2], height=page.mediabox[3])
        page2.mergeTranslatedPage(page, 0, 0)
        page2.mergeTranslatedPage(page, 20, 20)  # Add a border (adjust the values as needed)

        watermark = PageObject.create_text_object(watermark_text)
        watermark.mergeTranslatedPage(page2, (page2.mediabox[2] - watermark.mediabox[2]) / 2, (page2.mediabox[3] - watermark.mediabox[3]) / 2)
        page2.mergeTranslatedPage(watermark, 0, 0)
        pdf_writer.append_page(page2)

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
