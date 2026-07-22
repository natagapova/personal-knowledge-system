from pdf_loader import load_pdf 
text = load_pdf("data/crime.pdf")

from text_chunker import chunk_text
chunks = chunk_text(text)

from embeddings import embed_text
embeddings = embed_text(chunks)

from chroma_db import create_database, store_embeddings, search_database
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

    context = "\n".join(results["documents"][0])
    print(context)

    # Old results output
    """
    for i, document in enumerate(results["documents"][0], start=1):
        print(f"\nResult {i}:")
        print(document)
    """