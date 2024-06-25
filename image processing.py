import cv2
import os
from matplotlib import pyplot as plt

# Path to the directory containing images
directory_path = "C:\\Users\\Admin\\Desktop\\images"

# List all files in the directory
image_files = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]

# Process each image file
for image_file in image_files:
    # Full path to the image
    image_path = os.path.join(directory_path, image_file)

    # Load the image
    image = cv2.imread(image_path)

    # Check if the image was loaded correctly
    if image is None:
        print(f"Error: Unable to load image at {image_path}")
        continue

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply edge detection
    edges = cv2.Canny(gray, 50, 150, apertureSize=3)

    # Find contours in the edged image
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Assuming the largest contour in terms of height is the plant
    max_height = 0
    plant_contour = None
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        if h > max_height:
            max_height = h
            plant_contour = contour

    # Draw the contour of the plant on the original image
    cv2.drawContours(image, [plant_contour], -1, (0, 255, 0), 3)

    # Display the image with the plant contour
    plt.figure(figsize=(10, 8))
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title(f'Plant Contour - {image_file}')
    plt.axis('off')

    # Print the height of the plant in pixels
    print(f"Height of the plant in {image_file} in pixels: {max_height}")
