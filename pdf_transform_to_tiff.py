import os
from pdf2image import convert_from_path
from PIL import Image

def pdf_to_tiff(input_pdf_path, output_tiff_path):

    # Convert PDF to a list of PIL Image objects
    images = convert_from_path(input_pdf_path)

    # Create output directory if it doesn't exist
    os.makedirs(os.path.dirname(output_tiff_path), exist_ok=True)

    # Save each page as TIFF
    for i, image in enumerate(images):
        page_number = i + 1
        page_tiff_path = f"{output_tiff_path}_{page_number}.tiff"
        image.save(page_tiff_path, "TIFF", compression="tiff_deflate")
        print(f"Page {page_number} saved as TIFF: {page_tiff_path}")

# Specify the input PDF file path
input_pdf_path = "input_file.pdf"

# Specify the output TIFF file path (without the file extension)
output_tiff_path = "tiff_output/"

# Convert PDF to TIFF
pdf_to_tiff(input_pdf_path, output_tiff_path)