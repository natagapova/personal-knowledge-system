from pdf_loader import load_pdf
from text_chunker import chunk_text


pages = load_pdf("data/mathai.pdf")

chunks, page_positions = chunk_text(pages)

print(chunks[5:8])