# Contents of /image-processing-project/image-processing-project/PartE/task3_script.py

# This script provides a template for applying the Marr-Hildreth edge detection (Laplacian of Gaussian) on an image.
# Students will fill in the necessary code.

import cv2
import numpy as np
import matplotlib.pyplot as plt

def load_image(image_path):
    # Load the image in grayscale
    pass

def apply_laplacian_of_gaussian(image, sigma):
    # Apply Gaussian filter
    # Apply Laplacian filter
    pass

def visualize_zero_crossing(zero_crossing_image):
    # Visualize the zero-crossing map
    pass

def main():
    image_path = '../sample.png'  # Replace with your image path
    image = load_image(image_path)
    
    sigma = 1.0  # Adjust sigma as needed
    zero_crossing_image = apply_laplacian_of_gaussian(image, sigma)
    
    visualize_zero_crossing(zero_crossing_image)

if __name__ == "__main__":
    main()