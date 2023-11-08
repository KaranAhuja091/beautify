import streamlit as st
import fitz  # PyMuPDF
import io
import os

# Function to add a border and watermark to each page
def add_border_and_watermark(pdf_file, output_file, watermark_text):
    pdf_document = fitz.open(stream=pdf_file.read(), filetype="pdf")
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)

        # Add a border
        page.insertRect(page.MediaBox, width=20, color=(1, 1, 1), overlay=True)

        # Add a watermark
        page.insert_text(page.MediaBox.width / 2, page.MediaBox.height / 2, watermark_text, fontname="Helvetica", fontsize=40, overlay=True)

    # Save the PDF file in the current working directory
    output_path = output_file
    pdf_document.save(output_path)

    return output_path

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
