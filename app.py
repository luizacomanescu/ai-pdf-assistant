import streamlit as st
import PyPDF2
import io

st.set_page_config(page_title="AI PDF Assistant", layout="wide")
st.title("📄 AI PDF Assistant")

# Upload the PDF
uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

if uploaded_file:
    # Read PDF and extract text
    pdf_reader = PyPDF2.PdfReader(uploaded_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text() or ""

    st.subheader("📃 Extracted Text")
    st.write(text if text else "No readable text found in PDF.")
