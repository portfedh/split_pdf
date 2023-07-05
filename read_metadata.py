from PyPDF2 import PdfReader

reader = PdfReader("meta.pdf")

meta = reader.metadata
pages = len(reader.pages)

print(f"\nPages in document: {pages}. \n")
print(f"Full metadata: \n {meta}. \n")
print(f"Creation date: {meta.creation_date}. \n")
print(f"Modification date: {meta.modification_date}. \n")
print(f"Producer: {meta.producer}. \n")



