from PyPDF2 import PdfReader, PdfWriter

reader = PdfReader("input_file.pdf")
writer = PdfWriter()

# Add all pages to the writer
for page in reader.pages:
    writer.add_page(page)

# Add the metadata: Overwrites any previous data
writer.add_metadata(
    {
        "/Author": "Martin",
        "/Producer": "Libre Writer",
    }
)

# Save the new PDF to a file
with open("output_file_with_metadata.pdf", "wb") as f:
    writer.write(f)




