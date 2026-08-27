import chromadb
import ollama

client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_collection(
    name="powerbi_docs"
)

question = "Which company uses Power BI?"

response = ollama.embed(
    model="nomic-embed-text",
    input=question
)

question_embedding = response["embeddings"][0]

results = collection.query(
    query_embeddings=[question_embedding],
    n_results=1
)

print("\n--- Retrieved information ---")
print(results["documents"][0][0])

print("\n--- Distance ---")
print(results["distances"][0][0])