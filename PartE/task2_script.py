# Contents of /image-processing-project/image-processing-project/PartE/task2_script.py

import cv2
import numpy as np

# Load the image
image_path = '../sample.png'  # Replace with your image path
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Apply Canny edge detection
# Step 1: Gaussian Blur
blurred = cv2.GaussianBlur(image, (5, 5), 1.5)

# Step 2: Canny Edge Detection
# Define thresholds
low_threshold = 50
high_threshold = 150
edges = cv2.Canny(blurred, low_threshold, high_threshold)

# Display the results
cv2.imshow('Original Image', image)
cv2.imshow('Edges', edges)

# Wait until a key is pressed and close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()