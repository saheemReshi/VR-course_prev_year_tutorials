# File: /image-processing-project/image-processing-project/PartB/task1_script.py

# This script provides a template for computing the negative of a grayscale image.
# Students will fill in the necessary code.

import cv2
import numpy as np

def compute_negative(image_path):
    # Load the grayscale image
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    # Check if the image was loaded successfully
    if image is None:
        print("Error: Could not load image.")
        return
    
    # Compute the negative of the image
    # Formula: s = L - 1 - r
    # L is the intensity range (255 for 8-bit images)
    L = 255
    negative_image = L - 1 - image
    
    # Display the original and negative images
    cv2.imshow('Original Image', image)
    cv2.imshow('Negative Image', negative_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
# compute_negative('../sample.png')