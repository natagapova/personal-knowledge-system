from PyPDF2 import PdfReader
import os

def load_pdf(path):
    pages = []
    reader = PdfReader(path)

    current_position = 0

    for page_number, page in enumerate(reader.pages, start=1):
        page_text = page.extract_text()

        start = current_position
        end = start + len(page_text)

        pages.append(
            {
                "text": page.extract_text(),
                "filename": os.path.basename(path),
                "page_number": page_number,
                "start": start,
                "end": end
            }
        )

        current_position = end

    return pages