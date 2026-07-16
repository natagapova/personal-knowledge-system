# Personal Knowledge System

A Retrieval-Augmented Generation (RAG) system that answers questions using personal PDF documents.

## Overview

This project is a from-scratch implementation of a RAG pipeline built in Python. It allows users to upload PDF documents, retrieve the most relevant information using semantic search, and generate grounded answers with an LLM.

The goal of this project is to better understand every component of a modern RAG system by implementing the pipeline step by step rather than relying on high-level frameworks.

## Features

- 📄 PDF document processing
- ✂️ Text chunking
- 🧠 Embedding generation
- 🔎 Semantic search with a vector database
- 🤖 LLM-powered question answering
- 📚 Source citations

## Tech Stack

- Python
- PyPDF2
- Sentence Transformers
- ChromaDB
- OpenAI API

## Project Structure

```
personal-knowledge-system/
├── data/              # PDF documents
├── src/               # Source code
├── .venv/
├── .gitignore
├── README.md
└── requirements.txt
```

## How It Works

1. Read PDF documents.
2. Extract text.
3. Split text into chunks.
4. Generate embeddings.
5. Store embeddings in a vector database.
6. Retrieve the most relevant chunks for a query.
7. Send the retrieved context to an LLM.
8. Return an answer with citations.

## Roadmap

- [x] PDF text extraction
- [ ] Text preprocessing
- [ ] Chunking
- [ ] Embedding generation
- [ ] Vector database integration
- [ ] Semantic retrieval
- [ ] LLM integration
- [ ] Citation support
- [ ] User interface

## Learning Goals

This project is intentionally built without high-level RAG frameworks (such as LangChain or LlamaIndex) in the early stages in order to understand the underlying concepts and implementation details.

## License

MIT