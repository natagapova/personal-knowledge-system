from pdf_loader import load_pdf 
text = load_pdf("data/crime.pdf")

from text_chunker import chunk_text
chunks = chunk_text(text)

from embeddings import embed_chunks
embeddings = embed_chunks(chunks)
print(embeddings.shape)