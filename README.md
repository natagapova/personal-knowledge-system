# Personal Knowledge System

A Retrieval-Augmented Generation (RAG) system that answers questions using personal PDF documents.

## Overview

This project is a from-scratch implementation of a RAG pipeline built in Python. It allows users to upload PDF documents, retrieve the most relevant information using semantic search, and generate grounded answers with an LLM.

The goal of this project is to better understand every component of a modern RAG system by implementing the pipeline step by step rather than relying on high-level frameworks.

## Features

- PDF document processing
- Text chunking
- Embedding generation
- Semantic search with a vector database
- LLM-powered question answering
- Source citations

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

## MVP Roadmap

- [x] PDF text extraction
- [x] Text preprocessing
- [x] Chunking
- [x] Embedding generation
- [x] Vector database integration (ChromaDB)
- [x] Semantic retrieval
- [x] Prompt construction
- [x] LLM integration (Ollama)
- [ ] Citation support
- [ ] User interface

---

## Future Improvements

### Retrieval
- [ ] Metadata storage (filename, page number, chunk ID)
- [ ] Multi-document indexing
- [ ] Folder indexing
- [ ] Incremental indexing (only process new/modified files)
- [ ] Hybrid search (semantic + keyword/BM25)
- [ ] Query expansion
- [ ] Reranking retrieved chunks

### Supported Data Sources
- [ ] PDF documents
- [ ] Word documents (.docx)
- [ ] Markdown files
- [ ] Plain text files
- [ ] PowerPoint presentations
- [ ] Excel spreadsheets
- [ ] Web pages
- [ ] Entire local knowledge directory

### Generation
- [ ] Source-aware citations
- [ ] Configurable prompting
- [ ] Conversation memory
- [ ] Streaming responses

### User Experience
- [ ] Web interface
- [ ] Drag-and-drop document upload
- [ ] Search history
- [ ] Document management
- [ ] Settings page

### Performance
- [ ] Faster embedding pipeline
- [ ] Batch indexing
- [ ] Embedding cache
- [ ] Configurable embedding models
- [ ] Configurable LLMs

### Long-Term Vision
- [ ] Search across the entire local knowledge base
- [ ] Connect external applications (Notion, Google Drive, etc.)
- [ ] Cross-document reasoning
- [ ] Personal AI knowledge assistant

## Learning Goals

This project is intentionally built without high-level RAG frameworks (such as LangChain or LlamaIndex) in the early stages in order to understand the underlying concepts and implementation details.

## License

MIT