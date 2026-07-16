from PyPDF2 import PdfReader

reader = PdfReader("data/crime.pdf")
for page in reader.pages:
    text = page.extract_text()
    print(text[:200])

