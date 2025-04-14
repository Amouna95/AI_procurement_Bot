import streamlit as st
from langchain.text_splitter import RecursiveCharacterTextSplitter
from utils import load_pdf_document, load_url_document, load_audio_document, load_text_document
from langchain_community.vectorstores import Qdrant
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
import os

load_dotenv()

st.subheader("Add new document")

type_document = st.radio(
    "Upload documents using",
    ["PDF", "Url Web page", "audio", "text"]
)

collection_name = "Procurement"

# Initialisation de start_chat
if 'start_chat' not in st.session_state:
    st.session_state.start_chat = False

if type_document == "PDF":
    st.session_state.start_chat = False
    uploaded_files = st.file_uploader("Choose a PDF file", accept_multiple_files=True, type=["pdf"])
    if len(uploaded_files) > 0:
        for uploaded_file in uploaded_files:
            file_path = os.path.join("uploaded_files", uploaded_file.name)
            os.makedirs("uploaded_files", exist_ok=True)  # Crée le dossier s'il n'existe pas
            with open(file_path, "wb") as f:
                f.write(uploaded_file.getbuffer())
            
            documents_pages = load_pdf_document(pdf=file_path)
            remove_text = st.text_input(label="Add a text that you want to remove from documents before processing like personal information etc.", placeholder="Optional")

            process_btn = st.button(label="Process and store documents")

            if process_btn:
                for index, page in enumerate(documents_pages):
                    if remove_text != '':
                        documents_pages[index].page_content = page.page_content.replace(remove_text, '')
                    documents_pages[index].page_content = page.page_content.replace('\n', ' ').strip()

                text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=250)
                documents = text_splitter.split_documents(documents_pages)

                embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
                url = os.getenv("QDRANT_URL")

                qdrant = Qdrant.from_documents(
                    documents=documents,
                    embedding=embeddings,
                    url=url,
                    collection_name=collection_name,
                )
                
                st.write(f"{uploaded_file.name} is processed and successfully stored in database")
                st.session_state.start_chat = True
                
    if st.session_state.start_chat:
        st.page_link("chatbot.py", label="Start chatting with documents")

elif type_document == "Url Web page":
    st.session_state.start_chat = False
    url_web_page = st.text_input(label="Enter URL of the web page", placeholder="https://")
    remove_text = st.text_input(label="Add a text that you want to remove from documents before processing like personal information etc.", placeholder="Optional")

    process_btn = st.button(label="Process and store web page")
    if process_btn and url_web_page:
        web_url_documents = load_url_document(url_web_page)

        for index, page in enumerate(web_url_documents):
            if remove_text != '':
                web_url_documents[index].page_content = page.page_content.replace(remove_text, '')
            web_url_documents[index].page_content = page.page_content.replace('\n', ' ').strip()
        
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=250)
        documents = text_splitter.split_documents(web_url_documents)

        embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
        url = os.getenv("QDRANT_URL")

        qdrant = Qdrant.from_documents(
            documents=documents,
            embedding=embeddings,
            url=url,
            collection_name=collection_name,
        )
            
        st.write("The web page is processed and successfully stored in database")
        st.session_state.start_chat = True

        if st.session_state.start_chat:
            st.page_link("chatbot.py", label="Start chatting with web page")

elif type_document == "audio":
    st.session_state.start_chat = False
    uploaded_audio = st.file_uploader("Choose an audio file", accept_multiple_files=False, type=["mp3", "wav", "m4a"])
    if uploaded_audio:
        file_path = os.path.join("uploaded_files", uploaded_audio.name)
        os.makedirs("uploaded_files", exist_ok=True)  # Crée le dossier s'il n'existe pas
        with open(file_path, "wb") as f:
            f.write(uploaded_audio.getbuffer())
        
        documents_audio = load_audio_document(audio=file_path)
        remove_text = st.text_input(label="Add a text that you want to remove from documents before processing like personal information etc.", placeholder="Optional")

        process_btn = st.button(label="Process and store audio")

        if process_btn:
            for index, page in enumerate(documents_audio):
                if remove_text != '':
                    documents_audio[index].page_content = page.page_content.replace(remove_text, '')
                documents_audio[index].page_content = page.page_content.replace('\n', ' ').strip()
            
            text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=250)
            documents = text_splitter.split_documents(documents_audio)

            embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
            url = os.getenv("QDRANT_URL")

            qdrant = Qdrant.from_documents(
                documents=documents,
                embedding=embeddings,
                url=url,
                collection_name=collection_name,
            )
            
            st.write("The audio file is processed and successfully stored in database")
            st.session_state.start_chat = True

            if st.session_state.start_chat:
                st.page_link("chatbot.py", label="Start chatting with audio")

elif type_document == "text":
    st.session_state.start_chat = False
    text_input = st.text_area("Enter your text document content")
    remove_text = st.text_input(label="Add a text that you want to remove from documents before processing like personal information etc.", placeholder="Optional")
    
    process_btn = st.button(label="Process and store text")

    if process_btn and text_input:
        text_document = load_text_document(text_input)

        if remove_text:
            text_document.page_content = text_document.page_content.replace(remove_text, '')
        
        text_document.page_content = text_document.page_content.replace('\n', ' ').strip()

        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=250)
        documents = text_splitter.split_documents([text_document])

        embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
        url = os.getenv("QDRANT_URL")

        qdrant = Qdrant.from_documents(
            documents=documents,
            embedding=embeddings,
            url=url,
            collection_name=collection_name,
        )
        
        st.write("The text document is processed and successfully stored in database")
        st.session_state.start_chat = True

        if st.session_state.start_chat:
            st.page_link("chatbot.py", label="Start chatting with text document")
