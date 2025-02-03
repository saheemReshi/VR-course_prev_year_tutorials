# File: /image-processing-project/image-processing-project/PartB/task1_solution.py

import cv2
import numpy as np

def compute_negative(image_path):
    # Load the grayscale image
    gray_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    # Check if the image was loaded successfully
    if gray_image is None:
        print("Error: Could not load image.")
        return None
    
    # Compute the negative of the grayscale image
    L = 255  # Maximum intensity value for 8-bit images
    negative_image = L - 1 - gray_image
    
    return negative_image

def main():
    image_path = '../sample.png'  # Replace with your image path
    negative_image = compute_negative(image_path)
    
    if negative_image is not None:
        # Display the original and negative images
        cv2.imshow('Negative Image', negative_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()