import streamlit as st
import PyPDF2
from PyPDF2 import PdfReader, PdfFileWriter
import io

# Function to add a border and watermark to each page
def add_border_and_watermark(pdf_file, output_file, watermark_text):
    pdf_reader = PdfReader(pdf_file)
    pdf_writer = PdfFileWriter()

    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        page.mergeTranslatedPage(page, 0, 0)
        pdf_writer.addPage(page)

    pdf_writer.addPage(pdf_reader.pages[0])

    pdf_writer.updatePageFormFieldValues(pdf_reader.pages[0])
    pdf_writer.encrypt("")

    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        page.mergeTranslatedPage(page, 0, 0)
        pdf_writer.addPage(page)

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
