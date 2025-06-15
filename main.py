import streamlit as st
import time
import os
import pandas as pd
from io import StringIO

from dotenv import load_dotenv
from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from openai import OpenAI

load_dotenv()

client = OpenAI()

if "file" not in st.session_state:
    st.session_state["file"] = "not done"

def change_file_state():
    st.session_state["file"] = "done"

st.title("RAG Chat Application")

"---"

c1, c2 = st.columns([1,2])

c1.markdown("### Upload PDF file")
c2.markdown("### Process for Chatting")

uploaded_file = c1.file_uploader("Choose a file", on_change=change_file_state)

if uploaded_file is not None:
    with open(os.path.join(uploaded_file.name), "wb") as f:
        f.write(uploaded_file.getbuffer())

    if st.session_state["file"] == "done":
        progress_bar = c1.progress(0)
        for per_completed in range(100):
            time.sleep(0.05)
            progress_bar.progress(per_completed+1)

        c1.success("File uploaded successfully")
    st.session_state["file"] = "not done"


    pdf_path = Path(__file__).parent / uploaded_file.name

    #Loading
    loader = PyPDFLoader(file_path=pdf_path)
    docs = loader.load()

    #Chunking
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 1000,
        chunk_overlap = 400

    )

    split_docs = text_splitter.split_documents(documents=docs)

    # Vector Embedding

    embedding_model = OpenAIEmbeddings(
        model="text-embedding-3-large",
    )

    # Uding [embedding_model] create embeddings of [split_docs] and store in DB

    vector_store = QdrantVectorStore.from_documents(
        documents=split_docs,
        url="http://localhost:6333",
        collection_name="learning_vectors",
        embedding=embedding_model
    )

    # Take User Query

    query = c2.text_area("", placeholder="Ready for Chatting ...")

    if query is not None:
        
        # Vector Similarity Search [query] in DB
        search_results = vector_store.similarity_search(
            query=query
        )

        # print("search_results: ", search_results)

        context =[f"Page Context: {result.page_content}\n\n Page number: {result.metadata['page_label']}\n\n File source {result.metadata['source']} " for result in search_results]

        SYSTEM_PROMPT = f""" 
            You are a helpful AI Assistant who answers user query based on the available context
            retrieved from a PDF file along with page_contents and page number.

            You should only answer the user based on the following context and navigate the user
            to open the right page number to know more.

            Context:
            {context}
        """

        # print("SYSTEM_PROMPT : ", SYSTEM_PROMPT)

        #st.write(SYSTEM_PROMPT)

        chat_completion = client.chat.completions.create(
        model="gpt-4.1",
        messages=[
            {"role":"system", "content": SYSTEM_PROMPT},
            {"role":"user", "content":query},
        ]
        )

        #print(f"👀 : {chat_completion.choices[0].message.content}")
        st.write(chat_completion.choices[0].message.content)


