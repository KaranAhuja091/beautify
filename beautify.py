import streamlit as st
import io
from PIL import Image
import fitz  # for handling PDFs

# Set the title and page layout
st.set_page_config(page_title="Beautify Document", layout="wide")

# Define the main content of the Streamlit app
def main():
    st.title("Beautify Your Document")
    st.sidebar.header("Settings")

    # Add a file uploader to allow users to upload a document
    uploaded_file = st.sidebar.file_uploader("Upload a document (PDF, Word, etc.)", type=["pdf", "docx"])

    # Define default values for border and background color
    default_border_color = st.sidebar.color_picker("Select Border Color", "#000000")
    default_background_color = st.sidebar.color_picker("Select Background Color", "#ffffff")

    # Define a function to beautify the document
    def beautify_document(file, border_color, background_color):
        if file is not None:
            image_list = []  # Initialize the list of image IO objects
            if uploaded_file.type == 'application/pdf':
                # Handle PDF files and convert pages to images
                pdf_document = fitz.open(file)
                for page_num in range(len(pdf_document)):
                    page = pdf_document.load_page(page_num)
                    image = page.get_pixmap()
                    image_bytes = image.get_png_data()
                    image_io = io.BytesIO(image_bytes)
                    image_list.append(image_io)
            
            # Display the images with borders and background color
            for image_io in image_list:
                pil_image = Image.open(image_io)
                st.image(pil_image, caption="Beautified Document", use_column_width=True, width=None)

            st.success("Document Beautified!")

    # Check if the user has uploaded a document and beautify it if so
    if uploaded_file is not None:
        beautify_document(uploaded_file, default_border_color, default_background_color)

if __name__ == "__main__":
    main()
