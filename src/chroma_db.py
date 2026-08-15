import chromadb

def create_database():
    client = chromadb.PersistentClient(path="./chroma_db")
    collection = client.get_or_create_collection("documents")
    return collection

def store_embeddings(collection, chunks, embeddings, filename):
    """
    each record needs three things:
    1. an ID number
    2. the text chunk
    3. the embedding vector
    4. the filename
    """

    documents = [] # strings only
    metadata = [] # filename + pages per chunk

    for chunk in chunks:
        documents.append(chunk["text"])

        page_numbers = chunk["page_numbers"]
        pages_string = ",".join(str(p) for p in page_numbers)

        metadata.append({
            "filename": filename,
            "page_numbers": pages_string,
        })

    collection.add(
        ids=[f"{filename}_{str(i)}" for i in range(len(chunks))],
        documents = documents, # strings/chunks
        embeddings = embeddings,
        metadatas = metadata, # citation information for each chunk
    )

def search_database(collection, query_embedding, filename = None):
    if filename: # if filename is provided, only search that file
        results = collection.query(
            query_embeddings = [query_embedding],
            n_results = 5,
            where = {"filename": filename},
        )
    else: # if filename is not provided, search all files (the whole folder)
        results = collection.query(
            query_embeddings = [query_embedding],
            n_results = 5,
        )
    return results