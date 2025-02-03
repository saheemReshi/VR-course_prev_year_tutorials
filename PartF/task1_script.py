# Contents of /image-processing-project/image-processing-project/PartF/task1_script.py

import cv2
import numpy as np

# Load the image
image_path = '../sample.png'  # Replace with your image path
image = cv2.imread(image_path)

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Harris Corner Detection
# Parameters: gray_image, blockSize, ksize, k
block_size = 2  # Size of the neighborhood considered for corner detection
ksize = 3       # Aperture parameter for the Sobel operator
k = 0.04        # Harris detector free parameter

# Compute the Harris response
harris_response = cv2.cornerHarris(gray_image, block_size, ksize, k)

# Result is dilated for marking the corners
harris_response = cv2.dilate(harris_response, None)

# Thresholding to identify strong corners
threshold = 0.01 * harris_response.max()
image[harris_response > threshold] = [0, 0, 255]  # Mark corners in red

# Display the results
cv2.imshow('Harris Corners', image)
cv2.waitKey(0)
cv2.destroyAllWindows()