import chromadb
import ollama

# -----------------------------
# 1. Connect to ChromaDB
# -----------------------------

client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_collection(name="powerbi_docs")


# -----------------------------
# 2. Ask user a question
# -----------------------------

question = input("\nEnter your question: ")


# -----------------------------
# 3. Create question embedding
# -----------------------------

response = ollama.embed(model="nomic-embed-text", input=question)

question_embedding = response["embeddings"][0]


# -----------------------------
# 4. Search ChromaDB
# -----------------------------

results = collection.query(query_embeddings=[question_embedding], n_results=3)


# -----------------------------
# 5. Get relevant chunks
# -----------------------------

chunks = results["documents"][0]


print("\n--- Retrieved Chunks ---")

for i, chunk in enumerate(chunks):

    print(f"\nChunk {i + 1}:")
    print(chunk)


# -----------------------------
# 6. Combine chunks
# -----------------------------

context = "\n\n".join(chunks)


# -----------------------------
# 7. Create prompt
# -----------------------------

prompt = f"""
Answer the question using ONLY the information provided below.

If the information does not contain the answer, say:
"I don't have enough information in my documents."

Information:
{context}

Question:
{question}

Answer:
"""


# -----------------------------
# 8. Ask LLM
# -----------------------------

response = ollama.chat(
    model="llama3.2:1b", messages=[{"role": "user", "content": prompt}]
)


# -----------------------------
# 9. Display answer
# -----------------------------

print("\nAnswer:")

print(response["message"]["content"])
