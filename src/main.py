from pdf_loader import load_pdf 
text = load_pdf("data/crime.pdf")

from text_chunker import chunk_text
chunks = chunk_text(text)

from embeddings import embed_chunks
my_array = ['hello world this is a test', 'cats are great', 'dogs are wonderful', 'i love dogs']
embeddings = embed_chunks(my_array)
print(embeddings)