import chromadb

# Connect to ChromaDB
client = chromadb.PersistentClient(path="./chroma_db")

# Get the collection
collection = client.get_collection(name="powerbi_docs")

# Get everything stored in the collection
results = collection.get()

print("Number of documents:", len(results["documents"]))

print("\n--- Documents stored in ChromaDB ---")

for i, document in enumerate(results["documents"]):
    print(f"\nDocument {i + 1}:")
    print(document)