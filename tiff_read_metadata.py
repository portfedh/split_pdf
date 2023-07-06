import tifffile

def read_tiff_metadata(image_path):
    with tifffile.TiffFile(image_path) as tiff:
        metadata = tiff.pages[0].tags
        return metadata

# Provide the path to your TIFF image
tiff_path = 'tiff_output/1.tiff'
metadata = read_tiff_metadata(tiff_path)

# Print the metadata
for tag in metadata:
    print(f'{tag.name}: {tag.value}')

