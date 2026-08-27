import chromadb
import ollama

# -----------------------------
# 1. Connect to ChromaDB
# -----------------------------

client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_or_create_collection(
    name="powerbi_docs"
)


# -----------------------------
# 2. Read document
# -----------------------------

with open("document.txt", "r", encoding="utf-8") as file:
    text = file.read()


# -----------------------------
# 3. Split document into chunks
# -----------------------------

chunks = [
    chunk.strip()
    for chunk in text.split("\n\n")
    if chunk.strip()
]


# -----------------------------
# 4. Show chunks
# -----------------------------

print("\nNumber of chunks:", len(chunks))

for i, chunk in enumerate(chunks):
    print(f"\n--- Chunk {i + 1} ---")
    print(chunk)


# -----------------------------
# 5. Create embeddings
# -----------------------------

embeddings = []

for chunk in chunks:

    response = ollama.embed(
        model="nomic-embed-text",
        input=chunk
    )

    embedding = response["embeddings"][0]

    embeddings.append(embedding)


# -----------------------------
# 6. Store chunks in ChromaDB
# -----------------------------

ids = [
    f"chunk_{i}"
    for i in range(len(chunks))
]

collection.add(
    ids=ids,
    documents=chunks,
    embeddings=embeddings
)


print("\nSuccessfully stored chunks in ChromaDB!")