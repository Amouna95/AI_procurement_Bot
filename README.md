# AI Procurement Bot Powered by the Advanced RAG App – Handle PDFs, Web pages, Videos, Audios & Texts

## 🎯 Project Purpose

This project is an interactive chatbot interface built with **Streamlit** that allows users to query a collection of procurement-related documents using natural language.

It leverages modern NLP technologies to provide **accurate, context-based answers** by combining:

- **Semantic search** (via vector embeddings using OpenAI + Qdrant)
- **Large Language Model reasoning** (using LLaMA 3 via Groq)
- **Contextual prompting** to ensure answers are grounded in document content

## 🧠 How It Works

1. The user selects a document collection (currently only "Procurement").
2. They ask a question in natural language.
3. The app:
   - Uses **OpenAI Embeddings** to embed the question
   - Retrieves the most relevant document chunks from **Qdrant**
   - Feeds them into **LLaMA 3 (Groq)** with a prompt that ensures helpful and grounded responses
4. The chatbot responds with:
   - A helpful answer to the question
   - The **context/source** from which the answer was derived

## 🛠️ Tech Stack

- [Streamlit](https://streamlit.io/) – UI framework
- [LangChain](https://www.langchain.com/) – Orchestration framework
- [Qdrant](https://qdrant.tech/) – Vector database
- [OpenAI](https://openai.com/) – Embeddings (text-embedding-3-small)
- [Groq](https://groq.com/) – LLM inference with LLaMA 3 (70B)
- `.env` – Securely stores API keys

## ✅ Features

- Interactive chat interface
- Context-aware responses
- Easy integration with Qdrant collections
- Supports custom prompts for better control over model behavior


## How to run the app

#### 1. Clone the project
```sh
git clone https://github.com/Amouna95/AI_procurement_Bot.git
```
#### 2. Copy .env.example to .env file
```sh
cp .env.example .env
```  
  And add values for variables environnment
  
#### 3. Create virtual environment and install requirements
- To create virtual environment 
```sh
python -m venv venv 
``` 
To activate the virtual environment
- For linux
```sh
source venv/bin/activate 
```  

- For windows
```sh
venv/Scripts/activate
```  

To install all requirements

```sh
pip install -r requirements.txt
```  


#### 4. Install Qdrant locally using docker and run it
```sh
sudo docker pull qdrant/qdrant 
sudo docker run -p 6333:6333 -v .:/qdrant/storage qdrant/qdrant
```  

#### 5. finally run the app
```sh
streamlit run app.py
```  




   
   
