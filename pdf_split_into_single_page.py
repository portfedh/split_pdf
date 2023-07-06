from PyPDF2 import PdfReader, PdfWriter

def split_pdf(file_path):

    with open(file_path, 'rb') as file:

        reader = PdfReader(file)
        pages = len(reader.pages)

        for page_number in range(pages):

            writer = PdfWriter()
            writer.add_page(reader.pages[page_number])
            output_file_path = f'pdf_output/page_{page_number + 1}.pdf'
            with open(output_file_path, 'wb') as output_file:
                writer.write(output_file)
            print(f"Page {page_number + 1} saved as {output_file_path}.")

# Provide the path to your PDF file
pdf_file_path = 'split_example.pdf'

split_pdf(pdf_file_path)