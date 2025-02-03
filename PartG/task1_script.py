# Contents of /image-processing-project/image-processing-project/PartG/task1_script.py

import cv2
import numpy as np

# Load the image
image_path = '../sample.png'  # Replace with your image path
image = cv2.imread(image_path)

# Convert the image to grayscale
# TODO: Implement the conversion to grayscale

# Detect keypoints and compute descriptors using SIFT
# TODO: Initialize SIFT detector and detect keypoints

# Draw keypoints on the image
# TODO: Use cv2.drawKeypoints to visualize the keypoints

# Display the image with keypoints
# TODO: Use cv2.imshow to display the image and cv2.waitKey to wait for a key press

# Save the output image with keypoints
# TODO: Use cv2.imwrite to save the output image

# Clean up
# TODO: Use cv2.destroyAllWindows to close any open windows