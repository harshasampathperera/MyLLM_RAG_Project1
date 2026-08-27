import chromadb
import ollama

# add by harsha sampath 27/08/2026
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


print("\n--- Retrieved RAG Information ---")

for i, chunk in enumerate(chunks):

    print(f"\nChunk {i + 1}:")
    print(chunk)


# -----------------------------
# 6. Combine retrieved chunks
# -----------------------------

context = "\n\n".join(chunks)


# -----------------------------
# 7. Create HYBRID prompt
# -----------------------------

prompt = f"""
You are answering a user's question using two sources of knowledge:

SOURCE 1: Your general knowledge
SOURCE 2: Information retrieved from my RAG knowledge base

Use BOTH sources when appropriate.

Important rules:

1. Use your general knowledge to provide useful public/general information.
2. Use the RAG information to provide company-specific or document-specific information.
3. Clearly distinguish information that comes from the RAG knowledge base.
4. Do not ignore relevant information from the RAG knowledge base.
5. Do not invent facts.
6. If you are uncertain about a fact, say so.

RAG INFORMATION:
{context}

USER QUESTION:
{question}

Provide a useful combined answer.
"""


# -----------------------------
# 8. Ask LLM
# -----------------------------

response = ollama.chat(
    model="llama3.2:1b", messages=[{"role": "user", "content": prompt}]
)


# -----------------------------
# 9. Display final answer
# -----------------------------

print("\n--- Final Answer ---")

print(response["message"]["content"])
