import ollama
from ollama import chat

def generate_answer(question, context):
    # the f before the sring means "python, replace variables inside {} with their values"
    prompt = f"""
    You are a question answering assistant.
    Answer the user's question using ONLY the provided context.

    If the answer cannot be found in the context, say:
    "I don't know based on the provided documents."

    Do not use your own knowledge.
    Do not make up information.

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