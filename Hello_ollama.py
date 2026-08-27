import ollama

response = ollama.chat(
    model="llama3.2:1b",
    # model="gemma3:4b",
    messages=[
        {
            "role": "user",
            "content": "What is RAG? Explain it to me as a beginner.",
        }
    ],
)

print(response["message"]["content"])
