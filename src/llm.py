import ollama
from ollama import chat

"""
response = ollama.chat(
    model="llama3.2",
    messages=[
        {
            "role": "user",
            "content": "Hello! Tell me a fun fact."
        }
    ]
)
print(response.message.content)
"""

def generate_answer(question, context):
    # the f before the sring means "python, replace variables inside {} with their values"
    prompt = f"""
    Use the following context to answer the quetsion.

    Context:
    {context}

    Question:
    {question}
    """

    response = ollama.chat(
        model="llama3.2",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    return response.message.content