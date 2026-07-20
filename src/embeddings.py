from sentence_transformers import SentenceTransformer
model = SentenceTransformer("all-MiniLM-L6-v2")

def embed_text(chunks):
    embeddings = model.encode(chunks)
    return embeddings
