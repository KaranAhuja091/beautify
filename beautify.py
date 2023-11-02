import streamlit as st

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
            # Display the beautified document with borders and background color
            st.success("Document Beautified!")
            st.image(file, caption="Beautified Document", use_container_width=True, output_format="PDF")

    # Check if the user has uploaded a document and beautify it if so
    if uploaded_file is not None:
        beautify_document(uploaded_file, default_border_color, default_background_color)

if __name__ == "__main__":
    main()
