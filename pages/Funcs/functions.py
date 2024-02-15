from langchain.document_loaders import UnstructuredPDFLoader, OnlinePDFLoader, PyPDFLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma, Pinecone
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.chains.question_answering import load_qa_chain
from langchain import OpenAI
from langchain_experimental.agents import create_pandas_dataframe_agent
import pandas as pd
import json
import streamlit as st

def generate_response(query, vectorstore):
    docs = vectorstore.similarity_search(query)
    llm = ChatOpenAI(temperature=0.9)
    chain = load_qa_chain(llm, chain_type="stuff")
    return chain.run(input_documents=docs, question=query)


def load_pdf(file):
    load_pdf = PyPDFLoader(file)
    data = load_pdf.load()
    return data

def documents(data):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    texts = text_splitter.split_documents(data)
    return texts

def embeddings(texts):
    embeddings = OpenAIEmbeddings()
    vectorstore = Chroma.from_documents(texts, embeddings)
    return vectorstore


# For the CSV part I used parts of Gao's code in his GitHub
# https://github.com/tarikkaoutar/Talk_with_CSV/blob/main/talk_with_csv.py

# This will be the functions used in the CSV talk page

def agent_df(file):
    return create_pandas_dataframe_agent(OpenAI(temperature=0), file, verbose=True)


def ask_agent(agent, query):
    """
    The following function will be used to ask the agent a question.

    Gao describes the function as follows:

    Args:
        agent: The agent to query.
        query: The query to ask the agent.

    Returns:
        The response from the agent as a string.
    """
    # The prompt need query guidelines to answer and format the question
    prompt = (
        """
        Let's decode the way to respond to the queries. The responses depend on the type of information requested in the query. 

        1. If the query requires a table, format your answer like this:
           {"table": {"columns": ["column1", "column2", ...], "data": [[value1, value2, ...], [value1, value2, ...], ...]}}

        2. For a bar chart, respond like this:
           {"bar": {"columns": ["A", "B", "C", ...], "data": [25, 24, 10, ...]}}

        3. If a line chart is more appropriate, your reply should look like this:
           {"line": {"columns": ["A", "B", "C", ...], "data": [25, 24, 10, ...]}}

        Note: We only accommodate two types of charts: "bar" and "line".

        4. For a plain question that doesn't need a chart or table, your response should be:
           {"answer": "Your answer goes here"}

        For example:
           {"answer": "The Product with the highest Orders is '15143Exfo'"}

        5. If the answer is not known or available, respond with:
           {"answer": "I do not know."}

        Return all output as a string. Remember to encase all strings in the "columns" list and data list in double quotes. 
        For example: {"columns": ["Products", "Orders"], "data": [["51993Masc", 191], ["49631Foun", 152]]}

        Now, let's tackle the query step by step. Here's the query for you to work on: 
        """
        + query
    )
    response = agent.run(prompt)

    return str(response)

def decode_response(response: str) -> dict:
    """
    This function converts the string response from the model to a dictionary object.

    The agent response follows the following structure:
    - Question: they prompt
    - Thought: the agent's thought process
    - Action: the agent's action to take based on python
    - Action Input: the input to the action
    - Observation: the result of the action
    - Thought: the agent's knows the final answer
    - Final answer: the final answer to the original question (WHAT WE NEED!)

    Args:
        response (str): response from the model

    Returns:
        dict: dictionary with response data
    """
    return json.loads(response)

def write_answer(response_dict: dict):
    """
    This function extracts the final answer from the response dictionary.

    Args:
        response (dict): dictionary with response data

    Returns:
        str: the final answer
    """
    # Check if the response is an answer.
    if "answer" in response_dict:
        st.write(response_dict["answer"])

    # Check if the response is a bar chart.
    if "bar" in response_dict:
        data = response_dict["bar"]
        try:
            df_data = {
                    col: [x[i] if isinstance(x, list) else x for x in data['data']]
                    for i, col in enumerate(data['columns'])
                }       
            df = pd.DataFrame(df_data)
            st.bar_chart(df)
        except ValueError:
            print(f"Couldn't create DataFrame from data: {data}")

# Check if the response is a line chart.
    if "line" in response_dict:
        data = response_dict["line"]
        try:
            df_data = {col: [x[i] for x in data['data']] for i, col in enumerate(data['columns'])}
            df = pd.DataFrame(df_data)
            st.line_chart(df)
        except ValueError:
            print(f"Couldn't create DataFrame from data: {data}")


    # Check if the response is a table.
    if "table" in response_dict:
        data = response_dict["table"]
        df = pd.DataFrame(data["data"], columns=data["columns"])
        st.table(df)