\# Local LLM RAG Project



A beginner-friendly Retrieval-Augmented Generation (RAG) project using:



\- Python

\- Ollama

\- Llama 3.2

\- nomic-embed-text

\- ChromaDB





\## Architecture



Documents.txt

&#x20;      ↓

Text Extraction

&#x20;      ↓

Text Chunking

&#x20;      ↓

Embeddings

&#x20;      ↓

ChromaDB

&#x20;      ↓

Question

&#x20;      ↓

Semantic Search

&#x20;      ↓

Relevant Context

&#x20;      ↓

Llama

&#x20;      ↓

Answer



\## Models



LLM:

llama3.2:1b



Embedding:

nomic-embed-text



\## Setup



Create a virtual environment:



python -m venv venv



Activate:



.\\venv\\Scripts\\Activate.ps1



Install packages:



pip install -r requirements.txt



Make sure Ollama is installed and the required models are available.



\## Run



Ingest  documents:



python ingest\_.py



Run RAG:



python pdf\_rag.py

