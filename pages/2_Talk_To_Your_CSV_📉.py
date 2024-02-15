import streamlit as st
from langchain import OpenAI
from langchain_experimental.agents import create_pandas_dataframe_agent
import pandas as pd
import json
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
from pages.Funcs.functions import *
import os


def is_csv(file):
    _, ext = os.path.splitext(file.name)
    return ext.lower() == '.csv'

st.set_page_config(page_title="Talk To Your CSV!", page_icon="📊", layout="wide")

st.title('Talk To Your CSV! :bar_chart:')

openai_api_key = st.sidebar.text_input('OpenAI API Key', type='password')

st.write('Please Upload your CSV file')


uploaded_file = st.file_uploader("Choose a file", type=['csv'])
if uploaded_file is not None:
    if is_csv(uploaded_file):
        st.write('You have uploaded a CSV file.')
        df = pd.read_csv(uploaded_file, index_col=0)
        st.write('Here is a sample of your data:')
        st.write(df.head())
        st.write(f'Your dataset contains {len(df.columns)} columns and {len(df)} rows')

        tab1, tab2 = st.tabs(['Ask a question to the CSV', 'Generate a quick EDA'])
        with tab1:
            with st.form('my_form'):
                query = st.text_area('Enter text:', 'How many rows are in the CSV?')
                submitted = st.form_submit_button('Submit')
                if not openai_api_key.startswith('sk-'):
                    st.warning('Please enter your OpenAI API key!', icon='⚠')
                if submitted and openai_api_key.startswith('sk-'):
                    #st.write("You have submitted the form")
                    agent = agent_df(file=df)
                    response = ask_agent(agent=agent, query=query)
                    decoded_response = decode_response(response)
                    write_answer(decoded_response)
        with tab2:
            st.write("The following button will generate a quick Exploratory Data Analysis of your data")
            eda = st.button("Generate a quick EDA")
            if eda:
                st.write('Exploratory Data Analysis - Profiler')
                
                pr = ProfileReport(df, explorative=True)
                st_profile_report(pr)

    else:
        st.warning("Upload a CSV, your file is not in CSV format.",icon='⚠')