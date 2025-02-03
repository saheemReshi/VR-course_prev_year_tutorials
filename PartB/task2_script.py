# File: /image-processing-project/image-processing-project/PartB/task2_script.py

import cv2
import numpy as np

def log_transformation(image, c):
    # Apply log transformation to enhance dark regions
    # Formula: s = c * log(1 + r)
    pass  # Students will fill in the necessary code

def main():
    # Load the image
    image = cv2.imread('../sample.png', cv2.IMREAD_GRAYSCALE)
    
    # Set the scaling constant
    c = 1.0  # Adjust as necessary
    
    # Call the log transformation function
    transformed_image = log_transformation(image, c)
    
    # Display the original and transformed images
    cv2.imshow('Original Image', image)
    cv2.imshow('Log Transformed Image', transformed_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()