import os
from pdf_loader import load_pdf
from text_chunker import chunk_text
from embeddings import embed_text
from chroma_db import create_database, store_embeddings, search_database
from llm import generate_answer

data_folder = "data"
pdf_files = []
for filename in os.listdir(data_folder):
    if filename.endswith(".pdf"):
        pdf_files.append(filename)

while True:
    print("Search in:")
    print("1 - one file")
    print("2 - whole folder")
    choice = input("Enter 1 or 2: ")

    if choice == "1":
        print("\nAvailable files:")
        for i, pdf_file in enumerate(pdf_files):
            print(f"{i+1} - {pdf_file}")

        file_choice = input("Enter file number: ")
        selected_file = pdf_files[int(file_choice) - 1]
        print(f"Selected file: {selected_file}")

        break

    elif choice == "2":
        print("You chose whole folder")
        selected_file = None # none = all files

        break

    else:
        print("Invalid choice. Try again.")

collection = create_database()

if collection.count() == 0:
    print("Indexing PDFs...")
    for pdf_file in pdf_files:
        path = f"{data_folder}/{pdf_file}"
        pages = load_pdf(path)

        chunks, page_positions = chunk_text(pages)
        embeddings = embed_text(chunks)
        filename = pages[0]["filename"]

        store_embeddings(collection, chunks, embeddings, filename)

        print(f"Indexed {pdf_file}: {len(chunks)} chunks")
else:
    print("Database already exists.")

while True:
    query = input("\nAsk a question (or type 'exit'): ")

    if query.lower() == "exit":
        break

    query_embedding = embed_text([query])[0]
    results = search_database(collection, query_embedding, selected_file)

    context_parts = []
    for i in range(len(results["documents"][0])):
        doc = results["documents"][0][i]
        meta = results["metadatas"][0][i]

        citation = f"[{meta['filename']}, page {meta['page_numbers']}]"
        context_parts.append(f"{citation}\n{doc}")

    context = "\n\n".join(context_parts)
    answer = generate_answer(query, context)

    print(answer)
    print()
    if "I don't know" not in answer:
        print("Sources:")
        for i in range(len(results["documents"][0])):
            doc = results["documents"][0][i]
            meta = results["metadatas"][0][i]
            source = f"[{meta['filename']}, page {meta['page_numbers']}]"
            print(f'"{doc}" {source}')