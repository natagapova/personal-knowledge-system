from sentence_transformers import SentenceTransformer
model = SentenceTransformer("all-MiniLM-L6-v2")

def embed_text(chunks):
    texts = [chunk["text"] for chunk in chunks]
    embeddings = model.encode(texts)
    return embeddings
