from pdf_loader import load_pdf 
text = load_pdf("data/crime.pdf")

from text_chunker import chunk_text
chunks = chunk_text(text)

from embeddings import embed_chunks
embeddings = embed_chunks(chunks)

from chroma_db import create_database, store_embeddings, search_database
collection = create_database()
store_embeddings(collection, chunks, embeddings)

while True:
    query = input("\nAsk a question (or type 'exit'): ")

    if query.lower() == "exit":
        break

    query_embedding = embed_chunks([query])[0]
    results = search_database(collection, query_embedding)

    for i, document in enumerate(results["documents"][0], start=1):
        print(f"\nResult {i}:")
        print(document)