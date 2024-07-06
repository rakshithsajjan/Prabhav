from PIL import Image
import os

def convert_png_to_webp(directory):
    # List all files in the given directory
    for filename in os.listdir(directory):
        # Check if the file is a PNG image
        if filename.endswith(".png"):
            # Construct the full file path
            file_path = os.path.join(directory, filename)
            # Open the image file
            image = Image.open(file_path)
            # resize according to facebook app requirements
            image = image.resize((512, 512))
            # Define the output filename with the new extension
            output_filename = filename[:-4] + '.webp'
            # Save the image in WEBP format with specified quality
            image.save(os.path.join(directory, output_filename), 'WEBP', quality=90)
            # Optional: Remove the original PNG file
            os.remove(file_path)

# Usage
convert_png_to_webp('assets/')