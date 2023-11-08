import streamlit as st
import fitz  # PyMuPDF
import io
import tempfile

# Function to add a border and watermark to each page
def add_border_and_watermark(pdf_file, watermark_text):
    pdf_document = fitz.open(stream=pdf_file.read(), filetype="pdf")
    output_path = None

    with tempfile.TemporaryDirectory() as temp_dir:
        for page_num in range(len(pdf_document)):
            page = pdf_document.load_page(page_num)

            # Add a border
            page.insertRect(page.MediaBox, width=20, color=(1, 1, 1), overlay=True)

            # Add a watermark
            page.insert_text(page.MediaBox.width / 2, page.MediaBox.height / 2, watermark_text, fontname="Helvetica", fontsize=40, overlay=True)

        # Save the PDF file in the temporary directory
        output_path = os.path.join(temp_dir, "output.pdf")
        pdf_document.save(output_path)

    return output_path

st.title("PDF Page Border and Watermark")

uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file is not None:
    st.write("PDF file uploaded!")

    watermark_text = st.text_input("Watermark Text", "Z-DIVISION")

    if st.button("Add Border and Watermark"):
        try:
            with io.BytesIO(uploaded_file.read()) as pdf_file:
                output_path = add_border_and_watermark(pdf_file, watermark_text)
                if output_path:
                    st.success("Border and watermark added successfully!")
                    st.download_button("Download PDF", output_path)
                else:
                    st.error("An error occurred while processing the PDF.")
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
