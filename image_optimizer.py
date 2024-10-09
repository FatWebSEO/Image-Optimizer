import os
from PIL import Image

# Define the input and output folders
input_folder = "./Input"
output_folder = "./Output"

# Check if the output folder exists, create it if it doesn't
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Initialize variables to keep track of file sizes
original_size = 0
compressed_size = 0

# Loop through all files in the input folder
for filename in os.listdir(input_folder):
    # Get the full path of the input and output files
    input_path = os.path.join(input_folder, filename)
    output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + ".jpg")

    # Open the image file and get its format
    with Image.open(input_path) as img:
        img_format = img.format

        # Convert to JPG if not already in that format
        if img_format != "JPEG":
            img = img.convert("RGB")

        # Resize if necessary
        width, height = img.size
        if width > 1200:
            new_width = 1200
            new_height = int((new_width / width) * height)
            img = img.resize((new_width, new_height), resample=Image.LANCZOS)

        # Compress using Pillow
        img.save(output_path, format="JPEG", optimize=True, quality=85)

        # Update file size variables
        original_size += os.path.getsize(input_path)
        compressed_size += os.path.getsize(output_path)

# Calculate the file size reduction amount
reduction_amount = original_size - compressed_size

# Convert to KB or MB for readability
if reduction_amount > 1024 * 1024:
    reduction_amount = f"{reduction_amount / (1024 * 1024):.2f} MB"
else:
    reduction_amount = f"{reduction_amount / 1024:.2f} KB"

# Print the file size reduction amount
print(f"Compression complete. Reduced file size by {reduction_amount}.")
