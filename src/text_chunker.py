def chunk_text(text):
    import re
    return re.split(r'(?<=[.?!])', text)