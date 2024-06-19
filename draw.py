import cv2
import tkinter as tk
from tkinter import filedialog
import os


def convert_to_pencil_sketch(input_file, output_file):
    # Load the image
    image = cv2.imread(input_file)

    # Check if the image is loaded successfully
    if image is None:
        print(f"Error: Unable to load image {input_file}")
        return

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Invert the grayscale image
    inverted_image = 255 - gray_image

    # Apply Gaussian Blur to the inverted image
    blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)

    # Invert the blurred image
    inverted_blurred = 255 - blurred

    # Create the pencil sketch by dividing the grayscale image by the inverted blurred image
    pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)

    # Save the pencil sketch image
    cv2.imwrite(output_file, pencil_sketch)
    print(f"Pencil sketch saved as {output_file}")


def select_file():
    # Create a Tkinter root window (it won't be shown)
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    # Open the file dialog to select an image file
    file_path = filedialog.askopenfilename(
        title="Select an Image File",
        filetypes=[("Image Files", "*.jpg;*.jpeg;*.png;*.bmp;*.tiff")]
    )

    # Check if a file was selected
    if file_path:
        # Ask for output directory
        output_folder = filedialog.askdirectory(title="Select Output Directory")

        if output_folder:
            # Create the output file path
            output_file = os.path.join(output_folder, os.path.basename(file_path).rsplit('.', 1)[0] + '_sketch.png')

            # Convert the selected file to a pencil sketch and save it
            convert_to_pencil_sketch(file_path, output_file)
        else:
            print("No output directory selected")
    else:
        print("No file selected")


# Run the file selection function
select_file()
