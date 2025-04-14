from langchain_community.document_loaders import PyPDFLoader, WebBaseLoader, TextLoader
import speech_recognition as sr
import whisper

def load_pdf_document(pdf):
    loader = PyPDFLoader(pdf)
    documents = loader.load()
    return documents

def load_url_document(url):
    web_loader = WebBaseLoader(url)
    web_url_documents = web_loader.load()
    return web_url_documents

def load_audio_document(audio_path):
    model = whisper.load_model("small")
    result = model.transcribe(audio_path)
    return [{"page_content": result["text"], "source": audio_path}]

def load_text_document(text_path):
    loader = TextLoader(text_path)
    documents = loader.load()
    return documents

def custom_prompt(qdrant, query: str):
    results = qdrant.similarity_search(query, k=5)
    source_knowledge = "\n".join([x.page_content for x in results])
    augment_prompt = f"""Using the contexts below, answer the query:

    Contexts:
    {source_knowledge}

    Query: {query}"""
    return augment_prompt
