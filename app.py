import streamlit as st
import PyPDF2
import requests

st.set_page_config(page_title="AI PDF Assistant", layout="wide")
st.title("📄 AI PDF Assistant")

# Replace this with your actual Hugging Face API key
HUGGINGFACE_API_KEY = st.secrets["huggingface"]["api_key"]

API_URL = "https://api-inference.huggingface.co/models/deepset/roberta-base-squad2"
headers = {"Authorization": f"Bearer {HUGGINGFACE_API_KEY}"}

def extract_text_from_pdf(uploaded_file):
    reader = PyPDF2.PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

def query_huggingface(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

uploaded_file = st.file_uploader("Upload your PDF", type="pdf")

if uploaded_file:
    pdf_text = extract_text_from_pdf(uploaded_file)
    st.text_area("Extracted PDF Text", pdf_text, height=300)
    question = st.text_input("Ask a question about the PDF:")
    
    if st.button("Get Answer") and question:
        with st.spinner("Getting answer..."):
            data = {"inputs": {"question": question, "context": pdf_text}}
            result = query_huggingface(data)
            answer = result.get('answer', 'No answer found.')
            st.markdown(f"**Answer:** {answer}")