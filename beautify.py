import streamlit as st
import PyPDF2
from PyPDF2 import PdfReader, PdfFileWriter, PageObject
import io

# Function to add a border and watermark to each page
def add_border_and_watermark(pdf_file, output_file, watermark_text):
    pdf_reader = PdfReader(pdf_file)
    pdf_writer = PdfFileWriter()

    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]

        page2 = PageObject.createBlankPage(width=page.mediaBox.getWidth(), height=page.mediaBox.getHeight())
        page2.mergePage(page)

        transformation = PageObject.createBlankPage(width=page2.mediaBox.getWidth(), height=page2.mediaBox.getHeight())
        transformation.addTransformation(PageObject.Transformation().translate(20, 20))

        page2.mergePage(transformation)
        page2.mergeTranslatedPage(PageObject.createTextObject(watermark_text), (page2.mediaBox.getWidth() - page2.mediaBox.getWidth()) / 2, (page2.mediaBox.getHeight() - page2.mediaBox.getHeight()) / 2)

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
