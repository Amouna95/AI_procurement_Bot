 # Advanced RAG (Retrival Augmented Generation using multi sources: PDF, URL, VIDEO, AUDIO, IMAGE
### How does it work ?
#### 1. sources (each source is converted into text): 
- PDF: extract the text from the PDF
- URL: Extract the text (Web scrapping)
- Image: OCR: extract the text from an image
- Video : extract audio from video and transcribe it into text
- Audio: transcribe the audio into text

#### 2. Embeddings
extracting text from an source and splitting it into small chunks. each chunk is converted into numerical values (text-embedding) using openai embedding model

#### 3. store locally vectors into Qdrant database
 Qdrant is a vector similarity search engine and vector database.
 
#### 4. Extract top k (k=5 in the app) relevants informations 
Base on the user query, we extract k relevants informations by comparing the embedded user input and vectors store from qdrant using cosine similarity

#### 5. Passing these top 5 relevant informations into LLM (Large language model) as a context: llama-3.1-70B:
These relevants informations are passed into the prompts as a context : example of the final prompt: 
    """ Using the contexts below, answer the query:
        Contexts:
       {relevants_informations}
       Query: {query}"""
  

#### 6. Get the result
- Get the answer from the LLM


### How to run the app

#### 1. Clone the project
```sh
git clone https://github.com/ngamcode96/advanced_rag_chatbot.git
```
#### 2. Copy .env.example to .env file
```sh
cp .env.example .env
```  
  And add values for variables environnment
  
#### 3. Create virtual environment and install requirements
- To create virtual environment 
```sh
python3 -m venv venv 
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




   
   
