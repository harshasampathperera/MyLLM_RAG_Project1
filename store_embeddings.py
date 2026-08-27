import chromadb
import ollama

# Connect to ChromaDB
client = chromadb.PersistentClient(path="./chroma_db")

# Create collection
collection = client.get_or_create_collection(name="powerbi_docs")

# Read document
with open("document.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Create embedding
response = ollama.embed(model="nomic-embed-text", input=text)

embedding = response["embeddings"][0]

# Store in ChromaDB
collection.upsert(ids=["powerbi_document"], documents=[text], embeddings=[embedding])

print("Document successfully added to ChromaDB!")
