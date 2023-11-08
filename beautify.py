import streamlit as st
from fpdf import FPDF
import io
import os

# Function to add a border and watermark to each page
def add_border_and_watermark(pdf_file, output_file, watermark_text):
    class PDFWithBorderAndWatermark(FPDF):
        def header(self):
            pass  # Override FPDF header method to prevent page header

        def footer(self):
            pass  # Override FPDF footer method to prevent page footer

    pdf = PDFWithBorderAndWatermark()
    pdf.add_page()

    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=watermark_text, align="C", ln=1)

    pdf.set_draw_color(0)
    pdf.rect(10, 10, 190, 277)  # Add a border (adjust the values as needed)

    with open(output_file, "wb") as f:
        pdf.output(f)

    return output_file

st.title("PDF Page Border and Watermark")

uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file is not None:
    st.write("PDF file uploaded!")

    watermark_text = st.text_input("Watermark Text", "Z-DIVISION")
    output_file = "output.pdf"

    if st.button("Add Border and Watermark"):
        try:
            output_file = add_border_and_watermark(uploaded_file, output_file, watermark_text)
            st.success("Border and watermark added successfully!")
            st.download_button("Download PDF", output_file)
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
