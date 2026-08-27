import ollama

text = """
Power BI is a business intelligence and data visualization platform developed by Microsoft.

Power BI allows users to connect to different data sources such as SQL Server, Excel, SharePoint, Snowflake and cloud services.

Power BI uses DAX for creating calculated columns and measures.

One of the main companies use Power BI is London stock Exchange Group.
"""

response = ollama.embed(model="nomic-embed-text", input=text)

embedding = response["embeddings"][0]

print("Embedding created!")
print("Number of values:", len(embedding))
print("First 10 values:")
print(embedding[:10])
