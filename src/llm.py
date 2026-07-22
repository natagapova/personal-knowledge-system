import ollama
from ollama import chat

response = ollama.chat(
    model="llama3.2",
    messages=[
        {
            "role": "user",
            "content": "Hello! Tell me a fun fact."
        }
    ]
)
print(response)