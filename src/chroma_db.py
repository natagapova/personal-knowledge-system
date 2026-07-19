import chromadb

def create_database():
    client = chromadb.PersistentClient(path="./chroma_db")
    collection = client.get_or_create_collection("documents")
    return collection

def store_embeddings(collection, chunks, embeddings):
    """
    each record needs three things:
    1. an ID number
    2. the text chunk
    3. the embedding vector
    """
    collection.add(
        ids=[str(i) for i in range(len(chunks))],
        documents = chunks,
        embeddings = embeddings,
    )

def search_database(collection, query_embedding):
    results = collection.query(
        query_embeddings = [query_embedding],
        n_results = 3,
    )
    return results