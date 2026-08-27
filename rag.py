import chromadb
import ollama

# Connect to ChromaDB
client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_collection(name="powerbi_docs")

# Ask the user for a question
question = input("\nEnter your question: ")

# Create question embedding
response = ollama.embed(model="nomic-embed-text", input=question)

question_embedding = response["embeddings"][0]

# Retrieve relevant information from ChromaDB
results = collection.query(query_embeddings=[question_embedding], n_results=2)

# Combine the retrieved documents
context = "\n\n".join(results["documents"][0])

# Create prompt
prompt = f"""
Answer the question using ONLY the information provided below.

Information:
{context}

Question:
{question}

Answer:
"""

# Ask LLM
response = ollama.chat(
    model="llama3.2:1b", messages=[{"role": "user", "content": prompt}]
)

# Display answer
print("\nAnswer:")
print(response["message"]["content"])
