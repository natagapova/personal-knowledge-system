from pdf_loader import load_pdf 
text = load_pdf("data/crime.pdf")
print(text[:100])

from text_chunker import chunk_text
chunks = chunk_text(text)
print(chunks)