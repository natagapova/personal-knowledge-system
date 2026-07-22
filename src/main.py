from pdf_loader import load_pdf
from text_chunker import chunk_text
from embeddings import embed_text
from chroma_db import create_database, store_embeddings, search_database
from llm import generate_answer

text = load_pdf(f"data/mathai.pdf")
chunks = chunk_text(text)
embeddings = embed_text(chunks)

collection = create_database()
if collection.count() == 0:
    print("Indexing PDF...")
    store_embeddings(collection, chunks, embeddings)
else:
    print("Database already exists.")

while True:
    query = input("\nAsk a question (or type 'exit'): ")

    if query.lower() == "exit":
        break

    query_embedding = embed_text([query])[0]
    results = search_database(collection, query_embedding)

    context = "\n\n".join(results["documents"][0])
    
    answer = generate_answer(query, context)
    print(answer)
