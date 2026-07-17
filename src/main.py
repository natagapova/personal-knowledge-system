from pdf_loader import load_pdf 
text = load_pdf("data/crime.pdf")

from text_chunker import chunk_text
chunks = chunk_text(text)

from embeddings import embed_chunks
embeddings = embed_chunks(chunks)

from chroma_db import create_database, store_embeddings
collection = create_database()
store_embeddings(collection, chunks, embeddings)
print(collection.count())