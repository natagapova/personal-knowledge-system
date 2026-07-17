from pdf_loader import load_pdf 
text = load_pdf("data/crime.pdf")
print(text[:100])
