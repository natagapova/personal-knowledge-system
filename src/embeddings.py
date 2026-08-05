from sentence_transformers import SentenceTransformer
model = SentenceTransformer("all-MiniLM-L6-v2")

def embed_text(chunks):
    texts = []

    for chunk in chunks:
        if isinstance(chunk, str):
            texts.append(chunk)
        else:
            texts.append(chunk["text"])

    embeddings = model.encode(texts)
    return embeddings
