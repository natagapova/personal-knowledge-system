import re

def clean_text(text):

    # join words broken by hyphen + newline
    text = re.sub(r'-\n', '', text)

    # replace newlines with spaces
    text = text.replace('\n', ' ')

    # add missing spaces between lowercase-uppercase transitions
    text = re.sub(r'([a-z])([A-Z])', r'\1 \2', text)

    # remove multiple spaces
    text = re.sub(r'\s+', ' ', text)

    return text.strip()

def chunk_text(pages):

    # 1. text + page number map
    full_text = ""
    page_positions = []
    current_position = 0

    for page in pages:
        page_text = clean_text(page["text"])
        start = current_position
        end = current_position + len(page_text)

        page_positions.append(
            {
                "page_number": page["page_number"],
                "start": start,
                "end": end
            }
        )

        full_text += page_text + "\n"

        current_position = len(full_text)
   
    # 2. split into chunks
    chunks = []

    sentence_pattern = re.compile(
        r'(?<!\b[A-Z])(?<=[.!?])\s+'
    )

    sentences = sentence_pattern.split(full_text)

    current_position = 0

    for chunk in sentences:

        start = current_position
        end = start + len(chunk)

        if chunk.strip():
            chunks.append(
                {
                    "text": chunk.strip(),
                    "start": start,
                    "end": end
                }
            )

        current_position = end + 1

    print(full_text[:1000])
    return chunks, page_positions