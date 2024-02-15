import streamlit as st
from langchain.document_loaders import UnstructuredPDFLoader, OnlinePDFLoader, PyPDFLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma, Pinecone
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.chains.question_answering import load_qa_chain
import pandas as pd
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
from pages.Funcs.functions import *
import tempfile
import os

def is_pdf(file):
    _, ext = os.path.splitext(file.name)
    return ext.lower() == '.pdf'

st.set_page_config(page_title="Talk To Your PDF!", page_icon="📖", layout="wide")
st.title('Talk To Your PDF! :book:')


openai_api_key = st.sidebar.text_input('OpenAI API Key', type='password')

st.write('Please Upload your PDF file')
  
uploaded_file = st.file_uploader("Choose a file", type=['pdf'])
if uploaded_file is not None:
    if is_pdf(uploaded_file):
        st.write('You have uploaded a file.')
        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            tmp.write(uploaded_file.getvalue())
            tmp_path = tmp.name
        data = load_pdf(tmp_path)
        st.write(f'You have {len(data)} document(s) in your data')
        st.write(f'There are {len(data[0].page_content)} characters in your sample document')
        st.write(f'Here is a sample of 200 letters: {data[0].page_content[:200]}')

        with st.form('my_form'):
            query = st.text_area('Enter text:', 'What is the main idea in the document?')
            submitted = st.form_submit_button('Submit')
            if not openai_api_key.startswith('sk-'):
                st.warning('Please enter your OpenAI API key!', icon='⚠')
            if submitted and openai_api_key.startswith('sk-'):
                texts = documents(data)
                vectorstore = embeddings(texts)
                response = generate_response(query, vectorstore)
                st.write(response)
    else:
        st.warning("Upload a PDF, your file is not in PDF format.",icon='⚠')
