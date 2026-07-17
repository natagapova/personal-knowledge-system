def chunk_text(text):
    import re
    initial_chunks = re.split(r'(?<=[.?!])', text)
    chunks = []
    for chunk in initial_chunks:
        if chunk.strip():
            chunks.append(chunk.strip())
    return chunks 

